---
jira_key: "EXP-227"
aliases: ["EXP-227"]
summary: "API - Feat -Crear direccion para el cliente"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Ezequiel manzano"
created: "2023-03-02 12:41"
updated: "2023-05-16 09:56"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-227"
---

# EXP-227: API - Feat -Crear direccion para el cliente

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Ezequiel manzano |
| Creado | 2023-03-02 12:41 |
| Actualizado | 2023-05-16 09:56 |
| Etiquetas | ninguna |
| Jira | [EXP-227](https://bluinc.atlassian.net/browse/EXP-227) |

## Relaciones

- **Padre:** [[EXP-218 - Etiquetas para envíos que no las generan (genericas de ahora en mas)|EXP-218]] Etiquetas para envíos que no las generan (genericas de ahora en mas)
- **relates to:** [[EXP-228 - API - Feat - Crear direcciones|EXP-228]] API - Feat - Crear direcciones
- **blocks:** [[EXP-222 - APP - Feat - Modal para crear etiqueta de envío generica|EXP-222]] APP - Feat - Modal para crear etiqueta de envío generica

## Descripcion

```
{{API_URL}}/v1/shipments/createAddress
```



payload:

```
{
        "address": "Juan roman riquelme 10",
        "telefono": "1530510267",
        "localityId": "BSAS",
        "provinceId":  1,
        "postalCode": "1439",
        "telephone": "1123223222",
        "clientId": 25955 
}
```
