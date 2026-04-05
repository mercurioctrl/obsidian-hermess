---
jira_key: "COM-111"
aliases: ["COM-111"]
summary: "API - Feat - Crear orden de compra"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-06-24 13:00"
updated: "2025-05-13 14:45"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-111"
---

# COM-111: API - Feat - Crear orden de compra

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-06-24 13:00 |
| Actualizado | 2025-05-13 14:45 |
| Etiquetas | ninguna |
| Jira | [COM-111](https://bluinc.atlassian.net/browse/COM-111) |

## Relaciones

- **Padre:** [[COM-77]] Editar orden de compra
- **blocks:** [[COM-112]] APP - Feat - Agregar orden de compra
- **is blocked by:** [[COM-114]] API - Crear orden de compra - Error de tipo de dato
- **relates to:** [[COM-187]] API - Refactor- Crear orden de compra -> Guardar compañía 

## Descripcion

Crearemos un recurso para crear la base de una orden de forma tal que podamos editarlo posteriormente.


```
POST {{API_URL}}/v1/providerOrder
```

```
{
"provider":26806,
}
```



Al ejecutar este comando con  numero de proveedor crearemos una orden de compra a nombre de ese proveedor en la tabla

```
[NewBytes_DBF].[dbo].[PedProT]
```

Solo tendremos en cuenta la divisa del proveedor al momento de marcar `[NewBytes_DBF].[dbo].[PedProT].cCodDiv`
