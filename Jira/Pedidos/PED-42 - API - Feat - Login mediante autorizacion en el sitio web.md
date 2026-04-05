---
jira_key: "PED-42"
aliases: ["PED-42"]
summary: "API - Feat - Login mediante autorizacion en el sitio web "
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-08-21 19:51"
updated: "2023-08-22 14:19"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-42"
---

# PED-42: API - Feat - Login mediante autorizacion en el sitio web 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-08-21 19:51 |
| Actualizado | 2023-08-22 14:19 |
| Etiquetas | ninguna |
| Jira | [PED-42](https://bluinc.atlassian.net/browse/PED-42) |

## Relaciones

- **Padre:** [[PED-40]] Login automático como cliente
- **is blocked by:** [[PED-41]] API - Feat - Crear autorizacion en la api de ordenes
- **is blocked by:** [[PED-43]] APP - Feat - Pedir autorizacion y redirigir 
- **blocks:** [[PED-44]] APP - Feat - Login meidante autorizacion en el sitio web

## Descripcion

Crearemos un recurso en la API del sitio de NB [link](https://lioteam.atlassian.net/browse/NBWEB-6?jql=text%20~%20%22LOGIN%22%20AND%20project%20IN%20(10038)) basado en el recurso de login, pero que en lugar de utilizar un usuario y contraseña utiliza el token que creamos en el recurso [link](https://lioteam.atlassian.net/browse/PED-41) .

Este token se recibe desde el front [link](https://lioteam.atlassian.net/browse/PED-44) 

```
POST {API_URL}/v1/auth/autoLogin
```

```
{
  token: {token}
}
```

Retorna:

```
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2OTI2NzA3NjAsImF1ZCI6IjNjYjZlYTQxNzczODVhZjYxY2UzYjk0YWZlOGNiZjU2NDVhYmVkNTEiLCJ1c2VyIjp7ImlkIjo3NDYzLCJjb2RpZ29GUCI6IjAxOTIyNyIsInJvbGUiOjEsImNvcnJlb0NvbmZpcm1hZG8iOjEsImNhcnJpdG9BY3Rpdm8iOjgxODEzNzZ9LCJpYXQiOjE2OTI2NTk5NjAsIm5iZiI6MTY5MjY1OTk2MH0.-3NgJEgLT8raQ3rDjPyswCkBM8RVMpPcHKVhyRnHUtE"
}
```

¿Que hace?

Una vez que recibe el toke y hace el login, expira el registro que tiene el token para que no se pueda reutilizar.
