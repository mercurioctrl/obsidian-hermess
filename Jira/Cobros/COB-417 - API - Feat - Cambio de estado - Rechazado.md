---
jira_key: "COB-417"
aliases: ["COB-417"]
summary: "API - Feat - Cambio de estado -> Rechazado"
status: "Gamma"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-04-26 15:03"
updated: "2023-04-28 07:44"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-417"
---

# COB-417: API - Feat - Cambio de estado -> Rechazado

| Campo | Valor |
|-------|-------|
| Estado | Gamma (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-04-26 15:03 |
| Actualizado | 2023-04-28 07:44 |
| Etiquetas | ninguna |
| Jira | [COB-417](https://bluinc.atlassian.net/browse/COB-417) |

## Relaciones

- **Padre:** [[COB-183 - Feat - Listar cheques|COB-183]] Feat - Listar cheques

## Descripcion

Este cambio se da cuando el banco informa que el cheque no tiene fondo y fue justamente rechazado.

Refactorizaremos el recurso 

```
PATCH {API_URL}/v1/checks/
```

```
[
   {
      "checkId":328542,
      "newStatus":5,
   },
   {
      "checkId":328541,
      "newStatus":5,
   }
]
```

*no reciba bankId porque ya esta en el primer movimiento del cheque, cuando fue depositado.

Lo mas importante es trasladar la deuda al cliente y descontar el movimiento bancario que hicimos en el deposito original.

Para eso debemos crear un registro en la tabla, con el codigo TR 32	- Débitos Varios (segun la tabla `[NEW_BYTES].[dbo].[GL_TRANSACCIONES]`)

```
[NEW_BYTES].[dbo].[MC_CCORRIENTES_MOVIMIENTOS]
```

Siempre un cheque rechazado, **estuvo antes en estado vendido o depositado. **

Y por ultimo anularemos el movimiento de `[NEW_BYTES].[dbo].[BA_BP_MOVIMIENTOS_ENTRADAS]` (si queres charlamos sobre esto, porque no se si hacerlo negativo, anular, o ponerlo en salidas)
