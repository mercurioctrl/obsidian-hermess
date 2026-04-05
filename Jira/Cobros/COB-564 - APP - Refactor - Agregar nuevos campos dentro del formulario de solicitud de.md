---
jira_key: "COB-564"
aliases: ["COB-564"]
summary: "APP - Refactor - Agregar nuevos campos dentro del formulario de solicitud de salida de retiro (y precarga para generar la salida)"
status: "Finalizada"
type: "Tarea"
priority: "Low"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-06-03 07:47"
updated: "2025-07-14 10:33"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-564"
---

# COB-564: APP - Refactor - Agregar nuevos campos dentro del formulario de solicitud de salida de retiro (y precarga para generar la salida)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Low |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-06-03 07:47 |
| Actualizado | 2025-07-14 10:33 |
| Etiquetas | ninguna |
| Jira | [COB-564](https://bluinc.atlassian.net/browse/COB-564) |

## Relaciones

- **Padre:** [[COB-19]] Cola de salidas
- **action item from:** [[COB-562]] API - Refactor - Agregar informacion a las salidas pendientes necesaria para retiros de wallet  (POST)
- **action item from:** [[COB-563]] API - Refactor - Agregar informacion a las salidas pendientes necesaria para retiros de wallet (GET)
- **action item from:** [[COB-565]] API - Refactor - Incluir datos bancarios y cliente en proceso de salida de fondos que se hace con cashOut para procesar una solicitud de salida

## Descripcion

Revisa la historia completa y avisame si consideras que requiere algún cambio

Utilizando los refactors aplicados en [link](https://bluinc.atlassian.net/browse/COB-562)  y [link](https://bluinc.atlassian.net/browse/COB-563) 
Formulario para crear solicitud de salida

[adjunto]
Formulario para dar salida a una solicitud preexistente

[adjunto]
En ambos debo poder visualizar la nueva informacion

```
{
  "userIdLo": 32,
  "clientId": 3434 <-- Este es el cliente para NB
  "clientsBankAccountId": 432,
  "bankCBU": "2850590940090418135201",
  "bankAlias": "juanperez.mp",
  "output_concept_id": "retiros billetera libre opcion"
}
```
