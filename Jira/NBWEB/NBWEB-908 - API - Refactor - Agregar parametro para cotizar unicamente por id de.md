---
jira_key: "NBWEB-908"
aliases: ["NBWEB-908"]
summary: "API - Refactor - Agregar parametro para cotizar unicamente por id de transportista"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2024-11-01 14:54"
updated: "2024-11-06 16:16"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-908"
---

# NBWEB-908: API - Refactor - Agregar parametro para cotizar unicamente por id de transportista

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2024-11-01 14:54 |
| Actualizado | 2024-11-06 16:16 |
| Etiquetas | ninguna |
| Jira | [NBWEB-908](https://bluinc.atlassian.net/browse/NBWEB-908) |

## Relaciones

- **Padre:** [[NBWEB-423]] Logistica Envios
- **has action item:** [[SNB-2463]] MS -Envios - Refactor - Implementar cambiar el parametro 'items' por 'package_dimensions' par Entregar

## Descripcion

Se debe ajustar en 'Envios' el recurso:

GET /order/nb/0002-10356120/cp/7600**?shipmentId=4069&amountPackages=3**

En el que se le pueda pasar. **shipmentId **y** amountPackages.**

Teniendo como resultado unicamente el transportista enviado.

ej 4069 → Entregar.

Response:

```
{
   "quote": [
      {
         "id": 4069,
         "costo": 45838,
         "descripcion": "A domicilio por Entregar",
         "precio": 0,
         "plazoEntrega": "entre el martes 12 y el lunes 18",
         "plazoEntregaNumero": 6,
         "total": 55464
      }
   ],
   "package": {
      "weightKg": 3.78,
      "sizeCm": "12.44x12.44x12.44",
      "amount": 3
   }
}
```
