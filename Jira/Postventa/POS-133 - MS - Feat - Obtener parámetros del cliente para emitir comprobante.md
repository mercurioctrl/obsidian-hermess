---
jira_key: "POS-133"
aliases: ["POS-133"]
summary: "MS - Feat - Obtener parámetros del cliente para emitir comprobante"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-09-16 12:08"
updated: "2022-10-27 17:38"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-133"
---

# POS-133: MS - Feat - Obtener parámetros del cliente para emitir comprobante

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-09-16 12:08 |
| Actualizado | 2022-10-27 17:38 |
| Etiquetas | ninguna |
| Jira | [POS-133](https://bluinc.atlassian.net/browse/POS-133) |

## Relaciones

- **Padre:** [[POS-123]] MS - Servicio de emision de comprobantes
- **blocks:** [[POS-132]] MS - Feat - Emitir comprobante

## Descripcion

Este recurso nos da parte de la informacion necesaria para confeccionar el voucher, por ejemplo:

```
    'PtoVta'        => 1, // Punto de venta
    'CbteTipo'      => 6, // Tipo de comprobante (ver tipos disponibles) 
    'DocTipo'       => 80, // Tipo de documento del comprador (ver tipos disponibles)
    'DocNro'        => 20111111112, // Numero de documento del comprador
    'MonId'         => 'PES', //Tipo de moneda usada en el comprobante (ver tipos disponibles)('PES' para pesos argentinos) 
    'MonCotiz'      => 1, // Cotización de la moneda usada (1 para pesos argentinos)  
```



Pero ademas, sirve para obtener datos de la empresa que es la que emite realmente el comprobante (o voucher)

La empresa que emite el comprobante, siempre esta asociada al cliente. Es el cliente el que pertenece a una empresa determinada.

```
GET {API_URL}/v2/clientByCreateVoucher/{clientId}
```

```
GET {API_URL}/v2/clientByCreateVoucher/{clientId}?voucherTypeId={voucherTypeId}
```

Retorna

```
    {
      'PtoVta'        => 1, 
      'CbteTipo'      => 6, // solo viene si le pasamos un parametro del tipo de documento a emitir
      'DocTipo'       => 80,  
      'DocNro'        => 20111111112,  
      'MonId'         => 'PES',  
      'MonCotiz'      => 1, //cotizacion del dia, en caso de que corresponda 
    }
```

 

Para construir esto usaremos la query

```
SELECT
FP_Empresas.[CODEMP]
,[CNOMBRE]
,[CNIF] AS CUIT
,[SUCFacturaPlus] as FP_FactWebCliEncabezado_CNUMSUC
,FP_PuntosVenta.Descripcion AS ptovta
,FP_PuntosVenta.Id_PuntoVenta
,FP_Sucursales.Id_sucursal as FP_FactWebCliEncabezado_ID_PUNTOVENTA
,agente_ret
,clientes.niva as FP_FactWebCliEncabezado_NTIPOIVA
,FP_ComprobantesAFIP.ID_ComprobanteAFIP as CbteTipo
,clientes.cdnicif as DocNro
,FP_DocumentosAFIP.ndocidenti as DocTipo
,clientes.ID_DIVISA
FROM
[NewBytes_DBF].[dbo].[FP_Empresas]
INNER JOIN
NewBytes_DBF.dbo.FP_Sucursales ON FP_Sucursales.Descripcion =  FP_Empresas.SUCFacturaPlus
LEFT JOIN
NewBytes_DBF.dbo.FP_PuntosVenta ON FP_PuntosVenta.ID_Sucursal = FP_Sucursales.Id_sucursal AND FP_PuntosVenta.TipoFacturacion = 3
LEFT JOIN NewBytes_DBF.dbo.clientes ON clientes.CODEMP = FP_Empresas.CODEMP
left join [NewBytes_DBF].[dbo].[FP_CategoriasIVA] on clientes.niva = FP_CategoriasIVA.NIVA    
LEFT JOIN [NewBytes_DBF].[dbo].[FP_ComprobantesAFIP] ON FP_ComprobantesAFIP.CSerie = FP_CategoriasIVA.cSeriePredefinida
LEFT JOIN [NewBytes_DBF].[dbo].[FP_DocumentosAFIP] on clientes.ndocidenti = FP_DocumentosAFIP.Id_TipoDocumentoInterno
WHERE clientes.ID_CLIENTE = 043763 (idCliente)
--and FP_ComprobantesAFIP.ID_TiposDocumentosCobro = 2 (voucherTypeId)
  
```

[adjunto]
