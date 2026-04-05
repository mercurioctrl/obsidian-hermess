---
jira_key: "LIO-204"
aliases: ["LIO-204"]
summary: "APIv4 - Feat - Actualizar informacion del usuario en mi cuenta"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-02-03 06:14"
updated: "2025-02-10 04:06"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-204"
---

# LIO-204: APIv4 - Feat - Actualizar informacion del usuario en mi cuenta

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-02-03 06:14 |
| Actualizado | 2025-02-10 04:06 |
| Etiquetas | ninguna |
| Jira | [LIO-204](https://bluinc.atlassian.net/browse/LIO-204) |

## Relaciones

- **Padre:** [[LIO-203]] Mi cuenta
- **has action item:** [[LIO-205]] APP - Refactor - Actualizar informacion del usuario en mi cuenta

## Descripcion

Se debe agregar a v4 el recurso necesario para modificar los datos del usuario desde mi cuenta, para eso reutilizaremos un objeto como el que ya migramos pero con un PATCH

Solo modifica aquellos parámetros que recibe

```
PATCH {{APIv4_URL}}/auth/user
```

```
{
    "user": {
        "id": 2,
        "email": "catrielmercurio@gmail.com",
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
            "provincia_id": 1,
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
            "id": 7,,
        },
    }
}
```
