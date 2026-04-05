---
jira_key: "NBWEB-951"
aliases: ["NBWEB-951"]
summary: "API - Refactor - Transportar y procesar \"promesa de envio\""
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-02-10 10:04"
updated: "2025-02-18 04:10"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-951"
---

# NBWEB-951: API - Refactor - Transportar y procesar "promesa de envio"

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-02-10 10:04 |
| Actualizado | 2025-02-18 04:10 |
| Etiquetas | ninguna |
| Jira | [NBWEB-951](https://bluinc.atlassian.net/browse/NBWEB-951) |

## Relaciones

- **Padre:** [[NBWEB-777]] Carrito
- **action item from:** [[NBWEB-950]] APP - Refactor - Transportar y procesar "promesa de envio"

## Descripcion

Para poder guardar con fines estadísticos (todo lo relacionado a la historia [link](https://lioteam.atlassian.net/browse/STASK-8) )

Tomaremos el parámetro al momento que procesamos la orden el sitio de libre opción mediante el recurso

```
POST {API_URL}/pedidos/checkout/confirmar
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

Según el refactor de Front en [link](https://lioteam.atlassian.net/browse/NBWEB-950) 



**Actualización:**

El recurso seria:

```
POST {API_URL}/v1/carrito/process
```

** **
