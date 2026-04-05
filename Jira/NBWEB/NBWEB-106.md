---
jira_key: "NBWEB-106"
summary: "Agregar parametros (conmutadores) al objeto user"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-04-11 09:02"
updated: "2022-06-26 20:11"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-106"
---

# NBWEB-106: Agregar parametros (conmutadores) al objeto user

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-04-11 09:02 |
| Actualizado | 2022-06-26 20:11 |
| Etiquetas | ninguna |
| Jira | [NBWEB-106](https://bluinc.atlassian.net/browse/NBWEB-106) |

## Descripción

Se agregan los nuevos parametros para los conmutadores

```
GET {{API_URL}}/v1/auth/user
```

```json

{
"user":{
    "id": 27613,
    "name": "eze",
    "email": "soporteweb2@nb.com.ar",
    "shoppingCartId": "8002022",
    "codeFP": 25433,
    "showName": "EzeEze",
    "blackUser": 0,
    "internalAgent": 0,
    *"defaultCurrency":true,
    *"defaulIvas":false,
    *"defaulStock":false
}
}
```
