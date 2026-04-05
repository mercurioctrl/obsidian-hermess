---
jira_key: "NBWEB-172"
aliases: ["NBWEB-172"]
summary: "APP - Mi cuenta - Mis ususarios"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2022-05-08 20:46"
updated: "2022-06-26 20:17"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-172"
---

# NBWEB-172: APP - Mi cuenta - Mis ususarios

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2022-05-08 20:46 |
| Actualizado | 2022-06-26 20:17 |
| Etiquetas | ninguna |
| Jira | [NBWEB-172](https://bluinc.atlassian.net/browse/NBWEB-172) |

## Relaciones

- **Padre:** [[NBWEB-59]] APP -Maquetado y Desarrollo - Mi cuenta
- **relates to:** [[NBWEB-23]] Mis Usuarios
- **is blocked by:** [[NBWEB-212]] API - Crear nuevo sub usuario
- **is blocked by:** [[NBWEB-213]] API - Eliminar un sub usuario

## Descripcion

```
GET {{API_URL}}/v1/miCuenta/usuarios
```



```json
[
   {
        "id": 23,
        "name": "nombreDeUsuario",
        "email": "correo@delusuario.com",
        "emailVerification": true,
        "showName": "Nombre para mostrar"
        "role": "Postventa",
        "rootAcount": 324,
        "clientId": 324,
        },
           {
        "id": 23,
        "name": "nombreDeUsuario",
        "email": "correo@delusuario.com",
        "emailVerification": true,
        "showName": "Nombre para mostrar"
        "role": "Postventa",
        "rootAcount": 324,
        "clientId": 324,
        }
    ]


```
