---
jira_key: "NBWEB-130"
summary: "API - Registro y alta de cliente"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-04-22 12:46"
updated: "2022-06-26 21:34"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-130"
---

# NBWEB-130: API - Registro y alta de cliente

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-04-22 12:46 |
| Actualizado | 2022-06-26 21:34 |
| Etiquetas | ninguna |
| Jira | [NBWEB-130](https://bluinc.atlassian.net/browse/NBWEB-130) |

## Descripción

Para crear un registro pendiente se deben precargar una tabla con informacion del cliente y crear el usuario, pero mantenerlo desactivado.

En un paso posterior, se hace la carga del cliente en base a esas datos, y se habilita el usuario. (Eso se hace desde un backoffice)

En esta primer parte, solo utilizaremos 2 tablas que pueden vincularse de la siguiente manera:



```
SELECT *
FROM [NB_WEB].dbo.usuarios_nb
RIGHT JOIN [NB_WEB].dbo.info_usuarios
ON usuarios_nb.UserId = info_usuarios.UserLogId
```
