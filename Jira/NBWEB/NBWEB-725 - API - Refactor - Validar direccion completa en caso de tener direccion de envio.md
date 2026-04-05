---
jira_key: "NBWEB-725"
aliases: ["NBWEB-725"]
summary: "API - Refactor - Validar direccion completa en caso de tener direccion de envio y dar respuesta en consecuencia"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-04-26 09:32"
updated: "2024-05-02 20:43"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-725"
---

# NBWEB-725: API - Refactor - Validar direccion completa en caso de tener direccion de envio y dar respuesta en consecuencia

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-04-26 09:32 |
| Actualizado | 2024-05-02 20:43 |
| Etiquetas | ninguna |
| Jira | [NBWEB-725](https://bluinc.atlassian.net/browse/NBWEB-725) |

## Relaciones

- **Padre:** [[NBWEB-602 - Sitio Web|NBWEB-602]] Sitio Web
- **is blocked by:** [[NBWEB-724 - API - Feat - Agregaremos como posibilidad enviar la provincia sola, y en lugar|NBWEB-724]] API - Feat - Agregaremos como posibilidad enviar la provincia sola, y en lugar de placeId, enviaremos placeTxt
- **blocks:** [[PED-701 - APP - Refactor - Nueva validación al descargar una orden para cuando tiene una|PED-701]] APP - Refactor - Nueva validación al descargar una orden para cuando tiene una dirección incompleta 

## Descripcion

Refactorizaremos

```
POST {API_URL}/v1/downloadOrder/{order}
```

para que la** primera validación** sea la de dirección. Es decir, que según los cambios que aplicamos en [link](https://lioteam.atlassian.net/browse/NBWEB-724)  deberemos revisar la dirección asociada al pedido (en caso de que tenga una) y si verificamos que esta incompleta (solo tiene provinceId y placeTxt, en vez de tener placeId) entonces lanzaremos una excepción que interrumpa la descargad de la orden y devuelva 

```
{
    "success": false,
    "msg": "Completa bien la direccion cargada por el cliente",
    "items": [
        {
            "provinceId": 103506,
            "customerAddressId": 56223,
            "placeTxt": "Lo que pusieron en localidad",
            "clientId": 3433
        }
    ]
}
```

Estos datos sirven para que se pueda levantar el modal de edición correctamente
