---
jira_key: "PED-1288"
aliases: ["PED-1288"]
summary: "API - Review - Agregar nuevo parámetro voucherCompanyCode -> Clientes por migrar"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2026-01-27 00:36"
updated: "2026-01-27 11:42"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1288"
---

# PED-1288: API - Review - Agregar nuevo parámetro voucherCompanyCode -> Clientes por migrar

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2026-01-27 00:36 |
| Actualizado | 2026-01-27 11:42 |
| Etiquetas | ninguna |
| Jira | [PED-1288](https://bluinc.atlassian.net/browse/PED-1288) |

## Relaciones

- **Padre:** [[PED-600]] Edicion/Alta de cliente
- **clones:** [[PED-1283]] API - Refactor - Agregar nuevo parámetro voucherCompanyCode

## Descripcion

Se realizará una revisión para migrar los valores actuales de `companyCode` a `voucherCompanyCode` en los clientes que aún lo requieran.

```
SELECT
	clientes.ID_CLIENTE,
	clientes.clientLo,
	clientes.CODEMP,    
	clientes.companyCode,
	voucherCompanyCode
FROM NewBytes_DBF.dbo.clientes
WHERE voucherCompanyCode IS NULL
```

[adjunto]
