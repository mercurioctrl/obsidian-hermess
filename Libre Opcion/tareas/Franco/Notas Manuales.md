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
-- Solo puede ver 2 niveles: un JOIN = una relación
FROM categorias AS CH
LEFT JOIN categorias AS CP ON CH.categoria_padre = CP.id
```

Para soportar 4 niveles con JOINs necesitarías 3 JOINs anidados. Para N niveles, eso no escala. La solución es diferente: traer todo plano y armar el árbol en PHP.

---

## Archivos a modificar

| Archivo | Método |
|---|---|
| `app/app/Repository/Repositories/RepositoriesRepository.php` | `getHeaderCategories()` |
| `app/app/Service/Repositories/RepositoriesService.php` | `getHeaderCategories()` |

**No tocar:** `HeaderCategories.php` (Controller) ni `routes/api.php`.

---

## Qué hay que hacer

### En el Repository

Cambiar la query para que **no use JOIN**. En lugar de pedirle a SQL que arme la jerarquía, traer todas las categorías como filas planas:

```sql
SELECT id, nombre, categoria_padre, icon, directUrl, productosDisponibles
FROM LO.dbo.categorias
WHERE activa = 1
  AND eliminada = 0
  -- + el filtro de homeShow si viene el parámetro
ORDER BY nombre ASC
```

Resultado: un array plano de filas. El PHP se encarga del árbol, no el SQL.

Para el filtro `homeShow`, sanitizá el valor antes de interpolarlo en la query (pista: `intval()`).

---

### En el Service

Reemplazar la lógica actual (que agrupa por nombre de padre) por una que arme el árbol en dos pasos:

**Paso 1 — indexar por id:**
Recorrer las filas y construir un mapa `id → nodo`, donde cada nodo ya tiene su array `hijos` vacío. Esto permite acceder a cualquier nodo por su `id` en O(1).

**Paso 2 — enganchar cada nodo a su padre:**
Recorrer de nuevo. Si un nodo tiene `categoria_padre = NULL`, va al array raíz. Si tiene padre, se agrega a `$indexed[$padreId]['hijos']`.

El truco para que funcione sin recorrer el árbol de nuevo son las **referencias PHP** (`&`). Cuando enganchás un nodo al array de hijos de su padre, si usás referencia, cualquier modificación posterior al nodo (como agregarle sus propios hijos) se refleja automáticamente donde sea que ese nodo esté apuntado.

Ejemplo mínimo del concepto:

```php
$a = ['valor' => 1, 'hijos' => []];
$mapa = [1 => &$a];

// Modifico via el mapa...
$mapa[1]['hijos'][] = 'hijo1';

// ...y $a también cambió, porque apuntan al mismo lugar
// $a['hijos'] === ['hijo1']
```

Aplicá esa misma idea a la construcción del árbol de categorías.

---

## Response esperada

Estructura anidada recursivamente. Cada nodo tiene la misma forma sin importar el nivel:

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
              { "id": 1000, "nombre": "Laptops Gamer", "img": "icon-gaming.svg", "directUrl": "...", "hijos": [] }
            ]
          }
        ]
      }
    ]
  }
]
```

---

## Criterios de aceptación

### CA-1 — Soporte de 4+ niveles
- Dado que existen categorías con 4 niveles de profundidad en la base de datos
- Cuando se hace `GET /v4/cabecera-categorias`
- Entonces la respuesta incluye los 4 niveles anidados correctamente (el nivel 4 aparece dentro de `hijos` del nivel 3)

### CA-2 — Nodos raíz correctos
- Los únicos nodos en el array raíz del JSON son categorías cuyo `categoria_padre` es `NULL`
- No aparece ningún nodo en la raíz que debería ser hijo de otro

### CA-3 — El parámetro `homeShow` sigue funcionando
- `GET /v4/cabecera-categorias?homeShow=1` → solo categorías con `homeShow = 1`
- `GET /v4/cabecera-categorias` (sin parámetro) → todas las categorías activas y no eliminadas

### CA-4 — Caché no se rompe
- La primera llamada guarda el resultado en Redis con la clave `header_categories_{homeShow}`
- Las llamadas siguientes devuelven el valor cacheado sin ejecutar la query
- Llamadas con distintos valores de `homeShow` tienen cachés separados

### CA-5 — Formato de campos consistente
- Todos los nodos tienen exactamente: `id`, `nombre`, `img`, `directUrl`, `hijos`
- `img` es `null` si no tiene icono, o `"icon-{icon}.svg"` si tiene
- `hijos` es siempre un array (vacío en nodos hoja)

### CA-6 — Solo categorías activas y no eliminadas
- Ningún nodo con `activa = 0` o `eliminada = 1` aparece en la respuesta

### CA-7 — Regresión
- Las categorías que hoy se ven en producción siguen apareciendo con los mismos `id`, `nombre`, `img`, `directUrl`

---

## Checklist antes de hacer PR

- [ ] La query no tiene `LEFT JOIN`
- [ ] El filtro `homeShow` sanitiza el valor antes de interpolarlo
- [ ] El árbol se arma en dos pasadas (indexar, luego enganchar)
- [ ] Se usaron referencias (`&`) al construir el árbol
- [ ] Se probó con `?homeShow=1` y sin el parámetro
- [ ] Se verificó que el caché funciona (o se probó con `use_redis=false`)
- [ ] Se comparó la respuesta con la de producción para categorías conocidas
