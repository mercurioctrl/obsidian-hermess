---
jira_key: "EXP-120"
aliases: ["EXP-120"]
summary: "MS - Refactor - Creditos parciales o totales desde un pedido especifico"
status: "CodeReview"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-12-21 17:26"
updated: "2022-12-26 09:22"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-120"
---

# EXP-120: MS - Refactor - Creditos parciales o totales desde un pedido especifico

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-12-21 17:26 |
| Actualizado | 2022-12-26 09:22 |
| Etiquetas | ninguna |
| Jira | [EXP-120](https://bluinc.atlassian.net/browse/EXP-120) |

## Relaciones

- **Padre:** [[EXP-116 - Devoluciones|EXP-116]] Devoluciones

## Descripcion

Para poder emitir notas de crédito fiscales por devolución, necesitaremos agregar un nuevo parámetro para poder “ubicar” el comprobante original emitido, que nos permite realizar nota de crédito.

Haremos un refactor para poder pasar este parámetro y a su vez para poder relacionarlo con el nuevo comprobante de crédito dentro de los servicios de AFIP mediante el objeto `CbteAsoc` del servicio

```
<ar:CbteAsoc>
 <ar:Tipo>short</ar:Tipo>
 <ar:PtoVta>int</ar:PtoVta>
 <ar:Nro>Long</ar:Nro>
<ar:Cuit>String</ar:Cuit>
<ar:CbteFch>String</ar:CbteFch>
 </ar:CbteAsoc>
```



[link](https://lioteam.atlassian.net/browse/POS-135)
