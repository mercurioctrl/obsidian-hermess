---
jira_key: "PED-901"
aliases: ["PED-901"]
summary: "API - Refactor - Agregar descripcion de accion al oibjetivo total por string agrupado por vendedor"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-12-16 13:52"
updated: "2024-12-27 05:52"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-901"
---

# PED-901: API - Refactor - Agregar descripcion de accion al oibjetivo total por string agrupado por vendedor

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-12-16 13:52 |
| Actualizado | 2024-12-27 05:52 |
| Etiquetas | ninguna |
| Jira | [PED-901](https://bluinc.atlassian.net/browse/PED-901) |

## Relaciones

- **Padre:** [[PED-299 - Objetivos y Desafios|PED-299]] Objetivos y Desafios

## Descripcion

Agregaremos un parámetro extra llamado `rewardDescription` que sirve para explicar en cada linea (por eso se suele repetir por accion) de que se trata y cual es el premio

```

```

```
[
    {
        "sellerId": 8,
        "sellerDescription": "Altamiranda Andrea",
        "amount": 37388.3817,
        "targetAmount": 16000,
        "goalId": 1,
        "keywords": "PATRIOT",
        "startDate": "2024-12-10 00:00:00",
        "endDate": "2024-12-20 23:59:00",
        "rewardDescription": "Superar el monto objetivo paga u$s 100"  <<-- Se agrega
    },
    {
        "sellerId": 41,
    ...
```
