---
jira_key: "PED-541"
aliases: ["PED-541"]
summary: "APP - Feat - Maquetar cotizacion de \"Destino final para el transporte\""
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2024-02-07 16:31"
updated: "2024-02-13 02:31"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-541"
---

# PED-541: APP - Feat - Maquetar cotizacion de "Destino final para el transporte"

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2024-02-07 16:31 |
| Actualizado | 2024-02-13 02:31 |
| Etiquetas | ninguna |
| Jira | [PED-541](https://bluinc.atlassian.net/browse/PED-541) |

## Relaciones

- **Padre:** [[PED-58]] Agregar / Editar Envío en las ordenes de compra
- **is blocked by:** [[PED-543]] API - Feat - Agregar "Destinlo final para el transporte"
- **is blocked by:** [[PED-544]] API - Refactor - Cuando eliminamos un envio, debemos eliminar tambien el "destino final" que lo acompaña
- **relates to:** [[PED-554]] API - Destino final para el transporte - Eliminar destino final

## Descripcion

Maquetaremos como seria en el modal de cotización de envío la posibilidad de agregar una segunda dirección de “Destino final para el transparte:

[adjunto]
La idea es agregar debajo de todo un checkbox o algún tipo de accionable con la descripción “Viaja por transporte, agregar destino final”

Una vez activado, aparecerá abajo un selector de direcciones del cliente como el que esta arriba y nuevamente la posibilidad de agregar una nueva direccion.

Todo esto separado por alguna linea o de una forma clara para que no se mezcle con la idea del “envío de verdad” (lo que esta arriba).

```
POST {API_URL}/v1/orders/{branch-order}/addFinalShipping
```

```
{
  "customerAddressId":25976
}
```
