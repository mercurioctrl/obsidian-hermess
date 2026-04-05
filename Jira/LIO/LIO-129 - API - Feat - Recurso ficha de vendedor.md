---
jira_key: "LIO-129"
aliases: ["LIO-129"]
summary: "API - Feat - Recurso \"ficha de vendedor\""
status: "Backlog"
type: "Subtarea"
priority: "Medium"
assignee: "Sin asignar"
reporter: "Catriel Mercurio"
created: "2024-11-08 13:48"
updated: "2024-11-08 16:13"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-129"
---

# LIO-129: API - Feat - Recurso "ficha de vendedor"

| Campo | Valor |
|-------|-------|
| Estado | Backlog (Por hacer) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Sin asignar |
| Reportado por | Catriel Mercurio |
| Creado | 2024-11-08 13:48 |
| Actualizado | 2024-11-08 16:13 |
| Etiquetas | ninguna |
| Jira | [LIO-129](https://bluinc.atlassian.net/browse/LIO-129) |

## Relaciones

- **Padre:** [[LIO-124]] Calificaciones
- **action item from:** [[LIO-127]] APP - Research - Modelar el siguiente recurso con (solo) los requisitos necesarios para mostrar la ficha de vendedor

## Descripcion

```
{
    
    "horarioAtencion": "1", // mejorar porque trae cosas raras
    "cp": "1229",
    "avatar": 45,
    "reputacion": {
        "tiempoRespuestaChatPromedio": "Rápida", 
        "tiempoRespuestaPreguntasPromedio": "Muy Rápida",
        "puntajeChat": 5,
        "puntajePreguntas": 5,
        "puntajeCalificacion": 5, // Erecordar debe ser 1 | 3 | 5 correspondiente a las caritas de las calificaciones
        "puntajeSeguimiento": 0,
        "puntajeGlobal": 5,
        "ventas": true,
        "tasaDeRespuesta": "1.000",
        "productosDisponibles": 1199,
        "ventasConcretadas": 2259,
        "tiempoDeRespuesta": 1
    },
    "id": 447,
    "nombre": "Gears Store",
    "img": "4cfdc491658a2956333ec3654f06dfe8.png",
    "esReseller": true,
    "ciudad": {
        "nombre": "CABA",
    },
    "provincia": {
        "nombre": "CABA",
    },
    "pais": {
        "nombre": "ARGENTINA",
    }
}
```
