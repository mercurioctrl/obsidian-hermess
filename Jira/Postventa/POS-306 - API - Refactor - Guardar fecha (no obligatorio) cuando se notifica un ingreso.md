---
jira_key: "POS-306"
aliases: ["POS-306"]
summary: "API - Refactor - Guardar fecha (no obligatorio) cuando se notifica un ingreso "
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-07-17 12:32"
updated: "2024-07-22 12:45"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-306"
---

# POS-306: API - Refactor - Guardar fecha (no obligatorio) cuando se notifica un ingreso 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-07-17 12:32 |
| Actualizado | 2024-07-22 12:45 |
| Etiquetas | ninguna |
| Jira | [POS-306](https://bluinc.atlassian.net/browse/POS-306) |

## Relaciones

- **Padre:** [[POS-305 - Mejorar como se muestra cuando se acepta para que traigan mercaderia|POS-305]] Mejorar como se muestra cuando se acepta para que traigan mercaderia
- **blocks:** [[POS-307 - APP - Refactor - Permitir introducir una fecha futura (no olbigatoria) cuando|POS-307]] APP - Refactor - Permitir introducir una fecha futura (no olbigatoria) cuando se notifica un ingreso
- **blocks:** [[SNB-1159 - Mejora de estados de cara a los clientes en la web de NB|SNB-1159]] Mejora de estados de cara a los clientes en la web de NB

## Descripcion

```
PATCH v1/notifyPreAfterSales
```

```
{
"comment":"test",
"preAfterSaleId":"13075",
"initialDateEntry":"01-01-2025"
}
```
