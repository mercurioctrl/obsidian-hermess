---
jira_key: "POS-155"
aliases: ["POS-155"]
summary: "API - Feat - Enviar correo al crear un pase"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-09-26 09:15"
updated: "2022-10-18 14:20"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-155"
---

# POS-155: API - Feat - Enviar correo al crear un pase

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-09-26 09:15 |
| Actualizado | 2022-10-18 14:20 |
| Etiquetas | ninguna |
| Jira | [POS-155](https://bluinc.atlassian.net/browse/POS-155) |

## Relaciones

- **Padre:** [[POS-95]] API - Feat - Pedir un pase de mercaderia
- **is blocked by:** [[POS-156]] APP - Feat - Aplicativo para responder pase desde el deposito

## Descripcion

Al crear un pase desde postventa necesitamos comunicar esto al departamento de expedición o quien sea el receptor del mismo.

Si bien el Q que viene vamos a trabajar en la aplicación de expedición lo cual nos permitirá notificarlos directamente dentro del sistema.

El correo que vamos a enviar es parecido a lo que hicimos en [link](https://lioteam.atlassian.net/browse/NBWEB-424) . Una plantilla simple con un enlace que nos lleve a un apartado sin login (pero mediante un token) dentro de la aplicación de de postventa que tendrá ([link](https://lioteam.atlassian.net/browse/POS-156)) para que los chicos de expedicion puedan ingresar el producto que van a transferir.
