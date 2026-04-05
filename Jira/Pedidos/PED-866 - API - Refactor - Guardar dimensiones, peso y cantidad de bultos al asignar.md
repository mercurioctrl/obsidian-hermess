---
jira_key: "PED-866"
aliases: ["PED-866"]
summary: "API - Refactor - Guardar dimensiones, peso y cantidad de bultos al asignar transportista"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2024-11-04 14:50"
updated: "2024-11-21 21:14"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-866"
---

# PED-866: API - Refactor - Guardar dimensiones, peso y cantidad de bultos al asignar transportista

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2024-11-04 14:50 |
| Actualizado | 2024-11-21 21:14 |
| Etiquetas | ninguna |
| Jira | [PED-866](https://bluinc.atlassian.net/browse/PED-866) |

## Relaciones

- **has action item:** [[SNB-2463 - MS -Envios - Refactor - Implementar cambiar el parametro 'items' por|SNB-2463]] MS -Envios - Refactor - Implementar cambiar el parametro 'items' por 'package_dimensions' par Entregar
- **is caused by:** [[PED-867 - APP - Refactor- Guardar dimensiones, peso y cantidad de bultos al asignar|PED-867]] APP - Refactor- Guardar dimensiones, peso y cantidad de bultos al asignar trasnportista

## Descripcion

Refactorizacion en Recurso  

PEDIDOS:

Nueva estructura al solicitar cotizacion de envios.

con el fin de guardar dimension peso y cantidad de bultos cotizados al asignar transportista.

se debe guardar en los campos **packageWeight, packageSize,amountPackages** de **pedclit**.

```
   "package": {
      "weightKg": 5.73,
      "sizeCm": "18.65x18.65x18.65",
      "amount": 2
   }
```





respuesta completa del cotizador de ms-envios a Pedidos.

```
{
   "quote": [
      {
         "id": 4069,
         "costo": 3813,
         "descripcion": "A domicilio por Entregar",
         "precio": 0,
         "plazoEntrega": "entre el miércoles 06 y el martes 12",
         "plazoEntregaNumero": 2,
         "total": 4613
      },
      {
         "id": 3030,
         "costo": 4700,
         "descripcion": "Moto (Capital Federal)",
         "precio": 4700,
         "plazoEntrega": "mañana",
         "plazoEntregaNumero": 1,
         "total": 4700
      },
      {
         "id": 4041,
         "costo": 7784.46,
         "descripcion": "A domicilio por OCA",
         "precio": 7784.46,
         "plazoEntrega": "entre el jueves 07 y el martes 12",
         "plazoEntregaNumero": 3,
         "total": 7784.46
      },
      {
         "id": 3031,
         "costo": 16000,
         "descripcion": "Camioneta",
         "precio": 16000,
         "plazoEntrega": "mañana",
         "plazoEntregaNumero": 1,
         "total": 16000
      },
      {
         "id": 4065,
         "costo": 16335.31,
         "descripcion": "A domicilio por Andreani",
         "precio": 16335.31,
         "plazoEntrega": "entre el miércoles 06 y el lunes 11",
         "plazoEntregaNumero": 2,
         "total": 16335.31
      }
   ],
   "package": {
      "weightKg": 5.73,
      "sizeCm": "18.65x18.65x18.65",
      "amount": 2
   }
}
```
