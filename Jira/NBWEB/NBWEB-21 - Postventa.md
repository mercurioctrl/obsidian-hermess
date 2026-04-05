---
jira_key: "NBWEB-21"
aliases: ["NBWEB-21"]
summary: "Postventa"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-03-23 11:49"
updated: "2022-06-26 10:00"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-21"
---

# NBWEB-21: Postventa

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-03-23 11:49 |
| Actualizado | 2022-06-26 10:00 |
| Etiquetas | ninguna |
| Jira | [NBWEB-21](https://bluinc.atlassian.net/browse/NBWEB-21) |

## Relaciones

- **Padre:** [[NBWEB-2 - API - Mi cuenta|NBWEB-2]] API - Mi cuenta
- **relates to:** [[NBWEB-170 - APP - Mi cuenta - Postventa|NBWEB-170]] APP - Mi cuenta - Postventa

## Descripcion

Este recurso es para listar los ingresos de postventa. Es decir cuando el cliente ingresa mercadería con fallas o que necesita devolver por alguna razón.

```
GET {{API_URL}}/v1/miCuenta/postventa
```

El dataset se obtiene de las tablas `NEW_BYTES.dbo.ST_RMACABECERA` y `NEW_BYTES.dbo.ST_RMADETALLE`



```json
[
  {
    "rmaId": 31323,
    "clientId": "031759",
    "dateAdmission": "20220325",
    "status": "SIN REVISAR",
    "agentId": "LMENA",
    "outboundStatus": "SIN ENTREGAR",
        "isMessageChannel": true,
        "admitted": true
  },
  {
    "rmaId": 31323,
    "clientId": "031759",
    "dateAdmission": "20220325",
    "status": "SIN REVISAR",
    "agentId": "LMENA",
    "outboundStatus": "SIN ENTREGAR",
        "isMessageChannel": true,
        "admitted": false
  },
  ]
```
