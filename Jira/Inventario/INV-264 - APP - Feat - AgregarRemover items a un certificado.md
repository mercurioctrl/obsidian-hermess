---
jira_key: "INV-264"
aliases: ["INV-264"]
summary: "APP - Feat - Agregar/Remover items a un certificado"
status: "Finalizada"
type: "Tarea"
priority: "High"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-12-01 08:02"
updated: "2025-12-03 10:48"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-264"
---

# INV-264: APP - Feat - Agregar/Remover items a un certificado

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | High |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-12-01 08:02 |
| Actualizado | 2025-12-03 10:48 |
| Etiquetas | ninguna |
| Jira | [INV-264](https://bluinc.atlassian.net/browse/INV-264) |

## Relaciones

- **Padre:** [[INV-260]] Certificados eléctricos por Qr
- **action item from:** [[INV-263]] API - Feat - Agregar/Remover items a un certificado

## Descripcion

En la pestaña de *Certificados Eléctricos* del inventario se deberá permitir **asociar y desasociar ítems de producto a un certificado**, usando los endpoints:

- ```
POST /electricalCertificate/{id}/items
```


- ```
DELETE /electricalCertificate/{id}/items
```



**UI / Acceso**

- El accionable para gestionar ítems puede estar en:

- **Botón derecho** sobre el registro del certificado, y/o


- Un **botón/acción que abra un modal** desde la fila del listado.




- Al abrir el modal se mostrará:

- Información básica del certificado.


- **Listado de ítems asociados.**


- Buscador o selector para agregar nuevos ítems.





**Criterios de aceptación**

- Existe accionable por certificado para abrir el modal de gestión de ítems.


- Se pueden agregar ítems usando el endpoint de asociación.


- Cada ítem listado puede eliminarse desde un accionable individual en el modal.


- La UI se actualiza en tiempo real según la respuesta de la API.
