---
jira_key: "PED-1341"
aliases: ["PED-1341"]
summary: "API - Refactor - Validación de unicidad de pago para evitar autorización de pedidos duplicados"
status: "Ready for QA"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2026-04-01 17:03"
updated: "2026-04-01 18:16"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1341"
---

# PED-1341: API - Refactor - Validación de unicidad de pago para evitar autorización de pedidos duplicados

| Campo | Valor |
|-------|-------|
| Estado | Ready for QA (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2026-04-01 17:03 |
| Actualizado | 2026-04-01 18:16 |
| Etiquetas | ninguna |
| Jira | [PED-1341](https://bluinc.atlassian.net/browse/PED-1341) |

## Relaciones

- **Padre:** [[PED-123 - Feat - Liquidar pedido|PED-123]] Feat - Liquidar pedido

## Descripcion

Se detectó un incidente en el cual se generaron **dos órdenes a partir de una misma compra con un único pago**, lo que derivó en la creación de **dos envíos asociados a una misma transacción**.

Actualmente, el sistema permite avanzar con la autorización de múltiples pedidos vinculados a una misma instancia de pago, lo cual genera inconsistencias operativas (duplicación de envíos, productos serializados duplicados, etc.).

#### **Problema**

No existe una validación que impida autorizar más de un pedido cuando comparten la misma instancia de pago (mismo número de operación / transacción).

#### **Objetivo**

Implementar una validación en el flujo de autorización de pedidos que garantice que:

- Una instancia de pago solo pueda ser utilizada para **autorizar un único pedido**.


- En caso de existir múltiples pedidos asociados a la misma instancia de pago:

- Retornar una excepción impidiendo avazar con el/los pedidos.





#### **Alcance técnico**

- Antes de autorizar un pedido:

- Verificar si ya existe otro pedido autorizado con la misma instancia de pago.




- Definir comportamiento en caso de duplicidad:

- Rechazo de autorización con mensaje claro.


- Logging del incidente para trazabilidad.





#### **Criterios de aceptación**

- No es posible autorizar más de un pedido con el mismo número de operación/pago.


- Se devuelve un error controlado al intentar autorizar un pedido duplicado.


- Se registran logs para auditoría.
