---
jira_key: "PED-37"
aliases: ["PED-37"]
summary: "API - Repository - Medio de pago"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-08-20 21:29"
updated: "2023-08-22 10:25"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-37"
---

# PED-37: API - Repository - Medio de pago

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-08-20 21:29 |
| Actualizado | 2023-08-22 10:25 |
| Etiquetas | ninguna |
| Jira | [PED-37](https://bluinc.atlassian.net/browse/PED-37) |

## Relaciones

- **Padre:** [[PED-7]] Repositorios y base del proyecto

## Descripcion

```
GET {API_URL}/v1/paymenthMethods
```

```
[
  {
    "id": 1,
    "description": "Cta. Cte Cliente",
    "authorizedExit": "SI",
    "mustInformBank": "NO",
    "directCurrentAccount": "SI",
    "idInPaymentMethods": 5,
    "visible": "0",
    "interest": 0.0,
    "successStatus": "approved",
    "successStatusDetailConvert": "Lorem ipsum mensajito"
  },
  {
    "id": 2,
    "description": "Efectivo Moto",
    "authorizedExit": "SI",
    "mustInformBank": "NO",
    "directCurrentAccount": "NO",
    "idInPaymentMethods": 1,
    "visible": "0",
    "interest": 0.0,
    "successStatus": "in_process",
    "successStatusDetailConvert": "Lorem ipsum mensajito"
  },
  {
    "id": 3,
    "description": "Depósito en Banco",
    "authorizedExit": "NO",
    "mustInformBank": "SI",
    "directCurrentAccount": "NO",
    "idInPaymentMethods": 7,
    "visible": "1",
    "interest": 0.0,
    "successStatus": "in_process",
    "successStatusDetailConvert": "Aun debemos confirmar tu pago"
  },
  {
    "id": 4,
    "description": "Efectivo Camioneta",
    "authorizedExit": "NO",
    "mustInformBank": "NO",
    "directCurrentAccount": "NO",
    "idInPaymentMethods": 1,
    "visible": "0",
    "interest": 0.0,
    "successStatus": "approved",
    "successStatusDetailConvert": "Lorem ipsum mensajito"
  },
```

```
SELECT TOP (1000) 
    [ID_FORMA] as id,
    [DESCRIPCION] as description,
    [SALIDA_AUTORIZADA] as authorizedExit,
    [DEBE_INFORMAR_BANCO] as mustInformBank,
    [DIRECTO_CTACTE] as directCurrentAccount,
    [ID_EN_FP_FormasPagos] as idInPaymentMethods,
    [VISIBLE] as visible,
    [INTERES] as interest,
    [success_status] as successStatus,
    [success_status_detail_convert] as successStatusDetailConvert
FROM [NEW_BYTES].[dbo].[MS_FORMASPAGO_REMITOS_VENDEDORES]

```
