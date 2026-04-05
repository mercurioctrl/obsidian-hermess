---
jira_key: "LOCAPP-56"
aliases: ["LOCAPP-56"]
summary: "API - Refactor - Agregar \"internalTax\" a \"otros conceptos/impuestos\" al realizar el comprobante por AFIP e integrarlo dentro de [FP_FactWebCliEncabezado] y [FP_FactWebCliDetalle]"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-10-31 08:39"
updated: "2024-11-05 03:31"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LOCAPP-56"
---

# LOCAPP-56: API - Refactor - Agregar "internalTax" a "otros conceptos/impuestos" al realizar el comprobante por AFIP e integrarlo dentro de [FP_FactWebCliEncabezado] y [FP_FactWebCliDetalle]

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-10-31 08:39 |
| Actualizado | 2024-11-05 03:31 |
| Etiquetas | ninguna |
| Jira | [LOCAPP-56](https://bluinc.atlassian.net/browse/LOCAPP-56) |

## Relaciones

- **Padre:** [[LOCAPP-23]] Generar un comprobante

## Descripcion

De esta forma guardaremos en `FP_FactWebCliDetalle.internalTax `(como porcentaje)

Y guardaremos en `FP_FactWebCliEncabezado.internalTax` (como el monto nominal que es la suma de todo el impuesto interno)

Con respecto al **objeto en si que enviamos al webservice de AFIP,** según la documentación parecen colocarse en el array `OtrosTributos`

Recordemos que esto se guarda de esta forma en cada operacion, porque el impuesto puede variar en el tiempo en la tabla de referencia (`[NewBytes_DBF].[dbo].[articulo]`)

[adjunto]
[https://servicioscf.afip.gob.ar/publico/abc/ABCpaso2.aspx?id_nivel1=1017&id_nivel2=1018&p=Factura Electrónica](https://servicioscf.afip.gob.ar/publico/abc/ABCpaso2.aspx?id_nivel1=1017&id_nivel2=1018&p=Factura%20Electr%C3%B3nica)
