---
jira_key: "NBWEB-23"
summary: "Mis Usuarios"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-03-23 11:49"
updated: "2022-06-26 20:10"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-23"
---

# NBWEB-23: Mis Usuarios

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-03-23 11:49 |
| Actualizado | 2022-06-26 20:10 |
| Etiquetas | ninguna |
| Jira | [NBWEB-23](https://bluinc.atlassian.net/browse/NBWEB-23) |

## Descripción

Se debe crear un esquema multi usuario. 

Es decir que el usuario Administrador, pueda tener a la vez sub-usuarios que pueda entregar a sus colaboradores.

Para esto debe utilizarse la tabla `[NB_WEB].[dbo].[usuarios_nb]` .

Actualmente se usa la columna `[NB_WEB].[dbo].[usuarios_nb].subcuenta` para determinar cual es la cuenta principal, a la que se vincula ese usuario, pero es probable que esto sea erróneo y se pueda re definir.

Ademas, es necesario agregar una feature de “roles” bien definidos:

- Administrador


- Comprador


- Cotizador


- Servicio Técnico


- Administrativo



[TODO ESTO PODEMOS VERLO EN EL COWORKING O EN UNA MEET]

El recurso para obtener la lista de usuarios debe ser



```json
GET {{API_URL}}/v1/miCuenta/usuarios
```

y retorna el array de objetos



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
