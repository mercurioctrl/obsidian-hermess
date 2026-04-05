---
jira_key: "EXP-11"
aliases: ["EXP-11"]
summary: "Feat - Serializar entrada de mercadería"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Guillermo Avila"
reporter: "Catriel Mercurio"
created: "2022-10-31 14:05"
updated: "2024-01-17 07:36"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-11"
---

# EXP-11: Feat - Serializar entrada de mercadería

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Guillermo Avila |
| Reportado por | Catriel Mercurio |
| Creado | 2022-10-31 14:05 |
| Actualizado | 2024-01-17 07:36 |
| Etiquetas | ninguna |
| Jira | [EXP-11](https://bluinc.atlassian.net/browse/EXP-11) |

## Relaciones

- **Padre:** [[EXP-5]] Ingreso de mercaderia
- **Subtarea:** [[EXP-42]] API - Feat - Ingresar nuevos seriales a un producto, dentro de un pedido
- **Subtarea:** [[EXP-43]] APP - Feat - Ingresar nuevos seriales a un producto, dentro de un pedido
- **Subtarea:** [[EXP-44]] API - Feat - Ingresar nuevos seriales POR INTERVALO a un producto, dentro de un pedido
- **Subtarea:** [[EXP-45]] APP - Feat - Ingresar nuevos seriales POR INTERVALO a un producto, dentro de un pedido
- **Subtarea:** [[EXP-47]] API - Feat - Ingresar nuevos seriales a un producto NO SERIALIZADO, dentro de un pedido
- **Subtarea:** [[EXP-48]] APP - Feat - Ingresar nuevos seriales a un producto NO SERIALIZADO, dentro de un pedido
- **Subtarea:** [[EXP-56]] API - Feat - Ingresar nuevos seriales MÚLTIPLES POR INTERVALO a un producto, dentro de un pedido
- **Subtarea:** [[EXP-57]] APP - Feat - Ingresar nuevos seriales MÚLTIPLES POR INTERVALO a un producto, dentro de un pedido
- **Subtarea:** [[EXP-65]] API - Feat - Eliminar un serial o intervalo de seriales
- **Subtarea:** [[EXP-92]] API - Refactor - No dejar serializar un item que no tiene cargado al menos uno de los codigos unicos
- **Subtarea:** [[EXP-209]] APP - Refactor - Agregar opcion para imprimir seriales dobles
- **Subtarea:** [[EXP-388]] APP - Refactor - Evitar cierre y perdida de seriales
- **Subtarea:** [[EXP-447]] API - Refactor - No dejar serializar un item que no tiene pesos,medidas y cantidad por bulto
- **Subtarea:** [[EXP-448]] APP - Refactor - Cargar pesos y medidas del producto si no existen cuando se serializan y no los tienen
- **Subtarea:** [[EXP-449]] API - Refactor - Permitir editar pesos y medidas del item igual que ean/sku/gtin
- **Subtarea:** [[EXP-466]] APP - Refactor - Leer seriales con divisor especial (por ej: masterbox AMD)
- **Subtarea:** [[EXP-467]] APP - Refactor - Mejora de performance al abrir modal para ver los serials 
- **Subtarea:** [[EXP-525]] API - Refactor - Agregar stockWarehouseId al ingreso de seriales 
- **Subtarea:** [[EXP-526]] APP - Refactor - Agregar stockWarehouseId al ingreso de seriales 

## Descripcion

Conjunto de funcionalidades que se encargan de la carga de seriales por parte del personal de deposito.

Lo que se hace es cargar los seriales mediantes una pistola u archivo, para esto se buscaran los pedidos en la grilla [link](https://lioteam.atlassian.net/browse/EXP-34) y se seleccionara el producto al cual queremos cargarle los seriales, una vez dentro con botón derecho abriremos otro modal de carga.
