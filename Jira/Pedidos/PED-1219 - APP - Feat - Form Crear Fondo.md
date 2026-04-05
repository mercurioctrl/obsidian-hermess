---
jira_key: "PED-1219"
aliases: ["PED-1219"]
summary: "APP - Feat - Form Crear Fondo"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2026-01-05 08:08"
updated: "2026-01-20 10:09"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1219"
---

# PED-1219: APP - Feat - Form Crear Fondo

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-05 08:08 |
| Actualizado | 2026-01-20 10:09 |
| Etiquetas | ninguna |
| Jira | [PED-1219](https://bluinc.atlassian.net/browse/PED-1219) |

## Relaciones

- **Padre:** [[PED-1208 - Gestión de Aportes y Gastos de Marketing|PED-1208]] Gestión de Aportes y Gastos de Marketing
- **action item from:** [[PED-1209 - API - Feat - Crear Fondo de Marketing (Aporte de marca)|PED-1209]] API - Feat - Crear Fondo de Marketing (Aporte de marca)

## Descripcion

Formulario para cargar un nuevo aporte de marca (fondo). Debe validar datos básicos antes de enviar y mostrar errores del backend claramente.

**API**

```
POST /v1/marketing/funds
```

**Ejemplo payload**

```
{ 
"brandId": 12, 
"name": "ASUS - Q1 2026 - USD 5000", 
"currencyId": 1, 
"amountOriginal": 5000, 
"expiresAt": "2026-03-31T23:59:59-03:00", 
"notes": "Aporte trimestral"
}
```

**Criterios de aceptación**

- Campos mínimos: marca, nombre, moneda, monto; vencimiento y notas opcionales.


- Valida en UI `amountOriginal > 0` y moneda ARS/USD.


- Al submit exitoso, refresca `GET /v1/marketing/brands` y la pantalla origen (dashboard o fondos de marca).


- Si el backend devuelve error (400/409), se muestra mensaje accionable.


- Deshabilita submit mientras carga y evita doble envío.
