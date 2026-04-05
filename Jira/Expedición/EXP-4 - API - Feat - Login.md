---
jira_key: "EXP-4"
aliases: ["EXP-4"]
summary: "API - Feat - Login"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-10-31 09:27"
updated: "2023-06-28 13:21"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-4"
---

# EXP-4: API - Feat - Login

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-10-31 09:27 |
| Actualizado | 2023-06-28 13:21 |
| Etiquetas | ninguna |
| Jira | [EXP-4](https://bluinc.atlassian.net/browse/EXP-4) |

## Relaciones

- **Padre:** [[EXP-2 - Feat - Login y credenciales|EXP-2]] Feat - Login y credenciales

## Descripcion

Se trata del el recurso de login necesario para iniciar en las aplicaciones.

Ademas contiene los recursos para poder verificar los permisos y demás informacion del usuario y vendedor.

```
POST {{API_URL}}/v1/auth/login
```

Carga Útil:

- Usuario: Nombre de usuario en `usuarios_nb`


- Clave: Clave del cliente (md5) en `usuarios_nb`



Retorna:

```
{
    "user": {
        "id": 7463,
        "username": "catriel",
        "email": "hermess87@gmail.com",
        "codeFP": 19227,
        "codeAgent": 23,
        "showName": "capeage cnbrage",
        "internalAgent": 12,
        "roleId": 1,
        "usuIdentificacion": "Andrea"
    }
}

```

### Tablas que intervienen

##### `[NB_WEB].[dbo].[usuarios_nb]`

Esta tabla ya la hemos utilizado y es la que concentra informacion del login del usuario. En ella se mezclan todos los usuarios de los sistemas y apis mas generales.

En el caso de los usuarios que ademas pueden hacer login y tener acceso administrativo a algunas funciones, tienen la columna `usuarios_nb.agente` rellena con su id de agente.

`[NewBytes_DBF].[dbo].[agentes]`

Se trata de la tabla general de agentes, es decir aquellas personas que tienen una cuenta en el sistema. Agrupa informacion especifica sobre los agentes y es una tabla nexo con otras del sistema por contener claves para conectarse entre tablas.

`NB_WEB.dbo.permisos_agente`

Esta tabla es muy importante, porque contiene múltiples columnas que designan permisos. Cada permiso especifico se debe agregar en una columna y por lo tanto cada permiso que se agrega debe estar bien pensado. Cuando el agente tiene permiso para usar una determinada función o ver un área especifica, la consulta por el parámetro retorna un “1”.

`NEW_BYTES.dbo.PGM_USUARIOS`

Se trata de la tabla de usuarios que utilizan todo el software mas viejo que debemos remplazar.

Se debe utilizar lo menos posible. Se enlaza solamente porque algunos registros del sistema la requieren para vincularse con otra informacion.
