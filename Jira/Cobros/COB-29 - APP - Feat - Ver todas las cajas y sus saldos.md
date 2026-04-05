---
jira_key: "COB-29"
aliases: ["COB-29"]
summary: "APP - Feat - Ver todas las cajas y sus saldos"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-07-17 20:24"
updated: "2022-10-25 09:04"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-29"
---

# COB-29: APP - Feat - Ver todas las cajas y sus saldos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-07-17 20:24 |
| Actualizado | 2022-10-25 09:04 |
| Etiquetas | ninguna |
| Jira | [COB-29](https://bluinc.atlassian.net/browse/COB-29) |

## Relaciones

- **Padre:** [[COB-15]] Cajas

## Descripcion

Todas las cajas tienen saldos en distintas subcajas, que pertenecen al tipo de saldo. Pueden ser cheques, dolares, pesos, incluso subcuentas de tarjetas, etc

```
GET {{API_URL}}/v1/boxBalance/{idBox}
```

Retorna:

```json
[{
  "boxName": "CAJA1",
  "showName": "Carla Carpintieri",
  "boxId": 12,
  "balance":[
              {
                "FP_DESCRIPCION": "DOLARES",
                "SC_IMPORTE": 1532.4799999999525,
                "SC_FECHAPROCESO": "20220715",
              },
              {
                "FP_DESCRIPCION": "PESOS",
                "SC_IMPORTE": 411981.5900000157,
                "SC_FECHAPROCESO": "20220715",
              },
              {
                "FP_DESCRIPCION": "CUENTA CORRIENTE",
                "SC_IMPORTE": 0.0,
                "SC_FECHAPROCESO": "20220715",
              },
              {
                "FP_DESCRIPCION": "CHEQUE",
                "SC_IMPORTE": 1886625.480000004,
                "SC_FECHAPROCESO": "20220715",
              }
            ]
},
{
  "boxName": "CAJA1",
  "showName": "CAJA1",
  "boxId": 12,
  "balance":[
              {
                "FP_DESCRIPCION": "DOLARES",
                "SC_IMPORTE": 1532.4799999999525,
                "SC_FECHAPROCESO": "20220715",
              },
              {
                "FP_DESCRIPCION": "PESOS",
                "SC_IMPORTE": 411981.5900000157,
                "SC_FECHAPROCESO": "20220715",
              },
              {
                "FP_DESCRIPCION": "CUENTA CORRIENTE",
                "SC_IMPORTE": 0.0,
                "SC_FECHAPROCESO": "20220715",
              },
              {
                "FP_DESCRIPCION": "CHEQUE",
                "SC_IMPORTE": 1886625.480000004,
                "SC_FECHAPROCESO": "20220715",
              }
            ]
},
{
  "boxName": "CAJA1",
  "showName": "CAJA1",
  "boxId": 12,
  "balance":[
              {
                "FP_DESCRIPCION": "DOLARES",
                "SC_IMPORTE": 1532.4799999999525,
                "SC_FECHAPROCESO": "20220715",
              },
              {
                "FP_DESCRIPCION": "PESOS",
                "SC_IMPORTE": 411981.5900000157,
                "SC_FECHAPROCESO": "20220715",
              },
              {
                "FP_DESCRIPCION": "CUENTA CORRIENTE",
                "SC_IMPORTE": 0.0,
                "SC_FECHAPROCESO": "20220715",
              },
              {
                "FP_DESCRIPCION": "CHEQUE",
                "SC_IMPORTE": 1886625.480000004,
                "SC_FECHAPROCESO": "20220715",
              }
            ]
}
]
```
