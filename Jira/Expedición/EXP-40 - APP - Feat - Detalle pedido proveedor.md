---
jira_key: "EXP-40"
aliases: ["EXP-40"]
summary: "APP - Feat - Detalle pedido proveedor"
status: "Gamma"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2022-11-04 15:45"
updated: "2023-01-11 16:01"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-40"
---

# EXP-40: APP - Feat - Detalle pedido proveedor

| Campo | Valor |
|-------|-------|
| Estado | Gamma (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2022-11-04 15:45 |
| Actualizado | 2023-01-11 16:01 |
| Etiquetas | ninguna |
| Jira | [EXP-40](https://bluinc.atlassian.net/browse/EXP-40) |

## Relaciones

- **Padre:** [[EXP-10]] Feat - Listar pedidos (despachos) proveedores
- **is blocked by:** [[EXP-38]] API - Feat - Detalle pedido proveedor

## Descripcion

Basándonos en [link](https://lioteam.atlassian.net/browse/EXP-38) se debe construir un modal con la informacion para el detalle de los pedidos de compra.

Básicamente mostraremos informacion del contenido de un pedido de proveedor.

Mostraremos una fila por producto con la siguiente informacion:

- id interno


- Titulo


- sku


- imagen


- cantidad comprada


- cantidad serializada


- si es “no serializable”



Un modal del sistema viejo que se parece “un poco” es este:

[adjunto]


Aunque no le prestes tanta atención porque es demasiado básico.

**Cosas que estaría bueno implementar:**

Que puedas seguir el enlace del producto al sitio.

Que muestren en el modal informacion de la cabecera del pedido ya que la tenes en contexto.
