---
jira_key: "PED-44"
aliases: ["PED-44"]
summary: "APP - Feat - Login meidante autorizacion en el sitio web"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-08-21 20:08"
updated: "2023-08-25 11:28"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-44"
---

# PED-44: APP - Feat - Login meidante autorizacion en el sitio web

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-08-21 20:08 |
| Actualizado | 2023-08-25 11:28 |
| Etiquetas | ninguna |
| Jira | [PED-44](https://bluinc.atlassian.net/browse/PED-44) |

## Relaciones

- **Padre:** [[PED-40]] Login automático como cliente
- **blocks:** [[PED-43]] APP - Feat - Pedir autorizacion y redirigir 
- **is blocked by:** [[PED-42]] API - Feat - Login mediante autorizacion en el sitio web 

## Descripcion

**Contexto:** Siguiendo el modelo implementado en [NB](https://www.nb.com.ar/login), se propone la creación de un nuevo endpoint que permita gestionar el proceso de autologin.

**Objetivo:** Desarrollar un endpoint que reciba solicitudes de autologin desde el ticket [link](https://lioteam.atlassian.net/browse/PED-43) 

**Funcionalidad:** Una vez que se accede al nuevo endpoint, se realizará el proceso de login utilizando la lógica definida en [link](https://lioteam.atlassian.net/browse/PED-42)
