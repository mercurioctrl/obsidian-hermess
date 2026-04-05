---
jira_key: "LOCAPP-67"
aliases: ["LOCAPP-67"]
summary: "API - Refactor - Tomar archivos desde un directorio local de la aplicacion"
status: "Finalizada"
type: "Subtarea"
priority: "High"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-05-21 13:22"
updated: "2025-05-26 15:55"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LOCAPP-67"
---

# LOCAPP-67: API - Refactor - Tomar archivos desde un directorio local de la aplicacion

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | High |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-05-21 13:22 |
| Actualizado | 2025-05-26 15:55 |
| Etiquetas | ninguna |
| Jira | [LOCAPP-67](https://bluinc.atlassian.net/browse/LOCAPP-67) |

## Relaciones

- **Padre:** [[LOCAPP-62]] Descarga y procesamiento de padrones

## Descripcion

Siguiendo lo conversado y respecto a la historia realizada en [link](https://bluinc.atlassian.net/browse/LOCAPP-63) 

cambiaremos el metodo de lectura del archivo.

Para esto pondremos dentro de nuestras variables de entorno (`.env`) dos rutas diferenciadas dentro de un directorio de la aplicacion de donde leeremos los archivos.

Una para AGIP o CABA

Y otra para ARBA
