---
jira_key: "COM-54"
aliases: ["COM-54"]
summary: "API - Feat - Guardar / Leer comentario"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-02-20 09:15"
updated: "2024-02-21 14:53"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-54"
---

# COM-54: API - Feat - Guardar / Leer comentario

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-02-20 09:15 |
| Actualizado | 2024-02-21 14:53 |
| Etiquetas | ninguna |
| Jira | [COM-54](https://bluinc.atlassian.net/browse/COM-54) |

## Relaciones

- **Padre:** [[COM-38]] Ver orden de compra
- **blocks:** [[COM-55]] APP - Feat - Guardar / Leer comentario

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
