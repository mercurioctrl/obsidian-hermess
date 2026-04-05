---
jira_key: "PED-745"
aliases: ["PED-745"]
summary: "API - Agregar comprobantes de pago - Comprobantes guardados no coincidentes"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Guillermo Avila"
created: "2024-06-14 18:47"
updated: "2024-06-19 19:23"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-745"
---

# PED-745: API - Agregar comprobantes de pago - Comprobantes guardados no coincidentes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Guillermo Avila |
| Creado | 2024-06-14 18:47 |
| Actualizado | 2024-06-19 19:23 |
| Etiquetas | ninguna |
| Jira | [PED-745](https://bluinc.atlassian.net/browse/PED-745) |

## Relaciones

- **Padre:** [[PED-3]] Ordenes de compra
- **blocks:** [[PED-742]] API - Refactor - validar si el numero de operación de un comprobante ya esta registrado 

## Descripcion

Después de agregar dos comprobantes de pago a una orden `0002-10332851` solo se guarda uno de ellos.



```
PATCH {{API_URL}}/v1/paymentVoucher
```

[adjunto]
[adjunto]
