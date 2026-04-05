---
jira_key: "NBWEB-254"
aliases: ["NBWEB-254"]
summary: "API - Feat - Seguimiento de envios"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-06-10 19:26"
updated: "2024-04-15 18:29"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-254"
---

# NBWEB-254: API - Feat - Seguimiento de envios

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-06-10 19:26 |
| Actualizado | 2024-04-15 18:29 |
| Etiquetas | ninguna |
| Jira | [NBWEB-254](https://bluinc.atlassian.net/browse/NBWEB-254) |

## Relaciones

- **Padre:** [[NBWEB-50]] Sitio Web
- **relates to:** [[NBWEB-350]] APP - Feat - Diseñar y maquetar Seguimiento de envios
- **relates to:** [[NBWEB-711]] API - Seguimiento de envíos - Sin datos de seguimiento

## Descripcion

Se debe generar

```
{{API_URL}}/v1/miCuenta/ordenesDeCompra/{branch}/{order}/tracking
```

Para realizar el seguimiento de envios.

Debe mostrar el mismo array de objetos que muestra el micro servicio de envios para el mismo recurso



```
{{API_URL}}/trackingOrder/nb/{branch}-{order}
```
