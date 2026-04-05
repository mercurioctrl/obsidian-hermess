---
jira_key: "NBWEB-703"
summary: "API - Refactor - Agregar parametros para guardar correo y nombre del cliente"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-04-11 14:59"
updated: "2024-04-15 17:06"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-703"
---

# NBWEB-703: API - Refactor - Agregar parametros para guardar correo y nombre del cliente

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-04-11 14:59 |
| Actualizado | 2024-04-15 17:06 |
| Etiquetas | ninguna |
| Jira | [NBWEB-703](https://bluinc.atlassian.net/browse/NBWEB-703) |

## Descripción

Refactorizaremos el recurso para agregar el objeto `dpPayload` (opcional)

```
POST /v1/carrito/process
```

```
{
    "note": "",
    "medioDePagoId": 5,
    "codigoPostalFavorito": "1407",
    "mediodeEnvioId": 3030,
    "idDirCli": "19337",
    "dropShipping": "true",
    "dpPayload": [
      "clientName": "nombre del cliente", <-- NUEVO OPCIONAL
      "clientEmail": "cliente@email.com" <-- NUEVONUEVO OPCIONAL
    ]
    "datosBultos": {
        "weightKg": 0.6,
        "sizeCm": "12.16x12.16x12.16",
        "amount": 1
    },
    "salePriceItems": [
        {
        "salePrice": 122.34,
        "id": 109150
        },
        {
        "salePrice": 3122.34,
        "id": 116471
        }
    ]
}
```

Esta informacion la guardaremos en la tabla `[NewBytes_DBF].[dbo].[dropShipping]` que enlazaremos a traves de order y branch
