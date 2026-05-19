# API — Feat — Categorías con jerarquía ilimitada en cabecera

## Resumen

El endpoint `GET /v4/cabecera-categorias` hoy solo devuelve **2 niveles** de categorías (padre → hijo). Hay que refactorizarlo para que soporte **N niveles** (al menos 4), sin cambiar el contrato de la API ni romper el caché.

---

## Contexto

- **Endpoint:** `GET /v4/cabecera-categorias`
- **API:** `https://omega-api4.libreopcion.com.ar/v4/cabecera-categorias`
- **Parámetro opcional:** `?homeShow=1` (filtra categorías que aparecen en home)

---

## Diagnóstico

La tabla `LO.dbo.categorias` **ya es auto-referencial**: tiene la columna `categoria_padre` que apunta al `id` de otra fila de la misma tabla. No hay límite de profundidad en la base de datos.

El límite de 2 niveles es del código. La query actual hace un solo `LEFT JOIN`, lo que físicamente solo puede devolver padre e hijo directo:

```sql
-- Solo puede ver 2 niveles
FROM LO.dbo.categorias AS CH
LEFT JOIN LO.dbo.categorias AS CP ON CH.categoria_padre = CP.id
```

Y el Service construye el árbol manualmente agrupando por nombre de padre, lo que tampoco escala a más niveles.

---

## Archivos a modificar

| Archivo | Clase / Método |
|---|---|
| `app/app/Repository/Repositories/RepositoriesRepository.php` | `getHeaderCategories()` |
| `app/app/Service/Repositories/RepositoriesService.php` | `getHeaderCategories()` |

**No tocar:** el Controller (`HeaderCategories.php`) ni las rutas (`routes/api.php`).

---

## Qué hay que hacer

### Paso 1 — Repository: reemplazar la query con JOIN por una query plana

**Archivo:** `app/app/Repository/Repositories/RepositoriesRepository.php`

Reemplazar la query actual por esta:

```php
public function getHeaderCategories($homeShow)
{
    $filter = '';
    if (!is_null($homeShow)) {
        $filter = " AND homeShow = " . intval($homeShow);
    }

    $list = "
        SELECT id, nombre, categoria_padre, icon, directUrl, productosDisponibles
        FROM LO.dbo.categorias
        WHERE activa = 1
          AND eliminada = 0
          {$filter}
        ORDER BY nombre ASC
    ";

    return DB::select($list);
}
```

> **¿Por qué?** Al traer todas las categorías planas, el PHP puede armar el árbol a cualquier profundidad. Con el JOIN solo podíamos ver 2 niveles.

**Diferencias con la query anterior:**
- Se elimina el `LEFT JOIN` con alias `CP`/`CH`
- Se elimina el filtro `CH.productosDisponibles > 0` (los nodos intermedios pueden tener 0 productos propios pero tener hijos con productos)
- Se agrega `productosDisponibles` al `SELECT` por si se necesita en el futuro
- El filtro `homeShow` ahora usa `intval()` para evitar SQL injection (la query anterior interpolaba directo)

---

### Paso 2 — Service: reemplazar la lógica de árbol manual por construcción genérica

**Archivo:** `app/app/Service/Repositories/RepositoriesService.php`

Reemplazar el método `getHeaderCategories()` completo:

```php
public function getHeaderCategories($homeShow)
{
    $cacheKey = 'header_categories_' . $homeShow;

    if (config('app.use_redis')) {
        $cachedData = Redis::get($cacheKey);
        if ($cachedData) {
            return json_decode($cachedData);
        }
    }

    $rows = $this->repository->getHeaderCategories($homeShow);

    // 1. Indexar todos los nodos por id
    $indexed = [];
    foreach ($rows as $row) {
        $indexed[$row->id] = [
            'id'        => $row->id,
            'nombre'    => $row->nombre,
            'img'       => $row->icon ? 'icon-' . $row->icon . '.svg' : null,
            'directUrl' => $row->directUrl,
            'hijos'     => [],
        ];
    }

    // 2. Armar el árbol: enganchar cada nodo a su padre
    $roots = [];
    foreach ($rows as $row) {
        $parentId = $row->categoria_padre;

        if ($parentId === null || !isset($indexed[$parentId])) {
            // Nodo raíz
            $roots[] = &$indexed[$row->id];
        } else {
            // Nodo hijo: se agrega al array hijos de su padre
            $indexed[$parentId]['hijos'][] = &$indexed[$row->id];
        }
    }

    if (config('app.use_redis')) {
        Redis::setex($cacheKey, config('app.redis_expiration_time', 3600), json_encode($roots));
    }

    return $roots;
}
```

