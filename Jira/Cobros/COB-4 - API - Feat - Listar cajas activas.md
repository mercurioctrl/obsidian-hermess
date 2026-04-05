---
jira_key: "COB-4"
aliases: ["COB-4"]
summary: "API - Feat - Listar cajas activas"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-07-13 14:17"
updated: "2022-10-25 09:04"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-4"
---

# COB-4: API - Feat - Listar cajas activas

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-07-13 14:17 |
| Actualizado | 2022-10-25 09:04 |
| Etiquetas | ninguna |
| Jira | [COB-4](https://bluinc.atlassian.net/browse/COB-4) |

## Relaciones

- **Padre:** [[COB-15]] Cajas

## Descripcion

Este recurso se utiliza para listar las cajas activas, aquellas que tienen al menos un movimiento.

```
GET {API_URL}/v1/box
```

Retorna:

```json
 [ {
    "boxName": "CAJA1"
  },
  {
    "boxName": "CAJA2"
  },
  {
    "boxName": "CAJA3"
  }]
```

Usando 

```sql
SELECT  MC_SALDOS_CAJA.USU_IDENTIFICACION FROM [NEW_BYTES].[dbo].[MC_SALDOS_CAJA] 
INNER JOIN NEW_BYTES.dbo.PGM_USUARIOS ON MC_SALDOS_CAJA.USU_IDENTIFICACION = PGM_USUARIOS.USU_IDENTIFICACION
GROUP BY MC_SALDOS_CAJA.USU_IDENTIFICACION
```
