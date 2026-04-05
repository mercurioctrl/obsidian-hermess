---
jira_key: "NBWEB-217"
aliases: ["NBWEB-217"]
summary: "API - Aplicar intereses extra según el medio de pago"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-06-01 14:24"
updated: "2022-06-26 20:50"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-217"
---

# NBWEB-217: API - Aplicar intereses extra según el medio de pago

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-06-01 14:24 |
| Actualizado | 2022-06-26 20:50 |
| Etiquetas | ninguna |
| Jira | [NBWEB-217](https://bluinc.atlassian.net/browse/NBWEB-217) |

## Relaciones

- **Padre:** [[NBWEB-1 - API - Carrito de compras|NBWEB-1]] API - Carrito de compras

## Descripcion

Cuando se ejecuta el recurso

```
{{API_URL}}/v1/carrito/procesar
```

se debe agregar el ítem (109455 en la tabla `newbytes_dbf.dbo.articulo`) interés, en `pedclil`, pero marcando el precio  como el interes total por el total del pedido final.

Una vez que tenemos el valor final, debemos quitarle el 21% de iva y luego guardarlo en `pedclil` con ese precio

Para saber el interés de un producto se utiliza la columna INTERÉS de la tabla `[NEW_BYTES].[dbo].[MS_FORMASPAGO_REMITOS_VENDEDORES]`
