---
jira_key: "POS-135"
aliases: ["POS-135"]
summary: "API - Feat - Emitir comprobante de un credito de postventa"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-09-16 14:52"
updated: "2022-10-27 17:38"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-135"
---

# POS-135: API - Feat - Emitir comprobante de un credito de postventa

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-09-16 14:52 |
| Actualizado | 2022-10-27 17:38 |
| Etiquetas | ninguna |
| Jira | [POS-135](https://bluinc.atlassian.net/browse/POS-135) |

## Relaciones

- **Padre:** [[POS-123]] MS - Servicio de emision de comprobantes
- **is blocked by:** [[POS-132]] MS - Feat - Emitir comprobante

## Descripcion

Este recurso es el accionable para cuando se hace crédito por un ítem (o varios ).

Se tienen que realiza distintas cosas

- Realizar el crédito fiscal con [link](https://lioteam.atlassian.net/browse/POS-132)


- Realizar el crédito en la cuenta corriente del cliente


- Realizar los pasos administrativos necesarios para que el caso pase a la siguiente instancia.



```
POST {API_URL}/v1/makeAftersalesCredits
```

¿como realzar el crédito en la cuenta corriente del cliente?

Se hace mediante una inserción en la tabla `[NEW_BYTES].[dbo].[MC_CCORRIENTES_MOVIMIENTOS]` para ese cliente.

```
POST {API_RUL}/v1/currentAccount/{clientId}
```

Para esto se utiliza `[NEW_BYTES].[dbo].[MC_CCORRIENTES_MOVIMIENTOS] `

Vamos a inspeccionar la tabla para ver que valores son obligatorios. Pero los parámetros mas importantes son:

- El monto `CC_IMPORTEUSD` 


- Las fechas


- el Id del cliente


- El código TR (en ese caso se usa hardcodeado el  30 que es “creditos varios”)


- Como adicional, agregaremos en `CC_OBSERVACIONES` la inscripcion “NC Postventa N{id postventa}, Item: {Nombre del item}”





Importante: Siempre que se pone la leyenda de un item para la nota de crédito, debe estar precedido por el prefijo RMA
