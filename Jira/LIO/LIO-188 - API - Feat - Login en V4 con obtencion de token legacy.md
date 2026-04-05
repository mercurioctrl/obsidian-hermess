---
jira_key: "LIO-188"
aliases: ["LIO-188"]
summary: "API - Feat - Login en V4 con obtencion de token legacy"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-01-28 13:18"
updated: "2025-02-03 20:44"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-188"
---

# LIO-188: API - Feat - Login en V4 con obtencion de token legacy

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-01-28 13:18 |
| Actualizado | 2025-02-03 20:44 |
| Etiquetas | ninguna |
| Jira | [LIO-188](https://bluinc.atlassian.net/browse/LIO-188) |

## Relaciones

- **Padre:** [[LIO-187 - Login|LIO-187]] Login
- **has action item:** [[LIO-195 - APP - Feat - Login con v4 con obtencion de token de legacy|LIO-195]] APP - Feat - Login con v4 con obtencion de token de legacy

## Descripcion

Actualmente, nuestro sistema utiliza el login de V3 como principal, el cual realiza en segundo plano el login en V4 y maneja ambos tokens. 

Necesitamos invertir este flujo: el login de V4 debe ser el principal, y este deberá realizar en segundo plano el login en V3 para obtener el token legacy. Además, debemos asegurarnos de que los elementos devueltos por V3 (como el objeto JSON con el token y la información del usuario) se conserven o adapten correctamente en la respuesta de V4.

**Objetivos:**

- Implementar el login de V4 como el flujo principal de autenticación.


- Realizar en segundo plano el login en V3 para obtener el token legacy.


- Asegurar que los elementos devueltos por V3 (como el objeto JSON con el token y la información del usuario) se conserven o adapten correctamente en la respuesta de V4.


- Mantener la compatibilidad con los sistemas legacy que dependen del token legacy.



**Se crearan al menos dos recursos en V4**

```
POST {{APIv4_URL}}/auth/login
```

```
GET {{APIv4_URL}}/auth/user
```

```
{
    "user": {
        "id": 2,
        "email": "hermess87@gmail.com",
        "nombre": "Catriel Mercurio",
        "perfil": "vendedor",
        "documento": "33457962",
        "telefono": "4-636-3407",
        "direccion": {
            "calle": "Medina",
            "numero": "351",
            "piso": "1",
            "casaApto": "3"
        },
        "codigo_postal": "1407",
        "avatar": 12,
        "ciudad": {
            "id": 20832,
            "nombre": "CABA",
            "provincia_id": 1,
            "total": 0
        },
        "provincia": {
            "id": 1,
            "key": 1,
            "nombre": "CABA",
            "pais_id": 7,
            "total": 0,
            "ciudad_defecto_id": 0
        },
        "pais": {
            "id": 7,
            "nombre": "ARGENTINA",
            "total": 0
        },
        "tienda_id": 26806,
        "vendedor_id": 22,
        "tokenV3": "8B8C7012-2688-4C06-AB04-F854778AB1AA"
    }
}
```

```
GET {{API_URL}}/auth/logout
```
