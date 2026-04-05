---
jira_key: "NBWEB-403"
aliases: ["NBWEB-403"]
summary: "API - Feat - Enviar correo a soporte cuando se carga un preingreso de postventa"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-07-12 13:26"
updated: "2022-10-18 08:59"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-403"
---

# NBWEB-403: API - Feat - Enviar correo a soporte cuando se carga un preingreso de postventa

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-07-12 13:26 |
| Actualizado | 2022-10-18 08:59 |
| Etiquetas | ninguna |
| Jira | [NBWEB-403](https://bluinc.atlassian.net/browse/NBWEB-403) |

## Relaciones

- **Subtarea:** [[NBWEB-471 - Revisar mensaje en gamma|NBWEB-471]] Revisar mensaje en gamma
- **is caused by:** [[POS-5 - API - Feat - Enviar correo con el preingreso de postventa|POS-5]] API - Feat - Enviar correo con el preingreso de postventa

## Descripcion

Se debe enviar un correo con la plantilla habitual con el siguiente texto.

```
El cliente [nombre de razon social] acaba de crear una solicitud de ingreso de mercaderia.
Si desea darla de alta como un ingreso en el sistema haga clic em el siguietne enlace

[enlace]
```
