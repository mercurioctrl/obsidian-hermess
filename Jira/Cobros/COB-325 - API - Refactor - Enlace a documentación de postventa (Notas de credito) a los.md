---
jira_key: "COB-325"
aliases: ["COB-325"]
summary: "API - Refactor - Enlace a documentación de postventa (Notas de credito) a los movimientos de CC"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-02-02 09:06"
updated: "2024-02-14 15:53"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-325"
---

# COB-325: API - Refactor - Enlace a documentación de postventa (Notas de credito) a los movimientos de CC

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-02-02 09:06 |
| Actualizado | 2024-02-14 15:53 |
| Etiquetas | ninguna |
| Jira | [COB-325](https://bluinc.atlassian.net/browse/COB-325) |

## Relaciones

- **Padre:** [[COB-323]] Refactor - Enlace a documentación de postventa (Notas de credito) a los movimientos de CC
- **is blocked by:** [[COB-5]] API - Feat - Obtener cuenta corriente de un cliente
- **blocks:** [[COB-326]] APP - Refactor - Enlace a documentación de postventa (Notas de credito) a los movimientos de CC

## Descripcion

Agregaremos al recurso [https://lioteam.atlassian.net/browse/COB-5](https://lioteam.atlassian.net/browse/COB-5) los parámetros necesarios para poder enlazar y mostrar las notas de crédito en la cuenta corriente del cliente para que el cliente construya un enlace como el siguiente:

[link](https://omega.comprobantes.lio.red/voucher/F/486697/4f60e2a9a82c4d1a49e47bc4fa1878?show=1) 

[https://omega.comprobantes.lio.red/voucher/F/486697/4f60e2a9a82c4d1a49e47bc4fa1878?show=1](https://omega.comprobantes.lio.red/voucher/F/486697/4f60e2a9a82c4d1a49e47bc4fa1878?show=1)

Se necesitara el campo `ID_NROFACCLI_ENC` Y `token` de la tabla `[NewBytes_DBF].[dbo].[FP_FactWebCliEncabezado]`



agregaremos 

```
{
..
voucherID: 494702
token: 30e15381e48f42ba927d0d2f31a60d
..
}
```
