---
jira_key: "PED-164"
aliases: ["PED-164"]
summary: "API - Repository - Tipo de comprobante fiscal"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-10-24 09:18"
updated: "2023-10-24 10:33"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-164"
---

# PED-164: API - Repository - Tipo de comprobante fiscal

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-10-24 09:18 |
| Actualizado | 2023-10-24 10:33 |
| Etiquetas | ninguna |
| Jira | [PED-164](https://bluinc.atlassian.net/browse/PED-164) |

## Relaciones

- **Padre:** [[PED-7]] Repositorios y base del proyecto
- **blocks:** [[PED-165]] API - Refactor - filtrar por tipo de comprobante fiscal
- **blocks:** [[PED-166]] APP - Refactor - Filtrar por tipo de comprobante fiscal

## Descripcion

Al igual que lo realizado en expedición, agregaremos el repositorio

```
GET {{API_URL}}/v1/voucherTypeTax
```

```
[
    {
        "id": 1,
        "description": "01. Facturas A",
        "tax": "A"
    },
    {
        "id": 2,
        "description": "02. Notas de Debito A",
        "tax": "A"
    },
    {
        "id": 3,
        "description": "03. Notas de Credito A",
        "tax": "A"
    },
    {
        "id": 6,
        "description": "06. Facturas B",
        "tax": "B"
    },
    {
        "id": 7,
        "description": "07. Notas de Debito B",
        "tax": "B"
    },
    {
        "id": 8,
        "description": "08. Notas de Credito B",
        "tax": "B"
    },
    {
        "id": 19,
        "description": "19. Facturas de Exportacion",
        "tax": "E"
    },
    {
        "id": 20,
        "description": "20. N. Deb. p/operac. con el exterior",
        "tax": "E"
    },
    {
        "id": 21,
        "description": "21. N. Cre. p/operac. con el exterior",
        "tax": "E"
    },
    {
        "id": 39,
        "description": "39.OTROS COMPROBANTES A QUE CUMPLEN CON LA R G  1415",
        "tax": "A"
    }
]
```
