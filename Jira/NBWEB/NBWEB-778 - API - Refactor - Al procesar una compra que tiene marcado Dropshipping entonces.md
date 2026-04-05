---
jira_key: "NBWEB-778"
aliases: ["NBWEB-778"]
summary: "API - Refactor - Al procesar una compra que tiene marcado \"Dropshipping\" entonces debo marcar la direccion como \"Dropshipping\""
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-07-23 13:37"
updated: "2024-07-24 15:39"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-778"
---

# NBWEB-778: API - Refactor - Al procesar una compra que tiene marcado "Dropshipping" entonces debo marcar la direccion como "Dropshipping"

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-07-23 13:37 |
| Actualizado | 2024-07-24 15:39 |
| Etiquetas | ninguna |
| Jira | [NBWEB-778](https://bluinc.atlassian.net/browse/NBWEB-778) |

## Relaciones

- **Padre:** [[NBWEB-777 - Carrito|NBWEB-777]] Carrito
- **blocks:** [[NBWEB-779 - API - Refactor - Listado de direcciones en Mi cuenta Agregar filtro de|NBWEB-779]] API - Refactor - Listado de direcciones en "Mi cuenta": Agregar filtro de dropshipping y mostrar el parametro en el objeto

## Descripcion

Al procesar o enviar un carrito con el recurso

```
POST {API_URL}/v1/carrito/process
```

Si recibo el parámetro `dropShipping`

```
{
"note":"",
"medioDePagoId":3,
"dropShipping":true, <-----ESTE
"codigoPostalFavorito":"1407",
"mediodeEnvioId":4065,
"idDirCli":"19337",
"datosBultos":
{"weightKg":0.21,"sizeCm":"11.45x11.45x11.45",
"amount":1},
"dpPayload":
{"clientName":"Test",
"clientEmail":"test@test.com"}
}
```

Entonces marcare una columna en la tabla `NB_WEB.dbo.dircli`/`[NewBytes_DBF].[dbo].[dircli]` como `"dropShipping":true,` en esa direccion.

Mas adelante la devolveremos para poder filtrarla y separar aquellas que son del cliente y las de los clientes de nuestro cliente.
