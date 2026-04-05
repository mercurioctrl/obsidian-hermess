---
jira_key: "NBWEB-510"
aliases: ["NBWEB-510"]
summary: "API - Refactor - Mi cuenta - Mis comprobantes, no deben aparecer algunas facturas o creditos"
status: "Code Review"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-12-27 14:39"
updated: "2022-12-27 15:01"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-510"
---

# NBWEB-510: API - Refactor - Mi cuenta - Mis comprobantes, no deben aparecer algunas facturas o creditos

| Campo | Valor |
|-------|-------|
| Estado | Code Review (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-12-27 14:39 |
| Actualizado | 2022-12-27 15:01 |
| Etiquetas | ninguna |
| Jira | [NBWEB-510](https://bluinc.atlassian.net/browse/NBWEB-510) |

## Relaciones

- **Padre:** [[NBWEB-2 - API - Mi cuenta|NBWEB-2]] API - Mi cuenta

## Descripcion

Para el recurso

```
GET {{API_URL}}/v1/miCuenta/comprobantes
```

Se deben ocultar todos los comprobantes que en `FP_FactWebCliEncabezado` tenga la columna marcada de `NCNOTOCASALDONISTOCK` . El cliente no debe poder verlas.
