---
jira_key: "PED-35"
aliases: ["PED-35"]
summary: "API - Feat - Crear nueva orden para un cliente"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-08-20 21:15"
updated: "2023-09-27 10:09"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-35"
---

# PED-35: API - Feat - Crear nueva orden para un cliente

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-08-20 21:15 |
| Actualizado | 2023-09-27 10:09 |
| Etiquetas | ninguna |
| Jira | [PED-35](https://bluinc.atlassian.net/browse/PED-35) |

## Relaciones

- **Padre:** [[PED-34 - Generar Editar ordenes|PED-34]] Generar / Editar ordenes
- **blocks:** [[PED-71 - APP - Feat - Crear un nueva orden para un cliente|PED-71]] APP - Feat - Crear un nueva orden para un cliente

## Descripcion

Este recurso sirve para generar nuevas ordenes a las cuales posteriormente le agregaremos productos.

Puede recibir como parámetro 

- clientId


- branch (suc 10, suc 2 y suc 0, estos ultimos son presupuestos) 



```
POST {API_URL}/v1/orders
```

```
[
  {
    clientId: 23452
    branch: '0002'
  }
]
```



Crearemos entonces un nuevo pedido en `[NewBytes_DBF].[dbo].[pedclit]` para eso tendremos en cuenta los datos

`clientId` y  `branch`

Ademas, `branch` define tambien la observación en algunos casos siendo

```
($sucursal == 00) ? "PRESUPUESTO" : "INTERNO";
```



Query orientadora

```sql
DECLARE @MaxCnumped INT, @UserId INT;

-- Convertir el UserId solo una vez
SET @clientId = CAST({clientId} as INT);

-- Obtener el valor máximo de cnumped una vez
SELECT @MaxCnumped = MAX(cnumped) + 1 
FROM NewBytes_DBF.dbo.pedclit 
WHERE cnumsuc = {branch};

INSERT INTO NewBytes_DBF.dbo.pedclit 
(cnumped, cnumsuc, ccodcli, dfecped, ccodalm, cestado, cobserv, ccodage, ID_VENDEDOR, ID_ALMACEN, ID_CLIENTE, ID_Sucursal, secret_key, nvaldiv, medioEnvioId, idDirCliNbWeb, packageWeight, packageSize, amountPackages)
SELECT 
    @MaxCnumped AS cnumped,
    {branch} AS cnumsuc,
    C.ccodcli,
    GETDATE() AS dfecped,
    'SAF' AS ccodalm,
    'P' AS cestado,
    CASE 
    WHEN {branch} = '0000' THEN 'PRESUPUESTO'
    ELSE 'INTERNO'
    END AS cobserv,
    C.ccodage,
    C.ID_VENDEDOR,
    2 AS ID_ALMACEN,
    C.ID_CLIENTE,
    2 AS ID_Sucursal,
    ? AS secret_key,
    (SELECT TOP 1 COTIZACION FROM NB_WEB.dbo.MS_COTIZACIONES WHERE IDFORMAPAGO = 1) as nvaldiv,
FROM NewBytes_DBF.dbo.clientes C
WHERE C.ID_CLIENTE = @clientId

```
