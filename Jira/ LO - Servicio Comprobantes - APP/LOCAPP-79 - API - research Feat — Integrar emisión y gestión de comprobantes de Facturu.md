---
jira_key: "LOCAPP-79"
aliases: ["LOCAPP-79"]
summary: "API - [research] Feat — Integrar emisión y gestión de comprobantes de Facturu (Uruguay)"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-08-19 08:40"
updated: "2025-12-05 03:11"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LOCAPP-79"
---

# LOCAPP-79: API - [research] Feat — Integrar emisión y gestión de comprobantes de Facturu (Uruguay)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-08-19 08:40 |
| Actualizado | 2025-12-05 03:11 |
| Etiquetas | ninguna |
| Jira | [LOCAPP-79](https://bluinc.atlassian.net/browse/LOCAPP-79) |

## Relaciones

- **Padre:** [[LOCAPP-78 - Endpoints especiales|LOCAPP-78]] Endpoints especiales

## Descripcion

```
POST {{API_URL}}/v2/CreateVoucher
```

```
{
  "voucherTypeId":3,
  "clientId": 42330 , <-- Desde el cliente, segun su empresa sabemos si usamos este endpoint
  "cotizacion":1275,
    "trade":[
      {
          "internalId": 120753,
          "units": 1,
          "ivaTax":21,
          "price": 85.54,
          "description": "Monitor 24 Benq Gw2491 Black Fhd Ips 100hz",
          "internalTax": 0
      }
  ]
}
```

## Contexto

Debemos integrar el servicio de facturación y comprobantes de **Facturu (UY)** a nuestro micro servicio, de forma **transparente** para el resto del sistema. La integración debe activarse según la configuración de la tabla `[NewBytes_DBF].[dbo].[FP_Empresas]`:

- Si la empresa emisora está **radicada en Uruguay** o la fila indica explícitamente **usar Facturu**/**endpoint de Facturu**, entonces la emisión/consulta/impresión de comprobantes se realiza vía Facturu.


- Caso contrario, se usa el flujo actual.



**Ambientes Facturu** (para enrutar base URL según `ENV`):

- **Testing**: Web `http://test.facturu.com` · REST Base `http://api.test.facturu.com`


- **Producción**: Web `https://sistema.facturu.com` · REST Base `https://api.facturu.com`



**Autenticación**: todas las llamadas REST exigen header `Authorization` con el formato `API_KEY/API_SECRET`.

> ⚠️ **Credenciales**: las credenciales operativas (usuario web, API_KEY y API_SECRET) **no deben guardarse en código**. Usar nuestro gestor de secretos y variables por entorno. La clave web provista para onboarding inicial se cambia en primer login (flujo manual).


Pedir credenciales por privado 

## Alcance

- **Emisión** de CFE (eFactura, eTicket, NC/ND, exportación) vía **PUT** `/{base}/document/uy` con `cfeJson` (payload JSON).


- Resolución de **tipos** de documento y **códigos** (tipo CFE, tipoDocumento, modalidad, víaTransporte, indicadorFacturación, printStyle) conforme catálogo de Facturu y compatibilizacion de los mismos con el resto del sistema `[NewBytes_DBF].[dbo].[FP_TiposDocumentos]`, `[NewBytes_DBF].[dbo].[FP_TiposFacturacion]`, `[NewBytes_DBF].[dbo].[FP_Sucursales]`,`[NewBytes_DBF].[dbo].[clientes]`


- **Selección dinámica del proveedor** (Facturu vs. otros) según `FP_Empresas`.


- Se debe crear en `[NewBytes_DBF].[dbo].[FP_FactWebCliEncabezado]` y `[NewBytes_DBF].[dbo].[FP_FactWebCliDetalle]`
