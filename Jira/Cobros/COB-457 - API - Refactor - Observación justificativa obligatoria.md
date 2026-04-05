---
jira_key: "COB-457"
aliases: ["COB-457"]
summary: "API - Refactor - Observación justificativa obligatoria"
status: "CodeReview"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-07-10 09:05"
updated: "2023-07-10 16:43"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-457"
---

# COB-457: API - Refactor - Observación justificativa obligatoria

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-07-10 09:05 |
| Actualizado | 2023-07-10 16:43 |
| Etiquetas | ninguna |
| Jira | [COB-457](https://bluinc.atlassian.net/browse/COB-457) |

## Relaciones

- **Padre:** [[COB-456 - Refactor - Limitaciones para ingresar dinero a mano cuando no selecciono un|COB-456]] Refactor - Limitaciones para ingresar dinero "a mano" cuando no selecciono un pedido
- **blocks:** [[COB-458 - APP - Refactor - Nuevo modal emergente con formulario de ingreso de dinero a|COB-458]] APP - Refactor - Nuevo modal emergente con formulario de ingreso de dinero "a mano" 

## Descripcion

Pediremos una justificación obligatoria (mínimo 25 caracteres) y marcaremos el comentario de la siguiente manera al realizar un ingreso de dinero directo en la cuenta, sin seleccionar productos, quedando de la siguiente manera.

{USUARIO} REALIZA INGRESO IMPRUDENTE, justifica: {Justificacion} + Observacion (si la tiene de alguna forma)



Adicionalmente enviaremos esa misma informacion en un correo a [gerencia@nb.com.ar](mailto:gerencia@nb.com.ar) como hacemos en otros casos agregando la misma leyenda que compusimos arrib y agregando el saldo y el cliente para dar contexto en el correo.
