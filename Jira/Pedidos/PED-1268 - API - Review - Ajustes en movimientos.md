---
jira_key: "PED-1268"
aliases: ["PED-1268"]
summary: "API - Review - Ajustes en movimientos"
status: "Finalizada"
type: "Tarea"
priority: "High"
assignee: "Franco Callipo"
reporter: "Marbe Moreno"
created: "2026-01-15 10:17"
updated: "2026-01-16 09:54"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1268"
---

# PED-1268: API - Review - Ajustes en movimientos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | High |
| Asignado | Franco Callipo |
| Reportado por | Marbe Moreno |
| Creado | 2026-01-15 10:17 |
| Actualizado | 2026-01-16 09:54 |
| Etiquetas | ninguna |
| Jira | [PED-1268](https://bluinc.atlassian.net/browse/PED-1268) |

## Relaciones

- **Padre:** [[PED-1208 - Gestión de Aportes y Gastos de Marketing|PED-1208]] Gestión de Aportes y Gastos de Marketing

## Descripcion

1 - Al crear una accion debe poder recibir un entero sea 1 o 2 para dolar o peso en lugar de “ARS” o “USD”
Error actual : 

```
{
    "error": true,
    "message": "El campo original currency debe ser una cadena de caracteres. (and 2 more errors)"
}
```

2- Al listar los movimientos debe traer el `fundName` y el `actionName`
Ej : 

```
{
    "id": 4,
    "actionId":13
    "actionName": "Gprueba1028", // Nuevo campo
    "actionId":35,
    "fundName": "Fondo Marketing Ducky", // Nuevo Campo
    "allocationId": null,
    "conceptShort": "prueba de 1000",
    "originalCurrency": "USD",
    "originalAmount": 1000,
    "fxRateToFund": 1,
    "amountFinalFundCurrency": 1000,
    "occurredAt": "2026-01-15 03:00:00"

}
```

3- Ordenar los movimientos  de forma **Descendente** = de la fecha de creación **más reciente a la más antigua**
