---
jira_key: "COM-282"
aliases: ["COM-282"]
summary: "API - Review - al editar  el IVA -> el IVA no se refleja correctamente en el listado"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Marbe Moreno"
created: "2026-01-29 17:02"
updated: "2026-02-11 13:49"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-282"
---

# COM-282: API - Review - al editar  el IVA -> el IVA no se refleja correctamente en el listado

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Marbe Moreno |
| Creado | 2026-01-29 17:02 |
| Actualizado | 2026-02-11 13:49 |
| Etiquetas | ninguna |
| Jira | [COM-282](https://bluinc.atlassian.net/browse/COM-282) |

## Relaciones

- **Padre:** [[COM-9]] Listar ordenes de compra
- **has action item:** [[COM-283]] APP - Cambiar IVA por (taxAmount) impuestos en el listado de ordenes

## Descripcion

**Descripción:**
En el listado de ordenes, al editar una orden y agregarle IVA a un producto, el *total final* en el listado no se calcula correctamente.
Además, el campo correspondiente a *IVA* figura con valor **0**, cuando debería reflejar el monto aplicado.

**Pasos para reproducir:**

- Crear una nueva orden de compra


- Agregar un ítem


- Aplicar IVA


- Ir al listado de compras



**Resultado actual:**

- El total final es correcto


- El valor de *IVA* aparece en **0**



**Resultado esperado:**

- El valor de *IVA* debería mostrarse correctamente en el listado, acorde al cálculo aplicado en la orden





[adjunto]
