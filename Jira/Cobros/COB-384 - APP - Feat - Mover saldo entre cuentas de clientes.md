---
jira_key: "COB-384"
aliases: ["COB-384"]
summary: "APP - Feat - Mover saldo entre cuentas de clientes"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2023-03-27 10:13"
updated: "2023-03-30 10:38"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-384"
---

# COB-384: APP - Feat - Mover saldo entre cuentas de clientes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2023-03-27 10:13 |
| Actualizado | 2023-03-30 10:38 |
| Etiquetas | ninguna |
| Jira | [COB-384](https://bluinc.atlassian.net/browse/COB-384) |

## Relaciones

- **Padre:** [[COB-380 - Feat - Mover saldo entre cuentas de cliente|COB-380]] Feat - Mover saldo entre cuentas de cliente
- **is blocked by:** [[COB-381 - API - Feat - Mover saldo entre cuentas de clientes|COB-381]] API - Feat - Mover saldo entre cuentas de clientes

## Descripcion

De la misma forma que agregamos un accionable en el modal donde se ve la cuenta corriente de los clientes, agregaremos otro “boton” que se activa cuando tiene saldo a favor llamado “Mover saldo”

El mismo ejecuta el recurso [link](https://lioteam.atlassian.net/browse/COB-381) 

Al accionarlo se desplega un modal que tiene un formulario con los siguientes campos

- Monto (decimal)


- Cliente destino (Este es un selector que usa el repo de clientes para seleccionar el id)


- Comentario (string)
