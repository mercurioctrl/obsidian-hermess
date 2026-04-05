---
jira_key: "PED-73"
aliases: ["PED-73"]
summary: "API - Feat - Agregar \"item\" envío a una orden de compra"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-09-14 20:00"
updated: "2023-09-19 09:52"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-73"
---

# PED-73: API - Feat - Agregar "item" envío a una orden de compra

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-09-14 20:00 |
| Actualizado | 2023-09-19 09:52 |
| Etiquetas | ninguna |
| Jira | [PED-73](https://bluinc.atlassian.net/browse/PED-73) |

## Relaciones

- **Padre:** [[PED-58 - Agregar Editar Envío en las ordenes de compra|PED-58]] Agregar / Editar Envío en las ordenes de compra

## Descripcion

Este recurso no se trata de agregar un envío realmente un una etiqueta de envío ni mucho menos. 

Solo agregara un ítem a la orden dentro de la tabla `[NewBytes_DBF].[dbo].[pedclil]` (el ítem en cuestión es el `102048`, pero debe poder definirse como se hace aca). Ver metodo [https://github.com/New-Bytes/sitio-api-rest-v3/blob/main/app/src/Service/ShoppingCartService.php#L332](https://github.com/New-Bytes/sitio-api-rest-v3/blob/main/app/src/Service/ShoppingCartService.php#L332)

Pero al escribir `[NewBytes_DBF].[dbo].[pedclil]` la columna `cdetalle` que diga el nombre del currier, en lugar del nombre del item.

Adicionalmente debemos agregar en `[NewBytes_DBF].[dbo].[pedclit]`

```
medioEnvioId,
idDirCliNbWeb,
packageWeight,
packageSize,
amountPackages
```

Crearemos un recurso tipo

```
POST {{API_URL}}/order/{branch}-{order}/addShipping
```

```
{
  idDirCliNbWeb: 3434,
  shippingMethodId: 3233
}
```

Que nos permita agregarlo.

En caso de ya existir un envío dentro del pedido, se (elimina) re-calcula y se remplaza.
