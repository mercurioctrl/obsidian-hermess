---
jira_key: "PED-1097"
aliases: ["PED-1097"]
summary: "APP - Feat - Hacer reembolso a la wallet a parir de una devolución en cuenta corriente"
status: "Finalizada"
type: "Subtarea"
priority: "High"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-09-10 12:23"
updated: "2025-09-18 01:10"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1097"
---

# PED-1097: APP - Feat - Hacer reembolso a la wallet a parir de una devolución en cuenta corriente

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | High |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-09-10 12:23 |
| Actualizado | 2025-09-18 01:10 |
| Etiquetas | ninguna |
| Jira | [PED-1097](https://bluinc.atlassian.net/browse/PED-1097) |

## Relaciones

- **Padre:** [[PED-54 - Cuenta corriente de clientes|PED-54]] Cuenta corriente de clientes
- **action item from:** [[PED-1075 - API - Feat - Hacer reembolso a la wallet a parir de una devolución en cuenta|PED-1075]] API - Feat - Hacer reembolso a la wallet a parir de una devolución en cuenta corriente
- **action item from:** [[PED-1098 - APP - Refactor - Agragar HMAC y showWallet solo cuando esta disponible al|PED-1098]] APP - Refactor - Agragar HMAC y showWallet solo cuando esta disponible al objeto de cuenta corriente

## Descripcion

Agregaremos un “accionable” que diga “Mostrar en Billetera” con un mensaje de confirmación.

Si se confirma se ejecuta el recurso [link](https://bluinc.atlassian.net/browse/PED-1075) 

En el caso de que `HMAC`este completo para ese movimiento, y `showWallet` sea `true`entonces el accionable estará desactivado, ya que el movimiento ya fue realizado.

[adjunto]
