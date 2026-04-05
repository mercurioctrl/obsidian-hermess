---
jira_key: "LIO-356"
aliases: ["LIO-356"]
summary: "API - Refactor - Agregar al objeto \"user\" un parámetro para saber si ese usuario tiene habilitada la billetera"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-05-19 06:39"
updated: "2025-06-10 10:41"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-356"
---

# LIO-356: API - Refactor - Agregar al objeto "user" un parámetro para saber si ese usuario tiene habilitada la billetera

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-05-19 06:39 |
| Actualizado | 2025-06-10 10:41 |
| Etiquetas | ninguna |
| Jira | [LIO-356](https://bluinc.atlassian.net/browse/LIO-356) |

## Relaciones

- **Padre:** [[LIO-231 - Billetera|LIO-231]] Billetera
- **has action item:** [[LIO-357 - APP - Refactor - Mostrar accesos a billetera solo si esta habilitado en el|LIO-357]] APP - Refactor - Mostrar accesos a billetera solo si esta habilitado en el parámetro de usuario

## Descripcion

Con el objetivo de hacer un despliegue segmentado y tener control sobre que usuarios pueden utilizarla agregaremos un parámetro para saber si debemos o no mostrar la billetera para cada usuario de libre opción.

Para esto agregaremos un parámetro en la tabla `[LO].[dbo].[usuarios].activeWallet` que como valor inicial sera falso

Y lo agregaremos al recurso 

```
GET {API_URL}/v4/auth/user
```

```
{
    "user": {
        "id": 2,
        "email": "hermess87@gmail.com",
        "nombre": "Catriel Mercurioo",
        "perfil": "vendedor",
        "documento": "33457962",
        "telefono": "4-636-3407",
        "direccion": {
            "calle": "Medina",
            "numero": "351",
            "piso": "1",
            "casaApto": "3"
        },
        "codigoPostal": "1408",
        "avatar": 12,
        "ciudad": {
            "id": 20832,
            "nombre": "CABA",
            "provinciaId": 1
        },
        "provincia": {
            "id": 1,
            "nombre": "CABA",
            "paisId": 7,
            "ciudadDefectoId": 20832
        },
        "pais": {
            "id": 7,
            "nombre": "ARGENTINA"
        },
        "tiendaId": 26806,
        "vendedorId": 22,
        "tokenV3": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c3VhcmlvIjp7ImlkIjoyLCJlbWFpbCI6Imhlcm1lc3M4N0BnbWFpbC5jb20iLCJub21icmUiOiJDYXRyaWVsIE1lcmN1cmlvbyIsInBlcmZpbCI6InZlbmRlZG9yIiwiZG9jdW1lbnRvIjoiMzM0NTc5NjIiLCJ0ZWxlZm9ubyI6IjQtNjM2LTM0MDciLCJkaXJlY2Npb24iOnsiY2FsbGUiOiJNZWRpbmEiLCJudW1lcm8iOiIzNTEiLCJwaXNvIjoiMSIsImNhc2FBcHRvIjoiMyJ9LCJjb2RpZ29fcG9zdGFsIjoiMTQwOCIsImF2YXRhciI6MTIsImNpdWRhZCI6eyJpZCI6MjA4MzIsIm5vbWJyZSI6IkNBQkEiLCJwcm92aW5jaWFfaWQiOjEsInRvdGFsIjowfSwicHJvdmluY2lhIjp7ImlkIjoxLCJrZXkiOjEsIm5vbWJyZSI6IkNBQkEiLCJwYWlzX2lkIjo3LCJ0b3RhbCI6MCwiY2l1ZGFkX2RlZmVjdG9faWQiOjB9LCJwYWlzIjp7ImlkIjo3LCJub21icmUiOiJBUkdFTlRJTkEiLCJ0b3RhbCI6MH0sInRpZW5kYV9pZCI6MjY4MDYsInZlbmRlZG9yX2lkIjoyMiwidG9rZW5WNCI6IjE3Qzg4OUJGLUI3REUtNEVFMC1BRDEzLTM3MDI1RjgzODNGOSIsImNvZGlnb19wb3N0YWxfZGVmYXVsdCI6MTQwN30sImlzcyI6ImxpYnJlb3BjaW9uLmNvbSIsImF1ZCI6ImxpYnJlb3BjaW9uLmNvbSIsImlhdCI6MTc0NzY0NzQ3MSwibmJmIjoxNzQ3NjQ3NDcxfQ.vW0c3VGEf20kAW8CQ1ZK9EeI8Fuwl5-bjsBqtNuj33k",
        "codigoPostalDefault": 1407,
        "activeWallet": true|false, <-- SE AGREGA EL PARAMETRO
    }
}
```
