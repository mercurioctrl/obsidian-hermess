---
jira_key: "COB-134"
aliases: ["COB-134"]
summary: "API - Feat - Obtener cotizaciones"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-09-29 16:35"
updated: "2022-10-13 09:02"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-134"
---

# COB-134: API - Feat - Obtener cotizaciones

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-09-29 16:35 |
| Actualizado | 2022-10-13 09:02 |
| Etiquetas | ninguna |
| Jira | [COB-134](https://bluinc.atlassian.net/browse/COB-134) |

## Relaciones

- **Padre:** [[COB-21 - Base del proyecto y formularios|COB-21]] Base del proyecto y formularios
- **Subtarea:** [[COB-258 - API - Refactor - Incluir interes diario en el objeto cheques|COB-258]] API - Refactor - Incluir interes diario en el objeto cheques
- **is blocked by:** [[COB-31 - API - Feat - Listar formas de pago|COB-31]] API - Feat - Listar formas de pago

## Descripcion

## Descripción

```
GET {{API_URL}}/v1/paymentMethods
```

```
[
  {
    "id": 1,
    "description": "DOLARES",
    "increment": 0.0,
    "currencyAmount": 1.0,
    "isCheck": "NO"
  },
  {
    "id": 2,
    "description": "PESOS",
    "increment": 0.0,
    "currencyAmount": 143.25,
    "isCheck": "NO"
  },
  {
    "id": 14,
    "description": "CUENTA CORRIENTE",
    "increment": 0.0,
    "currencyAmount": 1.0,
    "isCheck": "NO"
  },
  {
    "id": 15,
    "description": "CHEQUE",
    "increment": 0.0,
    "currencyAmount": 155.02,
    "isCheck": "SI"
  }
]

```

Usando

```
SELECT   [ID_FORMAPAGO]
,[FP_DESCRIPCION]
,[FP_PORCENTAJERECARGO]
,[FP_COTIZACION]
,[FP_CANTIDADCUOTAS]
,[FP_COEFICIENTE]
,[FP_ESBILLETE]
,[FP_ESCHEQUE]
,[FP_ESCTACTE]
,[ID_TARJETA]
,[FP_COEFICIENTE_TARJETA]
,[ACTIVO]
,[IVA]
FROM [NEW_BYTES].[dbo].[MC_FORMAS_PAGO]
WHERE ACTIVO = 1
```
