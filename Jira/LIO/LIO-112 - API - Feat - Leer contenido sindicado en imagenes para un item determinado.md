---
jira_key: "LIO-112"
aliases: ["LIO-112"]
summary: "API - Feat - Leer contenido sindicado en imagenes para un item determinado"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-10-24 09:26"
updated: "2024-10-28 03:34"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-112"
---

# LIO-112: API - Feat - Leer contenido sindicado en imagenes para un item determinado

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-10-24 09:26 |
| Actualizado | 2024-10-28 03:34 |
| Etiquetas | ninguna |
| Jira | [LIO-112](https://bluinc.atlassian.net/browse/LIO-112) |

## Relaciones

- **Padre:** [[LIO-111]] Contenido sindicado
- **has action item:** [[LIO-113]] APP - Feat - Leer contenido sindicado en imagenes para un item determinado

## Descripcion

```
GET {API_URL}/v4/{itemId}/sindicateContentImg
```

```
{
    "sindicateContentImg": "https://i.imgur.com/bzJgKy9.jpeg"
}
```
