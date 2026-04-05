---
jira_key: "PED-1339"
aliases: ["PED-1339"]
summary: "APP - Feat - Incentivo gigabyte reutilizable"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2026-03-20 08:51"
updated: "2026-03-27 10:49"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1339"
---

# PED-1339: APP - Feat - Incentivo gigabyte reutilizable

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2026-03-20 08:51 |
| Actualizado | 2026-03-27 10:49 |
| Etiquetas | ninguna |
| Jira | [PED-1339](https://bluinc.atlassian.net/browse/PED-1339) |

## Relaciones

- **Padre:** [[PED-1337 - Incentivo Especial Gigabyte|PED-1337]] Incentivo Especial Gigabyte
- **has action item:** [[MKT-301 - NB_ INCENTIVO ESPECIAL GIGA|MKT-301]] NB_ INCENTIVO ESPECIAL GIGA

## Descripcion

Se necesita agregar una nueva sección en la página `/dashboard/incentivoGigabyte` que muestre el incentivo especial GIGA: el progreso individual de cada vendedor hacia sus metas de unidades por familia de producto, y un ranking competitivo entre los 6 participantes.

---

## Contexto del negocio

Del 16/03 al 31/03 se corre un incentivo especial de la marca Gigabyte. Cada uno de los 6 vendedores tiene metas individuales en 3 familias de producto (Placas de video, Mothers y Fuentes). Solo gana quien cumpla las 3 al mismo tiempo. Además compiten entre sí por 3 premios de performance: el que más clientes consiga, el que más facture y el que más unidades venda.

La sección debe ser visible a todos los usuarios que hoy pueden ver la página de objetivos. No requiere filtros ni selector de período histórico: el backend siempre devuelve los datos del período fijo del incentivo.

---

## Endpoint a consumir

```
GET /v1/objectives/gigaIncentive
```

Endpoint nuevo, sin parámetros. Ver historia de backend para el detalle del contrato.

### Query params

Sin parámetros.

---

### Mockup - Esquema orientativo

[adjunto]
---

## Response esperada

```
{
  "sellers": [
    {
      "sellerId": 12,
      "sellerName": "Andrea",
      "allCompleted": true,
      "objectives": [
        { "familyId": 23, "familyName": "Placas de video", "target": 50, "achieved": 52, "percentage": 100.0, "completed": true },
        { "familyId": 7,  "familyName": "Mothers",         "target": 200, "achieved": 207, "percentage": 100.0, "completed": true },
        { "familyId": 11, "familyName": "Fuentes",         "target": 100, "achieved": 102, "percentage": 100.0, "completed": true }
      ]
    }
  ],
  "rankings": {
    "mostClients": [ { "position": 1, "sellerId": 12, "sellerName": "Andrea", "value": 18 } ],
    "mostRevenue":  [ { "position": 1, "sellerId": 12, "sellerName": "Andrea", "value": 48200.50 } ],
    "mostUnits":    [ { "position": 1, "sellerId": 12, "sellerName": "Andrea", "value": 359 } ]
  },
  "period": { "startDate": "2026-03-16", "endDate": "2026-03-31" }
}
```

---

## Diseño de la sección

**Cards de vendedores (grilla 3×2)** Una card por vendedor con:

- Nombre del vendedor


- Ícono de trofeo si `allCompleted === true`


- Badge "Ganó el incentivo" (verde) si `allCompleted === true`


- 3 barras de progreso (`<a-progress type="line" size="small">`), una por familia:

- Label: nombre de familia + `achieved / target`


- `percent`: valor del campo `percentage` (ya viene cappado a 100 desde el back)


- Color verde (`#52c41a`) y `status="success"` si `completed === true`


- Color azul (default) y `status="active"` si no completado





**Sección de ranking competitivo (3 columnas)** Una tabla `<a-table>` por cada ranking (`mostClients`, `mostRevenue`, `mostUnits`). Columnas: posición, nombre del vendedor, valor. La columna de valor de `mostRevenue` muestra el número con formato de moneda (ej: `$48.200`).

Los primeros 3 puestos de cada ranking muestran indicador visual de posición (oro / plata / bronce).

**Estado de carga** Toda la sección wrapped en `<a-spin>` mientras el request está en curso.

**Estado vacío / error** Si el endpoint falla, mostrar error con `$messageAlert.errorCatch` igual que el resto del dashboard.

---

## Criterios de aceptación

- La sección se carga automáticamente al entrar a `/dashboard/incentivoGigabyte`, sin acción del usuario


- Los 6 vendedores aparecen siempre, aunque tengan 0 unidades vendidas


- Las barras de progreso no superan el 100% visualmente


- El trofeo y el badge "Ganó el incentivo" aparecen solo cuando `allCompleted === true`


- Cada barra muestra el color correcto según el estado `completed` del objetivo


- Los 3 rankings muestran todos los vendedores ordenados correctamente de mayor a menor


- La columna de facturación muestra el valor en formato `$XX.XXX` (moneda, sin decimales)


- Mientras carga se muestra el spinner sobre toda la sección


- Si el endpoint falla, se muestra el error sin romper el resto de la página


- La sección es compatible con el layout existente de la página (no rompe el scroll ni los márgenes de las otras secciones)
