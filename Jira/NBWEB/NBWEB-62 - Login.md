---
jira_key: "NBWEB-62"
aliases: ["NBWEB-62"]
summary: "Login"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2022-03-29 16:42"
updated: "2022-06-21 21:52"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-62"
---

# NBWEB-62: Login

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2022-03-29 16:42 |
| Actualizado | 2022-06-21 21:52 |
| Etiquetas | ninguna |
| Jira | [NBWEB-62](https://bluinc.atlassian.net/browse/NBWEB-62) |

## Relaciones

- **Padre:** [[NBWEB-52 - APP - Maquetado y Desarrollo - Home|NBWEB-52]] APP - Maquetado y Desarrollo - Home
- **is caused by:** [[NBWEB-6 - Login|NBWEB-6]] Login
- **relates to:** [[NBWEB-9 - APP - Home|NBWEB-9]] APP - Home

## Descripcion

Terminar de maquetar el componente de Login.

El mismo trabaja con el recurso

```
POST {{API_URL}}/v1/auth/login
```

y retora un objeto del tipo:



```json
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NDg1NzIwNzIsImF1ZCI6ImUwZDkwNjY3ODgzMmMwNjhmMzNkMGJhNGExNWI1ZWJmZjdlYWJkNTQiLCJ1c2VyIjp7ImlkIjoyNzYxMywibmFtZSI6InRlc3QiLCJlbWFpbCI6InNvcG9ydGV3ZWIyQG5iLmNvbS5hciIsInNob3BwaW5nQ2FydElkIjoiODAwMTA1MCIsImNvZGVGUCI6MjU0MzMsInNob3dOYW1lIjoiIiwiYmxhY2tVc2VyIjowLCJpbnRlcm5hbEFnZW50IjowfSwiaWF0IjoxNjQ4NTY4NDcyLCJuYmYiOjE2NDg1Njg0NzJ9.1RgYrCzuwZT209rq916zjWAR3_bihc27Fq8esJR82Hw"
}
```



Adicionalmente es necesario consultar el recurso 



```
GET {{API_URL}}/v1/auth/user
```

que retorna  un objeto de este tipo:



```json
 {
        "id": 27613,
        "name": "test",
        "email": "soporteweb2@nb.com.ar",
        "shoppingCartId": "8001050",
        "codeFP": 25433,
        "showName": "",
        "blackUser": 0,
        "internalAgent": 0
    }

```
