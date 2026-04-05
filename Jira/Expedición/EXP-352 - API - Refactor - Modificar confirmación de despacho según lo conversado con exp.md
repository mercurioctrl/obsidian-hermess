---
jira_key: "EXP-352"
aliases: ["EXP-352"]
summary: "API - Refactor - Modificar \"confirmación de despacho\" según lo conversado con exp"
status: "CodeReview"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-07-26 18:00"
updated: "2023-08-01 11:56"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-352"
---

# EXP-352: API - Refactor - Modificar "confirmación de despacho" según lo conversado con exp

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-07-26 18:00 |
| Actualizado | 2023-08-01 11:56 |
| Etiquetas | ninguna |
| Jira | [EXP-352](https://bluinc.atlassian.net/browse/EXP-352) |

## Relaciones

- **Padre:** [[EXP-325 - Feat - Pestaña seguimiento|EXP-325]] Feat - Pestaña seguimiento

## Descripcion

Paso a describir el nuevo funcionamiento de drops.



1er paso. 

Crear cabecera.

```
POST {{API_URL}}/v1/trackingOrders/createDrop
```

[adjunto]


Acá enviar el `trackings`es opcional, por si quieren solo crear la cabecera o si quieren crear la cabecera y ya guardar trackigns adentro



2do Paso: 

```
PATCH {{API_URL}}/v1/trackingOrders/dropTrackings
```

[adjunto]
Agregar trackings a una cabecera previamente creada.



3er Paso:

```
{{API_URL}}/v1/trackingOrders/finalizeDrop/{dropId}
```

[adjunto]


Este es el paso final, cuando se ejecuta se tiene en cuenta como que los trakings se fueron de la empresa o bien fueron retirados por el transportista.



---

Listados:

 

```
{{API_URL}}/v1/trackingOrders/drops?itemsPerPage=15&currentPage=1
```

[adjunto]
Filtros: 

between: filtra por fecha

status: filtra por estado

currierId : filtra por currier



```
{{API_URL}}/v1/trackingOrders/drops/{dropId}
```

[adjunto]
obtiene los trackigns asociados a la cabecera.



```
{{API_URL}}/v1/trackingOrders/status
```

[adjunto]
Obtiene los posibles estados de la cabecera



---

Lo del excel se mantiene de la misma forma como veniamos trabajando
