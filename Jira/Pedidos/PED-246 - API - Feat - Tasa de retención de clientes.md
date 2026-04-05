---
jira_key: "PED-246"
aliases: ["PED-246"]
summary: "API - Feat - Tasa de retención de clientes"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-11-08 09:50"
updated: "2025-02-25 18:49"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-246"
---

# PED-246: API - Feat - Tasa de retención de clientes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-11-08 09:50 |
| Actualizado | 2025-02-25 18:49 |
| Etiquetas | ninguna |
| Jira | [PED-246](https://bluinc.atlassian.net/browse/PED-246) |

## Relaciones

- **Padre:** [[PED-242 - Pestaña Estadisticas|PED-242]] Pestaña Estadisticas
- **is blocked by:** [[PED-291 - API - Tasa de retención de clientes - Incidencias varias|PED-291]]   API - Tasa de retención de clientes - Incidencias varias
- **relates to:** [[PED-959 - APP - Refactor- Modificacion en el indicador Tasa de retención de clientes|PED-959]] APP - Refactor- Modificacion en el indicador "Tasa de retención de clientes"

## Descripcion

Mide la fidelidad de los clientes a lo largo del tiempo, indicando qué tan bien el vendedor o la empresa mantienen relaciones a largo plazo.

Esta fórmula te proporciona el porcentaje de clientes que se han quedado durante todo el período en cuestión, excluyendo a los nuevos clientes, ya que quieres medir la retención y no el crecimiento. Una tasa de retención alta es generalmente indicativa de buena satisfacción del cliente y lealtad a la marca o empresa.

### Formula:

**Tasa de retención de clientes =** (Número total de clientes activos al comienzo del período - Número de clientes activos nuevos durante el período) / Número total de clientes activos al final del período

¿que se considera un cliente activo? Cualquiera que compro en los ultimos 3 meses

```
GET {API_URL}/statistics/customerRetentionRate?clientId={clientId}&sellerId{sellerId}&dateInterval={intervalo de fechas}&brandId={marca}&categoryId={categoria}
```

Se debe poder filtrar por 

- Intervalo de fechas


- Marca


- Categoría


- Cliente
