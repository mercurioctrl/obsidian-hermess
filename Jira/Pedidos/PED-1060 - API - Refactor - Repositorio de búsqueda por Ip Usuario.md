---
jira_key: "PED-1060"
aliases: ["PED-1060"]
summary: "API - Refactor - Repositorio de búsqueda por Ip / Usuario"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-07-23 07:25"
updated: "2025-08-05 19:19"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1060"
---

# PED-1060: API - Refactor - Repositorio de búsqueda por Ip / Usuario

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-07-23 07:25 |
| Actualizado | 2025-08-05 19:19 |
| Etiquetas | ninguna |
| Jira | [PED-1060](https://bluinc.atlassian.net/browse/PED-1060) |

## Relaciones

- **Padre:** [[PED-724]] Modal "Venta Market Place LO"

## Descripcion

Crearemos un recurso especifico para monitorear la actividad de una IP respecto a los intentos de compra, para esto permitiremos buscar una ip especifica devolviendo los resultados detallados de la misma

```
GET {{API_URL}}/v1/ipOrigin/4.232.201.147
```

Devuelve

```
[
  {
    "usuarioId": 306489,
    "fechaCreacion": "2025-06-20T01:36:05.947",
    "confirmado": null,
    "mpPaymentStatus": null,
    "mpPaymentStatusDetail": null,
    "canceladoUsuario": 0,
    "canceladoVendedor": 0,
    "canceladoLibreOpcion": 0,
    "canceladoAutomaticamente": null,
    "despachado": 0,
    "ipOrigin": "24.232.201.147",
    "motivoCancelacion": null,
    "paymentIntegrity": "0",
    "shippingIntegrity": "0",
    "discountIntegrity": "0",
    "fechaAlta": "2025-06-07T12:56:32.71",
    "nombre": "FRANCO BASPINEIRO",
    "correo": "francobas05@gmail.com",
    "documento": "42427139",
    "telefono": "3875648568",
    "direccion": "R MARQUES 536  536"
  },
  {
    "usuarioId": 306489,
    "fechaCreacion": "2025-06-20T01:35:31.52",
    "confirmado": null,
    "mpPaymentStatus": null,
    "mpPaymentStatusDetail": null,
    "canceladoUsuario": 0,
    "canceladoVendedor": 0,
    "canceladoLibreOpcion": 0,
    "canceladoAutomaticamente": null,
    "despachado": 0,
    "ipOrigin": "24.232.201.147",
    "motivoCancelacion": null,
    "paymentIntegrity": "0",
    "shippingIntegrity": "0",
    "discountIntegrity": "0",
    "fechaAlta": "2025-06-07T12:56:32.71",
    "nombre": "FRANCO BASPINEIRO",
    "correo": "francobas05@gmail.com",
    "documento": "42427139",
    "telefono": "3875648568",
    "direccion": "R MARQUES 536  536"
  },
  {
    "usuarioId": 306655,
    "fechaCreacion": "2025-06-10T12:40:29.553",
    "confirmado": null,
    "mpPaymentStatus": null,
    "mpPaymentStatusDetail": null,
    "canceladoUsuario": 0,
    "canceladoVendedor": 0,
    "canceladoLibreOpcion": 0,
    "canceladoAutomaticamente": null,
    ....
```

Consulta orientadora:

```
SELECT
    [usuarioID]
      , [fechaCreacion]
      , [confirmado]
      , [mp_payment_status]
      , [mp_payment_status_detail]
      , [canceladoUsuario]
      , [canceladoVendedor]
      , [canceladoLibreOpcion]
      , [canceladoAutomaticamente]
      , [despachado]
      , [ip_origin]
      , [motivoCancelacion]
      , [paymentIntegrity]
      , [shippingIntegrity]
      , [discountIntegrity]
      , usuarios.fechaAlta
      , usuarios.nombre
      , usuarios.correo
      , usuarios.documento
      , usuarios.telefono
      , usuarios.direccion
FROM [LO].[dbo].[pedidosCabecera]
    LEFT JOIN LO.dbo.usuarios ON pedidosCabecera.usuarioID = usuarios.id
WHERE ip_origin = '24.232.201.147'
ORDER BY fechaCreacion DESC 
```
