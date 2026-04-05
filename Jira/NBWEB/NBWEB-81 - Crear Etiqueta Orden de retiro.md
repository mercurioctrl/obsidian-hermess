---
jira_key: "NBWEB-81"
aliases: ["NBWEB-81"]
summary: "Crear Etiqueta / Orden de retiro"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-04-04 07:53"
updated: "2022-07-01 17:14"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-81"
---

# NBWEB-81: Crear Etiqueta / Orden de retiro

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-04-04 07:53 |
| Actualizado | 2022-07-01 17:14 |
| Etiquetas | ninguna |
| Jira | [NBWEB-81](https://bluinc.atlassian.net/browse/NBWEB-81) |

## Relaciones

- **Padre:** [[NBWEB-76]] API - Implementar MS envios

## Descripcion

Una vez que es posible cotizar un envío, es necesario crear la etiqueta u orden de retiro del mismo para que la empresa de correo pueda retirarlo, o bien el canal logístico pueda despacharlo a su destino.

Para esto se debe cotizar nuevamente la orden y generar su numero de tracking 

[Ver para oca ejemplos](https://github.com/guillebalmacedaonline/OCA-PHP-API-LARAVEL/blob/master/oca.php) , [Ver para oca ejemplos 2](https://docs.shippinggroup.net/wp-content/uploads/2019/03/OCA-e-Pak-WebServices.pdf)

[Ver para Andreani ejemplos](https://developers.andreani.com/documentacion/2#crearOrden), [Ver para Andreani ejemplos 2](https://github.com/alejoasotelo/andreani-sdk-rest)

```
POST {{API_URL}}/addTrackingOrder/nb/{branch}-{order}
```

 

Se recomienda empezar por el recurso para Andreani, que es mas completo.

En el cuerpo podrían ir los siguientes parámetros, aunque no todos son obligatorios:

(algunos parametros se encuentran en español, porque provienen del sistema original ¿lo cambiamos?)



```json
{
  "branch": "0002",
  "order" : "10265756"
  "medioEnvioId" : 2,
  "contrato": "400006711",
  "origen": {
    "postal": {
      "codigoPostal": "3378",
      "calle": "Av Falsa",
      "numero": "380",
      "localidad": "Puerto Esperanza",
      "region": "",
      "pais": "Argentina",
      "componentesDeDireccion": [
        {
          "meta": "entreCalle",
          "contenido": "Medina y Jualberto"
        }
      ]
    }
  },
  "destino": {
    "postal": {
      "codigoPostal": "1292",
      "calle": "Macacha Guemes",
      "numero": "28",
      "localidad": "C.A.B.A.",
      "region": "AR-B",
      "pais": "Argentina",
      "componentesDeDireccion": [
        {
          "meta": "piso",
          "contenido": "2"
        },
        {
          "meta": "departamento",
          "contenido": "B"
        }
      ]
    }
  },
  "remitente": {
    "nombreCompleto": "Alberto Lopez",
    "email": "remitente@andreani.com",
    "documentoTipo": "DNI",
    "documentoNumero": "33111222",
    "telefonos": [
      {
        "tipo": 1,
        "numero": "113332244"
      }
    ]
  },
  "destinatario": [
    {
      "nombreCompleto": "Juana Gonzalez",
      "email": "destinatario@andreani.com",
      "documentoTipo": "DNI",
      "documentoNumero": "33999888",
      "telefonos": [
        {
          "tipo": 1,
          "numero": "1112345678"
        }
      ]
    }
  ],
  "productoAEntregar": "Aire Acondicionado",
  "bultos": [
    {
      "kilos": 2,
      "largoCm": 10,
      "altoCm": 50,
      "anchoCm": 10,
      "volumenCm": 5000,
      "valorDeclaradoSinImpuestos": 1200,
      "valorDeclaradoConImpuestos": 1452,
      "referencias": [
        {
          "meta": "detalle",
          "contenido": "Secador de pelo"
        },
        {
          "meta": "idCliente",
          "contenido": "10000"
        }
      ]
    }
  ]
}
```



Debería retornar un objeto que tenga como mínimo los siguientes parámetros

```json
{
"status": "Ok",
"tracnkingNumber" : "278934897234897324"
}
```
