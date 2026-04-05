---
jira_key: "PEGA-154"
summary: "API - Refactor - Problema con la validacion de envio de correo"
status: "Finalizada"
type: "Subtarea"
priority: "Highest"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-12-10 12:22"
updated: "2024-12-13 10:39"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-154"
---

# PEGA-154: API - Refactor - Problema con la validacion de envio de correo

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Highest |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-12-10 12:22 |
| Actualizado | 2024-12-13 10:39 |
| Etiquetas | ninguna |
| Jira | [PEGA-154](https://bluinc.atlassian.net/browse/PEGA-154) |

## Descripción

```
POST {API_URL}/v1/addMyInventory
```

```
{
"email":"as@nb.com.ar", <-- obligatorio
"name":"As",
"siteUrl":"",
"siteApi":"",
"apiDocumentationUrl":"",
"storeName":"As",
"comment":"sdadsadsad"
}
```

```
{
    "errors": {
        "status": 500,
        "title": "Undefined array key \"siteUrl\"",
        "file": "\/var\/www\/app\/app\/Service\/Cms\/Inventory\/InventoryService.php",
        "line": 47
    }
}
```

No deberia ser obligatorio ningun dato para el back salvo el correo, en todo caso llega vacio.
