---
jira_key: "PED-774"
aliases: ["PED-774"]
summary: "API - Refactor - Al crear un cliente no aparece seteada la divisa"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-07-19 14:53"
updated: "2024-07-23 18:01"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-774"
---

# PED-774: API - Refactor - Al crear un cliente no aparece seteada la divisa

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-07-19 14:53 |
| Actualizado | 2024-07-23 18:01 |
| Etiquetas | ninguna |
| Jira | [PED-774](https://bluinc.atlassian.net/browse/PED-774) |

## Relaciones

- **Padre:** [[PED-600 - EdicionAlta de cliente|PED-600]] Edicion/Alta de cliente

## Descripcion

Según pude ver, hay muchos clientes que se dan de alta de esta forma



[adjunto]
Cuando fui a ver el recurso, parece estarse guardando en NULL al crear un cliente.

**El valor por defecto deveria ser id_divisa =1 y ccoddiv = 'DOL'**

Por otro lado note algunos registros que estan en PSO Y con id_divisa = 0 ESTO ES INCORRECTO 

[adjunto]
DEBERIA SER ASI

[adjunto]
no se si cuando cambias la divisa o cuando, lo marca asi en cero
