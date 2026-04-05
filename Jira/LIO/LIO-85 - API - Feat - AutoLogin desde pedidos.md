---
jira_key: "LIO-85"
aliases: ["LIO-85"]
summary: "API - Feat - AutoLogin desde pedidos"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-08-09 09:03"
updated: "2025-04-09 16:28"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-85"
---

# LIO-85: API - Feat - AutoLogin desde pedidos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-08-09 09:03 |
| Actualizado | 2025-04-09 16:28 |
| Etiquetas | ninguna |
| Jira | [LIO-85](https://bluinc.atlassian.net/browse/LIO-85) |

## Relaciones

- **Padre:** [[LIO-28 - El sitio debe funcionar correctamente, sin puntos grises o cosas que no se|LIO-28]] El sitio debe funcionar correctamente, sin puntos grises o cosas que no se entienden
- **blocks:** [[LIO-87 - APP - Feat - Pantalla de autologin (similar como se trabajo en NB)|LIO-87]] APP - Feat - Pantalla de autologin (similar como se trabajo en NB)
- **relates to:** [[LIO-91 - API - AutoLogin desde pedidos - Invalidar token al utilizar|LIO-91]] API - AutoLogin desde pedidos - Invalidar token al utilizar
- **relates to:** [[SNB-2979 - Libre Opción - Autologin desde pedidos fallido|SNB-2979]] Libre Opción - Autologin desde pedidos fallido 

## Descripcion

Crearemos un recurso en la API del sitio de LO basado en el recurso de login, pero que en lugar de utilizar un usuario y contraseña utiliza el token que creamos en el recurso  [link](https://lioteam.atlassian.net/browse/LIO-86) 

Este token se recibe desde el front 

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
