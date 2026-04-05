---
jira_key: "LIO-392"
aliases: ["LIO-392"]
summary: "APIv4 - Research - Investigar integración con OpenAI para verificar compatibilidad de productos (no es lo mismo que el armador)"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-07-25 09:40"
updated: "2025-08-04 10:31"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-392"
---

# LIO-392: APIv4 - Research - Investigar integración con OpenAI para verificar compatibilidad de productos (no es lo mismo que el armador)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-07-25 09:40 |
| Actualizado | 2025-08-04 10:31 |
| Etiquetas | ninguna |
| Jira | [LIO-392](https://bluinc.atlassian.net/browse/LIO-392) |

## Relaciones

- **Padre:** [[LIO-391 - Desarrollos IA para LIO (Aleph)|LIO-391]] Desarrollos IA para LIO (Aleph)
- **has action item:** [[LIO-395 - APP - Refactor - Asistente de compatibilidad en el carrito de compras|LIO-395]] APP - Refactor - Asistente de compatibilidad en el carrito de compras
- **has action item:** [[LIO-404 - API - Research - Implementacion deepseek para el asistente de compatibilidad|LIO-404]] API - Research - Implementacion deepseek para el asistente de compatibilidad

## Descripcion

Necesitamos realizar un *research* técnico en una **rama separada** de nuestra API Laravel que implemente un recurso para consultar la compatibilidad de productos utilizando la API de OpenAI ([[GPT-4]]).


El objetivo es que, dado un carrito con productos (cada uno con título, precio y SKU), se construya un prompt adecuado y se obtenga una respuesta breve y profesional simulando un experto en hardware.

**📌 Requisitos del recurso:**

- Ruta REST tipo `POST /aleph/compatibility`


- Recibe un JSON con un array de productos del carrito (`titulo`, `sku`, `precio`)


- Construye un *prompt* dinámico con esa información


- Llama a OpenAI (modelo [[GPT-4]]) con ese *prompt*


- Devuelve la respuesta textual generada por la IA en un campo `respuesta`


- La integración debe estar contenida en una **rama de research**, sin afectar el main



**Se obtiene una respusta de este tipo**

```
{
  "respuesta": "✅ ¡Todo en orden! El procesador AMD Ryzen 5 5600X es compatible con memorias DDR4 como la Netac 3200MHz, y la fuente Thermaltake TR2 600W brinda energía suficiente para esta configuración sin problemas."
}

```

`Role de ejemplo: Respondé como experto en hardware sobre la compatibilidad de los items. Respondé en 2 oraciones como máximo, en tono profesional, directo y estrictamente neutral. No uses frases de cortesía, introducciones ni conclusiones. Limitate a indicar si los productos son compatibles o no, y por qué.`



**Token de prueba de openAi=** `proj_RyXU47FSADnxOAJqJY5OYe9k`
