---
jira_key: "PEGA-179"
aliases: ["PEGA-179"]
summary: "API - Feat - Feedback sobre informacion especifica de los productos (arrancaremos con envios)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-04-21 08:07"
updated: "2025-05-14 10:52"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-179"
---

# PEGA-179: API - Feat - Feedback sobre informacion especifica de los productos (arrancaremos con envios)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-04-21 08:07 |
| Actualizado | 2025-05-14 10:52 |
| Etiquetas | ninguna |
| Jira | [PEGA-179](https://bluinc.atlassian.net/browse/PEGA-179) |

## Relaciones

- **Padre:** [[PEGA-177]] Envios Gratis
- **has action item:** [[PEGA-180]] APP - Feat - Feedback sobre informacion especifica de los productos (arrancaremos con envios)

## Descripcion

Crear un endpoint para recibir feedback del usuario sobre si un producto tiene envío gratis, guardar la información en base de datos y enviar un correo a `info@preciosgamer.com` cada vez que se reciba un nuevo aporte.

```
POST {API_URL}/feedback/{itemId}
```

```
{
  "type": "shipping",
  "value": {true/false}
  "ip": {ip enviada por el front}
}
```

Crearemos una tabla en `PEGA.dbo.itemFeedback`


| Campo | Tipo | Descripción |
| --- | --- | --- |
| `id` | BIGINT | Identificador único (PK autoincremental) |
| `itemId` | VARCHAR(255) | ID del producto sobre el cual se reporta feedback |
| `type` | VARCHAR(50) | Tipo de feedback (por ahora solo `"shipping"`) |
| `value` | BOOLEAN | Valor del feedback (`true` o `false`) |
| `ip` | VARCHAR(45) | Dirección IP del usuario que envió el feedback |
| `created_at` | TIMESTAMP | Fecha y hora en la que se registró el feedback |

- Al recibir el `POST`, validar que `type` sea `"shipping"` u otro de los parametros posibles (por ahora solo esta este).


- Guardar los datos en la tabla `feedback`.


- Enviar un correo a `info@preciosgamer.com` con el contenido:

`Nuevo feedback recibido  `
`Producto ID: {itemId} `
`Tipo: {type} `
`Valor: {value} `
`IP: {ip} `
`Fecha: {created_at} `


-  Retornar HTTP 200 con `{ "status": "ok" }` si todo fue exitoso y el error en caso de contrario.
