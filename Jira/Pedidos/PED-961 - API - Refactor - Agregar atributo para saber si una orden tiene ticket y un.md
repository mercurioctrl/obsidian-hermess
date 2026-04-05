---
jira_key: "PED-961"
aliases: ["PED-961"]
summary: "API - Refactor - Agregar atributo para saber si una orden tiene ticket y un filtro para filtrar las mismas"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-03-04 18:47"
updated: "2025-03-10 16:40"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-961"
---

# PED-961: API - Refactor - Agregar atributo para saber si una orden tiene ticket y un filtro para filtrar las mismas

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-03-04 18:47 |
| Actualizado | 2025-03-10 16:40 |
| Etiquetas | ninguna |
| Jira | [PED-961](https://bluinc.atlassian.net/browse/PED-961) |

## Relaciones

- **Padre:** [[PED-960 - Tickets de pedido|PED-960]] Tickets de pedido
- **has action item:** [[PED-965 - APP - Refactor - Agregar flag o indicador para representar cuando una orden|PED-965]] APP - Refactor - Agregar "flag" o indicador para representar cuando una orden posee un ticket

## Descripcion

Haremos un refactor sobre nuestro repositorio de ordenes

```
GET {API_URL}/v1/orders?ticket{true|false|null}
```

```
{
    "response": [
        {
            "date": "2025-03-04 18:31:26",
            "orderNumber": "10394360",
            "branchNumber": "0002",
            "albnumNumber": null,
            "realAlbumNumber": null,
            "clientDescription": "guillermo delgado",
            "clientId": 47009,
            "orderTypeId": 5,
            "observation": "PEDIDO LIBRE OPCION",
            "status": "P",
            "statusId": null,
            "statusDescription": "Pendiente",
            "invoice": null,
            "token": null,
            "voucherId": null,
            "sellerId": 100,
            "seller": "Opcion Libre",
            "totalInPesos": 528850.993725,
            "total": 466.92506,
            "finalTotal": 515.952189,
            "shippingMethod": 4041,
            "codePostal": 4000,
            "currency": 1025,
            "perception": 0,
            "shippingLabel": false,
            "idLo": 683194,
            "mpExternalReference": null,
            "paymentMethodId": 3,
            "paymentMethodDescription": "Dep\u00f3sito en Banco",
            "joinShipping": false,
            "dropShipping": false,
            "paymentVoucher": false,
            "mpPaymentStatus": null,
            "liquidateDestinationBankName": "",
            "delivered": false,
            "internalTax": 0,
            "companyCode": null,
            "tracking": "",
            "ticketStatus": 1 <<--NUEVO PARAMETRO (si es null, no tiene ticket. Si es 0, tiene ticket pero no esta pendiente. Si es 1, tiene ticket pendiente de respuesta)
        },
        {
            "date": "2025-03-04 17:37:01",
            "orderNumber": "10394359",
            "branchNumber": "0002",
            "albnumNumber": null,
            "realAlbumNumber": null,
            "clientDescription": "Alex Joaqu\u00edn Cepeda",
            "clientId": 87460,
            "orderTypeId": 5,
            "observation": "PEDIDO LIBRE OPCION",
            "status": "P",
            "statusId": null,
            "statusDescription": "Pendiente",
```

Se debe cumplir con la regla de performance midiendo antes y después intentando no retrasar el recurso, en caso de producirse un retraso debe ser menor a 2 segundos

## Buscar la construcción mas eficiente

En “teoría” es mas  eficiente generar la consulta de la siguiente manera, abordando una sola pregunta por el máximo para entender si tengo ticket y a su vez si ese requiere una respuesta

```
SELECT p.*, 
       CASE 
           WHEN MAX(t.pending) = 1 THEN 1
           WHEN COUNT(t.id) > 0 THEN 0
           ELSE NULL
       END AS estado_ticket
FROM [NewBytes_DBF].[dbo].[pedclit] p
LEFT JOIN [NewBytes_DBF].[dbo].[pedclitTicket] t 
       ON p.cnumped = t.cnumped 
      AND p.cnumsuc = t.cnumsuc
GROUP BY p.id, p.sitio, p.cnumped, p.dfecped, p.ccodcli -- (Incluir todas las columnas necesarias de 'pedclit')

```
