---
jira_key: "EXP-487"
aliases: ["EXP-487"]
summary: "API - MVP - Refactor - Agregar trackingNumber y arrivalDate en Ingresos"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-04-29 14:34"
updated: "2025-05-14 19:27"
labels: ["MVPLaset"]
jira_url: "https://bluinc.atlassian.net/browse/EXP-487"
---

# EXP-487: API - MVP - Refactor - Agregar trackingNumber y arrivalDate en Ingresos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-04-29 14:34 |
| Actualizado | 2025-05-14 19:27 |
| Etiquetas | MVPLaset |
| Jira | [EXP-487](https://bluinc.atlassian.net/browse/EXP-487) |

## Relaciones

- **Padre:** [[EXP-486]] Ver ingreso
- **has action item:** [[EXP-488]] APP - MVP - Refactor - Agregar trackingNumber y arrivalDate en Ingresos

## Descripcion

Según nuevos requerimientos, es necesario incorporar dos campos opcionales en las órdenes de compra:

- `trackingNumber` (número de seguimiento)


- `arrivalDate` (fecha estimada de arribo)



Estos datos deben poder visualizarse y actualizarse mediante los recursos actuales de la API.

```
GET {API_URL}/v1/providersOrders/
```

```
{
    "response": [
        {
            "id": 0,
            "providerOrder": "00011640",
            "providerId": "001150",
            "providerName": "LASET S.A.",
            "distpatchName": "",
            "userId": "14",
            "updated": null,
            "dispatchDate": "25\/04\/2025",
            "numPed": "11640",
            "fullSerialized": 0
            "trackingNumber": "AA9330SDFDKFF" <-- SE AGREGA
            "arrivalDate": {dateTime} <-- SE AGREGA
        },
        {
...        
```

### Criterios de Aceptación

- El recurso `GET {API_URL}/v1/providerOrder/{providerOrderId}` debe incluir los campos `trackingNumber` y `arrivalDate` si existen y caso contrario deben venir en `NULL`


- `arrivalDate` debe manejarse como un `datetime` válido y ser consistente con los formatos actuales del sistema.
