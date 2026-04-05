---
jira_key: "NBWEB-155"
aliases: ["NBWEB-155"]
summary: "MS Envios - Independizar la tabla envios y agregar el doble instanciado de db"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-04-29 16:28"
updated: "2022-07-01 17:40"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-155"
---

# NBWEB-155: MS Envios - Independizar la tabla envios y agregar el doble instanciado de db

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-04-29 16:28 |
| Actualizado | 2022-07-01 17:40 |
| Etiquetas | ninguna |
| Jira | [NBWEB-155](https://bluinc.atlassian.net/browse/NBWEB-155) |

## Relaciones

- **Padre:** [[NBWEB-76 - API - Implementar MS envios|NBWEB-76]] API - Implementar MS envios

## Descripcion

Se debe poder conectarse desde el servicio, tanto a las bases de datos del enlace local (conexion actual), como a la db mariadb del servicio.

Ademas es necesario que el servicio disponga de su propia tabla de medios de envío, con una columna clave para vincularse a la tabla de medios de envío en el enlace local.
