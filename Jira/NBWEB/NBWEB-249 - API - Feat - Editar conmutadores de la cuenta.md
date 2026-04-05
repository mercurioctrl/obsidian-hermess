---
jira_key: "NBWEB-249"
aliases: ["NBWEB-249"]
summary: "API - Feat - Editar conmutadores de la cuenta"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-06-09 16:03"
updated: "2022-06-26 20:15"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-249"
---

# NBWEB-249: API - Feat - Editar conmutadores de la cuenta

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-06-09 16:03 |
| Actualizado | 2022-06-26 20:15 |
| Etiquetas | ninguna |
| Jira | [NBWEB-249](https://bluinc.atlassian.net/browse/NBWEB-249) |

## Relaciones

- **Padre:** [[NBWEB-2]] API - Mi cuenta

## Descripcion

```
PATCH {{API_URL}}/v1/miCuenta/switch/{userId}
```



```
{
  *"defaultCurrency":true,
  *"defaulIvas":false,
  *"defaulStock":false
}
```
