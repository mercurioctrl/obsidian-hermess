---
jira_key: "LIO-213"
aliases: ["LIO-213"]
summary: "API - Feat - Mover recurso \"vendedor\" de Legacy y V4"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-02-11 10:01"
updated: "2025-02-21 15:47"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-213"
---

# LIO-213: API - Feat - Mover recurso "vendedor" de Legacy y V4

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-02-11 10:01 |
| Actualizado | 2025-02-21 15:47 |
| Etiquetas | ninguna |
| Jira | [LIO-213](https://bluinc.atlassian.net/browse/LIO-213) |

## Relaciones

- **Padre:** [[LIO-212]] Perfil de vendedor
- **has action item:** [[LIO-214]] APP - Refactor - Actualizar todos aquellos lugares del sitio (principalmente la ficha de reputacion, que utilizan el recurso vendedor por el nuevo de v4
- **has action item:** [[LIO-230]] API - Mover recurso "vendedor" de Legacy y V4 - Error de tipeo al filtrar por vendedor

## Descripcion

Moveremos el recurso 

```
GET {API_LEGACY}/vendedores/ficha/{vendedor}
```

```
{
"retiroPorLocal": true,
"horarioAtencion": "1",
"cp": "1407",
"direccion": "Calle Falsa 123",
"ciudadID": null,
"provinciaID": null,
"paisID": null,
"avatar": 18,
"productos": 0,
"reputacion": {
"tiempoRespuestaChatPromedio": "Regular",
"tiempoRespuestaPreguntasPromedio": "Regular",
"puntajeChat": 4,
"puntajePreguntas": 2,
"puntajeCalificacion": 5,
"puntajeSeguimiento": 0,
"puntajeGlobal": 5,
"ventas": true,
"tasaDeRespuesta": "2.000",
"productosDisponibles": 0,
"ventasConcretadas": 58,
"tiempoDeRespuesta": 22
},
"calificaciones": [],
"id": 22,
"nombre": "BsAsPC",
"uri": "buenos-aires-pc",
"key": 22,
"img": "67950734a4fe424a34f619b9889c004e.jpeg",
"esReseller": true,
"total": 0,
"ciudad": {
"id": 20832,
"nombre": "CABA",
"provincia_id": 1,
"total": 0
},
"provincia": {
"id": 1,
"key": 1,
"nombre": "CABA",
"pais_id": 0,
"total": 0,
"ciudad_defecto_id": 0
},
"pais": {
"id": null,
"nombre": null,
"total": null
}
}
```

Ejemplo: [https://api.gamma.libreopcion.com/vendedores/ficha/22](https://api.gamma.libreopcion.com/vendedores/ficha/22)

```
GET {{API_URL}}/v4/seller/{vendedor}
```

Tener en cuenta que algunos datos cambiaron en formato y origen como por ejemplo "horarioAtencion": "Lunes: 09:00 - 18:00 | Martes: 09:00 - 18:00" (ver recurso [https://gamma.api4.libreopcion.com/v4/myStore](https://gamma.api4.libreopcion.com/v4/myStore))
