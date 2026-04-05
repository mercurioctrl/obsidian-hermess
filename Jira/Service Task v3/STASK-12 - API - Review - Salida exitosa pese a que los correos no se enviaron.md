---
jira_key: "STASK-12"
aliases: ["STASK-12"]
summary: "API - Review - Salida \"exitosa\" pese a que los correos no se enviaron"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-02-14 15:15"
updated: "2025-02-21 10:49"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/STASK-12"
---

# STASK-12: API - Review - Salida "exitosa" pese a que los correos no se enviaron

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-02-14 15:15 |
| Actualizado | 2025-02-21 10:49 |
| Etiquetas | ninguna |
| Jira | [STASK-12](https://bluinc.atlassian.net/browse/STASK-12) |

## Relaciones

- **Padre:** [[STASK-2]] Correos

## Descripcion

Debugueado arriba, parece ser que por un tema de ruteo (nada que ver con el código) no se estaban enviando los correos.. osea que daba un error de conexion SMTP. Esto fue arreglado y los correos ya llegan correctamente, pero de todas maneras fallo todo el tiempo dando el mensaje “Emails enviados correctamente” y por eso no nos habiamos dado cuenta hasta recien.

Solo habria que hacer un arreglo para que evalue el criterio de envio de manera correcta segun la salida de phpMailer (se puede probar facilmente cambiando algun dato para que falle la conexion al smtp)

[adjunto]
