---
jira_key: "EXP-96"
aliases: ["EXP-96"]
summary: "API - Refactor - Serialziar salida"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-12-12 13:04"
updated: "2023-01-27 12:01"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-96"
---

# EXP-96: API - Refactor - Serialziar salida

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-12-12 13:04 |
| Actualizado | 2023-01-27 12:01 |
| Etiquetas | ninguna |
| Jira | [EXP-96](https://bluinc.atlassian.net/browse/EXP-96) |

## Relaciones

- **Padre:** [[EXP-15]] Feat - Serializar salida

## Descripcion

Refactor sobre : [link](https://lioteam.atlassian.net/browse/EXP-66)

Cuando ejecutamos el recurso debe devolver la siguiente salida cuando estoy ingresando seriales que ya existen

Return:

```
{
    "msg": "Los siguientes serial ya existen",
    "serials"[
      FAT43939393934, 
      FAT43939393936, 
      FAT43939393937, 
      FAT43939393938, 
      FAT43939393939
    ]
    "success": false
}
```

Si se cargaron todos los seriales de ese item, de manera correcta se debe 

retornar 

```
{
    "msg": "La serializacion del producto esta completa",
    "success": true
}
```

Y se debe marcar en una columna de la tabla `[NEW_BYTES].[dbo].[MS_REMITO_DETALLE].SERIALIZADO`
