---
jira_key: "POS-326"
aliases: ["POS-326"]
summary: "API - Refactor - Agregar excepción para ingreso de RMA fuera de garantía con validación de usuario y registro "
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-04-23 07:50"
updated: "2025-05-07 10:05"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-326"
---

# POS-326: API - Refactor - Agregar excepción para ingreso de RMA fuera de garantía con validación de usuario y registro 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-04-23 07:50 |
| Actualizado | 2025-05-07 10:05 |
| Etiquetas | ninguna |
| Jira | [POS-326](https://bluinc.atlassian.net/browse/POS-326) |

## Relaciones

- **Padre:** [[POS-325 - Excepciones de garantía|POS-325]] Excepciones de garantía
- **has action item:** [[POS-327 - APP - Feat - ermitir solicitud de excepción para ingreso de RMA fuera de|POS-327]] APP - Feat - ermitir solicitud de excepción para ingreso de RMA fuera de garantía con revalidación de usuario y motivo obligatorio

## Descripcion

Actualmente, los productos sin garantía no pueden ser ingresados al sistema de postventa. Se solicita implementar una excepción controlada que permita el ingreso manual de RMA bajo las siguientes condiciones:

Si el endpoint 

```
GET {API_URL}/v1/getSerial/{serial}
```

 devuelve `"currentWarranty": false`, se permitirá realizar un bypass manual.

Para esto, el backend debe:

- Exponer un recurso que valide la contraseña del usuario actual y cree la exepecion en si misma

```
POST {API_URL}/v1/makeSerialExcpetion
```

```
{
  "serialNumber": "TR500CAGMU000277",
  "observation": "Cliente solicita excepción por compra institucional con acuerdo especial.",
  "password": "contraseña_del_usuario"
}
```


- Si la contraseña es correcta, se debe registrar el pedido de excepción en una nueva tabla `RMA_GARANTIA_EXCEPCION` (o similar según la lógica de tablas vigentes) con los siguientes campos:

- `id`


- `user_id`


- `serial_number`


- `product_id`


- `sale_date`


- `warranty`


- `elapsed_months`


- `observation` (motivo ingresado por el usuario)


- `created_at`




- Cambiar la respuesta de `"currentWarranty": false` a `"currentWarranty": true` para permitir el ingreso del RMA para que el front pueda cargarlo normalmente luego de esto.


- Enviar un correo a `gerencia@nb.com.ar` notificando el pedido de excepción con los siguientes datos:

- Usuario solicitante


- Fecha y hora de la solicitud


- Serial


- Referencia de venta


- Motivo/observación ingresado





**Criterios de aceptación:**

- Validación exitosa de la contraseña.


- Registro en base de datos correcto.


- Email enviado a gerencia con los datos completos.


- Modificación del flag `currentWarranty` a `true` cuando corresponda.
