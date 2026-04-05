---
jira_key: "PED-1311"
aliases: ["PED-1311"]
summary: "API - Review - Ajuste para refresco rapido de precios en el syncUp"
status: "Tareas por hacer"
type: "Tarea"
priority: "Medium"
assignee: "Sin asignar"
reporter: "Catriel Mercurio"
created: "2026-02-20 07:11"
updated: "2026-02-20 07:13"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1311"
---

# PED-1311: API - Review - Ajuste para refresco rapido de precios en el syncUp

| Campo | Valor |
|-------|-------|
| Estado | Tareas por hacer (Por hacer) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Sin asignar |
| Reportado por | Catriel Mercurio |
| Creado | 2026-02-20 07:11 |
| Actualizado | 2026-02-20 07:13 |
| Etiquetas | ninguna |
| Jira | [PED-1311](https://bluinc.atlassian.net/browse/PED-1311) |

## Relaciones

- **Padre:** [[PED-1170 - Kits|PED-1170]] Kits

## Descripcion

Una sola vez al final del syncUp ejecutaremos lo siguiente para evitar que quede algún precio desactualizado porque aun no paso por el control del stored 


```
USE [NewBytes_DBF];
GO

SET NOCOUNT ON;
SET XACT_ABORT ON;
SET DEADLOCK_PRIORITY LOW;

DECLARE @BatchSize INT = 1000;
DECLARE @Rows INT = 1;

-- Rebates agregados una sola vez (evita recalcular MAX() en cada lote)
IF OBJECT_ID('tempdb..#RebatesLO') IS NOT NULL
    DROP TABLE #RebatesLO;

CREATE TABLE #RebatesLO
(
    internalId INT NOT NULL PRIMARY KEY,
    nominal DECIMAL(18,2) NOT NULL
);

INSERT INTO #RebatesLO (internalId, nominal)
SELECT
    R.internalId,
    MAX(CAST(R.nominal AS DECIMAL(18,2))) AS nominal
FROM [NewBytes_DBF].dbo.rebates AS R WITH (READPAST)
WHERE R.lo = 1
GROUP BY R.internalId;

-- Update por lotes para minimizar locks largos
WHILE (@Rows > 0)
BEGIN
    ;WITH Lote AS
    (
        SELECT TOP (@BatchSize)
            A.ID_ARTICULO,
            A.ncosteprom,
            B.PORC_GANAN_ESTIPLO,
            B.PORC_GANAN_ESTIPLO1,
            B.PORC_GANAN_ESTIP3,
            B.PORC_GANAN_ESTIP4,
            B.PORC_GANAN_ESTIP,
            B.PORC_GANAN_ESTIP2,
            B.PORC_GANAN_ESTIPMK1,
            B.PORC_GANAN_ESTIP6,
            ISNULL(RB.nominal, 0) AS rebate_nominal
        FROM [NewBytes_DBF].dbo.articulo AS A WITH (ROWLOCK, READPAST, UPDLOCK)
        INNER JOIN [NEW_BYTES].dbo.ST_GANANCIA_ESTIPULADA_ARTICULOS AS B WITH (READPAST)
            ON A.cRef = B.ID_ARTICULO
        LEFT JOIN #RebatesLO AS RB
            ON RB.internalId = A.ID_ARTICULO
        WHERE A.ccodfam <> '0065'
          AND A.kit = 1
        ORDER BY A.ID_ARTICULO
    )
    UPDATE A
    SET
        A.nplo  = X.Nuevo_nplo,
        A.npvp5 = X.Nuevo_npvp5,
        A.npvp1 = X.Nuevo_npvp1,
        A.npvp3 = X.Nuevo_npvp3,
        A.npvp6 = X.Nuevo_npvp6
    FROM [NewBytes_DBF].dbo.articulo AS A
    INNER JOIN Lote AS L
        ON A.ID_ARTICULO = L.ID_ARTICULO
    CROSS APPLY
    (
        SELECT
            costo_lo = CASE
                          WHEN (L.ncosteprom - L.rebate_nominal) < 0 THEN 0
                          ELSE (L.ncosteprom - L.rebate_nominal)
                       END
    ) AS C
    CROSS APPLY
    (
        SELECT
            Nuevo_nplo  = C.costo_lo + (C.costo_lo * (L.PORC_GANAN_ESTIPLO + L.PORC_GANAN_ESTIPLO1) / 100.0),
            Nuevo_npvp5 = L.ncosteprom + (L.ncosteprom * (L.PORC_GANAN_ESTIP3 + L.PORC_GANAN_ESTIP4) / 100.0),
            Nuevo_npvp1 = L.ncosteprom + (L.ncosteprom * (L.PORC_GANAN_ESTIP + L.PORC_GANAN_ESTIP2) / 100.0),
            Nuevo_npvp3 = L.ncosteprom + (L.ncosteprom * (L.PORC_GANAN_ESTIP3 + L.PORC_GANAN_ESTIP4 + L.PORC_GANAN_ESTIPMK1) / 100.0),
            Nuevo_npvp6 = L.ncosteprom + (L.ncosteprom * L.PORC_GANAN_ESTIP6 / 100.0)
    ) AS X;

    SET @Rows = @@ROWCOUNT;

    -- opcional: pequeña pausa para aliviar presión si hay mucha concurrencia
    -- WAITFOR DELAY '00:00:00.050';
END;

DROP TABLE #RebatesLO;
GO
```
