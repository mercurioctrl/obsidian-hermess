---
jira_key: "PED-730"
aliases: ["PED-730"]
summary: "API - Refactor - Que pueda editarse el numero de operacion"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-05-29 07:03"
updated: "2024-06-04 15:44"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-730"
---

# PED-730: API - Refactor - Que pueda editarse el numero de operacion

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-05-29 07:03 |
| Actualizado | 2024-06-04 15:44 |
| Etiquetas | ninguna |
| Jira | [PED-730](https://bluinc.atlassian.net/browse/PED-730) |

## Relaciones

- **Padre:** [[PED-729]] Comprobante de pago y autorizacion
- **blocks:** [[PED-731]] APP - Refactor - Que pueda editarse el numero de operacion

## Descripcion

```
PATCH {API_URL}/v1/paymentVoucher/{order}-{branch}
```

```
[
    {
        "id": 2013985,
        "nroOperacion": "3786618595"
    }
]
```



Respuesta http 200.

```
{
    "success": true,
    "message": "Numero de operación actualizado correctamente",
    "code": 200
}
```

Respuesta error: 401

```
{
    "success": true,
    "message": "No fue posible actualizar numero de operación",
    "code": 401
}
```

Errores de la capa del framework.

```
{
    "errors": {
        "status": 500,
        "title": "La orden no existe",
        "file": "/var/www/app/app/Repositories/PaymentVoucher/PaymentVoucherRepository.php",
        "line": 106
    }
}
```
