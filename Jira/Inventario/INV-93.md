---
jira_key: "INV-93"
summary: "API - Refactor - Agregar parametro companyCode a los productos"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-08-15 14:05"
updated: "2024-08-20 11:32"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-93"
---

# INV-93: API - Refactor - Agregar parametro companyCode a los productos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-08-15 14:05 |
| Actualizado | 2024-08-20 11:32 |
| Etiquetas | ninguna |
| Jira | [INV-93](https://bluinc.atlassian.net/browse/INV-93) |

## Descripción

Agregaremos a la tabla `NewBytes_DBF.dbo.articulos` la columna `companyCode` para designar un producto como de una empresa especifica de manera no excluyente. 

Funciona con los valores de este repo  `[NewBytes_DBF].[dbo].[FP_Empresas]`

Refactorizaremos tanto la lectura(tanto como parametro en la respuesta, como filtro en la peticion) como la modificación para incluirlo

```
GET /item?companyCode={companyCode/null}
```

El Filtro puede ser especifico o estar vacio y en ese caso no lo utilizamos.

```
{
..
        "companyCode": 8,
        "description": "MUGELLO SRL"
..
}
```

```
PATCH /item/{itemId}
```

```
{
  
"companyCode": 8
}

```
