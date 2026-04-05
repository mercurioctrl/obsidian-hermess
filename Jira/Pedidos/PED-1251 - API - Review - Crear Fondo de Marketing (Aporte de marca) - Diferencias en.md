---
jira_key: "PED-1251"
aliases: ["PED-1251"]
summary: "API - Review - Crear Fondo de Marketing (Aporte de marca) - Diferencias en CreatedAt, CreateByUserId y respuesta del error"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Franco Callipo"
reporter: "Guillermo Avila"
created: "2026-01-12 17:06"
updated: "2026-01-16 09:57"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1251"
---

# PED-1251: API - Review - Crear Fondo de Marketing (Aporte de marca) - Diferencias en CreatedAt, CreateByUserId y respuesta del error

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Franco Callipo |
| Reportado por | Guillermo Avila |
| Creado | 2026-01-12 17:06 |
| Actualizado | 2026-01-16 09:57 |
| Etiquetas | ninguna |
| Jira | [PED-1251](https://bluinc.atlassian.net/browse/PED-1251) |

## Relaciones

- **Padre:** [[PED-1208]] Gestión de Aportes y Gastos de Marketing
- **clones:** [[PED-1209]] API - Feat - Crear Fondo de Marketing (Aporte de marca)

## Descripcion

Realizaremos la revisión de los siguientes elementos sobre el recurso.

```
POST /v1/marketing/funds
```

### 

- Al comparar la fecha almacenada en `CreatedAt` con la actual, parece haber una diferencia de 3 horas. 


- `CreateByUserId` se guarda en NULL.



[adjunto]


- Al enviar un `brandId` o `currencyId` inexistente, aparece un error no controlado. Al no encontrar alguno de estos valores el objeto de respuesta debe ser el ya definido con el código http 400 Bad Request.



[adjunto]
```
{
  "success": false,
  "message": "Mensaje de error" 
}
```
