---
jira_key: "LIO-319"
aliases: ["LIO-319"]
summary: "API - Refactor - se debe guardar en pedidosCabeceraVendedor.medioDePagoInteres el id de pago con tarjeta"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2025-04-10 12:26"
updated: "2025-04-16 00:18"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-319"
---

# LIO-319: API - Refactor - se debe guardar en pedidosCabeceraVendedor.medioDePagoInteres el id de pago con tarjeta

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2025-04-10 12:26 |
| Actualizado | 2025-04-16 00:18 |
| Etiquetas | ninguna |
| Jira | [LIO-319](https://bluinc.atlassian.net/browse/LIO-319) |

## Relaciones

- **Padre:** [[LIO-8]] Proceso pago sencillo y competitiva a nivel financiamiento

## Descripcion

Se debe guardar el interes de la tabla 

```
--los posibles intereses
select interes1,
       interes3,
       interes6,
       interes9,
       interes12
from [LO].[dbo].[mediosPago]
where id = 5076 --> el id que corresponda a tarjeta de credito/debito

```

segun la cuota confirmada por el cliente en:



```
-- cantidad de cuotas
SELECT installments
FROM lo.dbo.payment_gateway_transactions
where pedido_cabecera_id = ? -> id de cabecera pedido
```



El interes % (porcentual) se debe registrar en el campo `medioDePagoInteres` de la tabla `[LO].[dbo].[pedidosCabeceraVendedor]`.
