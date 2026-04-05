---
jira_key: "COB-173"
aliases: ["COB-173"]
summary: "API - Feat - Listar conceptos de entrada"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-10-17 10:32"
updated: "2022-10-27 08:37"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-173"
---

# COB-173: API - Feat - Listar conceptos de entrada

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-10-17 10:32 |
| Actualizado | 2022-10-27 08:37 |
| Etiquetas | ninguna |
| Jira | [COB-173](https://bluinc.atlassian.net/browse/COB-173) |

## Relaciones

- **Padre:** [[COB-170]] Feat - Realizar entrada de caja
- **blocks:** [[COB-172]] APP - Feat - Realizar entrada

## Descripcion

Basados en la tabla `SELECT * from dbo.BA_BP_ORIGENES_ENTRADAS;`

```
GET {URL_API}/v1/inputConcepts
```

```json
[
    {
        "id": 1,
        "description": "Pago de Clientes con Tarjetas"
    },
    {
        "id": 2,
        "description": "Depósito a Proveedores"
    },
    {
        "id": 3,
        "description": "Saldo Inicio"
    },
    {
        "id": 5,
        "description": "Remitos Facturados"
    }
]...
```
