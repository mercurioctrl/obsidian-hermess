---
jira_key: "NBWEB-556"
summary: "API - Repositorio empresas"
status: "Code Review"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-07-12 14:33"
updated: "2023-07-12 15:10"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-556"
---

# NBWEB-556: API - Repositorio empresas

| Campo | Valor |
|-------|-------|
| Estado | Code Review (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-07-12 14:33 |
| Actualizado | 2023-07-12 15:10 |
| Etiquetas | ninguna |
| Jira | [NBWEB-556](https://bluinc.atlassian.net/browse/NBWEB-556) |

## Descripción

Basandonos en `[NewBytes_DBF].[dbo].[FP_Empresas] crearemos el recurso `

```
{API_URL}/v1/cms/companies
```

```
[
  {
    "id": "02",
    "DESCRIPTION": "OXXEN SRL"
  },
  {
    "id": "03",
    "DESCRIPTION": "NBGLOBAL"
  },
  {
    "id": "04",
    "DESCRIPTION": "NB DISTRIBUIDORA MAYORISTA SRL"
  },
  {
    "id": "05",
    "DESCRIPTION": "DIGITO BINARIO SRL"
  },
  {
    "id": "07",
    "DESCRIPTION": "SUC 10"
  },
  {
    "id": "08",
    "DESCRIPTION": "MUGELLO SRL"
  },
  {
    "id": "06",
    "DESCRIPTION": "CONSORCIO DE COOPERACION RED DE TECNOLOGIA"
  }
]
```
