---
jira_key: "PED-374"
aliases: ["PED-374"]
summary: "API - Feat - Leer condiciones de liquidación "
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-12-21 10:18"
updated: "2024-01-11 16:52"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-374"
---

# PED-374: API - Feat - Leer condiciones de liquidación 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-12-21 10:18 |
| Actualizado | 2024-01-11 16:52 |
| Etiquetas | ninguna |
| Jira | [PED-374](https://bluinc.atlassian.net/browse/PED-374) |

## Relaciones

- **Padre:** [[PED-123 - Feat - Liquidar pedido|PED-123]] Feat - Liquidar pedido
- **blocks:** [[PED-372 - APP - Feat - Guardar condiciones de liquidación (Sin liquidar)|PED-372]] APP - Feat - Guardar condiciones de liquidación (Sin liquidar)
- **relates to:** [[PED-473 - API - Leer condiciones de liquidación - Condiciones no ingresadas|PED-473]] API - Leer condiciones de liquidación - Condiciones no ingresadas

## Descripcion

Crearemos un recurso para leer las condiciones de liquidación y dejarlas prefijadas en caso de ser necesario.

A veces sucede que los vendedores las fijan, y luego viene un PM y solo liquida el pedido con su cupo.

```
GET {API_URL}/v1/makeSaleConditions/{pedido}
```

```
[
  {
    "id": 93644,
    "pedido": "X000200570446",
    "paymentMethodId": 3,
    "shippingMethod": 20,
    "bankId": 13,
    "manualCurrencyQuote": 10500000000.0,
    "comment": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem"
  }
]
```

Se deben leer en la tabla `[NB_WEB].[dbo].[liquidacion_guardada]`
