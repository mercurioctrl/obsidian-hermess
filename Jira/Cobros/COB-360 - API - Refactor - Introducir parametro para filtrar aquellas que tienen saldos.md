---
jira_key: "COB-360"
aliases: ["COB-360"]
summary: "API - Refactor - Introducir parametro para filtrar aquellas que tienen saldos distintos de cero"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-03-14 13:30"
updated: "2023-04-11 10:26"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-360"
---

# COB-360: API - Refactor - Introducir parametro para filtrar aquellas que tienen saldos distintos de cero

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-03-14 13:30 |
| Actualizado | 2023-04-11 10:26 |
| Etiquetas | ninguna |
| Jira | [COB-360](https://bluinc.atlassian.net/browse/COB-360) |

## Relaciones

- **Padre:** [[COB-28]] API - Feat - Listar saldos de caja
- **blocks:** [[COB-361]] APP - Feat - Agregar filtro para ver las caja activas (las que tienen saldos distintos de cero)

## Descripcion

Haremos un refactor del recurso [link](https://lioteam.atlassian.net/browse/COB-28) para poder mostrar aquellas que mas nos interesan y son las que tienen movimientos.

Lo agregaremos del siguiente modo

```
GET {{API_URL}}/v1/boxBalance/{boxId}?activeBalance=true
```

Los que debemos chequear son 

- Dolares


- Pesos


- Cuenta corriente


- Cheque
