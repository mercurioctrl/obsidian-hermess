---
jira_key: "NBWEB-26"
aliases: ["NBWEB-26"]
summary: "Detalle Mis Comprobantes"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-03-25 10:35"
updated: "2022-06-26 20:10"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-26"
---

# NBWEB-26: Detalle Mis Comprobantes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-03-25 10:35 |
| Actualizado | 2022-06-26 20:10 |
| Etiquetas | ninguna |
| Jira | [NBWEB-26](https://bluinc.atlassian.net/browse/NBWEB-26) |

## Relaciones

- **Padre:** [[NBWEB-2]] API - Mi cuenta
- **is blocked by:** [[NBWEB-20]] Mis comprobantes

## Descripcion

Se trata del recurso para listar los comprobantes fiscales o facturas. El mismo ya proviene de un servicio, por lo que no existe ninguna acción que realizar, mas que implementarlo en el issue asociado a este.

```
GET https://comprobantes.lio.red/?F={id_nrofaccli_enc}&show=1
```
