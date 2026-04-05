---
jira_key: "NBWEB-443"
aliases: ["NBWEB-443"]
summary: "API - Feat - Generar hard token"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-08-05 13:45"
updated: "2022-09-15 12:50"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-443"
---

# NBWEB-443: API - Feat - Generar hard token

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-08-05 13:45 |
| Actualizado | 2022-09-15 12:50 |
| Etiquetas | ninguna |
| Jira | [NBWEB-443](https://bluinc.atlassian.net/browse/NBWEB-443) |

## Relaciones

- **Padre:** [[NBWEB-2]] API - Mi cuenta
- **blocks:** [[NBWEB-445]] API - Feat - Se tiene que poder descargar el archivo sin login, en caso de tener el token

## Descripcion

Un hard token es un token creado por el usuario, que permanece tal cual lo genero a menos que decida regenerarlo.

Debe ser aleatorio y no se puede repetir con el de otros usuarios.

Le permite al usuario acceder a recursos muy específicos sin la necesidad de tener que loguearse solo teniendo que usar el token.

```
POST {{API_URL}}/v1/miCuenta/tokenRegenerate
```

Retorna el token regenerado y que guardo en 

`[NB_WEB].[dbo].[usuarios_nb].hardToken`

Solo el usuario administrador de la cuenta puede generar el token
