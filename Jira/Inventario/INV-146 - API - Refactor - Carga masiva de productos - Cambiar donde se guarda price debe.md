---
jira_key: "INV-146"
aliases: ["INV-146"]
summary: "API - Refactor - Carga masiva de productos - Cambiar donde se guarda \"price\" debe ser ncosteprom"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-10-02 06:53"
updated: "2024-10-09 11:39"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-146"
---

# INV-146: API - Refactor - Carga masiva de productos - Cambiar donde se guarda "price" debe ser ncosteprom

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-10-02 06:53 |
| Actualizado | 2024-10-09 11:39 |
| Etiquetas | ninguna |
| Jira | [INV-146](https://bluinc.atlassian.net/browse/INV-146) |

## Relaciones

- **Padre:** [[INV-23]] Aplicacion de inventario
- **has action item:** [[SNB-2366]] Importador masivo de productos

## Descripcion

Guardaremos price en `[NewBytes_DBF].[dbo].[articulo].ncosteprom` de forma tal que la columna mapeada a ese concepto se guarde en el costo promedio
