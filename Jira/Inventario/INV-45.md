---
jira_key: "INV-45"
summary: "API - Refactor - Filtro inicial al listar productos"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-11-28 10:29"
updated: "2025-09-02 08:24"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-45"
---

# INV-45: API - Refactor - Filtro inicial al listar productos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-11-28 10:29 |
| Actualizado | 2025-09-02 08:24 |
| Etiquetas | ninguna |
| Jira | [INV-45](https://bluinc.atlassian.net/browse/INV-45) |

## Descripción

Cuando no marque ningun otro filtro, entonces voy a mostrar los ultimos productos que ingresaron y aun no tienen la carga completa… para esto agregaremos las siguientes clausulas en el WHERE Y ORDER BY al reposotorio que ya tenemos

```
WHERE [articulo].EXCLUIR <> 1
    AND codigoForzado IS NULL
    AND (articulo.id_distribuidora = 1)
    AND (nstock + nstock_lo + nstock_en_cola + nstock_d1 + nstock_virtual) > 0

ORDER BY ULTIMO_INGRESO DESC
```
