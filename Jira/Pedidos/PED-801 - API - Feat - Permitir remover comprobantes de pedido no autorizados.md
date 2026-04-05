---
jira_key: "PED-801"
aliases: ["PED-801"]
summary: "API - Feat - Permitir remover comprobantes de pedido no autorizados"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2024-08-19 13:30"
updated: "2024-08-25 23:17"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-801"
---

# PED-801: API - Feat - Permitir remover comprobantes de pedido no autorizados

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2024-08-19 13:30 |
| Actualizado | 2024-08-25 23:17 |
| Etiquetas | ninguna |
| Jira | [PED-801](https://bluinc.atlassian.net/browse/PED-801) |

## Relaciones

- **Padre:** [[PED-5]] Comprobantes
- **blocks:** [[SNB-2233]] SUBIR   COMPROBANTE DE PAGO

## Descripcion

Se debe agregar recurso que permita remover comprobante subidos (softdelete).

SDebe cumplir con los criterios para el caso de uso.

- No debe existir en `MS_REMITO_CABECERA`. → no debe estar liquidado.


- id status = 1 || id status = null 





```
DELETE  URL/v1/paymentVoucher
```

payload :

```
{
  "id":212
}
```
