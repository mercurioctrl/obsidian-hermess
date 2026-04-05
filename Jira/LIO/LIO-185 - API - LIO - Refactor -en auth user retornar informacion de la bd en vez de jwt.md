---
jira_key: "LIO-185"
aliases: ["LIO-185"]
summary: "API - LIO - Refactor -en auth user retornar informacion de la bd en vez de jwt"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2025-01-27 18:03"
updated: "2025-01-29 03:00"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-185"
---

# LIO-185: API - LIO - Refactor -en auth user retornar informacion de la bd en vez de jwt

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2025-01-27 18:03 |
| Actualizado | 2025-01-29 03:00 |
| Etiquetas | ninguna |
| Jira | [LIO-185](https://bluinc.atlassian.net/browse/LIO-185) |

## Relaciones

*Sin relaciones*

## Descripcion

Se debe retornar la misma informacion de GET auth/user de LO legacy, pero apuntando a DB y no desencriptando el JWT.

GET /auth/user

```
{
   "user": {
      "id": 274942,
      "email": "ferreyra-emanuel@outlook.com",
      "nombre": "Emanuel Jesus",
      "perfil": "vendedor",
      "documento": "37892999",
      "telefono": "2235181922",
      "direccion": {
         "calle": "castelli",
         "numero": "5262",
         "piso": "1",
         "casaApto": ""
      },
      "codigo_postal": "7600",
      "avatar": 3,
      "ciudad": {
         "id": 13430,
         "nombre": "MAR DEL PLATA",
         "provincia_id": 2,
         "total": 0
      },
      "provincia": {
         "id": 2,
         "key": 2,
         "nombre": "BUENOS AIRES",
         "pais_id": 7,
         "total": 0,
         "ciudad_defecto_id": 0
      },
      "pais": {
         "id": 7,
         "nombre": "ARGENTINA",
         "total": 0
      },
      "tienda_id": 0,
      "vendedor_id": 243218,
      "tokenV4": "E6F1E4BB-FEC1-4F4B-BDE5-43A1BB53E7C6",
      "codigo_postal_default": 7600
   }
}
```
