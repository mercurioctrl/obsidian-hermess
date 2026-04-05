---
jira_key: "PED-1165"
aliases: ["PED-1165"]
summary: "API - MVP - Refactor - Listar comprobantes según la tabla correspondiente para los casos que tienenen tabla propia (LASET)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-10-30 12:54"
updated: "2025-12-05 04:08"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1165"
---

# PED-1165: API - MVP - Refactor - Listar comprobantes según la tabla correspondiente para los casos que tienenen tabla propia (LASET)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-10-30 12:54 |
| Actualizado | 2025-12-05 04:08 |
| Etiquetas | ninguna |
| Jira | [PED-1165](https://bluinc.atlassian.net/browse/PED-1165) |

## Relaciones

- **Padre:** [[PED-98 - Feat - Listar comprobantes|PED-98]] Feat - Listar comprobantes
- **action item from:** [[PED-998 - Intervención Técnica|PED-998]] Intervención Técnica

## Descripcion

Refactorizaremos el recurso

```
GET {API_URL}/v1/vouchers?companyCode={companyCode}
```

Para que cuando tengas `companyCode=11` use las nuevas tablas`[NewBytes_DBF].[dbo].[FP_FactWebCliEncabezado_Uy]`
