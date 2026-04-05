---
jira_key: "PED-585"
aliases: ["PED-585"]
summary: "API - Feat - Agregar comprobantes de pago"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-03-07 12:56"
updated: "2024-06-14 18:44"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-585"
---

# PED-585: API - Feat - Agregar comprobantes de pago

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-03-07 12:56 |
| Actualizado | 2024-06-14 18:44 |
| Etiquetas | ninguna |
| Jira | [PED-585](https://bluinc.atlassian.net/browse/PED-585) |

## Relaciones

- **Padre:** [[PED-584]] Comprobantes de pago
- **blocks:** [[PED-587]] APP - Feat - Subir comprobante de pago
- **is blocked by:** [[PED-602]] API - Agregar comprobantes de pago - Seguridad y buenas prácticas 
- **relates to:** [[COB-489]] API - Feat - Ver comprobante de pago
- **relates to:** [[COB-498]] API - Refactor - Ver comprobante de pago - Apuntar a NB

## Descripcion

Crearemos un recurso para guardar imágenes (comprobantes) para NB o para Libre opcion.

```
PATCH {API_URL}/v1/order/paymentVoucher
```

Para esto crearemos la siguiente tabla (identica a la de libre opcio, ya que posteriormente haremos una migracion)

```
SELECT TOP (1000) [id]
      ,[pedidoCabeceraID] (puede ser null)
      ,[order]
      ,[branch] 
      ,[titular] (puede ser null)
      ,[documento]  (puede ser null)
      ,[cbu] (puede ser null)
      ,[nroOperacion] (puede ser null)
      ,[archivo]
      ,[fechaCreacion]
      ,[fechaActualizacion]
      ,[operacionInterna] (puede ser null)
  FROM [NBWEB].[dbo].[pedidosCabeceraComprobantePago]
```

En el .env debe estar el endpoint del servidor de imágenes
