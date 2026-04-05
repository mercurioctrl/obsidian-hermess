---
jira_key: "PED-691"
aliases: ["PED-691"]
summary: "API - Autorizar pedido (cobrar) liquidado si tiene el comprobante guardado y si es de libre opcion"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-04-23 13:18"
updated: "2025-04-08 08:16"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-691"
---

# PED-691: API - Autorizar pedido (cobrar) liquidado si tiene el comprobante guardado y si es de libre opcion

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-04-23 13:18 |
| Actualizado | 2025-04-08 08:16 |
| Etiquetas | ninguna |
| Jira | [PED-691](https://bluinc.atlassian.net/browse/PED-691) |

## Relaciones

- **Padre:** [[PED-5 - Comprobantes|PED-5]] Comprobantes
- **blocks:** [[PED-692 - APP - Feat - Agregar el boton para autorizar un pedido de libre opcion cuando|PED-692]] APP - Feat - Agregar el boton para autorizar un pedido de libre opcion cuando tiene comprobante de banco
- **is blocked by:** [[PED-702 - API - Autorizar pedido liquidado con comprobante y de LO - Datos del|PED-702]] API - Autorizar pedido liquidado con comprobante y de LO - Datos del comprobante completos
- **relates to:** [[PED-740 - API - Refactor - Autorizar pedido liquidado con comprobante de LO - Considerar|PED-740]] API - Refactor - Autorizar pedido liquidado con comprobante de LO - Considerar sobrante del monto transferido
- **blocks:** [[LIO-56 - API - PED - Refactor - Al hacer una autorizacion (ID_STATUS = 2) para un PEDIDO|LIO-56]] API - PED - Refactor - Al hacer una autorizacion (ID_STATUS = 2) para un PEDIDO DE LIBRE OPCION debe marcarse como cobrado tambien en libre opcion
- **has action item:** [[PED-979 - API - Refactor - Al autorizar un pedido de banco (casos especificos de LO)|PED-979]] API - Refactor - Al autorizar un pedido de banco (casos especificos de LO) marcaremos el movimiento de billetera
- **has action item:** [[PED-982 - API - Refactor - Guardar cotización al autorizar un pago de Libre Opción con|PED-982]] API - Refactor - Guardar cotización al autorizar un pago de Libre Opción con comprobante (Billetera Lo)

## Descripcion

Lo que necesitamos hacer es que un pedido liquidado se pueda autorizar (como se hace en cobros cuando es pedido por banco). 

Lo que se busca es:

- hacer una autorización simplificada del cobro: Es decir marcar (id_status =2)


- Que se cree su nontaxvoucher


- Envie la plata al banco correcto


- Ponga el asiento del cobro en la cuenta corriente del cliente.





Las condiciones necesarias para que se permita hacer esto son

- Que el monto abonado y cargado en el formulario sea mayor o igual al monto del pedido.


- Que estén todos los datos del comprobante guardados, incluido el archivo


- Que sea un pedido de libre opción


- Que ya se encuentre liquidado



Avisame cuando lo leas y lo revisamos en una meet!
