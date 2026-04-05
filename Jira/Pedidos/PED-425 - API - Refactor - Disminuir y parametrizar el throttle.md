---
jira_key: "PED-425"
aliases: ["PED-425"]
summary: "API - Refactor - Disminuir y parametrizar el throttle"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-01-03 07:20"
updated: "2024-01-16 23:53"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-425"
---

# PED-425: API - Refactor - Disminuir y parametrizar el throttle

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-01-03 07:20 |
| Actualizado | 2024-01-16 23:53 |
| Etiquetas | ninguna |
| Jira | [PED-425](https://bluinc.atlassian.net/browse/PED-425) |

## Relaciones

- **Padre:** [[PED-2 - Bases y repositorios|PED-2]] Bases y repositorios

## Descripcion

Es frecuente al ingresar a la aplicación, o al moverse muy rápido por ella recibir el mensaje "Too Many Attempts".

Esto se debe a el efecto “throttle” que tiene el framework para evitar ciertos tipos de ataques.

Necesitamos poner aquellos parametros que producen esta limitacion en nuestro archivo de variables de entorno (.env) o si ya estan ahi identificarlos.

Una vez que esten ahi empezaremos por duplicar el tiempo y cantidad de peticiones para recibir menos veces ese mensaje.
