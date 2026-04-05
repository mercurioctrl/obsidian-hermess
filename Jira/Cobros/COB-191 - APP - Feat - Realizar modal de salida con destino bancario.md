---
jira_key: "COB-191"
aliases: ["COB-191"]
summary: "APP - Feat - Realizar modal de salida con destino bancario"
status: "CodeReview"
type: "Historia"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2022-10-21 09:31"
updated: "2022-10-26 13:22"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-191"
---

# COB-191: APP - Feat - Realizar modal de salida con destino bancario

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2022-10-21 09:31 |
| Actualizado | 2022-10-26 13:22 |
| Etiquetas | ninguna |
| Jira | [COB-191](https://bluinc.atlassian.net/browse/COB-191) |

## Relaciones

- **Padre:** [[COB-16]] Cuentas bancarias
- **is blocked by:** [[COB-177]] API - Feat - Realizar salida con destino bancario

## Descripcion

Basandonos en el mismo modal de [link](https://lioteam.atlassian.net/browse/COB-102) se debe generar lo mismo, pero para salidas bancarias.

Para eso utilzaremos [link](https://lioteam.atlassian.net/browse/COB-177)para procesar el formulario.

Como repositorio de destino para los bancos, usaremos [link](https://lioteam.atlassian.net/browse/COB-9)

Esto afecta el saldo de caja por lo tanto debe refrescarse al finalizar la operacion
