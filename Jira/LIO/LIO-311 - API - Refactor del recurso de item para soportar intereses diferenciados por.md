---
jira_key: "LIO-311"
aliases: ["LIO-311"]
summary: "API - Refactor del recurso de item para soportar intereses diferenciados por cuota"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-04-03 09:01"
updated: "2025-04-09 03:54"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-311"
---

# LIO-311: API - Refactor del recurso de item para soportar intereses diferenciados por cuota

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-04-03 09:01 |
| Actualizado | 2025-04-09 03:54 |
| Etiquetas | ninguna |
| Jira | [LIO-311](https://bluinc.atlassian.net/browse/LIO-311) |

## Relaciones

- **Padre:** [[LIO-119]] Inventario
- **has action item:** [[LIO-312]] APP - Refactor - Mostrar cuotas diferenciadas por medio de pago en la ficha del producto

## Descripcion

Actualizar la estructura del recurso para que los medios de pago devuelvan los intereses diferenciados por cantidad de cuotas como propiedades adicionales planas dentro de cada objeto de medio de pago.

Actualmente se devuelve un único campo `interes` por medio de pago. Sin embargo, en la base de datos `[LO].[dbo].[mediosPago]` ahora existen campos adicionales que definen intereses específicos por cantidad de cuotas (`interes1`, `interes3`, `interes6`, etc.). Es necesario reflejar esa información en la respuesta de la API.

```
GET /v4/item/{id}
```

**Ejemplo:** [https://omega-api4.libreopcion.com.ar/v4/item/711727](https://omega-api4.libreopcion.com.ar/v4/item/711727)

### 💡 Cambios requeridos

#### 1. **Modificar la respuesta del atributo **`mediosPago`

Agregar los siguientes campos directamente dentro de cada objeto de medio de pago:

- `interes1`


- `interes3`


- `interes6`


- `interes9`


- `interes12`



Cada uno debe mapearse directamente desde la base de datos, respetando estos criterios:

- Si el valor es `NULL` en la base, devolver `null`.


- Si el valor es `0`, devolver `0`.



```
...
"stock": true,
"revision": false,
"rechazado": false,
"usado": false,
"preventa": false,
"instantFlash": false
},
"precios": {
"precioLO": 54880,
"precioSinDescuento": 54880,
"cotizacion": 1056,
"descuentoLO": 0,
"descuentoDolares": 0,
"precioLista": 58996
},
"envios": {
"activo": true,
"rapido": false,
"gratis": true,
"codigoPostalOrigen": "1229",
"cotizar": true
},
"retiro": {
"activo": 1,
"retiroDireccion": "Libre Opción Express, CABA",
"retiroHorarioAtencion": "Lunes a Viernes de 9:00 a 17:00 hs"
},
"marca": {
"id": 3169,
"nombre": "AMD",
"img": "266f407b98b3c0721710b6c651d4108f.jpg"
},
"categoria": {
"id": 44,
"nombre": "Procesadores",
"uri": "procesador"
},
"vendedor": {
"id": 28,
"nombre": "BitBayres",
"esReseller": true,
"reputacion": {
"tiempoRespuestaChatPromedioHoras": "Rápida",
"tiempoRespuestaPreguntasPromedioHoras": "Muy Rápida",
"puntajeChat": 5,
"puntajePreguntas": 5,
"puntajeCalificacion": 5,
"puntajeSeguimiento": 0,
"puntajeGlobal": 5,
"ventas": 405,
"productosDisponibles": 11874,
"ventasConcretadas": 405
}
},
"mediosPago": [
{
"id": 4004,
"activo": true,
"nombre": "Efectivo",
"descripcion": "Efectivo",
"interes": 0,
"cuotas": 1,
"soloSucursal": true,
"total": 0
},
{
  "id": 5071,
  "activo": true,
  "nombre": "Ahora 6 cuotas",
  "descripcion": "6 cuotas fijas",
  "interes": 12.83,
  "cuotas": 6,
  "soloSucursal": false,
  "total": 0,
  "interes1": 0,   <-----

  "interes3": 6.83,   <-----

  "interes6": 12.83,   <-----

  "interes9": null,   <-----

  "interes12": null   <-----
}
....
```
