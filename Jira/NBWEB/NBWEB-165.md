---
jira_key: "NBWEB-165"
summary: "MS Envios - Agregar sistema de login y token"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-05-02 12:18"
updated: "2022-06-26 21:39"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-165"
---

# NBWEB-165: MS Envios - Agregar sistema de login y token

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-05-02 12:18 |
| Actualizado | 2022-06-26 21:39 |
| Etiquetas | ninguna |
| Jira | [NBWEB-165](https://bluinc.atlassian.net/browse/NBWEB-165) |

## Descripción

Se debe crear una tabla de usuarios del servicio, donde puedan hacer uso del recurso de login. 

Esto se hará integrando [JWT](https://es.wikipedia.org/wiki/JSON_Web_Token) al servicio 

```
POST {{API_URL}}/auth/login
```

Request:

```
{
"email": "tucorreo@algo.com",
"password": "123456"
}
```

Retorna un objeto de este tipo

```
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NTE1ODcwNTksImF1ZCI6IjhjMmQ4YzczMmZmNTg5NjJjOWVkMTdhZDBmYzM3MjMwY2FhN2EzMDUiLCJ1c2VyIjp7ImlkIjoyNzYxMywiY29kaWdvRlAiOiIwMjY4MDYiLCJyb2xlIjoxfSwiaWF0IjoxNjUxNTgzNDU5LCJuYmYiOjE2NTE1ODM0NTl9.X8GbGEaYqUiR5vtpTPQF7Kv9ysS4aCy5KvA0n3mfiOs"
}
```



El primer usuario que se cargara sera

[testing@nb.com.ar](mailto:testing@nb.com.ar) 

clave: password



En la tabla usuarios se debe recolectar informacion del agente y direccion ip del cliente, ademas del horario de ultimo login
