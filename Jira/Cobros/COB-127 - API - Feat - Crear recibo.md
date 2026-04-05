---
jira_key: "COB-127"
aliases: ["COB-127"]
summary: "API - Feat - Crear recibo"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-09-28 22:10"
updated: "2022-10-27 08:36"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-127"
---

# COB-127: API - Feat - Crear recibo

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-09-28 22:10 |
| Actualizado | 2022-10-27 08:36 |
| Etiquetas | ninguna |
| Jira | [COB-127](https://bluinc.atlassian.net/browse/COB-127) |

## Relaciones

- **Padre:** [[COB-115 - Feat - Realizar un cobro|COB-115]] Feat - Realizar un cobro
- **blocks:** [[COB-126 - API - Feat - Realizar cobro|COB-126]] API - Feat - Realizar cobro
- **blocks:** [[COB-128 - API - Feat - Mostrar recibo|COB-128]] API - Feat - Mostrar recibo

## Descripcion

Esto no es un recurso en si mismo, sino el agregado de la tabla numerada que hablamos para generar los recibos.

Dijimos que agregariamos unta tabla con

- id en `.MC_LOG_OPERACIONES` //opcional


- id en `MC_CCORRIENTES_MOVIMIENTOS` //opcional


- pedido //opcional


- id (incremental)


- type (int) //estaa campo lo vamos a setear en 1 harcodeado, por so queremos usar la misma tabla para otros comprobantes



Cada vez que se ejecuta un cobro por caja, se genera esta contraparte
