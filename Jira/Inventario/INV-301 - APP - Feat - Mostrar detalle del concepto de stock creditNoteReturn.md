---
jira_key: "INV-301"
aliases: ["INV-301"]
summary: "APP - Feat - Mostrar detalle del concepto de stock creditNoteReturn"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-12-23 16:43"
updated: "2026-01-05 10:28"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-301"
---

# INV-301: APP - Feat - Mostrar detalle del concepto de stock creditNoteReturn

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-12-23 16:43 |
| Actualizado | 2026-01-05 10:28 |
| Etiquetas | ninguna |
| Jira | [INV-301](https://bluinc.atlassian.net/browse/INV-301) |

## Relaciones

- **Padre:** [[INV-199]] Control de Stock / Stock en general  / Control de Precios

## Descripcion

La idea es que al hacer clic en un concepto de stock, en este caso `creditNoteReturn` que es un numero, podamos ver los documentos asociados a ese numero y sus cantidades en un modal. 

[adjunto]
Para esto ejecutaremos el recurso [link](https://bluinc.atlassian.net/browse/INV-247)  de la siguiente manera 

```
GET {API_URL}/itemsStocks/examine?between=12-11-2025_13-11-2025&itemId=343&type=creditNoteReturn
```

Y de esta forma podremos mostrar la informacion relevante obtenida en una tabla que para este caso, tendrá el numero de pedido/ingreso de compras y su proveedor. De este modo, al leer 600, sabremos como ingresaron esos 600 y podremos ir a buscar la información completa

```
{
  "data": [
    {
      "date": "01-01-01 01:01",
      "linkedDocument": "0002-3334532",
      "amount": 3,
      "clientId": 2333,
      "clientName": "Nombre del cliente",
      "providerId": null,
      "providerName": null
    }
  ],
  "pagination": {
    "total": 3213,
    "pageSize": 50,
    "current": 1
  }
}

```
