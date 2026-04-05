---
jira_key: "LIO-385"
aliases: ["LIO-385"]
summary: "API - Refactor - Repositorios promocionales de la home, tienen algunas restricciones para que deben mostrar"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-07-13 21:19"
updated: "2025-07-22 12:10"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-385"
---

# LIO-385: API - Refactor - Repositorios promocionales de la home, tienen algunas restricciones para que deben mostrar

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-07-13 21:19 |
| Actualizado | 2025-07-22 12:10 |
| Etiquetas | ninguna |
| Jira | [LIO-385](https://bluinc.atlassian.net/browse/LIO-385) |

## Relaciones

- **Padre:** [[LIO-261]] Implementar Redis

## Descripcion

Haremos un refactor sobre los recursos

```
GET {API_URL}/v4/specialForYou
```

```
GET {API_URL}/v4/basedOnYourSearches
```

- Mostraremos solo los companyCode que se encuentren en mi `.env` separado por coma en un parametro llamado `COMPANY_CODE`


- Tampoco mostraremos nunca un producto que no disponee de imagen.
