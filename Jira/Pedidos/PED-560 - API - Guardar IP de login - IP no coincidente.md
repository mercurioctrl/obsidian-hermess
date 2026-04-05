---
jira_key: "PED-560"
aliases: ["PED-560"]
summary: "API - Guardar IP de login - IP no coincidente"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2024-02-14 17:05"
updated: "2024-06-11 16:09"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-560"
---

# PED-560: API - Guardar IP de login - IP no coincidente

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2024-02-14 17:05 |
| Actualizado | 2024-06-11 16:09 |
| Etiquetas | ninguna |
| Jira | [PED-560](https://bluinc.atlassian.net/browse/PED-560) |

## Relaciones

- **Padre:** [[PED-3]] Ordenes de compra
- **blocks:** [[PED-717]] API - Feat - Guardar IP de login

## Descripcion

Al iniciar sesión en Pedidos con la cuenta de máster, observo que la dirección IP registrada no coincide con la mía. Además, en el objeto users no aparece la IP como parámetro.

Quiero creer que es posible que el desplegado no se haya realizado con éxito.

[adjunto]
[adjunto]
---

Actualización 27/05/24

Realice la prueba de nuevo y obtengo los mismos resultados

- IP guardada no coincidente


- IP no devuelta en el objeto users
