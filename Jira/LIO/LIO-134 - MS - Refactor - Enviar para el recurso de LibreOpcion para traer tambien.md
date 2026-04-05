---
jira_key: "LIO-134"
aliases: ["LIO-134"]
summary: "MS - Refactor - Enviar para el recurso de LibreOpcion para traer tambien pesos,medida y bultos en Entregar como hicimos para NB"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-11-20 16:05"
updated: "2024-11-27 10:48"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-134"
---

# LIO-134: MS - Refactor - Enviar para el recurso de LibreOpcion para traer tambien pesos,medida y bultos en Entregar como hicimos para NB

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-11-20 16:05 |
| Actualizado | 2024-11-27 10:48 |
| Etiquetas | ninguna |
| Jira | [LIO-134](https://bluinc.atlassian.net/browse/LIO-134) |

## Relaciones

- **Padre:** [[LIO-133]] Ms Envios Libre Opcion

## Descripcion

Debemos refactorizar en la linea de lo que hicimos con NB, para que el Front disponga de los datos de los bultos de modo tal de enviarlo al procesar.

```
GET {{API_URL}}/pedido/{pedidoLo}/cp/{cpDestino}/cphost/{cpOrigen}
```





```
{
   "quote": [
      {
         "id": 4041,
         "costo": 6298.02,
         "descripcion": "A domicilio por OCA",
         "precio": 0,
         "plazoEntrega": "entre el martes 26 y el viernes 29",
         "plazoEntregaNumero": 5,
         "total": 6298.02
      },
      {
         "id": 4065,
         "costo": 7112.3,
         "descripcion": "A domicilio por Andreani",
         "precio": 7112.3,
         "plazoEntrega": "entre el lunes 25 y el jueves 28",
         "plazoEntregaNumero": 4,
         "total": 7112.3
      },
      {
         "id": 3030,
         "costo": 7000,
         "descripcion": "Moto (Capital Federal)",
         "precio": 7000,
         "plazoEntrega": "mañana",
         "plazoEntregaNumero": 1,
         "total": 7000
      },
      {
         "id": 4069,
         "costo": 2524,
         "descripcion": "A domicilio por Entregar",
         "precio": 3054,
         "plazoEntrega": "entre el lunes 25 y el martes 26",
         "plazoEntregaNumero": 4,
         "total": 3054
      }
   ],
   "package": {
      "weightKg": 0.5,
      "sizeCm": "6.26x6.26x6.26",
      "amount": 1
   }
}
```
