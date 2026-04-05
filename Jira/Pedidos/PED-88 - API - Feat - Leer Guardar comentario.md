---
jira_key: "PED-88"
aliases: ["PED-88"]
summary: "API - Feat - Leer / Guardar comentario"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-09-22 10:23"
updated: "2024-02-20 09:17"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-88"
---

# PED-88: API - Feat - Leer / Guardar comentario

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-09-22 10:23 |
| Actualizado | 2024-02-20 09:17 |
| Etiquetas | ninguna |
| Jira | [PED-88](https://bluinc.atlassian.net/browse/PED-88) |

## Relaciones

- **Padre:** [[PED-8 - Listar ordenes de compra|PED-8]] Listar ordenes de compra
- **blocks:** [[PED-89 - APP - Feat - Leer Guardar comentario|PED-89]] APP - Feat - Leer / Guardar comentario

## Descripcion

Utilizaremos un recurso para leer y crear comentarios asociados a una orden

Este pedido seguirá mas adelante todo el camino y sera Editable en todo momento

```
GET {API_URL}/v1/purchaserComments/{order}
```

```
POST {API_URL}/v1/purchaserComments/{order}
```

```
{
  comment: {value}
}
```

```
IF NOT EXISTS
    (SELECT order FROM [NB_WEB].[dbo].[purchaseOrderComments] WHERE order = ?)
BEGIN
    INSERT INTO [NB_WEB].[dbo].[purchaseOrderComments] (order,comment) VALUES (?,?)
END
ELSE
BEGIN
UPDATE [NB_WEB].[dbo].[comentariosPedidos] SET comment = ? WHERE order = ?
END
```
