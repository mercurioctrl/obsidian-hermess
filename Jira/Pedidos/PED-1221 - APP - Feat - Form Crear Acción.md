---
jira_key: "PED-1221"
aliases: ["PED-1221"]
summary: "APP - Feat - Form Crear Acción"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2026-01-05 08:09"
updated: "2026-01-20 09:58"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1221"
---

# PED-1221: APP - Feat - Form Crear Acción

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-05 08:09 |
| Actualizado | 2026-01-20 09:58 |
| Etiquetas | ninguna |
| Jira | [PED-1221](https://bluinc.atlassian.net/browse/PED-1221) |

## Relaciones

- **Padre:** [[PED-1208 - Gestión de Aportes y Gastos de Marketing|PED-1208]] Gestión de Aportes y Gastos de Marketing
- **action item from:** [[PED-1211 - API - Feat - Crear Acción de Marketing|PED-1211]] API - Feat - Crear Acción de Marketing

## Descripcion

Formulario para crear una acción (campaña). Permite fechas opcionales y valida coherencia.

**API**

```
POST /v1/marketing/actions
```

**Ejemplo payload**

```
{ 
"name": "Hot Sale 2026", 
"description": "Campaña multiproducto", 
"startAt": "2026-05-11T00:00:00-03:00", 
"endAt": "2026-05-13T23:59:59-03:00" 
}

```

**Criterios de aceptación**

- `name` requerido; `description` opcional; fechas opcionales.


- Si hay fechas, valida `startAt <= endAt` antes de enviar.


- Al éxito, vuelve al listado y refresca `GET /v1/marketing/actions`.


- Maneja errores de backend con feedback visible.


- Previene doble submit y muestra loading.



---

##
