---
jira_key: "NBWEB-170"
aliases: ["NBWEB-170"]
summary: "APP - Mi cuenta - Postventa"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2022-05-08 20:45"
updated: "2022-06-26 10:00"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-170"
---

# NBWEB-170: APP - Mi cuenta - Postventa

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2022-05-08 20:45 |
| Actualizado | 2022-06-26 10:00 |
| Etiquetas | ninguna |
| Jira | [NBWEB-170](https://bluinc.atlassian.net/browse/NBWEB-170) |

## Relaciones

- **Padre:** [[NBWEB-59]] APP -Maquetado y Desarrollo - Mi cuenta
- **relates to:** [[NBWEB-21]] Postventa
- **relates to:** [[NBWEB-27]] Detalle Postventa

## Descripcion

```
GET {{API_URL}}/v1/miCuenta/postventa
```



```json
[
  {
    "rmaId": 31323,
    "clientId": "031759",
    "dateAdmission": "20220325",
    "status": "SIN REVISAR",
    "agentId": "LMENA",
    "outboundStatus": "SIN ENTREGAR",
        "isMessageChannel": true, #Esto es si es una postventa nueva y puede tener canal de mensajes
        "admitted": true  #Si ya dejo de ser un pre ingreso
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
  }
  ]
```
