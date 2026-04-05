---
jira_key: "POS-40"
aliases: ["POS-40"]
summary: "API - Feat - Definir solucion tecnica"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-07-28 17:07"
updated: "2022-10-27 17:36"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-40"
---

# POS-40: API - Feat - Definir solucion tecnica

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-07-28 17:07 |
| Actualizado | 2022-10-27 17:36 |
| Etiquetas | ninguna |
| Jira | [POS-40](https://bluinc.atlassian.net/browse/POS-40) |

## Relaciones

- **Padre:** [[POS-20]] Diagnoistico
- **Subtarea:** [[POS-73]] API - Feat - Permiso administrativo para 'marcar' una solución técnica 
- **Subtarea:** [[POS-81]] API - Test - Revisar el fallo al intentar definir una solucion tecnica
- **Subtarea:** [[POS-186]] API - Review - Verificar instancia irreversible de una accion

## Descripcion

Define la acción que se va a tomar para darle solución al caso de post venta

```
PATCH {API_URL}/v1/aftersales/{afterSaleId}/{detailId}
```

```
{
"testProductStatusId":3,
}

```
