---
jira_key: "NBWEB-75"
summary: "Corregir modelado del objeto user"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-04-04 06:11"
updated: "2022-04-11 16:46"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-75"
---

# NBWEB-75: Corregir modelado del objeto user

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-04-04 06:11 |
| Actualizado | 2022-04-11 16:46 |
| Etiquetas | ninguna |
| Jira | [NBWEB-75](https://bluinc.atlassian.net/browse/NBWEB-75) |

## Descripción

Se debe corregir el objeto para retornar la salida, como era originalmente. En un momento lo hablamos y di la indicacion incorrecta de como formatearlo



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
    "internalAgent": 0
}
}
```
