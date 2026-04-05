---
jira_key: "POS-253"
aliases: ["POS-253"]
summary: "API - Refactor - Ingresos de cambios de postventa"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-04-18 10:24"
updated: "2023-04-24 08:06"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-253"
---

# POS-253: API - Refactor - Ingresos de cambios de postventa

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-04-18 10:24 |
| Actualizado | 2023-04-24 08:06 |
| Etiquetas | ninguna |
| Jira | [POS-253](https://bluinc.atlassian.net/browse/POS-253) |

## Relaciones

- **Padre:** [[POS-18 - Pre-Ingresos|POS-18]] Pre-Ingresos

## Descripcion

Se da un caso a veces donde un cambio de postventa, puede llegara fallar, dando como resultado un punto ciego, donde no podes realizar un ingreso, porque la mercadería que queres ingresar no proviene de un pedido sino de un cambio.

Modificaremos el recurso

```
GET {API_URL}/v1/createPreAfterSale/
```

Se debe buscar la forma de ofrecer el producto al cargar el serial, en caso de que un cliente se lo llevo como cambio (avisame y vemos las query si queres, lo que tenemos y como deberia ser)

Caso de ejemplo: # Postventa 31681

[(109350) MEMORIA PATRIOT VIPER RGB 16 GB 3600 MHZ CL18 BLK HS (2x8)](https://www.nb.com.ar/fromExpedicion_-_109350)

sku: PVR416G360C8K

Serial: 9DE200-00543

Pedido original (Por el cual se realizo el primero cambio):

Pedido 10267319

Remito: 00531274
