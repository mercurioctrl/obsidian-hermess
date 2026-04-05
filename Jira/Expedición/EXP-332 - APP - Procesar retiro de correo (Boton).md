---
jira_key: "EXP-332"
aliases: ["EXP-332"]
summary: "APP - Procesar retiro de correo (Boton)"
status: "CodeReview"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2023-07-05 09:04"
updated: "2023-07-07 16:01"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-332"
---

# EXP-332: APP - Procesar retiro de correo (Boton)

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2023-07-05 09:04 |
| Actualizado | 2023-07-07 16:01 |
| Etiquetas | ninguna |
| Jira | [EXP-332](https://bluinc.atlassian.net/browse/EXP-332) |

## Relaciones

- **Padre:** [[EXP-325 - Feat - Pestaña seguimiento|EXP-325]] Feat - Pestaña seguimiento

## Descripcion

Agregaremos un “boton” para utilizar el recurso [link](https://lioteam.atlassian.net/browse/EXP-327)  en la seccion seguimiento 

[adjunto]
En el mismo nivel que pusimos el de “Mover seriales” en la otra sección.

Básicamente lo que hace es abrir un modal con un formulario, que al enviar [link](https://lioteam.atlassian.net/browse/EXP-327) interpone el token de autorizacion. O bien ya esta en el formulario.

El formulario debe tener un Campo para cargar o pistoletear los números de tracking y un select para elegir el correo (OCA,Andreani, Entregar, etc)

Una vez generado el retiro, lanza para imprimir el archivo generado con [link](https://lioteam.atlassian.net/browse/EXP-328)
