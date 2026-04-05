---
jira_key: "COB-604"
aliases: ["COB-604"]
summary: "API - Review - Se debe hacer la descarga del reporte de balances sensible a los mismos filtros que se aplica al repositorio - Error de clase no encontrada"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Guillermo Avila"
created: "2026-01-09 19:07"
updated: "2026-01-12 16:35"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-604"
---

# COB-604: API - Review - Se debe hacer la descarga del reporte de balances sensible a los mismos filtros que se aplica al repositorio - Error de clase no encontrada

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Guillermo Avila |
| Creado | 2026-01-09 19:07 |
| Actualizado | 2026-01-12 16:35 |
| Etiquetas | ninguna |
| Jira | [COB-604](https://bluinc.atlassian.net/browse/COB-604) |

## Relaciones

- **Padre:** [[COB-573 - Clientes|COB-573]] Clientes
- **clones:** [[COB-602 - API - Refactor - Se debe hacer la descarga del reporte de balances sensible a|COB-602]] API - Refactor - Se debe hacer la descarga del reporte de balances sensible a los mismos filtros que se aplica al repositorio

## Descripcion

```
GET {API_URL}/v1/clients/xlsx?balanceState={balanceState}&companyCode={companyCode}&balanceStateOrder={balanceStateOrder}&sellerId={sellerId}&desactive={desactive}
```

[adjunto]
[adjunto]
