---
jira_key: "LIO-302"
aliases: ["LIO-302"]
summary: "APIv4 - Feat - Refactor de recurso de pedidos para unificar listado de ventas y compras"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-03-28 06:08"
updated: "2025-04-15 11:27"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-302"
---

# LIO-302: APIv4 - Feat - Refactor de recurso de pedidos para unificar listado de ventas y compras

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-03-28 06:08 |
| Actualizado | 2025-04-15 11:27 |
| Etiquetas | ninguna |
| Jira | [LIO-302](https://bluinc.atlassian.net/browse/LIO-302) |

## Relaciones

- **Padre:** [[LIO-281]] Compras
- **has action item:** [[LIO-303]] APP - Refactor - Consumir y mostrar pedidos desde el nuevo recurso unificado GET /purchases
- **relates to:** [[LIO-324]] API - Unificado del listado de ventas y compras - Detalles en la búsqueda por texto y filtrado del estado del pedido

## Descripcion

No iniciar la historia hasta que el front valide la compatibilidad de los objetos con la plantilla de la sección

Como usuario autenticado, quiero acceder a un único endpoint, y que según mi rol (vendedor o comprador), me devuelva los pedidos correspondientes, con filtros, paginación, y una estructura unificada y clara.

```
GET {API4_URL}/purchases?rol=vendedor&estado=todas&busqueda=&tipoStock=virtual&page=1&limit=20
```

### 🖼 Contexto actual:

Hoy existen dos endpoints separados en LEGACY:

- `GET /pedidos/ventas`: lista de ventas hechas por el usuario.


- `GET /pedidos/compras`: lista de compras hechas por el usuario.



Esto duplica lógica y complica la integración del frontend. Queremos reemplazarlos con un único recurso consolidado.

### 🎯 Alcance:

- Crear el endpoint `GET /purchases`.


- Este recurso devuelve:

- Pedidos donde el usuario fue **vendedor**, si `rol=vendedor`.


- Pedidos donde fue **comprador**, si `rol=comprador`.




- La estructura de salida debe unificar y mantener el formato actual.


- Se debe incluir un nuevo campo `"tipo"` con valores `"venta"` o `"compra"`.


- Soportar filtros por:

- Estado (`estado`)


- Texto de búsqueda (`busqueda`)


- Tipo de stock (`tipoStock`)


- Estado de orden (`orderStatus`)




- Soportar paginación y orden por fecha descendente (por defecto).



📥 Parámetros del endpoint

```
GET /purchases?rol=vendedor&estado=todas&busqueda=&tipoStock=virtual&excluir=659506,658342&page=1&limit=20
```

| Parámetro | Tipo | Descripción |
| --- | --- | --- |
| `rol` | string | **Obligatorio.** `"vendedor"` o `"comprador"` |
| `estado` | string | Opcional. `"todas"` (default), `"pendientes"`, `"concretadas"`, `"canceladas"` |
| `busqueda` | string | Opcional. Texto libre a buscar (producto, marca, cliente, vendedor) |
| `tipoStock` | string | Opcional. `"virtual"`, `"fisico"`, `"todos"` (default) |
| `page` | int | Opcional. Página de resultados (default: 1) |
| `limit` | int | Cantidad de resultados por página (default: 20) |
| `orderStatus` | string | Una de `   "Recibimos tu pedido",   "Listo para retirar",   "Listo para enviar",   "Enviado",   "Entregado",   "Pedido Cancelado",   "Enviado, con cambios",   "Entregado, con cambios",   "Cancelado",   "Sin Estado" ` |

### 📤 Ejemplo de respuesta

```json
[
  {
    "id": 659526,
    "fecha": "2025-03-27 16:24:06.760",
    "tracking": "",
    "orderNb": "10356415",
    "tipo": "venta",
    "detalle": {
      "id": 723244,
      "titulo": "MOUSE GENIUS RS2 ERGO 9000S CHAMPAGNE TITANIUM",
      "cantidad": 1,
      "precio": 16867,
      "marca": {
        "nombre": "GENIUS"
      },
      "cliente": {
        "nombre": "Gprueba LO"
      },
      "vendedor": {
        "nombre": "BsAsPC"
      },
      "tipoStock": "virtual",
      "pedidoDetalleId": 676887,
      "pedidoPaqueteId": 602953,
      "pedidoVendedorId": 653013
    }
  },
  {
    "id": 659506,
    "fecha": "2025-03-21 17:21:38.420",
    "tracking": "AAAAAAA111111",
    "orderNb": "10356382",
    "tipo": "compra",
    "detalle": {
      "id": 723219,
      "titulo": "GENIUS CABLE USB-A/USB-C 150CM",
      "cantidad": 1,
      "precio": 4298,
      "marca": {
        "nombre": "GENIUS"
      },
      "cliente": {
        "nombre": "Catriel Mercurio"
      },
      "vendedor": {
        "nombre": "BitBayres"
      },
      "tipoStock": "virtual",
      "pedidoDetalleId": 676863,
      "pedidoPaqueteId": 602933,
      "pedidoVendedorId": 652992
    }
  }
]

```

### Criterios de aceptación

- El endpoint `GET /purchases` devuelve pedidos filtrados por `rol`.


- `rol` es obligatorio. Si no se envía o es inválido, retorna 400 con error claro.


- Si `rol=vendedor`, se devuelven pedidos donde el usuario es el vendedor.


- Si `rol=comprador`, se devuelven pedidos donde es el cliente.


- Cada pedido incluye el campo `"tipo"` con `"venta"` o `"compra"`.


- La estructura de datos es compatible con los endpoints actuales.


- Se filtra correctamente por:

- Estado (`estado`)


- Texto de búsqueda (`busqueda`)


- Tipo de stock (`tipoStock`)




- El sistema respeta `page` y `limit`, y ordena por `fecha DESC` por default.


- Si el usuario figura como cliente y vendedor en el mismo pedido, se devuelve en ambos aunque esto es una anomalía del entorno de desarrollo



### 💡 Consideraciones técnicas

- El `usuarioId` se obtiene del token autenticado.


- Para `busqueda`, aplicar búsqueda insensible a mayúsculas/minúsculas (`ILIKE`, `LOWER`) sobre:

- `detalle.titulo`


- `marca.nombre`


- `cliente.nombre`


- `vendedor.nombre`
