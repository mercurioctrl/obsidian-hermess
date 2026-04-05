---
jira_key: "PED-674"
aliases: ["PED-674"]
summary: "APP - Feat - Agregar correo electronico del cliente a los detalles de la liquidacion"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2024-04-17 08:29"
updated: "2024-04-19 21:23"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-674"
---

# PED-674: APP - Feat - Agregar correo electronico del cliente a los detalles de la liquidacion

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2024-04-17 08:29 |
| Actualizado | 2024-04-19 21:23 |
| Etiquetas | ninguna |
| Jira | [PED-674](https://bluinc.atlassian.net/browse/PED-674) |

## Relaciones

- **Padre:** [[PED-123 - Feat - Liquidar pedido|PED-123]] Feat - Liquidar pedido
- **is blocked by:** [[PED-673 - API - Feat - Agregar correo electronico del cliente a los detalles del pedido|PED-673]] API - Feat - Agregar correo electronico del cliente a los detalles del pedido
- **blocks:** [[SNB-1768 - PONER PALABRA CLAVE VISIBLE|SNB-1768]] PONER PALABRA CLAVE VISIBLE

## Descripcion

En base a las sugerencias del cliente en [link](https://lioteam.atlassian.net/browse/SNB-1768)  agregaremos en el formulario de liquidación el correo del cliente pre cargado y con la oportunidad de cambiarlo.

Diria de cambiarlo en tiempo real (independiente de la liquidacion), con un lapizito al igual que se hace con la cotización.

Al cambiarlo mostrar un mensaje como “Si realiza este cambio, cambiara el correo del cliente para todos los correos y mensajes del sistema ¿desea continuar””. 



Y para leer el correo y el userId usaremos el recurso [link](https://lioteam.atlassian.net/browse/SNB-1768) 

```
GET {APU_URL}/v1/orders/{ORDER}
```

Usaremos el recurso 

```
PATCH {APU_URL}/v1/user/{userId}
```

[adjunto]


Solo es necesario agregar el correo del cliente, para poder ofrecer cambiarlo antes de cerrar la venta y de esta forma tener la oportunidad de verificarlo y cambiarlo en cada oportunidad en caso de que sea incorrecto.

```
{
    "orderNumber": "10343845",
    "branchNumber": "0002",
    "albnumNumber": "00577365",
    "realAlbumNumber": null,
    "clientName": "MERCURIO CATRIEL EDUARDO",
    "clientEmail": "correoDelClienteEnUsuarios@correo.com", <<<--- NUEVO PARAMETRO
    "clientId": 26806,
    "observation": null,
    "status": "S",
    "invoice": null,
    "token": null,
    "voucherId": null,
    "seller": "Sistema",
    "sellerId": "12 ",
    "sellerCreator": "Sistema Web",
    "sellerIdCreator": "12 ",
    "items": [
    ...
}
```
