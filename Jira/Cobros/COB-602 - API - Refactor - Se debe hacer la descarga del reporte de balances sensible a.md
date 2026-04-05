---
jira_key: "COB-602"
aliases: ["COB-602"]
summary: "API - Refactor - Se debe hacer la descarga del reporte de balances sensible a los mismos filtros que se aplica al repositorio"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2026-01-02 09:36"
updated: "2026-01-20 11:43"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-602"
---

# COB-602: API - Refactor - Se debe hacer la descarga del reporte de balances sensible a los mismos filtros que se aplica al repositorio

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-02 09:36 |
| Actualizado | 2026-01-20 11:43 |
| Etiquetas | ninguna |
| Jira | [COB-602](https://bluinc.atlassian.net/browse/COB-602) |

## Relaciones

- **Padre:** [[COB-573 - Clientes|COB-573]] Clientes
- **has action item:** [[COB-603 - APP - Refactor - Al descargar el archivo con los balances, se deben incorporar|COB-603]] APP - Refactor - Al descargar el archivo con los balances, se deben incorporar los mismos parámetros de filtrado que el repositorio en si
- **is cloned by:** [[COB-604 - API - Review - Se debe hacer la descarga del reporte de balances sensible a los|COB-604]] API - Review - Se debe hacer la descarga del reporte de balances sensible a los mismos filtros que se aplica al repositorio - Error de clase no encontrada
- **is cloned by:** [[COB-605 - API - Review - Se debe hacer la descarga del reporte de balances sensible a los|COB-605]] API - Review - Se debe hacer la descarga del reporte de balances sensible a los mismos filtros que se aplica al repositorio -> Deuda cheque no coincidente

## Descripcion

Se debe hacer que la descarga del `xlsx` sea sensible a los filtros que es sensible el repositorio

```
GET {API_URL}/v1/clients/xlsx?balanceState={balanceState}&companyCode={companyCode}&balanceStateOrder={balanceStateOrder}&sellerId={sellerId}&desactive={desactive}
```

- balanceState


- companyCode


- balanceStateOrder


- sellerId


- desactive
