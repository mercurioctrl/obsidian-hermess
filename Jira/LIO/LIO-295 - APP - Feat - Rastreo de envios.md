---
jira_key: "LIO-295"
aliases: ["LIO-295"]
summary: "APP - Feat - Rastreo de envios"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-03-21 07:53"
updated: "2025-03-28 01:59"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-295"
---

# LIO-295: APP - Feat - Rastreo de envios

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-03-21 07:53 |
| Actualizado | 2025-03-28 01:59 |
| Etiquetas | ninguna |
| Jira | [LIO-295](https://bluinc.atlassian.net/browse/LIO-295) |

## Relaciones

- **Padre:** [[LIO-277 - Centro de ayuda|LIO-277]] Centro de ayuda
- **action item from:** [[LIO-294 - API - Feat - Recurso para permitir a usuarios sin login consultar el estado de|LIO-294]] API - Feat - Recurso para permitir a usuarios sin login consultar el estado de su envío desde el Centro de Ayuda



## Descripcion

A partir del recurso definido en [link](https://lioteam.atlassian.net/browse/LIO-294)  , vamos a desarrollar una nueva sección pública de rastreo de envíos.
Esta sección estará disponible sin necesidad de login y permitirá a cualquier usuario consultar el estado de su pedido mediante un buscador que acepte:

- Número de pedido de NB (no mencionar NB)


- Número de pedido de LO


- Número de tracking



Usaremos

```
GET {API_V4}/v4/findShipments
```

El objetivo es brindar una experiencia simplificada de seguimiento de envíos accesible desde el Centro de Ayuda, sin requerir autenticación.

**Criterios de aceptación:**

- Se debe mostrar un campo de búsqueda que acepte número de pedido (NB o LO) o número de tracking.


- La visualización del historial de envíos debe seguir el mismo formato utilizado en “Mi cuenta”.


- La sección debe estar disponible públicamente, sin requerir login.


- El recurso debe manejar casos de error (ej: pedido no encontrado, tracking inválido) con mensajes claros para el usuario.
