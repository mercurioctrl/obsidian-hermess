---
jira_key: "LIO-395"
aliases: ["LIO-395"]
summary: "APP - Refactor - Asistente de compatibilidad en el carrito de compras"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-07-29 08:30"
updated: "2025-08-04 10:30"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-395"
---

# LIO-395: APP - Refactor - Asistente de compatibilidad en el carrito de compras

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-07-29 08:30 |
| Actualizado | 2025-08-04 10:30 |
| Etiquetas | ninguna |
| Jira | [LIO-395](https://bluinc.atlassian.net/browse/LIO-395) |

## Relaciones

- **Padre:** [[LIO-391]] Desarrollos IA para LIO (Aleph)
- **action item from:** [[LIO-394]] API - Refactor - Pequeños ajuste de role y otros parametros
- **action item from:** [[LIO-392]] APIv4 - Research - Investigar integración con OpenAI para verificar compatibilidad de productos (no es lo mismo que el armador)
- **has action item:** [[LIO-400]] API - Refactor - Ajustes para el asistente de compatibilidad, ejecutar la consulta solo si parece ser relevante

## Descripcion

Utilizando el recurso [link](https://bluinc.atlassian.net/browse/LIO-394) agregaremos un apartado para el asistente de compatibilidad en nuestro carrito.

La idea es enviar el contenido del mismo de esta manera o similar

```
 {"productos" :
  [
    {
      "titulo": "PROCESADOR INTEL (LGA1200) CORE I3 10105",
      "sku": "BX8070110105",
      "precio": 299.99
    },
    {
      "titulo": "Memoria RAM DDR4 Netac 16GB 3200MHz",
      "sku": "NETAC-16GB-3200",
      "precio": 89.99
    },
    {
      "titulo": "Fuente Thermaltake TR2 600W",
      "sku": "TT-TR2-600W",
      "precio": 79.99
    },
    {
      "titulo": "MOTHER GIGABYTE (AM4) A520M K V2 1.1",
      "sku": "A520M K V2 1.1",
      "precio": 79.99
    }
  ]}
```

Para obtener una respuesta del siguiente tipo

```
{
  "compatibility": false,
  "message": "El análisis con IA detecta que los productos no son compatibles entre sí. El procesador Intel Core i3 10105 utiliza socket LGA1200, pero la placa madre Gigabyte A520M K V2 tiene socket AM4 para procesadores AMD."
}
```



Ejemplos orientativos auto-generados

Estos esquemas son ostentativos, así que todas las sugerencias son bienvenidas y los cambios deben aplicarse a la historia original.

[adjunto]
[adjunto]
