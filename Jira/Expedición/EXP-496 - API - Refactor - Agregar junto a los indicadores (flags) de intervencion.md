---
jira_key: "EXP-496"
aliases: ["EXP-496"]
summary: "API - Refactor - Agregar junto a los indicadores (flags) de intervencion tecnica, la fecha de intervencion tecnica completa"
status: "Finalizada"
type: "Subtarea"
priority: "Low"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-05-22 08:20"
updated: "2025-08-29 11:05"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-496"
---

# EXP-496: API - Refactor - Agregar junto a los indicadores (flags) de intervencion tecnica, la fecha de intervencion tecnica completa

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Low |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-05-22 08:20 |
| Actualizado | 2025-08-29 11:05 |
| Etiquetas | ninguna |
| Jira | [EXP-496](https://bluinc.atlassian.net/browse/EXP-496) |

## Relaciones

- **Padre:** [[EXP-493]] Listar envios

## Descripcion

Agregaremos un parámetro extra para indiciar cuando la intervención técnica esta completa como hicimos en [link](https://bluinc.atlassian.net/browse/POS-331)  pero al repositorio  [link](https://bluinc.atlassian.net/browse/EXP-494) 



```
GET {API_URL}/v1/shipments
```

```
GET {API_URL}/v1/pickUp
```

```
{
    "response": [
        {
           ...
            "assemblePc": true,
            "updateBios": false,
            "installOS": true,
            "tiSucces": "2025-05-25 12:28:09" <-- SE AGREGA, si no esta es null
        },
        {
            "date": "2025-05-15 10:11:45",
            "pedido": "X000200617315",
            "clientId": 87774,
```

Mantener la performance del recurso en los mismos valores para evitar demoras en un recurso que es muy utilizado
