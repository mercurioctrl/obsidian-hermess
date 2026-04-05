---
jira_key: "COB-263"
aliases: ["COB-263"]
summary: "API - Test - Comprobar salud de cuna cuenta especifica"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Guillermo Avila"
reporter: "Catriel Mercurio"
created: "2022-12-19 10:24"
updated: "2024-04-16 12:17"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-263"
---

# COB-263: API - Test - Comprobar salud de cuna cuenta especifica

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Guillermo Avila |
| Reportado por | Catriel Mercurio |
| Creado | 2022-12-19 10:24 |
| Actualizado | 2024-04-16 12:17 |
| Etiquetas | ninguna |
| Jira | [COB-263](https://bluinc.atlassian.net/browse/COB-263) |

## Relaciones

- **Padre:** [[COB-262 - API - Test - Salud cuenta corriente clientes|COB-262]] API - Test - Salud cuenta corriente clientes

## Descripcion

Se debe crear un recurso para comparar el monto calculado y el monto guardado del saldo total de un cliente especifico, recibido por parámetro.

Debe retornar:

```
{
calculatedBalance: 234534.43
savedBalance: 234534.43
goodHealth:true
}
```

Se debe calcular logicamente los saldos de las cuentas corrientes de cliente y verificar que sean iguales al monto guardado en `[NEW_BYTES].[dbo].[MS_CTACTE_CLIENTES]`



SQL referencia

```
SELECT [MC_CCORRIENTES_MOVIMIENTOS].ID_CLIENTE,
sum(CASE [MC_CCORRIENTES_MOVIMIENTOS].TR_CODIGO
WHEN 4 THEN
CC_IMPORTEUSD*-1
WHEN 24 THEN
CC_IMPORTEUSD*-1
WHEN 125 THEN
CC_IMPORTEUSD*-1
WHEN 14 THEN
CC_IMPORTEUSD*-1
WHEN 34 THEN
CC_IMPORTEUSD*-1
WHEN 32 THEN
CC_IMPORTEUSD*-1
WHEN 41 THEN
CC_IMPORTEUSD*-1
ELSE CC_IMPORTEUSD
END ) AS TOTAL,
(SELECT
COTIZACION
FROM NEW_BYTES.dbo.MS_COTIZACIONES
WHERE NOMBRE = 'PESOS')
AS COTIZACION_HOY
FROM [NEW_BYTES].[dbo].[MC_CCORRIENTES_MOVIMIENTOS]
WHERE ID_CLIENTE = 013667   and  CC_ANULADO = 'NO' 
GROUP BY ID_CLIENTE
```
