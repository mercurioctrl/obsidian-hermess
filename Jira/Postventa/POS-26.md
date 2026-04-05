---
jira_key: "POS-26"
summary: "API - Feat - Listar técnicos"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-07-18 10:15"
updated: "2022-10-12 08:50"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-26"
---

# POS-26: API - Feat - Listar técnicos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-07-18 10:15 |
| Actualizado | 2022-10-12 08:50 |
| Etiquetas | ninguna |
| Jira | [POS-26](https://bluinc.atlassian.net/browse/POS-26) |

## Descripción

```
GET {{API_URL}}/v1/technicals
```

Retorna:

```json
[
  {
    "usderId": 3564,
    "UserName": "cnbaldi",
    "agentId": 6,
    "usuIdentificacion": "cbaldi",
    "showName": "Baldisera Christian"
  },
  {
    "usderId": 60742,
    "UserName": "jtamagnone",
    "agentId": 52,
    "usuIdentificacion": "JTAMA",
    "showName": "Juan Jose Tamagnone"
  },
  {
    "usderId": 62195,
    "UserName": "lmena",
    "agentId": 55,
    "usuIdentificacion": "LMENA",
    "showName": "Lucas Mena"
  }
]
```



Puede usarse un dataset de este tipo

```sql
SELECT 
*
FROM [NB_WEB].[dbo].[usuarios_nb]
INNER JOIN NewBytes_DBF.dbo.agentes ON usuarios_nb.agente = agentes.ccodage
LEFT JOIN NEW_BYTES.dbo.PGM_USUARIOS ON PGM_USUARIOS.ID_AGENTE = agentes.ccodage
WHERE USU_SECTOR = 2
```
