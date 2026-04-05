---
jira_key: "COB-31"
summary: "API - Feat - Listar formas de pago"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-07-17 21:12"
updated: "2022-10-13 09:01"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-31"
---

# COB-31: API - Feat - Listar formas de pago

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-07-17 21:12 |
| Actualizado | 2022-10-13 09:01 |
| Etiquetas | ninguna |
| Jira | [COB-31](https://bluinc.atlassian.net/browse/COB-31) |

## Descripción

```
get {{API_URL}}/v1/paymentMethods
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
