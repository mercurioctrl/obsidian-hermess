---
jira_key: "COB-25"
summary: "APP - Feat - Login"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2022-07-17 19:59"
updated: "2022-10-13 09:01"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-25"
---

# COB-25: APP - Feat - Login

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2022-07-17 19:59 |
| Actualizado | 2022-10-13 09:01 |
| Etiquetas | ninguna |
| Jira | [COB-25](https://bluinc.atlassian.net/browse/COB-25) |

## Descripción

Se trata del el recurso de login necesario para iniciar en las aplicaciones.

Ademas contiene los recursos para poder verificar los permisos y demás informacion del usuario y vendedor.

```
POST {{API_URL}}/v1/cms/auth/login
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
