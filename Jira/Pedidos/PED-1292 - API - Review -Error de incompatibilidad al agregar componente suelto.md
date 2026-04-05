---
jira_key: "PED-1292"
aliases: ["PED-1292"]
summary: "API - Review -Error de incompatibilidad al agregar componente suelto perteneciente a un kit en órdenes con componentes individuales existentes que tambien contienen un componente de kit"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2026-01-29 10:09"
updated: "2026-02-11 13:38"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1292"
---

# PED-1292: API - Review -Error de incompatibilidad al agregar componente suelto perteneciente a un kit en órdenes con componentes individuales existentes que tambien contienen un componente de kit

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-29 10:09 |
| Actualizado | 2026-02-11 13:38 |
| Etiquetas | ninguna |
| Jira | [PED-1292](https://bluinc.atlassian.net/browse/PED-1292) |

## Relaciones

- **Padre:** [[PED-1170 - Kits|PED-1170]] Kits

## Descripcion

Al intentar agregar un componente individual que pertenece a un kit dentro de una orden que ya contiene otro componente del mismo kit (también agregado de forma individual), el sistema devuelve un error de incompatibilidad como si el kit completo ya estuviera presente, cuando en realidad solo hay componentes sueltos.

**Pasos para reproducir:**

- Crear o usar una orden existente.


- Agregar un componente que pertenece a un kit, de forma individual (no el kit).


- Intentar agregar otro componente del mismo kit, también individual.


- El sistema responde con error de incompatibilidad.

```
{
    "errors": {
        "status": 400,
        "title": "No se puede agregar este producto porque forma parte del kit 'Kit Test 1' que ya est\u00e1 en el pedido",
        "file": "\/var\/www\/app\/app\/Services\/Order\/OrderService.php",
        "line": 584
    }
}
```



**Request de ejemplo:**

```
PATCH /v1/orders/addItem
{
  "order": "10447499",
  "branch": "0002",
  "itemId": 121630,
  "amount": 1,
  "stockWarehouseId": 2
}

```

**Resultado actual:**
Error de incompatibilidad por kit existente.

**Resultado esperado:**
Permitir agregar componentes individuales mientras el kit no haya sido agregado explícitamente.
