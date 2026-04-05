---
jira_key: "EXP-28"
aliases: ["EXP-28"]
summary: "API - Feat - Procesar un pase de expedición"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-11-01 12:32"
updated: "2023-03-13 15:57"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-28"
---

# EXP-28: API - Feat - Procesar un pase de expedición

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-11-01 12:32 |
| Actualizado | 2023-03-13 15:57 |
| Etiquetas | ninguna |
| Jira | [EXP-28](https://bluinc.atlassian.net/browse/EXP-28) |

## Relaciones

- **Padre:** [[EXP-19]] Feat -Procesar pases de mercadería

## Descripcion

```
PATCH {{API_URL}}/v1/passes
```

Es prácticamente lo mismo que [https://lioteam.atlassian.net/browse/POS-97](https://lioteam.atlassian.net/browse/POS-97) solo que hay una verificación de login.

Para esto vamos a obtener un permiso para realizar la accion.

Introducimos entonces un recurso extra en la base del proyecto llamado “autorización” el cual utilizaremos varias veces al momento de despachar mercadería para cualquier fin.
