---
jira_key: "NBWEB-171"
aliases: ["NBWEB-171"]
summary: "APP - Mi cuenta - Mis datos"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2022-05-08 20:45"
updated: "2022-06-26 20:08"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-171"
---

# NBWEB-171: APP - Mi cuenta - Mis datos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2022-05-08 20:45 |
| Actualizado | 2022-06-26 20:08 |
| Etiquetas | ninguna |
| Jira | [NBWEB-171](https://bluinc.atlassian.net/browse/NBWEB-171) |

## Relaciones

- **Padre:** [[NBWEB-59]] APP -Maquetado y Desarrollo - Mi cuenta
- **relates to:** [[NBWEB-22]] Mis Datos

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
