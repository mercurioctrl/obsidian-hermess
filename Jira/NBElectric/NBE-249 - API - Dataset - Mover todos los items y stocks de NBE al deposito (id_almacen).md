---
jira_key: "NBE-249"
aliases: ["NBE-249"]
summary: "API - Dataset - Mover todos los items y stocks de NBE al deposito (id_almacen) de NBE"
status: "Listo"
type: "Tarea"
priority: "Low"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2026-03-20 08:41"
updated: "2026-03-20 15:59"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBE-249"
---

# NBE-249: API - Dataset - Mover todos los items y stocks de NBE al deposito (id_almacen) de NBE

| Campo | Valor |
|-------|-------|
| Estado | Listo (Listo) |
| Tipo | Tarea |
| Prioridad | Low |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2026-03-20 08:41 |
| Actualizado | 2026-03-20 15:59 |
| Etiquetas | ninguna |
| Jira | [NBE-249](https://bluinc.atlassian.net/browse/NBE-249) |

## Relaciones

*Sin relaciones*

## Descripcion

### Resumen

Mover todos los artículos y stocks de NBE al depósito (id_almacen) de NBE. Actualmente, los ítems están repartidos entre el almacén 2 de NB y el de NBE debido a la implementación previa de la lógica de depósitos.

### Contexto

Los artículos y stocks están distribuidos entre dos depósitos. Esto ha causado confusión y la necesidad de consolidar el stock en un solo lugar para evitar problemas futuros.

### Criterios de aceptación

- Mover los siguientes elementos:

- Artículos


- Stocks


- Seriales




- Actualizar pedclil y albclil pendientes para evitar problemas.


- Sumar el stock de ambos depósitos en la tabla de stocks antes de eliminar uno para garantizar que no se pierda stock.
