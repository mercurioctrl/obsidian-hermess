---
jira_key: "PED-43"
aliases: ["PED-43"]
summary: "APP - Feat - Pedir autorizacion y redirigir "
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-08-21 19:51"
updated: "2023-08-24 17:10"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-43"
---

# PED-43: APP - Feat - Pedir autorizacion y redirigir 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-08-21 19:51 |
| Actualizado | 2023-08-24 17:10 |
| Etiquetas | ninguna |
| Jira | [PED-43](https://bluinc.atlassian.net/browse/PED-43) |

## Relaciones

- **Padre:** [[PED-40 - Login automático como cliente|PED-40]] Login automático como cliente
- **is blocked by:** [[PED-41 - API - Feat - Crear autorizacion en la api de ordenes|PED-41]] API - Feat - Crear autorizacion en la api de ordenes
- **is blocked by:** [[PED-44 - APP - Feat - Login meidante autorizacion en el sitio web|PED-44]] APP - Feat - Login meidante autorizacion en el sitio web
- **blocks:** [[PED-42 - API - Feat - Login mediante autorizacion en el sitio web|PED-42]] API - Feat - Login mediante autorizacion en el sitio web 

## Descripcion

Agregaremos un accionable en el listado de cliente (mas adelante tendremos una herramienta en el contexto para esto) que ejecute el recurso [link](https://lioteam.atlassian.net/browse/PED-41) que nos devolverá un token.

Una vez obtenido el token redirigiremos al sitio web y si recurso de autoLogin, creado para tal fin [link](https://lioteam.atlassian.net/browse/PED-44)
