---
jira_key: "LIO-91"
aliases: ["LIO-91"]
summary: "API - AutoLogin desde pedidos - Invalidar token al utilizar"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Guillermo Avila"
created: "2024-08-16 04:02"
updated: "2024-08-26 00:04"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-91"
---

# LIO-91: API - AutoLogin desde pedidos - Invalidar token al utilizar

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Guillermo Avila |
| Creado | 2024-08-16 04:02 |
| Actualizado | 2024-08-26 00:04 |
| Etiquetas | ninguna |
| Jira | [LIO-91](https://bluinc.atlassian.net/browse/LIO-91) |

## Relaciones

- **Padre:** [[LIO-1]] Experiencia del Usuario (UX)
- **relates to:** [[LIO-85]] API - Feat - AutoLogin desde pedidos

## Descripcion

Una vez que el token se haya utilizado para iniciar sesión, este no debería poder utilizarse.

Te comparto dos capturas con diferentes ventanas utilizando el mismo token:

[adjunto]
[adjunto]
---

Actualización 19/08/24

Al generar el token, se asigna una fecha de expiración de 10 minutos. Sin embargo, al intentar acceder por primera vez, el token expira antes de ingresar, impidiendo el acceso.

[adjunto]
[adjunto]
[adjunto]
