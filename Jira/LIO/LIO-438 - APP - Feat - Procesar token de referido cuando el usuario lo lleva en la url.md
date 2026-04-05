---
jira_key: "LIO-438"
aliases: ["LIO-438"]
summary: "APP - Feat - Procesar token de referido cuando el usuario lo lleva en la url (con y sin login)"
status: "Finalizada"
type: "Tarea"
priority: "High"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-08-31 23:08"
updated: "2025-09-11 17:46"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-438"
---

# LIO-438: APP - Feat - Procesar token de referido cuando el usuario lo lleva en la url (con y sin login)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | High |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-08-31 23:08 |
| Actualizado | 2025-09-11 17:46 |
| Etiquetas | ninguna |
| Jira | [LIO-438](https://bluinc.atlassian.net/browse/LIO-438) |

## Relaciones

- **Padre:** [[LIO-408]] Referidos
- **action item from:** [[LIO-414]] API - Feat - Guardar token referido para un usuario ya logueado
- **action item from:** [[LIO-413]] API  - Refactor - Recibir token de referido al hacer login (este caso es para cuando esta guardado en localStorage, porque aun no logueo)

## Descripcion

Se debe guardar y enviar el token de referido 

Cuando el usuario ingrese al sitio con un enlace que tiene el atributo `refer`(ejemplo: `libreopcion.com.ar?producto_35434&refer=lucas123`) entonces el front ejecutara nuestro recurso para avisarle a backend que debe almacenarlo si aun no lo tiene

De esta forma podremos registrarlo en caso de que no exista.
[link](https://bluinc.atlassian.net/browse/LIO-414) 

Si no esta logueado, lo guardaremos hasta poder enviarlo una vez que haga el login con [link](https://bluinc.atlassian.net/browse/LIO-413)
