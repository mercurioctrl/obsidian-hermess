---
jira_key: "LIO-282"
aliases: ["LIO-282"]
summary: "APIv4 - Feat - Migrar repositorio de compras y liberar una parte para visualizarlo sin login"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-03-19 10:07"
updated: "2025-04-01 01:26"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-282"
---

# LIO-282: APIv4 - Feat - Migrar repositorio de compras y liberar una parte para visualizarlo sin login

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-03-19 10:07 |
| Actualizado | 2025-04-01 01:26 |
| Etiquetas | ninguna |
| Jira | [LIO-282](https://bluinc.atlassian.net/browse/LIO-282) |

## Relaciones

- **Padre:** [[LIO-281]] Compras
- **has action item:** [[LIO-293]] APP - Feat - Buscador de ordenes en centro de ayuda
- **has action item:** [[LIO-304]] APP - Oportunidad de mejora - Ver Venta

## Descripcion

**Migración a la Versión 4 de la API**

**Versión Anterior:**

```
GET {API_LEGACY}/pedidos/compras/{id}
```

**Nueva Versión:**

```
GET {API_v4}/purchase/{id}
```

Esta actualización forma parte de nuestra migración hacia una API más optimizada y estructurada, alineada con los estándares modernos de integración y desempeño.

### **Cambios Relevantes**

- **Nuevo Endpoint:** Ahora, todas las consultas deberán realizarse a `https://api.libreopcion.com.ar/purchase/{id}`.


- **Diferenciación por Estado de Autenticación:**

- Si el usuario **está logueado**, recibirá un objeto con la información completa del pedido.


- Si el usuario **no está logueado**, solo obtendrá un conjunto reducido de datos esenciales.





### **Formato de Respuesta**

#### **Para Usuarios Logueados**

Recibirán un objeto con los siguientes atributos:

```
{
    "id": 632921,
    "envio": {
        "activo": true,
        "medioEnvioId": 4069,
        "direccion": {
            "completa": "calle 319 entre 324 y 326 B° Milenio 92,  ,  CP: 3700, PRESIDENCIA ROQUE SAENZ PEÑA  , CHACO",
            "calle": "calle 319 entre 324 y 326 B° Milenio",
            "numero": "92",
            "piso": "",
            "casaApto": "",
            "codigoPostal": "3700",
            "ciudadId": "15454",
            "provinciaId": "0",
            "observacion": "Rejas blancas, plantas afuera, lona blanca"
        },
        "costo": {
            "cliente": 0,
            "libreopcion": 9462
        },
        "tracking": "E000588075",
        "fechaEntrega": "entre el jueves 20 y el viernes 21"
    },
    "retiro": {
        "activo": false,
        "sucursalId": 0,
        "fechaEntrega": ""
    },
    "pago": {
        "medioPagoId": 4005,
        "cuotas": 1,
        "costo": {
            "cuotas": 31540,
            "interes": 0
        },
        "limiteTiempoHoras": 48
    },
    "descuentoLO": 0,
    "subtotal": 31540,
    "productos": [
        {
            "id": 682159,
            "enNB": true,
            "idInterno": 117258,
            "titulo": "DISCO SSD SATA 480GB WD GREEN",
            "img": "30353392d06b64e3384abe336a4bf8f8.png",
            "cantidad": 1,
            "precio": 31540,
            "descuento": 0,
            "descuentoLO": 0,
            "interesPago": 0,
            "instantFlash": false,
            "esTiendaOficial": false,
            "idRegaloUsuario": 0,
            "pedidoDetalleId": 715858,
            "pedidoPaqueteId": 632921,
            "pedidoVendedorId": 685074,
            "distribuidoraId": 1,
            "marca": {
                "id": 3140,
                "nombre": "WD",
                "img": "c6ab87d63363e40dfe3338023b5838c6.jpg",
                "activa": true,
                "uri": "wd",
                "svg": "images/logos/marcas/wd.svg",
                "key": 3140
            },
            "vendedor": {
                "id": 69,
                "usuarioId": 48,
                "email": "gabrielstepke@gmail.com",
                "telefono": "11-24808615",
                "nombre": "STORE GS",
                "esReseller": true,
                "uri": ""
            },
            "cliente": {
                "id": 252756,
                "email": "angeljonatanaguirre@gmail.com",
                "telefono": "3644141237",
                "nombre": "Angel Aguirre"
            },
            "solicitudDevolucion": false,
            "mensajesSinLeer": 0,
            "specialOffer": true
        }
    ]
}

```

#### **Para Usuarios No Logueados**

Solo recibirán los siguientes datos:

```
{
    "id": 689494,
    "paquetes": [
        {
            "id": 632921,
            "tracking": "E000588075",
            "fechaEntrega": "entre el jueves 20 y el viernes 21",
            "productos": [
                {
                    "cantidad": 1,
                    "img": "30353392d06b64e3384abe336a4bf8f8.png",
                    "titulo": "DISCO SSD SATA 480GB WD GREEN"
                }
            ],
            "vendedor": {
                "nombre": "STORE GS"
            }
        }
    ]
}

```





Se modificará el recurso para que pueda ser visto por el vendedor.



Se agregara al objeto, si y solo si, el que usa el recurso es el vendedor el siguiente objeto





```
{
    "id": 0,
    "costo": 7531.094349999999,
    "ganancia": 1655.91,
    "comision": 0,
    "cantidad": 1,
    "precioVenta": 9187,
    "precioVentaConInteres": 9876.025,
    "interesMedioPago": 7.5,
    "vendedorId": 22
}
```
