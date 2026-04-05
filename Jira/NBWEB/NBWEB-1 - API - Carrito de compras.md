---
jira_key: "NBWEB-1"
aliases: ["NBWEB-1"]
summary: "API - Carrito de compras"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-03-21 09:35"
updated: "2022-07-11 09:13"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-1"
---

# NBWEB-1: API - Carrito de compras

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-03-21 09:35 |
| Actualizado | 2022-07-11 09:13 |
| Etiquetas | ninguna |
| Jira | [NBWEB-1](https://bluinc.atlassian.net/browse/NBWEB-1) |

## Relaciones

- **Subtarea:** [[NBWEB-40 - Crear Carrito de compras|NBWEB-40]] Crear Carrito de compras
- **Subtarea:** [[NBWEB-41 - Cambiar Carrito de compras|NBWEB-41]] Cambiar Carrito de compras
- **Subtarea:** [[NBWEB-42 - Eliminar Carrito de compras|NBWEB-42]] Eliminar Carrito de compras
- **Subtarea:** [[NBWEB-43 - Agregar producto al carrito|NBWEB-43]] Agregar producto al carrito
- **Subtarea:** [[NBWEB-44 - API - Procesar carrito de compras (enviar pedido)|NBWEB-44]] API - Procesar carrito de compras (enviar pedido)
- **Subtarea:** [[NBWEB-45 - Chequear disponibilidad en carrito de compras|NBWEB-45]] Chequear disponibilidad en carrito de compras
- **Subtarea:** [[NBWEB-46 - Traer subtotales del carrito|NBWEB-46]] Traer subtotales del carrito
- **Subtarea:** [[NBWEB-47 - Listar contenido del carrito|NBWEB-47]] Listar contenido del carrito
- **Subtarea:** [[NBWEB-68 - Descargar Carrito en TXT|NBWEB-68]] Descargar Carrito en TXT
- **Subtarea:** [[NBWEB-138 - Vaciar Carrito|NBWEB-138]] Vaciar Carrito
- **Subtarea:** [[NBWEB-139 - Agregar comentario al procesar el carrito|NBWEB-139]] Agregar comentario al procesar el carrito
- **Subtarea:** [[NBWEB-217 - API - Aplicar intereses extra según el medio de pago|NBWEB-217]] API - Aplicar intereses extra según el medio de pago
- **Subtarea:** [[NBWEB-243 - API - Refactor - Procesar carrito|NBWEB-243]] API - Refactor - Procesar carrito
- **blocks:** [[NBWEB-80 - Cotizador de carritos de compra|NBWEB-80]] Cotizador de carritos de compra
- **blocks:** [[NBWEB-140 - APP - Conexión con el carrito|NBWEB-140]] APP - Conexión con el carrito

## Descripcion

```
GET {{API_URL}}/carrito/
```

Se trata de todos los recursos necesarios para operar el carrito de compras del sitio y procesar la orden de compra.
