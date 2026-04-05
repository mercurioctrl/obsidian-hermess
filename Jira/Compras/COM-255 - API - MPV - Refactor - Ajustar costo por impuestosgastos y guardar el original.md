---
jira_key: "COM-255"
aliases: ["COM-255"]
summary: "API - MPV - Refactor - Ajustar costo por impuestos/gastos y guardar el original para comisiones -> Separar costo distribuido "
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Guillermo Avila"
created: "2025-12-01 00:13"
updated: "2025-12-05 05:59"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-255"
---

# COM-255: API - MPV - Refactor - Ajustar costo por impuestos/gastos y guardar el original para comisiones -> Separar costo distribuido 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Guillermo Avila |
| Creado | 2025-12-01 00:13 |
| Actualizado | 2025-12-05 05:59 |
| Etiquetas | ninguna |
| Jira | [COM-255](https://bluinc.atlassian.net/browse/COM-255) |

## Relaciones

- **Padre:** [[COM-98]] Repositorio de impuestos por posicionar arancelaria
- **relates to:** [[COM-231]] API- MVP - Refactor - Al agregar un impuesto/gasto a una orden de compra se debe calcular segun prorratee o no el nuevo costo y guardar el costo original (Futuro calculo comisiones)

## Descripcion

Haremos un refactor para que en la columna `nPreDivDistributed` se registre únicamente el valor adicional del prorrateo; es decir, en el ejemplo, solo se guardarán 5 y 10, ya que el costo del artículo ya está almacenado en `nPreDiv`.

[adjunto]