> **¿Por qué funciona para cualquier profundidad?**
> El loop recorre cada nodo **una sola vez** (`O(n)`). Cada nodo simplemente se engancha a su padre via referencia (`&`). No importa si hay 2, 4 o 10 niveles — el mismo código los maneja sin cambios.
>
> **¿Qué son los `&`?** Son referencias en PHP. Al escribir `$roots[] = &$indexed[$row->id]`, no se copia el array sino que se apunta al mismo lugar en memoria. Entonces cuando más abajo alguien agrega hijos a `$indexed[$parentId]['hijos']`, ese cambio también se refleja en `$roots` automáticamente.

---

## Response esperada

La estructura cambia de ser plana a **anidada recursivamente**. Cada nodo tiene la misma forma independientemente del nivel:

```json
[
  {
    "id": 1,
    "nombre": "Tecnología",
    "img": null,
    "directUrl": null,
    "hijos": [
      {
        "id": 10,
        "nombre": "Computadoras",
        "img": "icon-computer.svg",
        "directUrl": "/tecnologia/computadoras",
        "hijos": [
          {
            "id": 100,
            "nombre": "Laptops",
            "img": null,
            "directUrl": null,
            "hijos": [
              {
                "id": 1000,
                "nombre": "Laptops Gamer",
                "img": "icon-gaming.svg",
                "directUrl": "/tecnologia/computadoras/laptops/gamer",
                "hijos": []
              }
            ]
          }
        ]
      }
    ]
  }
]
```

> **Diferencia con la respuesta actual:** antes los nodos padre no tenían `img` ni `directUrl`. Ahora todos los nodos tienen la misma forma. El frontend puede asumir que cada nodo tiene `id`, `nombre`, `img`, `directUrl`, `hijos`.

---

## Criterios de aceptación

### CA-1 — Soporte de 4+ niveles
- Dado que existen categorías con 4 niveles de profundidad en la base de datos
- Cuando se hace `GET /v4/cabecera-categorias`
- Entonces la respuesta incluye los 4 niveles anidados correctamente (el nivel 4 aparece dentro de `hijos` del nivel 3, y así)

### CA-2 — Nodos raíz correctos
- Los únicos nodos en el array raíz del JSON son categorías cuyo `categoria_padre` es `NULL` o apunta a una categoría que no existe / está inactiva
- No aparece ningún nodo raíz que debería ser hijo de otro

### CA-3 — El parámetro `homeShow` sigue funcionando
- Dado `GET /v4/cabecera-categorias?homeShow=1`
- Entonces solo se devuelven categorías que tienen `homeShow = 1` en la base de datos
- Dado `GET /v4/cabecera-categorias` (sin parámetro)
- Entonces se devuelven todas las categorías activas y no eliminadas

### CA-4 — Caché no se rompe
- Si `use_redis = true`, la primera llamada guarda el resultado en Redis con la clave `header_categories_{homeShow}`
- Las llamadas siguientes devuelven el valor cacheado (no ejecutan la query)
- Si se llama con `homeShow=1` y después sin parámetro, son cachés separados (claves distintas: `header_categories_1` vs `header_categories_`)

### CA-5 — Formato de campos consistente
- Todos los nodos (sin importar el nivel) tienen exactamente estos campos: `id`, `nombre`, `img`, `directUrl`, `hijos`
- `img` es `null` si la categoría no tiene icono, o `"icon-{icon}.svg"` si tiene
- `hijos` es siempre un array (vacío `[]` si es hoja, con elementos si tiene hijos)

### CA-6 — Solo categorías activas y no eliminadas
- No aparece ninguna categoría con `activa = 0` o `eliminada = 1`
- Si un nodo padre está inactivo/eliminado, sus hijos tampoco deben aparecer en la respuesta (no quedan huérfanos)

### CA-7 — Regresión: el endpoint actual sigue respondiendo igual para 2 niveles
- Las categorías que hoy se ven en producción (2 niveles) deben seguir apareciendo con los mismos `id`, `nombre`, `img`, `directUrl`
- No se rompe el frontend actual

---

## Lo que NO hay que tocar

- `HeaderCategories.php` (Controller) — no cambia nada
- `routes/api.php` — no cambia nada
- La autenticación del endpoint — sigue siendo pública (sin middleware `token.auth`)
- La clave de caché y el TTL — misma lógica que hoy

---

## Checklist antes de hacer PR

- [ ] La query nueva no tiene `LEFT JOIN`
- [ ] El filtro `homeShow` usa `intval()` antes de interpolar
- [ ] Los `&` (referencias) están en ambos `foreach` del Service
- [ ] Se probó con `?homeShow=1` y sin el parámetro
- [ ] Se verificó que el caché guarda y lee correctamente (o se desactivó con `use_redis=false` para probar)
- [ ] Se comparó la respuesta actual con la nueva para categorías conocidas (mismos `id` y `nombre`)
