
## Contexto

Recurso involucrado: `GET /v4/cabecera-categorias`
API: `https://omega-api4.libreopcion.com.ar/v4/cabecera-categorias`

---

## Problema actual

El endpoint devuelve categorías con solo **2 niveles** (Padre → Hijo).

Se necesita soporte para **al menos 4 niveles** de jerarquía.

---

## Diagnóstico

La tabla `LO.dbo.categorias` **ya es auto-referencial**: tiene la columna `categoria_padre` que apunta al `id` de otra fila de la misma tabla.

El límite de 2 niveles es puramente del código, no de la base de datos. La query actual hace un solo `LEFT JOIN`:

```sql
-- CP = padre, CH = hija (1 JOIN = solo 2 niveles)
FROM categorias AS CH
LEFT JOIN categorias AS CP ON CH.categoria_padre = CP.id
```

---

## Solución propuesta

Reemplazar los JOINs por una **query plana + construcción del árbol en PHP**.

### 1. Query — traer todo plano

```sql
SELECT id, nombre, categoria_padre, icon, directUrl, productosDisponibles
FROM LO.dbo.categorias
WHERE activa = 1 AND eliminada = 0
```

Resultado: array plano de filas, sin jerarquía todavía:

| id   | nombre            | categoria_padre |
|------|-------------------|-----------------|
| 1    | Tecnología        | NULL            |
| 10   | Computadoras      | 1               |
| 100  | Laptops           | 10              |
| 1000 | Laptops Gamer     | 100             |
| 2    | Electrodomésticos | NULL            |
| 20   | Cocina            | 2               |

---

### 2. PHP — indexar por id

```php
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
```

Resultado: un mapa `id → nodo`, todos en memoria.

---

### 3. PHP — armar el árbol

```php
$roots = [];

foreach ($indexed as $id => $node) {
    $parentId = $rows[$id]->categoria_padre;

    if ($parentId === null || !isset($indexed[$parentId])) {
        // Es raíz
        $roots[] = &$indexed[$id];
    } else {
        // Es hijo: se engancha al array hijos de su padre
        $indexed[$parentId]['hijos'][] = &$indexed[$id];
    }
}
```

> Los `&` (referencias) hacen que al agregar hijos a `$indexed[$parentId]`, el nodo en `$roots` también se actualice — sin recorrer de nuevo.

---

### 4. Response esperada

```json
[
  {
    "id": 1,
    "nombre": "Tecnología",
    "hijos": [
      {
        "id": 10,
        "nombre": "Computadoras",
        "hijos": [
          {
            "id": 100,
            "nombre": "Laptops",
            "hijos": [
              { "id": 1000, "nombre": "Laptops Gamer", "hijos": [] }
            ]
          }
        ]
      }
    ]
  }
]
```

---

## Por qué funciona para cualquier profundidad

El loop recorre cada nodo **una sola vez** (`O(n)`). No importa si hay 2 niveles o 4 — cada nodo simplemente se engancha a su padre. Si mañana aparece un nivel 5, el mismo código lo maneja sin cambios.

---

## Diferencia con el código actual

El Service actual construye la jerarquía manualmente padre/hija porque la query SQL ya le dice quién es padre y quién es hijo (via JOIN).

Con esta solución, esa lógica se mueve a PHP y se vuelve **genérica para cualquier profundidad**.
