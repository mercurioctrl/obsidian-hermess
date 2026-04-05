---
jira_key: "LOCAPP-90"
aliases: ["LOCAPP-90"]
summary: "API - Refactor - Emitir comprobante Uy"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-10-17 12:20"
updated: "2025-12-15 10:39"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LOCAPP-90"
---

# LOCAPP-90: API - Refactor - Emitir comprobante Uy

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-10-17 12:20 |
| Actualizado | 2025-12-15 10:39 |
| Etiquetas | ninguna |
| Jira | [LOCAPP-90](https://bluinc.atlassian.net/browse/LOCAPP-90) |

## Relaciones

- **Padre:** [[LOCAPP-88]] FactUru
- **has action item:** [[LOCAPP-80]] MVP - Vouchers para LASET (eticket, efactura,packingList "PL", SLI)

## Descripcion

Modificaremos el siguiente recurso, para que en los casos de que según el cliente use un servicio particular según la empresa.



En este caso si no esta definido usaremos el sistema que ya usamos para AFIP, pero si `[NewBytes_DBF].[dbo].[FP_Empresas].serivce`esta definido como `UY` utilizaremos el sistema de Facturu para emitir el comprobante

```
POST /v1/makeVoucher
```

```
{
"voucherTypeId":"1",
"clientId":19019,
"pedido":"X000200615589",
"iibbPerception":"0.00" 
}
```

Cuando emitimos el comprobante usaremos 

- `[NewBytes_DBF].[dbo].[FP_FactWebCliEncabezado_Uy]`


- `[NewBytes_DBF].[dbo].[FP_FactWebCliDetalle_Uy]`
