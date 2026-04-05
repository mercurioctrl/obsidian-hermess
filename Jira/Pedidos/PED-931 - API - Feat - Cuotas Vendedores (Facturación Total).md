---
jira_key: "PED-931"
aliases: ["PED-931"]
summary: "API - Feat - Cuotas Vendedores (Facturación Total)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-01-19 17:07"
updated: "2025-01-27 17:19"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-931"
---

# PED-931: API - Feat - Cuotas Vendedores (Facturación Total)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-01-19 17:07 |
| Actualizado | 2025-01-27 17:19 |
| Etiquetas | ninguna |
| Jira | [PED-931](https://bluinc.atlassian.net/browse/PED-931) |

## Relaciones

- **Padre:** [[PED-845]] Incentivos Vendedores
- **has action item:** [[MKT-243]] NB_ INCENTIVO VENDEDORES CUOTA MENSUAL
- **has action item:** [[PED-932]] API - Feat - Cuotas Vendedores (Facturación Total)

## Descripcion

Crearemos un repositorio similar al anterior por objetivos “via matcheo” pero esta vez mensual y global (es decir de toda la facturación para cada vendedor)

```
GET {API_URL}/v1/objectives/totalSale
```

## **Parámetros de la API y sus descripciones:**

- **sellerId** (número): Identificador único del vendedor en el sistema.


- **sellerDescription** (texto): Nombre y descripción del vendedor.


- **amount** (número decimal): Monto total de ventas realizadas por el vendedor en el periodo actual.


- **targetAmount** (número decimal): Cuota mensual asignada al vendedor, calculada automáticamente o configurada manualmente.


- **percentageAchieved** (número decimal): Porcentaje alcanzado del objetivo mensual, calculado como `(amount / targetAmount) * 100`.



```
[
  ...
  {
    "sellerId": 8,
    "sellerDescription": "Altamiranda Andrea",
    "totalSold": 48537.48428, <<-- Para el vendedor logueado o si tiene ped_full_benefits
    "totalCost": 30343.45
    "profit": 18194.03
    "targetAmount": 16000, <<-- Para el vendedor logueado o si tiene ped_full_benefits
    "percentageAchieved": 62.51
  },
  {
    "sellerId": 30,
    "sellerDescription": "Albarracin Julian",
    "percentageAchieved": 80.43
  }
  ...
]
```

- Se debe tener en cuenta el mes en curso completo, es decir que cada mes se reinicia


- En los casos donde un vendedor visualiza información de otros, solo se devuelve el `sellerId`, `sellerDescription` y `percentageAchieved` para proteger datos sensibles como `amount` y `targetAmount`. También puede verlos el usuario que tenga el permiso `ped_full_benefits` que ve el de todos.


- Agregaremos el parámetro `NewBytes_DBF.dbo.agentes.monthlyTargetAmount` para almacenar mensualmente el objetivo 



## **Query orientativa**

 (esta query es útil porque se basa en algo similar a lo que ven hoy con las comisiones y demas)

```sql
SELECT albclit.ccodage
    ,agentes.cnbrage+' '+agentes.capeage
    ,agentes.monthlyTargetAmount
    , SUM(CANTIDAD) AS cantidad
    , SUM(P_VENTA * CANTIDAD) AS totalSold
    , SUM(COSTO * CANTIDAD) AS totalCost
    , (SUM(P_VENTA * CANTIDAD) - SUM(COSTO * CANTIDAD)) as profit
FROM NewBytes_DBF.dbo.albclit
LEFT JOIN NewBytes_DBF.dbo.albclil
    ON albclit.ID_NROREMCLI_ENC = albclil.ID_NROREMCLI_ENC
LEFT JOIN NewBytes_DBF.dbo.articulo
    ON articulo.ID_ARTICULO = albclil.ID_ARTICULO
LEFT JOIN NB_WEB.dbo.marcas m
    ON m.id = articulo.Id_Marca
LEFT JOIN NEW_BYTES.dbo.MS_ENLACE_REMITOS_GANANCIAS
    ON albclit.cnumalb = MS_ENLACE_REMITOS_GANANCIAS.REMITO_FP
        AND albclit.cnumsuc = MS_ENLACE_REMITOS_GANANCIAS.SUCURSAL_REMITO
LEFT JOIN [NEW_BYTES].dbo.MS_REMITO_DETALLE_GANANCIA_ENLACE
    ON albclit.cnumalb = MS_REMITO_DETALLE_GANANCIA_ENLACE.REMITO_FP
        AND albclit.cnumsuc = MS_REMITO_DETALLE_GANANCIA_ENLACE.SUCURSAL_REMITO
        AND articulo.cref = MS_REMITO_DETALLE_GANANCIA_ENLACE.ID_aRTICULO
INNER JOIN NewBytes_DBF.dbo.clientes
    ON albclit.ID_CLIENTE = clientes.ID_CLIENTE
    LEFT JOIN NewBytes_DBF.dbo.agentes ON agentes.ccodage = albclit.ccodage
WHERE albclit.ID_CLIENTE IS NOT NULL
    AND FECHA_PROCESADO BETWEEN '20250101' AND '20250119'
    AND ntipoalb > 1
    AND MS_ENLACE_REMITOS_GANANCIAS.TIPO_R_NOTA = 'X'
    AND MS_REMITO_DETALLE_GANANCIA_ENLACE.TIPO_R_NOTA = 'X'
    AND (
        albclit.ccodcli <> 6
        AND albclit.ccodcli <> 9456
        AND albclit.ccodcli <> 29719
        AND albclit.ccodcli <> 33181
        )
GROUP BY albclit.ccodage,agentes.capeage , agentes.cnbrage

```
