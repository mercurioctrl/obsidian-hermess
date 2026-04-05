---
jira_key: "PED-50"
aliases: ["PED-50"]
summary: "MS - Feat - Integracion de padron de afip mediante documento del cliente"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-08-29 08:58"
updated: "2023-08-29 09:05"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-50"
---

# PED-50: MS - Feat - Integracion de padron de afip mediante documento del cliente

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-08-29 08:58 |
| Actualizado | 2023-08-29 09:05 |
| Etiquetas | ninguna |
| Jira | [PED-50](https://bluinc.atlassian.net/browse/PED-50) |

## Relaciones

- **Padre:** [[PED-16]] Listar clientes
- **blocks:** [[PED-45]] API - Feat - Integración con Padrones de AFIP por documento de cliente

## Descripcion

Se agregara la consulta al padrón en el sistema de comprobantes

```
GET {{API_URL}}/v2/padron/{cuit/cuil/dni}
```

```
{
    "datosGenerales": {
        "domicilioFiscal": {
            "codPostal": "1753",
            "descripcionProvincia": "BUENOS AIRES",
            "direccion": "MIGUEL CANE 4189",
            "idProvincia": 1,
            "localidad": "VILLA LUZURIAGA",
            "tipoDomicilio": "FISCAL"
        },
        "estadoClave": "ACTIVO",
        "fechaContratoSocial": "2001-12-28T12:00:00-03:00",
        "idPersona": 30708043830,
        "mesCierre": 12,
        "razonSocial": "ABAL TRANS S.R.L.",
        "tipoClave": "CUIT",
        "tipoPersona": "JURIDICA"
    },
    "datosRegimenGeneral": {
        "actividad": {
            "descripcionActividad": "SERVICIO DE TRANSPORTE AUTOMOTOR DE MERCADERÍAS A GRANEL N.C.P.",
            "idActividad": 492229,
            "nomenclador": 883,
            "orden": 1,
            "periodo": 201311
        },
        "impuesto": [
            {
                "descripcionImpuesto": "IIBB CONVENIO MULTILATERAL",
                "idImpuesto": 5900,
                "periodo": 200208
            },
            {
                "descripcionImpuesto": "IVA",
                "idImpuesto": 30,
                "periodo": 200208
            },
            {
                "descripcionImpuesto": "GANANCIAS SOCIEDADES",
                "idImpuesto": 10,
                "periodo": 200208
            },
            {
                "descripcionImpuesto": "BP-ACCIONES O PARTICIPACIONES",
                "idImpuesto": 211,
                "periodo": 200305
            },
            {
                "descripcionImpuesto": "REGIMENES DE INFORMACIÓN",
                "idImpuesto": 103,
                "periodo": 200701
            },
            {
                "descripcionImpuesto": "EMPLEADOR-APORTES SEG. SOCIAL",
                "idImpuesto": 301,
                "periodo": 200209
            }
        ],
        "regimen": [
            {
                "descripcionRegimen": "PARTICIPACIONES SOCIETARIAS",
                "idImpuesto": 103,
                "idRegimen": 68,
                "periodo": 20070101
            },
            {
                "descripcionRegimen": "PRESENTACION DE ESTADOS CONTABLES EN FORMATO PDF",
                "idImpuesto": 103,
                "idRegimen": 255,
                "periodo": 20091201
            }
        ]
    },
    "metadata": {
        "fechaHora": "2023-08-29T09:00:20.342-03:00",
        "servidor": "linux11"
    }
}
```
