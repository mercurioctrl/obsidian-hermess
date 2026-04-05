---
jira_key: "NBWEB-984"
summary: "API - Refactor - Agregar percepciones CABA y percepciones ARBA para el cliente de un usuario determinado"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-07-20 22:09"
updated: "2025-07-31 10:42"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-984"
---

# NBWEB-984: API - Refactor - Agregar percepciones CABA y percepciones ARBA para el cliente de un usuario determinado

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-07-20 22:09 |
| Actualizado | 2025-07-31 10:42 |
| Etiquetas | ninguna |
| Jira | [NBWEB-984](https://bluinc.atlassian.net/browse/NBWEB-984) |

## Descripción

Agregamos las percepciones para el cliente según la tabla `[NewBytes_DBF].[dbo].[clientes]`

```
GET {API_URL}/v1/auth/user
```

```
{
    "user": {
        "id": 7463,
        "username": "catriel",
        "email": "hermess87@gmail.com",
        "shoppingCartId": "8301768",
        "codeFP": 19227,
        "showName": "catriel2",
        "blackUser": 1,
        "internalAgent": 12,
        "defaultCurrency": true,
        "defaultIvas": false,
        "defaultStock": false,
        "roleId": 1,
        "agentId": 12,
        "agentDescription": "Sistema Web",
        "perception": 1 <-- Agregamos percepciones CABA,
        "perceptionArba": 2 <- Agregamos percepciones ARBA
    }
}
```
