---
jira_key: "NBWEB-719"
aliases: ["NBWEB-719"]
summary: "API - Refactor- Envio gratis solo para transportista habilitados para este fin"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2024-04-19 13:04"
updated: "2024-04-23 23:21"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-719"
---

# NBWEB-719: API - Refactor- Envio gratis solo para transportista habilitados para este fin

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2024-04-19 13:04 |
| Actualizado | 2024-04-23 23:21 |
| Etiquetas | ninguna |
| Jira | [NBWEB-719](https://bluinc.atlassian.net/browse/NBWEB-719) |

## Relaciones

- **Padre:** [[NBWEB-668 - Envíos bonificados|NBWEB-668]] Envíos bonificados

## Descripcion

Agregar debe agregar a LO.dbo.mediosEnvio 

el campo **activoBonificado.**

En el caso de que un pedido cumpla con los criterios para ser **envio gratis.** se filtraran los transportistas por aquellos habilitados por este nuevo campo.
