---
jira_key: "PED-969"
aliases: ["PED-969"]
summary: "API - Feat - SyncUp API de MercadoLibre para obtener órdenes de venta"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-03-17 06:44"
updated: "2025-04-08 09:44"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-969"
---

# PED-969: API - Feat - SyncUp API de MercadoLibre para obtener órdenes de venta

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-03-17 06:44 |
| Actualizado | 2025-04-08 09:44 |
| Etiquetas | ninguna |
| Jira | [PED-969](https://bluinc.atlassian.net/browse/PED-969) |

## Relaciones

- **Padre:** [[PED-915 - MercadoLibre|PED-915]] MercadoLibre
- **relates to:** [[PED-984 - API - Refactor - SyncUp API de MercadoLibre para obtener órdenes de venta -|PED-984]] API - Refactor - SyncUp API de MercadoLibre para obtener órdenes de venta -> Mensaje de éxito al no completarse la sincronización

## Descripcion

Realizar una solicitud a la API de MercadoLibre para obtener la lista de órdenes de venta asociadas a un usuario vendedor, de manera que pueda procesar y visualizar la información en nuestro sistema.

```
GET {API_URL}/v1//syncUp/mercadolibreOrders
```

**Criterios de aceptación:**

- Se debe realizar una solicitud HTTP `GET` a la API de MercadoLibre utilizando `curl` o una alternativa programática.


- Se debe autenticar la solicitud con un `access_token` válido.


- La respuesta debe ser almacenada o procesada en el sistema.


- En caso de error o expiración del `access_token`, el sistema debe manejar la excepción adecuadamente.


- La integración debe ser documentada para facilitar su mantenimiento.



```
curl -X GET "https://api.mercadolibre.com/orders/search?seller=2004876920" \
     -H "Authorization: Bearer APP_USR-6953534962889483-031705-156fd697ba2454f3d8fbdf0263dc100b-2004876920" \
     -H "Content-Type: application/json"
```

- Implementar una función en el backend para realizar la solicitud `GET`.


- Manejar la autenticación con el `access_token`.


- Procesar la respuesta JSON y extraer la información relevante de las órdenes. Es decir que crearemos cabecera y detalle en` [NewBytes_DBF].[dbo].pedclit` y `[NewBytes_DBF].[dbo].pedclil` respectivamente. Para esto tambien relacionaremos con un parámetro nuevo la venta al numero de venta de mercadolibre una vez creado. Y lo mismo haremos con el item.


- Manejar posibles errores y casos en los que el `access_token` haya expirado.



Ejemplo de respuesta de mercadolibre

```
{
  "id": 2000011046243154,
  "date_created": "2025-03-17T05:36:41.000-04:00",
  "date_closed": "2025-03-17T05:36:43.000-04:00",
  "status": "paid",
  "total_amount": 1000,
  "paid_amount": 1000,
  "currency_id": "ARS",
  "seller": {
    "id": 2004876920,
    "nickname": "DD20240923144352"
  },
  "buyer": {
    "id": 2261571,
    "nickname": "HERMESS87"
  },
  "order_items": [
    {
      "item": {
        "id": "MLA1985568058",
        "title": "Disyuntor Diferencial 4x25 A Chint 30ma 6ka Clase Ac",
        "category_id": "MLA30208",
        "seller_sku": "[[NXL-63]] 3P+N 25A 30mA AC 6kA",
        "condition": "new",
        "warranty": "Garantía de fábrica: 12 días"
      },
      "quantity": 1,
      "unit_price": 1000,
      "full_unit_price": 1000,
      "currency_id": "ARS",
      "sale_fee": 1140,
      "listing_type_id": "gold_special"
    }
  ],
  "payments": [
    {
      "id": 105037119215,
      "date_created": "2025-03-17T05:36:41.000-04:00",
      "date_approved": "2025-03-17T05:36:43.000-04:00",
      "status": "approved",
      "status_detail": "accredited",
      "transaction_amount": 1000,
      "payment_method_id": "amex",
      "payment_type": "credit_card",
      "installments": 1,
      "currency_id": "ARS",
      "collector": {
        "id": 2004876920
      },
      "payer_id": 2261571
    }
  ],
  "tags": ["no_shipping", "paid", "not_delivered"],
  "context": {
    "channel": "marketplace",
    "site": "MLA"
  }
}

```

Dentro del objeto podemos ver que hay un parámetro `order_items.item.seller_sku` el cual utilizaremos para vincular con nuestro SKU 

Existen varios enfoques para hacer esta tarea, en uno podemos crear directamente en pedclit, pedclil y pedcliml  con los datos complementarios como 

- **ID de la orden** (`id`)


- **Fecha de creación y cierre** (`date_created`, `date_closed`)


- **Estado del pago** (`status`)


- **Monto total y pagado** (`total_amount`, `paid_amount`)


- **Información del vendedor y comprador** (`seller`, `buyer`)


- **Información del pago** (`payments`)



En otro enfoque podemos primero crear una tabla de cabecera y detallae en base a la respuesta de mercadolibre y una vez realizado, en base a esas tablas crear nuestra orden.

Sentite libre de seguir el camino que te da mas confianza y si necesitas que charlemos me avisas y lo vemos
