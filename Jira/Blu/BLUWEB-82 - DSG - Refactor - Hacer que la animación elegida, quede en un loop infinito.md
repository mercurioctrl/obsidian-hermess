---
jira_key: "BLUWEB-82"
aliases: ["BLUWEB-82"]
summary: "DSG - Refactor - Hacer que la animación elegida, quede en un loop infinito"
status: "LISTO"
type: "Subtarea"
priority: "Highest"
assignee: "Belu Ontivero"
reporter: "Catriel Mercurio"
created: "2025-07-15 14:31"
updated: "2025-07-17 20:19"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/BLUWEB-82"
---

# BLUWEB-82: DSG - Refactor - Hacer que la animación elegida, quede en un loop infinito

| Campo | Valor |
|-------|-------|
| Estado | LISTO (Listo) |
| Tipo | Subtarea |
| Prioridad | Highest |
| Asignado | Belu Ontivero |
| Reportado por | Catriel Mercurio |
| Creado | 2025-07-15 14:31 |
| Actualizado | 2025-07-17 20:19 |
| Etiquetas | ninguna |
| Jira | [BLUWEB-82](https://bluinc.atlassian.net/browse/BLUWEB-82) |

## Relaciones

- **Padre:** [[BLUWEB-13 - Sitio Web_Etapa 0|BLUWEB-13]] Sitio Web_Etapa 0

## Descripcion

Animación elegida:

[adjunto]
> Editar la animación que avance hasta el final y luego regrese exactamente por el mismo recorrido, de modo que al repetirse no se note el punto de inicio/fin.


- **Dos mitades iguales**

- La primera mitad recorre la animación “hacia adelante” desde el principio hasta el final.


- La segunda mitad recorre el mismo trayecto, pero en sentido inverso.




- **Efecto ping‑pong**

- Pensar en esto como un “efecto ping‑pong” o “yoyo”: el elemento avanza, toca el tope y luego regresa.




- **Empalme invisible**

- Al terminar la segunda mitad, la posición y el estado del elemento coinciden con los del punto inicial.


- Esto permite que, al encadenar la animación (loop), no haya salto ni corte visible.




- **Detalles a considerar**

- Mantener la misma velocidad al regresar para que el rebote sea uniforme.


- Asegurarse de que no haya “stutter” o fotogramas duplicados en el punto de volteo.
