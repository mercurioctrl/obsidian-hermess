---
jira_key: "NBWEB-243"
aliases: ["NBWEB-243"]
summary: "API - Refactor - Procesar carrito"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-06-08 14:32"
updated: "2022-06-26 20:16"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-243"
---

# NBWEB-243: API - Refactor - Procesar carrito

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-06-08 14:32 |
| Actualizado | 2022-06-26 20:16 |
| Etiquetas | ninguna |
| Jira | [NBWEB-243](https://bluinc.atlassian.net/browse/NBWEB-243) |

## Relaciones

- **Padre:** [[NBWEB-1 - API - Carrito de compras|NBWEB-1]] API - Carrito de compras
- **blocks:** [[NBWEB-215 - APP - Paginas de destino para los pagos|NBWEB-215]] APP - Paginas de destino para los pagos

## Descripcion

Estuvimos hablando con   de tipificar la forma en la que procesamos la salida para poder retornar un estado y detalle para cada operación, al momento de crear una orden de compra.



```
    {
    "status": "approved",
    "status_detail_convert": "¡Listo! Se acreditó tu pago. En tu resumen verás
    }
```

Para poder asociar esto a la salida, en el caso de que puedas procesar el carrito con éxito, vamos a traernos ambos parámetros por asociación con el medio de pago (se considera que la compra esta realizada una vez pagada).

Los parámetros los vamos a ubicar en la tabla 

`[NEW_BYTES].[dbo].[MS_FORMASPAGO_REMITOS_VENDEDORES]`

y son dos

`succces_status `y `succes_status_detail_convert`

## La columna `succces_status`

Puede tener los valores 

- approved


- in_process


- rejected


- pending 



## La columna `succes_status_detail_convert`

Puede ser cualquier string máximo 256 caracteres
