---
jira_key: "PED-260"
aliases: ["PED-260"]
summary: "API - Feat - Tasa de conversion"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-11-13 16:33"
updated: "2023-12-13 12:55"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-260"
---

# PED-260: API - Feat - Tasa de conversion

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-11-13 16:33 |
| Actualizado | 2023-12-13 12:55 |
| Etiquetas | ninguna |
| Jira | [PED-260](https://bluinc.atlassian.net/browse/PED-260) |

## Relaciones

- **Padre:** [[PED-242]] Pestaña Estadisticas
- **is blocked by:** [[PED-295]] API - Tasa de conversión - Incidencias varias

## Descripcion

Esta métrica nos proporciona el porcentaje de visitantes que realizan una compra o una acción deseada durante un período determinado. Una alta tasa de conversión indica que nuestras tácticas de marketing son efectivas y que estamos atrayendo al público adecuado.

**Fórmula**:

Tasa de Conversión = (Número total de conversiones únicas en el período) / (Número total de visitantes únicos en el período sobre ese producto)

Una conversion la consideramos sobre la cantidad de veces que el producto se encuentra en `[NewBytes_DBF].[dbo].[albclil]` para el periodo

**Endpoint de la API**:

```
GET {API_URL}/statistics/customerConversionRate?clientId={clientId}&sellerId={sellerId}&dateInterval={intervalo de fechas}&brandId={marca}&categoryId={categoria}
```

**Filtrado**:

- Intervalo de fechas


- Marca


- Categoría


- Cliente
