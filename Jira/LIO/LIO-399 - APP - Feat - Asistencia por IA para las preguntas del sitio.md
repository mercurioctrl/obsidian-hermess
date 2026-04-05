---
jira_key: "LIO-399"
aliases: ["LIO-399"]
summary: "APP - Feat - Asistencia por IA para las preguntas del sitio"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-07-30 08:52"
updated: "2025-08-12 10:42"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-399"
---

# LIO-399: APP - Feat - Asistencia por IA para las preguntas del sitio

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-07-30 08:52 |
| Actualizado | 2025-08-12 10:42 |
| Etiquetas | ninguna |
| Jira | [LIO-399](https://bluinc.atlassian.net/browse/LIO-399) |

## Relaciones

- **Padre:** [[LIO-391]] Desarrollos IA para LIO (Aleph)

## Descripcion

Basándonos en esta herramienta de ml 

[adjunto]
Decidimos hacer una herramienta parecida con la idea que si obtenes una respuesta mas rápida (cuando aun tenes el impulso de compra) aumentan mucho las posibilidades de realizar una conversión.

Pero en nuestro caso, la idea es enviar todas las preguntas para que se respondan por los vendedores, solo que mientras tanto (si es posible) responderemos con una respuesta instantánea generada por IA, para eso usaremos el recurso [link](https://bluinc.atlassian.net/browse/LIO-396) 

Para eso debemos tener en cuenta que si el recurso devuelve el parámetro `reliable:false` no debemos mostrar nada, solo enviamos la pregunta al vendedor como hacemos siempre, dado que la respuesta no es confiable. Pero si tengo `reliable:true`y `reply` entonces la mostramos y paso siguiente le enviamos la pregunta al vendedor de todas formas.


**Ejemplo de respuesta ideal**

```
{
  "reply": "Sí, viene con pasta térmica preaplicada en el cooler de fábrica.",
  "confidence": "high",
  "reliable": true
}
```

**Si no tengo suficiente informacion:**

```
{
  "reply": null,
  "reliable": false
}
```

Estos esquemas son ostentativos, así que todas las sugerencias son bienvenidas y los cambios deben aplicarse a la historia original.
