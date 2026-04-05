---
jira_key: "LIO-535"
aliases: ["LIO-535"]
summary: "APP - Refactor - Se debe migrar a V4 el recurso para navegar el inventario"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2026-02-10 08:52"
updated: "2026-02-24 14:27"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-535"
---

# LIO-535: APP - Refactor - Se debe migrar a V4 el recurso para navegar el inventario

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2026-02-10 08:52 |
| Actualizado | 2026-02-24 14:27 |
| Etiquetas | ninguna |
| Jira | [LIO-535](https://bluinc.atlassian.net/browse/LIO-535) |

## Relaciones

- **Padre:** [[LIO-98]] Inventario resellers
- **action item from:** [[LIO-496]] API - Refactor - Obtener productos para un usuario determinado dentro de su cuenta

## Descripcion

Migrar el endpoint de **búsqueda de productos por inventario** desde la API legacy al nuevo recurso de **Inventories v4**, unificando la lógica en el endpoint:

```
GET /v4/inventories/products
```

El nuevo endpoint debe reemplazar completamente al recurso legacy.

---

## Endpoint objetivo

```
GET {{API_URL}}/v4/inventories/products
```

### Ejemplo de request

```
curl --location --request GET 'http://localhost:8097/v4/inventories/products?paymentMethod=&shippingMethod=&search=PLAYSTATION&brandId=3344&categoryId=22&orderDirection=asc&order=priceUsd&limit=1' \
--header 'Content-Type: text/plain' \
--header 'Authorization: Bearer {token}' \
--data '{
    "clientId": 7876,
    "branch": "0002",
    "dropShipping": 0
}'
```

---

## ⚠️ Alcance funcional

El nuevo endpoint debe:

- Reemplazar el comportamiento del endpoint legacy de búsqueda por inventario.


- Mantener compatibilidad funcional con los consumidores actuales.


- Centralizar toda la lógica en el repositorio v4.


- Soportar los filtros ya disponibles en v4.


- Cualquier filtro existente en legacy que **no esté aún soportado en v4** debe:

- ser marcado como **deprecated**


- no bloquear la migración


- documentarse para futura implementación.





---

## 🔎 Parámetros soportados

### Query params

| Parámetro | Descripción |
| --- | --- |
| `search` | Texto de búsqueda libre |
| `brandId` | Filtro por marca |
| `categoryId` | Filtro por categoría |
| `paymentMethod` | Método de pago |
| `shippingMethod` | Método de envío |
| `order` | Campo de ordenamiento |
| `orderDirection` | asc / desc |
| `limit` | Cantidad máxima de resultados |

### Body

| Campo | Descripción |
| --- | --- |
| `clientId` | Cliente que consulta |
| `branch` | Sucursal del cliente |
| `dropShipping` | Flag de operación drop shipping |

---

## 🧪 Criterios de aceptación

| ID | Criterio |
| --- | --- |
| AC1 | El endpoint v4 devuelve resultados equivalentes al endpoint legacy |
| AC2 | Los filtros soportados actualmente funcionan correctamente |
| AC3 | Los filtros no implementados quedan documentados como deprecated |
| AC4 | No quedan dependencias activas del endpoint legacy |
| AC5 | El endpoint queda documentado para consumidores |

---

##  Resultado esperado

- Endpoint legacy listo para desactivación.


- Búsqueda de inventario centralizada en v4.


- Base preparada para futuras mejoras de filtros sin dependencia del sistema anterior.
