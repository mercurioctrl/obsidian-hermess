---
jira_key: "NBWEB-545"
aliases: ["NBWEB-545"]
summary: "API - Refactor - Precio especial desde costo"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-05-23 06:54"
updated: "2023-08-04 09:42"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-545"
---

# NBWEB-545: API - Refactor - Precio especial desde costo

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-05-23 06:54 |
| Actualizado | 2023-08-04 09:42 |
| Etiquetas | ninguna |
| Jira | [NBWEB-545](https://bluinc.atlassian.net/browse/NBWEB-545) |

## Relaciones

- **Padre:** [[NBWEB-544]] Refactor - Precios especiales por cliente y para marketplace
- **blocks:** [[SNB-783]] Integracion - Producteca

## Descripcion

Así como se hace con `specialPrice` que se encuentra en la tabla `[NewBytes_DBF].[dbo].[clientes]` se debe agregar una nueva columna que llamaremos: `specialPriceFromCost`.

El concepto es casi el mismo, se trata de un porcentual de incremento (`specialPriceFromCost`) pero en lugar de ser sobre el precio de la lista correspondiente (como `specialPrice`) este caso se hace sobre el costo del producto directamente (usando `[NewBytes_DBF].[dbo].[articulo].ncosteprom`)

Es decir

```
precioNuevo = ncosteprom * (1 + specialPriceFromCost/100)
```

Este precio, es excluyente de todos los otros. Cuando un cliente lo tiene (caso contrario debe estar en NULL), es el único precio que voy a tomar en cuenta y por lo tanto no necesito calcular el resto. Ademas, en algunos casos puede ser cero por si necesito vender a un socio a costo y no debe fallar en ese caso.

Al tener que meter esta lógica en **App\Controller\Price::getPrice **nos conviene que sea lo mas ágil posible porque se itera mucho
