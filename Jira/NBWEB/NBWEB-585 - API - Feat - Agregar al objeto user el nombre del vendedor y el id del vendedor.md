---
jira_key: "NBWEB-585"
aliases: ["NBWEB-585"]
summary: "API - Feat - Agregar al objeto \"user\" el nombre del vendedor y el id del vendedor para esa cuenta, si existe"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-09-20 08:52"
updated: "2023-09-20 10:51"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-585"
---

# NBWEB-585: API - Feat - Agregar al objeto "user" el nombre del vendedor y el id del vendedor para esa cuenta, si existe

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-09-20 08:52 |
| Actualizado | 2023-09-20 10:51 |
| Etiquetas | ninguna |
| Jira | [NBWEB-585](https://bluinc.atlassian.net/browse/NBWEB-585) |

## Relaciones

- **Padre:** [[NBWEB-498 - Oportunidades de mejora|NBWEB-498]] Oportunidades de mejora
- **blocks:** [[NBWEB-586 - APP - Feat - Agregar mensaje en el carrito y desplegable en la confirmación de|NBWEB-586]] APP - Feat - Agregar mensaje en el carrito y desplegable en la confirmación de la compra

## Descripcion

```
{API_URL}/v1/auth/user
```

```
{
    "user": {
        "id": 7463,
        "username": "catriel",
        "email": "hermess87@gmail.com",
        "shoppingCartId": "8182929",
        "codeFP": 19227,
        "showName": "catriel2",
        "blackUser": 1,
        "internalAgent": 12,
        "defaultCurrency": false,
        "defaultIvas": true,
        "defaultStock": true,
        "roleId": 1,
        ->"agentId": 12,
        ->"agentDescription": Catriel Mercurio
        
    }
}
```
