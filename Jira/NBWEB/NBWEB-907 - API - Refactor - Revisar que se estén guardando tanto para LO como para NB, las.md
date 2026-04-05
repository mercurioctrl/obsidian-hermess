---
jira_key: "NBWEB-907"
aliases: ["NBWEB-907"]
summary: "API - Refactor - Revisar que se estén guardando tanto para LO como para NB, las dimensiones y peso al cotizar"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2024-11-01 14:52"
updated: "2024-11-06 15:58"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-907"
---

# NBWEB-907: API - Refactor - Revisar que se estén guardando tanto para LO como para NB, las dimensiones y peso al cotizar

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2024-11-01 14:52 |
| Actualizado | 2024-11-06 15:58 |
| Etiquetas | ninguna |
| Jira | [NBWEB-907](https://bluinc.atlassian.net/browse/NBWEB-907) |

## Relaciones

- **Padre:** [[NBWEB-423]] Logistica Envios
- **has action item:** [[SNB-2463]] MS -Envios - Refactor - Implementar cambiar el parametro 'items' por 'package_dimensions' par Entregar

## Descripcion

Se ajusto recurso `/v1/order/nb/{branch}-{order}/cp/{cp}`

con el fin de que tenga esta estructura logrando recuperar las dimensiones peso y cantidad de bultos enviadas al cotizador.

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
      "sizeCm": 18.65,
      "amount": 2
   }
}
```



QA: se debe validar que la respuesta cumpla esta estructura.
