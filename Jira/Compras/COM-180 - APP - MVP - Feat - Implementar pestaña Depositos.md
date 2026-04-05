---
jira_key: "COM-180"
aliases: ["COM-180"]
summary: "APP - MVP - Feat - Implementar pestaña \"Depositos\""
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-05-05 08:48"
updated: "2025-05-19 17:59"
labels: ["MVPLaset"]
jira_url: "https://bluinc.atlassian.net/browse/COM-180"
---

# COM-180: APP - MVP - Feat - Implementar pestaña "Depositos"

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-05-05 08:48 |
| Actualizado | 2025-05-19 17:59 |
| Etiquetas | MVPLaset |
| Jira | [COM-180](https://bluinc.atlassian.net/browse/COM-180) |

## Relaciones

- **Padre:** [[COM-178]] Depositos
- **action item from:** [[COM-179]] API - MVP - Feat - Implementar endpoints REST CRUD para el recurso warehouses basado en la tabla [FP_Almacen]
- **is blocked by:** [[COM-183]] API-MVP-Refactor- Agregar al get de warehouses los nombres de pais,provincia y ciudad
- **relates to:** [[COM-188]] APP - MVP - Oportunidad de mejora - Depósitos -> al editar actualizar automáticamente 

## Descripcion

[adjunto]
Siguiendo lo realizado en [link](https://bluinc.atlassian.net/browse/COM-179)  se debe crear una pantalla donde pueda ver, crear, editar y eliminar depósitos,
**para** gestionar las ubicaciones físicas o virtuales del stock de forma centralizada y eficiente.

- La tabla debe mostrar las columnas: `code`, `name`, `address`, `cityCode`, `provinceCode`, `default`.


- Al cargar la vista, debe realizarse un `GET /v1/warehouses` y poblar la tabla.


- Si no hay resultados, debe mostrar mensaje: “No se encontraron depósitos”.


- Opción de búsqueda por nombre y código.
