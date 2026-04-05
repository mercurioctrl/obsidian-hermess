---
jira_key: "NBWEB-357"
summary: "API - Feat - Agregar un recurso para consumir el ms-envios para generar un nuevo paquete"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-07-04 09:06"
updated: "2022-08-03 12:52"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-357"
---

# NBWEB-357: API - Feat - Agregar un recurso para consumir el ms-envios para generar un nuevo paquete

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-07-04 09:06 |
| Actualizado | 2022-08-03 12:52 |
| Etiquetas | ninguna |
| Jira | [NBWEB-357](https://bluinc.atlassian.net/browse/NBWEB-357) |

## Descripción

Se trata del recurso necesario para ejecutar la orden del recurso, desde la API del sitio.

Se debe generar un recurso 

```
{{API_URL}}/v1/miCuenta/ordenesDeCompra/0002/10217260/addTrackingOrder
```



Para consumir el recurso (mediante un token de `{{MS-ENVIOS_URL}}/auth/login`)

```
{{MS-ENVIOS_URL}}/addTrackingOrder/nb
```

Se debe construir una request del siguiente tipo (pero solo con los datos del pedido en si, ya que los otros, en realidad se encuentran del otro lado ver este tema ocn  ), del lado le la API, con todos los datos del pedido requeridos por el recurso. 



```
{
    "branch": "0002",
    "order": "10283166",
    "medioEnvioId": 5066,
    "contrato": "400006711",
    "origen": {
        "postal": {
            "codigoPostal": "1229",
            "calle": "Medina",
            "numero": "351",
            "localidad": "Capital Federal",
            "region": "",
            "pais": "Argentina",
            "componentesDeDireccion": [
                {
                    "meta": "entreCalle",
                    "contenido": "Medina y Alberdi"
                }
            ]
        }
    },
    "destino": {
        "postal": {
            "codigoPostal": "1407",
            "calle": "Medina",
            "numero": "351",
            "localidad": "Capital Federal",
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
        "nombreCompleto": "NB distribuidora Mayorista",
        "email": "remitente@andreani.com",
        "documentoTipo": "DNI",
        "documentoNumero": "33457962",
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
    "productoAEntregar": "Varios",
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
