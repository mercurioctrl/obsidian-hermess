---
jira_key: "NBWEB-160"
aliases: ["NBWEB-160"]
summary: "API - Listar medios de pago"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-05-02 09:23"
updated: "2022-06-26 21:08"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-160"
---

# NBWEB-160: API - Listar medios de pago

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-05-02 09:23 |
| Actualizado | 2022-06-26 21:08 |
| Etiquetas | ninguna |
| Jira | [NBWEB-160](https://bluinc.atlassian.net/browse/NBWEB-160) |

## Relaciones

- **Padre:** [[NBWEB-77]] Implementar Pagos
- **relates to:** [[NBWEB-184]] APP - Medio de pago - Componente para el carrito

## Descripcion

*se podra agregar el parametro para el interes?

Agregar la columna para hacer visible / no visible un determinado medio de pago en `[NEW_BYTES].[dbo].[MS_FORMASPAGO_REMITOS_VENDEDORES]`

Que luego sera listado por el recurso

```
GET {{API_URL}}/v1/carrito/paymentMethods
```

Utilizando la informacion obtenida por

```sql
SELECT TOP (1000) [ID_FORMA]
      ,[DESCRIPCION]
      ,[SALIDA_AUTORIZADA]
      ,[DEBE_INFORMAR_BANCO]
      ,[DIRECTO_CTACTE]
      ,[ID_EN_FP_FormasPagos]
  FROM [NEW_BYTES].[dbo].[MS_FORMASPAGO_REMITOS_VENDEDORES]
```

Retorna



```json
[
  {
    "payMethodId": 1,
    "description": "Cta. Cte Cliente"
  },
  {
    "payMethodId": 2,
    "description": "Efectivo Moto"
  },
  {
    "payMethodId": 3,
    "description": "Depósito en Banco"
  },
  {
    "payMethodId": 4,
    "description": "Efectivo Camioneta"
  },
  {
    "payMethodId": 5,
    "description": "Efectivo Caja"
  }
```
