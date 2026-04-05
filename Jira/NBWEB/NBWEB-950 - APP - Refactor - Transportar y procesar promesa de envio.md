---
jira_key: "NBWEB-950"
aliases: ["NBWEB-950"]
summary: "APP - Refactor - Transportar y procesar \"promesa de envio\""
status: "Finalizada"
type: "Subtarea"
priority: "High"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-02-10 10:04"
updated: "2025-02-18 03:59"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-950"
---

# NBWEB-950: APP - Refactor - Transportar y procesar "promesa de envio"

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | High |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-02-10 10:04 |
| Actualizado | 2025-02-18 03:59 |
| Etiquetas | ninguna |
| Jira | [NBWEB-950](https://bluinc.atlassian.net/browse/NBWEB-950) |

## Relaciones

- **Padre:** [[NBWEB-777 - Carrito|NBWEB-777]] Carrito
- **has action item:** [[NBWEB-951 - API - Refactor - Transportar y procesar promesa de envio|NBWEB-951]] API - Refactor - Transportar y procesar "promesa de envio"

## Descripcion

Con fines estadísticos es necesario poder guardar la promesa de envío que se le hace al usuario en el sitio.

Para eso es necesario llevarla desde el chekcout hasta el momento de poder procesarlo, tal como hacemos con las dimensiones del paquete 

Usaremos el parámetro que proviene de 

```
GET {API_URL}/v1/carrito/calcularEnvioPara/1754/20116
```

```
{
    "cotizacion": [
        {
            "id": 4041,
            "description": "A domicilio por OCA",
            "plazoEntrega": "entre el mi\u00e9rcoles 12 y el lunes 17",
            "plazoEntregaNumero": 2,
            "total": 6736.56,
            "dropshipping": true
        },
...
    ],
    "datosBulto": {
        "weightKg": 0.2,
        "sizeCm": "7.21x7.21x7.21",
        "amount": 1
    }
}
```

Y finalmente lo enviaremos en el recurso

```
POST {API_URL}/v1/carrito/process
```

**Carga util:**

```
{
  "note": "",
  "medioDePagoId": 3,
  "dropShipping": false,
  "codigoPostalFavorito": "1754",
  "mediodeEnvioId": 4065,
  "idDirCli": 20116,
  "quotes":
      {
        "deliveryTimeRange": "entre el lunes 10 y el viernes 14",
        "deliveryDays": 4,
      },  
  "datosBultos": {
    "weightKg": 0.2,
    "sizeCm": "7.21x7.21x7.21",
    "amount": 1
  }
}
```
