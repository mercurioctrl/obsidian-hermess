---
jira_key: "LIO-396"
aliases: ["LIO-396"]
summary: "API - Feat - Respuesta automatica generada por asistencia IA"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-07-29 08:45"
updated: "2025-08-11 10:44"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-396"
---

# LIO-396: API - Feat - Respuesta automatica generada por asistencia IA

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-07-29 08:45 |
| Actualizado | 2025-08-11 10:44 |
| Etiquetas | ninguna |
| Jira | [LIO-396](https://bluinc.atlassian.net/browse/LIO-396) |

## Relaciones

- **Padre:** [[LIO-391]] Desarrollos IA para LIO (Aleph)

## Descripcion

Buscaremos la mejor forma de construir asistencia para responder automaticamente, en el momento las preguntas de los usuarios. Si bien mostraremos la respuesta, igual el front enviara la pregunta para ser respondida cuando lo haga el vendedor. Lo que se busca es tener una respeusta asistida por IA de manera inmediata pero no prescindir del sistema anterior.

```
POST /aleph/answer
```

Para esto tendremos algunas considereciones

- El recurso recibe el ID del producto nada mas


- Con el id, obtiene todos los productos del mismo tipo utilizando su id interno


- Se le pasaran como parte del prompt el historial de preguntas y respuestas para ese item, ademas de su nombre y sku para dar contexto al asistente



Estos esquemas son ostentativos, así que todas las sugerencias son bienvenidas y los cambios deben aplicarse a la historia original.

**Algo asi:**

```
SELECT P.texto, R.texto
FROM [LO].[dbo].[productosPreguntas] P
    LEFT JOIN [LO].[dbo].[productosRespuestas] R ON P.id = R.pregunta_id
WHERE P.producto_id in (
    SELECT [id]
FROM [CS].[dbo].[productos]
WHERE id_interno = ?
  )
```

**Ejemplo:**

```
{
  "question": "Hola, ¿viene con pasta térmica?",
  "product": {
    "name": "PROCESADOR AMD (AM4) RYZEN 3 3200G",
    "sku": "P123456"
  },
  "history": [
    {
    "pregunta": "Hola , es compatible Motherboard Asrock A320m-hdv R4.0?Es nuevo ?",
    "respuesta": "Hola es compatible pero si tenes ese mother tenes que actualizarle la bios , si nos compras a nosotros algun motherboard te actualizamos la bios gratis ."
  },
  {
    "pregunta": "Buenas seguis teniendo stock?\nSaludos",
    "respuesta": "Hola! Si, hay stock Gracias por consultar. Saludos de HTGComputacion"
  },
  {
    "pregunta": "Si lo compro ahora puedo retirarlo mañana?",
    "respuesta": "Hola ! Si, pero hace la reserva para que genere el numero de pedido. Podes ir de 9.30 a 16.30 x Av Jujuy 1039  . Gracias x consultar. Saludos HTG COMPUTACION"
  },
  {
    "pregunta": "Como puedo comprar",
    "respuesta": "Hola! Actualmente hay STOCK. Tenes que generar la reserva y con ese numero pagas y retiras, recorda que lo tenes que hacer dentro de las 48 horas. Estamos de LUNES a VIERNES de 9.00 a 16.30 en Av JUJUY 1039.  Gracias por consultar. Saludos de HTGComputacion"
  },
  {
    "pregunta": "Hola, tenes stock?",
    "respuesta": "Hola! Actualmente hay STOCK. Gracias por consultar. Saludos de HTGComputacion"
  },
  {
    "pregunta": "Buenas puedo pagar y retirar del local??",
    "respuesta": "Hola! Actualmente hay STOCK. Tenes que generar la reserva y con ese numero pagas en forma presencial y retiras, recorda que lo tenes que hacer dentro de las 48 horas. Estamos de LUNES a VIERNES de 9.00 a 16.30 en Av JUJUY 1039.  Gracias por consultar. Saludos de HTGComputacion"
  },
  {
    "pregunta": "Hola, buen día. Es compatible con la mother A520M- DS3h v2 ?  y que ram en 3200mhz me recomiendan? Gracias.",
    "respuesta": "Hola si es compatible, con rgb o normales ? Pero todas van a ir ok a 3200mhz , te paso la saqué tenemos https://www.libreopcion.com/memorias-ram?vendedores=gears_store&onlyReseller=gears_store"
  },
  {
    "pregunta": "Hola buenas. Si hago la compra el 01/03/24, podría pasar a buscarlo el mismo día. Muchas gracias",
    "respuesta": "hola si"
  },
}
```

**Ejemplo de respuesta ideal**

```
{
  "reply": "Sí, viene con pasta térmica preaplicada en el cooler de fábrica.",
  "confidence": "high",
  "reliable": true
}
```

**Si no tengo suficiente informacion:**

```
{
  "reply": null,
  "reliable": false
}
```

**Ejemplos de prompteo útiles:**

```
$messages = [
    [
        "role" => "system",
        "content" => "Sos un vendedor técnico de una tienda de hardware, respondé brevemente, con precisión y en tono profesional. Respondé en base al historial anterior de preguntas y respuestas similares, y los datos del producto (nombre y SKU). Si no tenés suficiente información o no podés responder con certeza, respondé con el valor JSON 'false'."
    ],
    [
        "role" => "user",
        "content" => "Historial de preguntas y respuestas:\n\n" . $historial . "\n\nProducto: $nombreProducto\nSKU: $sku\n\nPregunta actual: $pregunta"
    ]
];

```
