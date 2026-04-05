---
jira_key: "PED-1284"
aliases: ["PED-1284"]
summary: "APP - Refactor - Agregar selector de empresa de facturación con nuevo parámetro"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2026-01-26 08:17"
updated: "2026-01-27 00:36"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1284"
---

# PED-1284: APP - Refactor - Agregar selector de empresa de facturación con nuevo parámetro

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-26 08:17 |
| Actualizado | 2026-01-27 00:36 |
| Etiquetas | ninguna |
| Jira | [PED-1284](https://bluinc.atlassian.net/browse/PED-1284) |

## Relaciones

- **Padre:** [[PED-600]] Edicion/Alta de cliente
- **action item from:** [[PED-1283]] API - Refactor - Agregar nuevo parámetro voucherCompanyCode
- **has action item:** [[PED-1287]] API - Refactor - Agregar voucherCompanyCode para lectura

## Descripcion

En base a lo implementado en
[link](https://bluinc.atlassian.net/browse/PED-1283) 
se incorporará un nuevo selector utilizando el repositorio de empresas, que permitirá definir la empresa de facturación del cliente.

La empresa de facturación podrá ser distinta de la empresa a la que el cliente pertenece, manteniendo ambos conceptos desacoplados a nivel de interfaz.

---

### Criterios de aceptación

- Se visualiza un nuevo selector de empresa de facturación en la pantalla correspondiente.


- El selector utiliza el repositorio de empresas ya existente.


- Es posible seleccionar una empresa de facturación distinta de la empresa de pertenencia del cliente.


- La selección de la empresa de facturación no modifica ni afecta la empresa de pertenencia.


- El selector se integra sin romper el comportamiento actual de la vista ni los flujos existentes.


- La interfaz refleja correctamente la empresa de facturación seleccionada.



[adjunto]
