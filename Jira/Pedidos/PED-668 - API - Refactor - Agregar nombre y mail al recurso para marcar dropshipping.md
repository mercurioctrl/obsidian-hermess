---
jira_key: "PED-668"
aliases: ["PED-668"]
summary: "API - Refactor - Agregar nombre y mail al recurso para marcar dropshipping"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-04-15 14:38"
updated: "2024-04-19 20:35"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-668"
---

# PED-668: API - Refactor - Agregar nombre y mail al recurso para marcar dropshipping

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-04-15 14:38 |
| Actualizado | 2024-04-19 20:35 |
| Etiquetas | ninguna |
| Jira | [PED-668](https://bluinc.atlassian.net/browse/PED-668) |

## Relaciones

- **Padre:** [[PED-646]] Dropshipping
- **blocks:** [[PED-669]] APP - Refactor - Agregar un modal con la posibilidad de incluir nombre y correo ademas del parametro de dropshipping

## Descripcion

Al patch previo 

```
{{API_URL}}/v1/setDropShipping/0002-10332673
```

se le agrego un body opcional 

```
{
    "clientName" : "eze ma",
    "clientEmail" : "edq@qgaa.com"
}
```

para guardar estos datos en la db y poder levantarlos despues con el get de la historia

 [link](https://lioteam.atlassian.net/browse/PED-670)
