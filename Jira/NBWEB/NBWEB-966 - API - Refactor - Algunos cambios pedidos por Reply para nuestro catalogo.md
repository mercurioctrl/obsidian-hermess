---
jira_key: "NBWEB-966"
aliases: ["NBWEB-966"]
summary: "API - Refactor - Algunos cambios pedidos por Reply para nuestro catalogo"
status: "Finalizada"
type: "Tarea"
priority: "Highest"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-04-21 08:44"
updated: "2025-04-23 14:32"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-966"
---

# NBWEB-966: API - Refactor - Algunos cambios pedidos por Reply para nuestro catalogo

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Highest |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-04-21 08:44 |
| Actualizado | 2025-04-23 14:32 |
| Etiquetas | ninguna |
| Jira | [NBWEB-966](https://bluinc.atlassian.net/browse/NBWEB-966) |

## Relaciones

- **Padre:** [[NBWEB-602]] Sitio Web
- **action item from:** [[NBWEB-960]] API - Feat - Generar catálogo exclusivo para ReplyLatam con precio en pesos final y columnas adicionales

## Descripcion

Haremos algunos cambios que surgen de las pruebas realizadas por REPLY y a pedido de ellos para facilitar la operacion sobre el repositorio

[https://api.nbe.com.ar/v1/priceListReplyLatam/4520348d5e5ab6d973b54aec33dcd3](https://api.nbe.com.ar/v1/priceListReplyLatam/4520348d5e5ab6d973b54aec33dcd3)

Sacaremos la columna llamada “MONEDA” ya que al ser solo en pesos final, confunde.Agregaremos una columna extra llamada “Descripción” con la descripción generada por IAMoveremos las “filas” que tienen la categoría a una columna llamada “Categoria” ya que aparentemente si bien habian aprobado este diseño, parecen tener problemas para tomarla correctamente.[adjunto]
