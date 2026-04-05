---
jira_key: "NBWEB-527"
aliases: ["NBWEB-527"]
summary: "APP - Feat - Seccion Parametros varios"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2023-03-22 09:25"
updated: "2023-04-12 10:25"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-527"
---

# NBWEB-527: APP - Feat - Seccion Parametros varios

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2023-03-22 09:25 |
| Actualizado | 2023-04-12 10:25 |
| Etiquetas | ninguna |
| Jira | [NBWEB-527](https://bluinc.atlassian.net/browse/NBWEB-527) |

## Relaciones

- **Padre:** [[NBWEB-524]] CMS - Parametros varios
- **is blocked by:** [[NBWEB-526]] API - Feat - Editar Parametros varios
- **is blocked by:** [[NBWEB-525]] API - Feat - Listar Parametros varios

## Descripcion

Agregaremos una nueva sección “parametros varios” para poder agrupar todos aquellos parámetros globales de los sistemas de la empresa.

Se debe listar o colocar en un formulario los siguientes parametros [link](https://lioteam.atlassian.net/browse/NBWEB-525) y los mismois pueden editarse en e el contexto con [link](https://lioteam.atlassian.net/browse/NBWEB-526) .

Esta sección es probable que siempre reciba y se agreguen nuevos parámetros a medida que veamos creando distintos sistemas.

| **Variable** | **Nombre para mostrar** |
| --- | --- |
| `rangeAuthOrders` | Margen autorización remito |
| `truckLimit` | Límite de seguro de envío: Es el máximo de costo de mercadería asegurado para transporte camioneta. |
| `varCurrency` | Variación de cotización: Es la variación que se puede hacer al cambiar la cotización, sin que me muestre un alerta (evita que nos equivoquemos al setear la cotización del día) |
| `checksDays` | Días máximos para cheques: Es la cantidad máxima de días que puede tener un cheque |
| `maxCurrencyUser` | Cotización máxima: Es la variación máxima entre cotización del día y cotización liquidada |
| `annualRate` | Tasa de interés anual: Es la tasa de interés anual general |
| `perceptionAndRetention` | Percepcion/Retencion: Indica si se cobran y pagan retenciones/percepciones |
