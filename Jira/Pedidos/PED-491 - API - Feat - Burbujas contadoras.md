---
jira_key: "PED-491"
aliases: ["PED-491"]
summary: "API - Feat - Burbujas contadoras"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-01-17 07:49"
updated: "2024-01-25 15:57"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-491"
---

# PED-491: API - Feat - Burbujas contadoras

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-01-17 07:49 |
| Actualizado | 2024-01-25 15:57 |
| Etiquetas | ninguna |
| Jira | [PED-491](https://bluinc.atlassian.net/browse/PED-491) |

## Relaciones

- **Padre:** [[PED-490]] Burbujas contadoras para las pestañas
- **blocks:** [[PED-492]] APP - Feat - Burbujas contadoras

## Descripcion

Agregaremos el recurso ya utilizado en otros proyectos para actualizar las burbujas de las pestañas

```
{API_URL}/v1/pendings
```

```
{
"pendingOrders":3, 
"clientsRequest":2
}
```



**pendingOrders**: Se trata de aquellas ordenes o pedidos que aun no fueron liquidados PARA EL VENDEDOR QUE ESTA LOGUEADO.

**clientsRequest:** Se trata de todas las solicitudes de alta pendientes.
