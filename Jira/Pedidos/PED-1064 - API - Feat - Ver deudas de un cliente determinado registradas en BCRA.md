---
jira_key: "PED-1064"
aliases: ["PED-1064"]
summary: "API - Feat - Ver deudas de un cliente determinado registradas en BCRA"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-07-24 12:39"
updated: "2025-08-05 19:09"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1064"
---

# PED-1064: API - Feat - Ver deudas de un cliente determinado registradas en BCRA

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-07-24 12:39 |
| Actualizado | 2025-08-05 19:09 |
| Etiquetas | ninguna |
| Jira | [PED-1064](https://bluinc.atlassian.net/browse/PED-1064) |

## Relaciones

- **Padre:** [[PED-54 - Cuenta corriente de clientes|PED-54]] Cuenta corriente de clientes
- **has action item:** [[PED-1065 - APP - Feat - Ver deudas de un cliente determinado registradas en BCRA|PED-1065]] APP - Feat - Ver deudas de un cliente determinado registradas en BCRA

## Descripcion

Investigando un poco encontré una forma de hacer una consulta al BCRA que no me pide token con algo como esto

```
curl -k -X GET "https://api.bcra.gob.ar/centraldedeudores/v1.0/Deudas/30715775014" \
     -H "Accept: application/json"
```

Me gustaría tener un recurso local para facilitar esta tarea al momento de ver la cuenta de un cliente y para esto crearemos un nuevo recurso que hace lo siguiente

```
GET {API_URL}/v1/clients/bcraDebt/30715775014
```

```
{
  "status": 200,
  "results": {
    "identificacion": 30715775014,
    "denominacion": "GRUPO MAXIMUS S.R.L.",
    "periodos": [
      {
        "periodo": "202505",
        "entidades": [
          {
            "entidad": "REBA COMPAÑIA FINANCIERA S.A.",
            "situacion": 1,
            "fechaSit1": "2018-03-30",
            "monto": 58168.0,
            "diasAtrasoPago": 0,
            "refinanciaciones": false,
            "recategorizacionOblig": false,
            "situacionJuridica": false,
            "irrecDisposicionTecnica": false,
            "enRevision": false,
            "procesoJud": false
          },
          {
            "entidad": "BANCO BBVA ARGENTINA S.A.",
            "situacion": 1,
            "fechaSit1": "2018-03-30",
            "monto": 324026.0,
            "diasAtrasoPago": 0,
            "refinanciaciones": false,
            "recategorizacionOblig": false,
            "situacionJuridica": false,
            "irrecDisposicionTecnica": false,
            "enRevision": false,
            "procesoJud": false
          },
          {
            "entidad": "BANCO DE GALICIA Y BUENOS AIRES S.A.",
            "situacion": 1,
            "fechaSit1": "2018-03-30",
            "monto": 254160.0,
            "diasAtrasoPago": 0,
            "refinanciaciones": false,
            "recategorizacionOblig": false,
            "situacionJuridica": false,
            "irrecDisposicionTecnica": false,
            "enRevision": false,
            "procesoJud": false
          }
        ]
      }
    ]
  }
}
```
