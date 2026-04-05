---
jira_key: "NBWEB-555"
aliases: ["NBWEB-555"]
summary: "API - Feat - Vincular envío LO con NB"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-06-21 14:10"
updated: "2023-07-17 06:27"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-555"
---

# NBWEB-555: API - Feat - Vincular envío LO con NB

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-06-21 14:10 |
| Actualizado | 2023-07-17 06:27 |
| Etiquetas | ninguna |
| Jira | [NBWEB-555](https://bluinc.atlassian.net/browse/NBWEB-555) |

## Relaciones

- **Padre:** [[NBWEB-495]] API - Features especiales

## Descripcion

Lo que buscamos es poder traer la informacin desde la otra plataforma para integrarlo a la misma logistica de envios que creamos para los pedidos de nb.

Todos los pedidos de libre opcion, tienen una orden creada y por lo tanto en ella nos basaremos para generar el recurso.

```
POST {{API_URL}}/v1/miCuenta/ordenesDeCompra/0002/10286763/completeLoShipment
```

**1- Obtener datos del pedido de libre opción **

Utilizaremos el siguiente repositorio para obtener los datos

```
SELECT top 5
pedidosCabeceraPaquete.tracking,
pedidosCabeceraPaquete.id as pedidosCabeceraPaqueteID,
mediosEnvio.nombre as nombreMedioDeEnvio,
mediosEnvio.descripcion as DescripcionEnvio,
medioDeEnvioDatos,
[pedidosCabeceraVendedor].[medioDeEnvioID],
pedidosCabeceraPaquete.provinciaEnvioElegidoID,
pedidosCabeceraPaquete.ciudadEnvioElegidoID,
pedidosCabeceraPaquete.codigoPostalEnvio,
pedidosCabeceraPaquete.direccionEnvio,
pedidosCabeceraPaquete.direccionEnvioCalle,
pedidosCabeceraPaquete.direccionEnvioCasaApto,
pedidosCabeceraPaquete.direccionEnvioNumero,
pedidosCabeceraPaquete.direccionEnvioObservacion,
pedidosCabeceraPaquete.direccionEnvioPiso,
pedclit.cnumped
FROM
  [LO].[dbo].pedidosCabeceraVendedor
  INNER JOIN [LO].[dbo].[pedidosCabecera] ON pedidosCabecera.id = pedidosCabeceraVendedor.pedidoCabeceraID
  LEFT JOIN NewBytes_DBF.dbo.pedclit ON pedidosCabeceraVendedor.pedclitID = pedclit.cnumped
  LEFT JOIN LO.dbo.pedidosCabeceraPaquete ON pedidosCabecera.id = pedidosCabeceraPaquete.pedidoCabeceraID
  LEFT JOIN [LO].[dbo].[vendedores] ON vendedores.id = [pedidosCabeceraVendedor].vendedorID
  LEFT JOIN [LO].[dbo].[usuarios] ON usuarios.id = [pedidosCabecera].[usuarioID]
  LEFT JOIN [LO].[dbo].[mediosEnvio] ON mediosEnvio.id = [pedidosCabeceraVendedor].[medioDeEnvioID]
  LEFT JOIN [LO].[dbo].[mediosPago] ON mediosPago.id = [pedidosCabeceraVendedor].[medioDePagoID]
  LEFT JOIN NewBytes_DBF.dbo.albclit ON albclit.cnumped = pedclit.cnumped
  LEFT JOIN NewBytes_DBF.dbo.agentes ON agentes.ccodage = pedclit.ccodage
WHERE
    pedclit.cnumped = 10314615 and pedclit.cnumsuc =2
GROUP BY
pedidosCabeceraPaquete.tracking,
pedidosCabeceraPaquete.id,
mediosEnvio.nombre,
mediosEnvio.descripcion,
medioDeEnvioDatos,
[pedidosCabeceraVendedor].[medioDeEnvioID],
pedidosCabeceraPaquete.provinciaEnvioElegidoID,
pedidosCabeceraPaquete.ciudadEnvioElegidoID,
pedidosCabeceraPaquete.codigoPostalEnvio,
pedidosCabeceraPaquete.direccionEnvio,
pedidosCabeceraPaquete.direccionEnvioCalle,
pedidosCabeceraPaquete.direccionEnvioCasaApto,
pedidosCabeceraPaquete.direccionEnvioNumero,
pedidosCabeceraPaquete.direccionEnvioObservacion,
pedidosCabeceraPaquete.direccionEnvioPiso ,
pedclit.cnumped
order by pedidosCabeceraPaquete.id desc
```

**2 - Crear la nueva dirección para el cliente**

Le agregaremos al cliente propietario del pedido la nueva dirección dentro de sus direcciones en `dircli`

3 - **Marcar en **`[NewBytes_DBF].[dbo].[pedclit]`** las columnas, según el registro que acabamos de crear y los datos del repositorio**

```
[idDirCliNbWeb] <- Esta es la direccion nueva que acabamos de crear
[medioEnvioId]
```
