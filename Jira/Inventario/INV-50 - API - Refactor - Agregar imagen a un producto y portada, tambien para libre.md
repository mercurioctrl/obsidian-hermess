---
jira_key: "INV-50"
aliases: ["INV-50"]
summary: "API - Refactor - Agregar imagen a un producto y portada, tambien para libre opcion"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-01-12 08:33"
updated: "2024-02-08 13:58"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-50"
---

# INV-50: API - Refactor - Agregar imagen a un producto y portada, tambien para libre opcion

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-01-12 08:33 |
| Actualizado | 2024-02-08 13:58 |
| Etiquetas | ninguna |
| Jira | [INV-50](https://bluinc.atlassian.net/browse/INV-50) |

## Relaciones

- **Padre:** [[INV-38]] Feat - Buscar imagenes en repositorios remotos
- **is blocked by:** [[INV-55]] API - Agregar imagen a un producto y portada, también para libre opción - No se agrega a LO

## Descripcion

Segun lo que estuvimos viendo ayer, parece que si bien se cumple el circuito que te permite agregar imagenes a NB, no lo hace de forma inmediata para libreopcion, sino que este depende de una sincronizacion que se produce de madrugada.

Para esto Refactorizaremos todos los recursos que agreguen imagenes en `[NB_WEB].[dbo].[fotos_productos]` para que en el mismo acto, hagan lo mismo sobre la tabla ` [CS].[dbo].[productosFotos]`
