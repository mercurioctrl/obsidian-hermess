---
jira_key: "INV-234"
aliases: ["INV-234"]
summary: "APP - Feat - Mostrar seriales para un item/almacen determinado"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-11-10 08:51"
updated: "2025-12-05 04:41"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-234"
---

# INV-234: APP - Feat - Mostrar seriales para un item/almacen determinado

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-11-10 08:51 |
| Actualizado | 2025-12-05 04:41 |
| Etiquetas | ninguna |
| Jira | [INV-234](https://bluinc.atlassian.net/browse/INV-234) |

## Relaciones

- **Padre:** [[INV-199 - Control de Stock Stock en general Control de Precios|INV-199]] Control de Stock / Stock en general  / Control de Precios
- **action item from:** [[INV-228 - API - Feat - Ver seriales para un stock determinado|INV-228]] API - Feat - Ver seriales para un stock determinado

## Descripcion

Se debe implementar en el frontend una vista modal que consuma el recurso del backend definido en [[[INV-228]]](https://bluinc.atlassian.net/browse/INV-228) para listar todos los seriales asociados a un ítem.

El recurso a utilizar es:

```
GET {API_URL}/serials/{itemId}?stockWarehouseId={stockWarehouseId}
```

Cada elemento del listado representa un serial con la siguiente estructura:

```
{
  "serial": "VW205A802711",
  "admissionDate": "30/05/2025 17:37",
  "dispatchDate": "30/05/2025 17:38",
  "stockWarehouseId": 2,
  "stockWarehouseDescription": "SAFcom",
  "stockWarehouseCode": "SAF",
  "dispatchOrder": "0002-0042344"
}

```

**Requisitos funcionales:**

- El modal debe mostrar todos los seriales devueltos por el recurso, diferenciando claramente cuáles **están disponibles** (sin `dispatchDate`) y cuáles **ya fueron despachados** (con `dispatchDate`).


- Para cada serial, deben mostrarse las fechas y horas exactas de **ingreso** (`admissionDate`) y, si corresponde, de **egreso** (`dispatchDate`).


- Si el serial fue despachado, debe incluirse también el número de **orden de despacho** (`dispatchOrder`).


- En el **título del modal**, se debe mostrar el formato:

```
{itemId} - {itemName}
```

Esto permite identificar fácilmente qué ítem se está visualizando.


- Los seriales disponibles y despachados deben diferenciarse visualmente (por color, ícono o etiqueta).



**Ejemplo de visualización:**

- Serial disponible → Mostrar en verde o con etiqueta “Disponible”.


- Serial despachado → Mostrar en gris o con etiqueta “Despachado (Orden 0002-0042344)”.



[adjunto]
