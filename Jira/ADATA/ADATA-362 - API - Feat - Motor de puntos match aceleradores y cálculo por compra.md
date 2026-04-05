---
jira_key: "ADATA-362"
aliases: ["ADATA-362"]
summary: "API - Feat - Motor de puntos: match aceleradores y cálculo por compra"
status: "Listo"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2026-02-19 11:20"
updated: "2026-02-23 12:40"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/ADATA-362"
---

# ADATA-362: API - Feat - Motor de puntos: match aceleradores y cálculo por compra

| Campo | Valor |
|-------|-------|
| Estado | Listo (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2026-02-19 11:20 |
| Actualizado | 2026-02-23 12:40 |
| Etiquetas | ninguna |
| Jira | [ADATA-362](https://bluinc.atlassian.net/browse/ADATA-362) |

## Relaciones

- **Padre:** [[ADATA-356 - XPG - Landing Fidelización (Puntos + Aceleradores + Ranking + Carga Compras)|ADATA-356]] XPG - Landing Fidelización (Puntos + Aceleradores + Ranking + Carga Compras)

## Descripcion

Al insertar una compra, calcular puntos finales aplicando acelerador vigente si corresponde.

Reglas

- `puntosBase = montoTotal`


- Determinar fecha para vigencia:

- si fechaCompra existe → usar fechaCompra


- si no → usar fechaCarga




- Match:

- SKU exacto: compra.sku == acelerador.sku


- Parcial: acelerador.match está contenido en compra.nombreProducto (normalizar: uppercase + trim + colapsar espacios)




- Colisión:

- si hay más de un acelerador aplicable, aplicar el de **mayor multiplicador**





Recomendado

- Guardar auditoría (puntosBase, multiplicadorAplicado, puntosFinales, aceleradorId)



### Acceptance Criteria

| AC | Criterio |
| --- | --- |
| AC1 | Compras generan puntos finales correctos según reglas. |
| AC2 | Match por SKU exacto funciona. |
| AC3 | Match parcial “contiene” funciona con normalización. |
| AC4 | Colisión resuelta aplicando el mayor multiplicador. |
| AC5 | (Si hay tabla auditoría) queda registro del acelerador aplicado. |
