---
jira_key: "COM-166"
aliases: ["COM-166"]
summary: "APP - Feat - Agregar cotizacion y cotizacion fiscal"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-01-20 07:56"
updated: "2025-01-29 02:24"
labels: ["esperandoDependencia"]
jira_url: "https://bluinc.atlassian.net/browse/COM-166"
---

# COM-166: APP - Feat - Agregar cotizacion y cotizacion fiscal

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-01-20 07:56 |
| Actualizado | 2025-01-29 02:24 |
| Etiquetas | esperandoDependencia |
| Jira | [COM-166](https://bluinc.atlassian.net/browse/COM-166) |

## Relaciones

- **Padre:** [[COM-77 - Editar orden de compra|COM-77]] Editar orden de compra
- **action item from:** [[COM-165 - API - Feat - Agregar cotizacion y cotizacion fiscal|COM-165]] API - Feat - Agregar cotizacion y cotizacion fiscal

## Descripcion

Agregaremos como elementos editables tanto la cotizacion (`currencyQuote`) como la cotizacion fiscal (`currencyFiscalQuote`)

Que proviene de 

```
GET {API_URL}/v1/providerOrder/{providerOrdeId}
```

y se puede editar con

```
PATCH GET {API_URL}/v1/providerOrder/{providerOrdeId}
```

[adjunto]
