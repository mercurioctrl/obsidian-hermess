---
jira_key: "PED-562"
aliases: ["PED-562"]
summary: "API - Refactor - Listar ordenes de compra -> Agregar destino final"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Guillermo Avila"
created: "2024-02-15 19:05"
updated: "2024-02-22 14:03"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-562"
---

# PED-562: API - Refactor - Listar ordenes de compra -> Agregar destino final

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Guillermo Avila |
| Creado | 2024-02-15 19:05 |
| Actualizado | 2024-02-22 14:03 |
| Etiquetas | ninguna |
| Jira | [PED-562](https://bluinc.atlassian.net/browse/PED-562) |

## Relaciones

- **Padre:** [[PED-8]] Listar ordenes de compra
- **relates to:** [[PED-563]] APP -  Refactor - Listar ordenes de compra -> Agregar destino final
- **causes:** [[PED-567]] API - Listar ordenes de compra -> Agregar destino final - Error al abrir nueva cotización de envío

## Descripcion

Vamos a realizar una refactor en la cotización de envío para que, al abrirla, se puedan ver claramente tanto el destino principal como el destino final, en caso de que ya estén definidos. Adjunto una captura que muestra los recursos que se solicitan al abrir la cotización de envío.

[adjunto]
Dato extra:

El destino principal que aparece en “Envio NB“ no es el previamente definido, es la dirección predeterminada.
