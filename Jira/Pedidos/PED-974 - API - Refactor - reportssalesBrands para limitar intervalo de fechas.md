---
jira_key: "PED-974"
aliases: ["PED-974"]
summary: "API - Refactor - reports/salesBrands para limitar intervalo de fechas"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-03-26 08:34"
updated: "2025-03-28 12:24"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-974"
---

# PED-974: API - Refactor - reports/salesBrands para limitar intervalo de fechas

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-03-26 08:34 |
| Actualizado | 2025-03-28 12:24 |
| Etiquetas | ninguna |
| Jira | [PED-974](https://bluinc.atlassian.net/browse/PED-974) |

## Relaciones

- **Padre:** [[PED-213]] Reportes de ventas

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
