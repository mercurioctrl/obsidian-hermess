---
jira_key: "INV-289"
aliases: ["INV-289"]
summary: "API - Refactor - Kit con "
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-12-18 07:34"
updated: "2025-12-22 21:02"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-289"
---

# INV-289: API - Refactor - Kit con 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-12-18 07:34 |
| Actualizado | 2025-12-22 21:02 |
| Etiquetas | ninguna |
| Jira | [INV-289](https://bluinc.atlassian.net/browse/INV-289) |

## Relaciones

- **Padre:** [[INV-253]] Crear y modificar Kits
- **action item from:** [[INV-258]] API - Feat - SyncUp para actualizar el stock (nstock) de kits según el stock de sus componentes

## Descripcion

Modificar el endpoint de **syncUp de itemsKits** para eliminar el login y utilizar autenticación mediante **token configurado en variables de entorno**, alineándolo con el resto de los recursos de syncUp.

---

### Endpoint del syncUp

```
POST {API_URL}/itemsKits/syncUp
```
