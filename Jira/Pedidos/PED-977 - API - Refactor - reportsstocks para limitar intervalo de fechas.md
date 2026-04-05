---
jira_key: "PED-977"
aliases: ["PED-977"]
summary: "API - Refactor - reports/stocks para limitar intervalo de fechas"
status: "Tareas por hacer"
type: "Subtarea"
priority: "Medium"
assignee: "Sin asignar"
reporter: "Catriel Mercurio"
created: "2025-03-26 08:45"
updated: "2025-03-26 08:45"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-977"
---

# PED-977: API - Refactor - reports/stocks para limitar intervalo de fechas

| Campo | Valor |
|-------|-------|
| Estado | Tareas por hacer (Por hacer) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Sin asignar |
| Reportado por | Catriel Mercurio |
| Creado | 2025-03-26 08:45 |
| Actualizado | 2025-03-26 08:45 |
| Etiquetas | ninguna |
| Jira | [PED-977](https://bluinc.atlassian.net/browse/PED-977) |

## Relaciones

- **Padre:** [[PED-213 - Reportes de ventas|PED-213]] Reportes de ventas

## Descripcion

Refactor de recurso

```
 GET {API_URL}/v1/reports/salesBrands
```

para limitar intervalo de fechas**:**
Se realizará un refactor del recurso  con el objetivo de agregar una validación de intervalo máximo de fechas permitido.

### Cambios a implementar:

- Se permitirá consultar estadísticas de **cualquier rango de fechas**, pero el intervalo **no podrá exceder los X meses**.


- El valor de **X será configurable** a través de una variable de entorno (`.env`), con valor por defecto 3 meses si no esta disponible.


- Esta restricción **no aplicará a usuarios que cuenten con el permiso **`unlimitedReports`.



Si no posee el permiso, o excede los 3 meses se debe emitir un mensaje estándar tipo

```
{

    "success": "false",
    "message": "No tenes permisos para reportar mas de x meses"

}
```
