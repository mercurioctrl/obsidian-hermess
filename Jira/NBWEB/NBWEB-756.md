---
jira_key: "NBWEB-756"
summary: "API - Feat - Agregar al objeto \"user\" el grupo al que pertenece el ususariuo"
status: "Finalizada"
type: "Subtarea"
priority: "Highest"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-06-26 09:47"
updated: "2024-06-26 10:07"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-756"
---

# NBWEB-756: API - Feat - Agregar al objeto "user" el grupo al que pertenece el ususariuo

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Highest |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-06-26 09:47 |
| Actualizado | 2024-06-26 10:07 |
| Etiquetas | ninguna |
| Jira | [NBWEB-756](https://bluinc.atlassian.net/browse/NBWEB-756) |

## Descripción

```
GET {{API_URL}}/v1/auth/user
```

```
{
    "user": {
        "id": 7463,
        "username": "catriel",
        "email": "hermess87@gmail.com",
        "shoppingCartId": "8204683",
        "codeFP": 19227,
        "showName": "catriel2",
        "blackUser": 1,
        "internalAgent": 12,
        "defaultCurrency": true,
        "defaultIvas": false,
        "defaultStock": true,
        "roleId": 1,
        "agentId": 12,
        "agentDescription": "Sistema Web",
        "userGroup": "C"
    }
}
```
