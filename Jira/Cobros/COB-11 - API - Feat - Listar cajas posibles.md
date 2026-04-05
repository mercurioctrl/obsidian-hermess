---
jira_key: "COB-11"
aliases: ["COB-11"]
summary: "API - Feat - Listar cajas posibles"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-07-15 08:51"
updated: "2022-10-27 08:38"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-11"
---

# COB-11: API - Feat - Listar cajas posibles

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-07-15 08:51 |
| Actualizado | 2022-10-27 08:38 |
| Etiquetas | ninguna |
| Jira | [COB-11](https://bluinc.atlassian.net/browse/COB-11) |

## Relaciones

- **Padre:** [[COB-15]] Cajas
- **blocks:** [[COB-40]] APP - Feat - Listar movimientos caja

## Descripcion

Se trata del recurso que lista todas las cajas, no solo aquellas activas y con saldo, sino cualquiera para poder crearse. En la practica, cada empleado puede tener una caja abierta, por esto, es el equivalente a mostrar los empleados. Ademas agregaremos un parámetro para saber si ya tiene una caja abierta (saldo a favor o en contra).

```
GET {{API_URL}}/v1/box/all
```

Retorna

```
 [ {
    "boxName": "CAJA1",
    "showName": "CAJA1",
    "boxId": 12,
    "withBalance":true //esta parametro muestra si la caja ya tiene saldo
  },
  {
    "boxName": "CAJA2",
    "showName": "CAJA1",
    "boxId": 12,
    "withBalance":false
  },
  {
    "boxName": "CAJA3",
    "showName": "CAJA1",
    "boxId": 12,
    "withBalance": true
  }]
```

Se puede hacer basado en

```
SELECT 
PGM_USUARIOS.USU_IDENTIFICACION
FROM [NB_WEB].[dbo].[usuarios_nb]
INNER JOIN NewBytes_DBF.dbo.agentes ON usuarios_nb.agente = agentes.ccodage
LEFT JOIN NB_WEB.dbo.permisos_agente ON usuarios_nb.UserId = permisos_agente.id_usuario_web AND agentes.ccodage = permisos_agente.agente_fp
LEFT JOIN NEW_BYTES.dbo.PGM_USUARIOS ON PGM_USUARIOS.ID_AGENTE = agentes.ccodage
LEFT JOIN NEW_BYTES.dbo.MC_SALDOS_CAJA ON MC_SALDOS_CAJA.USU_IDENTIFICACION = PGM_USUARIOS.USU_IDENTIFICACION
```

El parametro `showname`

En caso de estar presente `capeage` y `cnbrage` se debe mostrar en `showName`. Sino `showName` debe venir vació.

```
SELECT 
PGM_USUARIOS.USU_IDENTIFICACION,capeage,cnbrage
FROM NEW_BYTES.dbo.PGM_USUARIOS
LEFT JOIN NewBytes_DBF.dbo.agentes 
ON PGM_USUARIOS.ID_AGENTE = agentes.ccodage
LEFT JOIN NEW_BYTES.dbo.MC_SALDOS_CAJA ON MC_SALDOS_CAJA.USU_IDENTIFICACION = PGM_USUARIOS.USU_IDENTIFICACION
```
