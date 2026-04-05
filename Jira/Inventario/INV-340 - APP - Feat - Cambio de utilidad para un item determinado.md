---
jira_key: "INV-340"
aliases: ["INV-340"]
summary: "APP - Feat - Cambio de utilidad para un item determinado"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2026-02-18 09:11"
updated: "2026-02-26 16:54"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-340"
---

# INV-340: APP - Feat - Cambio de utilidad para un item determinado

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2026-02-18 09:11 |
| Actualizado | 2026-02-26 16:54 |
| Etiquetas | ninguna |
| Jira | [INV-340](https://bluinc.atlassian.net/browse/INV-340) |

## Relaciones

- **Padre:** [[INV-199 - Control de Stock Stock en general Control de Precios|INV-199]] Control de Stock / Stock en general  / Control de Precios
- **action item from:** [[INV-338 - API - Feat - Cambio de precio por utilidad para un item determinado|INV-338]] API - Feat - Cambio de precio por utilidad para un item determinado

## Descripcion

Para cada una de las columnas 

- PL


- PLI


- MAY1


- MAY2


- PML


- PCAM


- LO1


- LO2



Mostraremos al desplazarnos sobre el la posibilidad de editar el campo con un decimal (mostrar 2 caracteres). Si se hace clic se puede editar en el momento y al sacar el foco se envía 

```
PATCH /itemsPrice
```

### Payload (JSON)

```
{
  "itemId": 104150,
  "type": "PL",
  "value": 31
}
```

Con el resultado de la respuesta, modificaremos los parametros de la fila segun la respuesta

```
    "current": {
      "unitPrice": 1234.56,
      "pl": 31.0,
      "pli": 5.0,
      "may1": 15.0,
      "may2": 10.0,
      "pml": 0.0,
      "lo1": 20.0,
      "lo2": 8.0,
      "dt2": 0.0,
      "dt3": 0.0,
      "pcam": 0.0,
      "mk1": 0.0,
      "cost": 100.0,
      "fob": 0.0,
      "loCost": 0.0,
      "mayPrice": 0.0,
      "priceLoReseller": 0.0,
      "PVP": 0.0,
      "mlPrice": 0.0,
      "IINT": 0.0
}
```
