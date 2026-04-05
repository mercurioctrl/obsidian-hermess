---
jira_key: "NBWEB-22"
aliases: ["NBWEB-22"]
summary: "Mis Datos"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-03-23 11:49"
updated: "2022-06-26 20:09"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-22"
---

# NBWEB-22: Mis Datos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-03-23 11:49 |
| Actualizado | 2022-06-26 20:09 |
| Etiquetas | ninguna |
| Jira | [NBWEB-22](https://bluinc.atlassian.net/browse/NBWEB-22) |

## Relaciones

- **Padre:** [[NBWEB-2]] API - Mi cuenta
- **relates to:** [[NBWEB-171]] APP - Mi cuenta - Mis datos

## Descripcion

```
GET {{API_URL}}/v1/miCuenta/misDatos
```

Retorna



```json
[
   {
        "id": 23,
        "name": "nombreDeUsuario",
        "email": "correo@delusuario.com",
        "emailVerification": true,
        "showName": "Nombre para mostrar"
        }
    ]
```
