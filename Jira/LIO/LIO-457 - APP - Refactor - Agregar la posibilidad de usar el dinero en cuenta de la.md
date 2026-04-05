---
jira_key: "LIO-457"
aliases: ["LIO-457"]
summary: "APP - Refactor - Agregar la posibilidad de usar el dinero en cuenta de la billetera para una compra en el checkout"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-09-17 08:15"
updated: "2025-09-25 10:36"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-457"
---

# LIO-457: APP - Refactor - Agregar la posibilidad de usar el dinero en cuenta de la billetera para una compra en el checkout

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-09-17 08:15 |
| Actualizado | 2025-09-25 10:36 |
| Etiquetas | ninguna |
| Jira | [LIO-457](https://bluinc.atlassian.net/browse/LIO-457) |

## Relaciones

- **Padre:** [[LIO-231]] Billetera
- **action item from:** [[LIO-444]] API - Refactor - Traer monto de billetera en el checkout
- **has action item:** [[LIO-461]] APP - Refactor - Cambiar descripciones de medio de paago billetera

## Descripcion

Como **cliente**, quiero **usar parte o todo mi dinero en cuenta (billetera)** para pagar mi compra durante el checkout, **pudiendo elegir el monto a aplicar**, de manera similar a la referencia (ver captura) donde se ve un medio “Dinero disponible” y un **selector de monto**.

Nos basamos en el recurso del backend [link](https://bluinc.atlassian.net/browse/LIO-444) :

```
GET {API_URL}/pedidos/checkout/{id}
```

```
...
"walletBalance": {
  "available": number,   // saldo disponible total para usar en este checkout
  "usedHere":  number    // monto aplicado en este checkout (editable desde UI)
}
```

[adjunto]
## El frontend debe:

- **Mostrar** el saldo disponible (`available`) dentro del bloque de “Medios de pago”.


- **Permitir ingresar/seleccionar** el monto a usar (`usedHere`), con validaciones (esto seria ideal un modal para elegir el monto, no en el contexto).


- **Recalcular totales** del checkout en tiempo real al cambiar `usedHere` (esto es una logica muy similar a como mostramos un descuento).


- **Combinar** el uso de billetera con otro medio de pago (tarjeta/transferencia/efectivo), aplicando billetera **como primer componente** y el resto como complemento.
