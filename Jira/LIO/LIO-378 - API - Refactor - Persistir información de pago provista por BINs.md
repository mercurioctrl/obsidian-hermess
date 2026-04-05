---
jira_key: "LIO-378"
aliases: ["LIO-378"]
summary: "API - Refactor - Persistir información de pago provista por BINs"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-07-06 19:39"
updated: "2025-07-16 10:41"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-378"
---

# LIO-378: API - Refactor - Persistir información de pago provista por BINs

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-07-06 19:39 |
| Actualizado | 2025-07-16 10:41 |
| Etiquetas | ninguna |
| Jira | [LIO-378](https://bluinc.atlassian.net/browse/LIO-378) |

## Relaciones

- **Padre:** [[LIO-373]] Seguridad del checkout y protección de transacciones

## Descripcion

Se debe refactorizar el recurso agregando la propiedad `"bin":12345678` el cual tiene los primeros 8 numeros de la tarjate credito/debito

para identificar el banco emisor y su respectivos interes. La informacion de los interes quedara registrada en la tabla:

`LO.dbo.checkout_snapshot_data` en los campos `interes_payload `y ` interes_response` . 



```
PATCH pedidos/checkout
```



```json
"datosPagoConTarjeta": {
    "token": "9c0443cd34aee55ef61c89d05d6d967b",
    "transactionAmount": 369454.08,
    "description": "Compra #659832 - Libre Opción MONITOR SAMSUNG 27 SMART MONITOR ",
    "installments": 6,
    "paymentMethodId": "visa",
    "issuer": 310,
    "email": "ferreyra-emanuel@outlook.com",
    "identificationType": "DNI",
    "identificationNumber": "12345678",
    "cardholderName": "APRO22",
    "additional_info": {
        "items": [
            {
                "id": "536398",
                "title": "Compra #659832 - Libre Opción MONITOR SAMSUNG 27 SMART MONITOR",
                "description": "Compra #659832 - Libre Opción ",
                "quantity": "1",
                "unit_price": "300620"
            }
        ]
    },
    "installmentRate": 0,
    "financingFee": 0,
    "bin":"45099535" --> nueva propiedad 
}
```





Requiere agregar en el .env MP_PUBLIC_KEY={variable public key utilizada en el front para mp}
