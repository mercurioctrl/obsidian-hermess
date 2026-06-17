# Script de Optimización SQL Server (resiliente, apto producción)

**Fecha:** 2026-06-17 · Parte de la [[Migracion_SQLServer_Dev|migración SQL Server]].

Optimiza índices + estadísticas **salteando tablas corruptas/bloqueadas** sin abortar. Nació de la corrupción de [[Migracion_SQLServer_Dev#NEW_BYTES — corrupción de metadata|NEW_BYTES]] (que viene de producción). Copia local en `~/mssql/optimizar_NEW_BYTES_prod.sql`.

## Cómo funciona (lecciones aprendidas)

- **Fragmentación-aware por tabla:** REORGANIZE 5-30%, REBUILD >30%. Solo toca lo fragmentado → no infla el log.
- **`TRY/CATCH` por tabla:** si una tabla falla (corrupción/lock), la saltea, la registra y sigue. El reporte final lista qué saltó.
- **Clave técnica:** el DMF `sys.dm_db_index_physical_stats` sobre **toda la DB** tira error **fatal Level 21 NO atrapable** en bases corruptas. Pero llamándolo **por tabla** (con `OBJECT_ID` específico) dentro de `TRY/CATCH` **SÍ es atrapable**. Por eso el script consulta la fragmentación tabla por tabla.
- **NO usa `DBCC UPDATEUSAGE`** (aborta con la corrupción de catálogo).
- **`ONLINE=ON`** con fallback automático a OFFLINE (para columnas LOB en SQL 2012, o ediciones Standard).

## Parámetros

- `@Online` = 1 en **Enterprise/Developer** (sin bloqueos). En **Standard** → 0.
- `@FragReorg` / `@FragRebuild` = umbrales de fragmentación.
- `@MinPaginas` = 1000 (ignora índices < ~8 MB).

## Consideraciones producción

1. Producción es **SQL Server 2012 SP4 Enterprise** → `@Online = 1` correcto. Script 100% compatible con 2012.
2. **Recovery FULL:** tener backups de log corriendo durante la optimización (los REBUILD generan log; en una prueba se llenó el log de NEW_BYTES en dev).
3. Guardar la lista de "objetos salteados" → son las tablas corruptas a revisar con `DBCC CHECKDB`.
4. Agendar como **job semanal de SQL Agent** (las stats/fragmentación se degradan con el uso).

## Script

```sql
SET NOCOUNT ON; SET QUOTED_IDENTIFIER ON; SET ARITHABORT ON;

DECLARE @Online      bit   = 1;     -- 1 sin bloqueos (Ent/Dev). STANDARD -> 0.
DECLARE @FragReorg   float = 5.0;
DECLARE @FragRebuild float = 30.0;
DECLARE @MinPaginas  int   = 1000;  -- ignora indices < ~8 MB
DECLARE @UpdateStats bit   = 1;

DECLARE @oid int, @full nvarchar(520), @idx sysname, @frag float,
        @sql nvarchar(max), @sqlOff nvarchar(max), @okIdx int=0, @okStat int=0;
DECLARE @err   TABLE(objeto nvarchar(520), fase varchar(12), motivo nvarchar(2000));
DECLARE @frags TABLE(idxname sysname, frag float);

DECLARE cur CURSOR LOCAL FAST_FORWARD FOR
  SELECT object_id, QUOTENAME(SCHEMA_NAME(schema_id))+N'.'+QUOTENAME(name) FROM sys.tables;
OPEN cur; FETCH NEXT FROM cur INTO @oid, @full;
WHILE @@FETCH_STATUS = 0
BEGIN
  BEGIN TRY
    DELETE @frags;
    INSERT @frags(idxname, frag)
      SELECT i.name, ps.avg_fragmentation_in_percent
      FROM sys.dm_db_index_physical_stats(DB_ID(), @oid, NULL, NULL, 'LIMITED') ps
      JOIN sys.indexes i ON i.object_id=ps.object_id AND i.index_id=ps.index_id
      WHERE ps.index_id > 0 AND i.name IS NOT NULL
        AND ps.page_count >= @MinPaginas
        AND ps.avg_fragmentation_in_percent >= @FragReorg;

    DECLARE ci CURSOR LOCAL FAST_FORWARD FOR SELECT idxname, frag FROM @frags;
    OPEN ci; FETCH NEXT FROM ci INTO @idx, @frag;
    WHILE @@FETCH_STATUS = 0
    BEGIN
      IF @frag >= @FragRebuild
        SET @sql = N'ALTER INDEX '+QUOTENAME(@idx)+N' ON '+@full+N' REBUILD'
                 + CASE WHEN @Online=1 THEN N' WITH (ONLINE=ON)' ELSE N'' END + N';';
      ELSE
        SET @sql = N'ALTER INDEX '+QUOTENAME(@idx)+N' ON '+@full+N' REORGANIZE;';
      BEGIN TRY EXEC sp_executesql @sql; SET @okIdx += 1; END TRY
      BEGIN CATCH
        BEGIN TRY SET @sqlOff=REPLACE(@sql,N' WITH (ONLINE=ON)',N''); EXEC sp_executesql @sqlOff; SET @okIdx += 1; END TRY
        BEGIN CATCH INSERT @err VALUES(@full+N'.'+QUOTENAME(@idx),'indice',ERROR_MESSAGE()); END CATCH
      END CATCH
      FETCH NEXT FROM ci INTO @idx, @frag;
    END
    CLOSE ci; DEALLOCATE ci;

    IF @UpdateStats = 1
    BEGIN SET @sql=N'UPDATE STATISTICS '+@full+N';'; EXEC sp_executesql @sql; SET @okStat += 1; END
  END TRY
  BEGIN CATCH
    INSERT @err VALUES(@full, 'tabla', ERROR_MESSAGE());
    IF CURSOR_STATUS('local','ci') >= 0 BEGIN CLOSE ci; DEALLOCATE ci; END
  END CATCH
  FETCH NEXT FROM cur INTO @oid, @full;
END
CLOSE cur; DEALLOCATE cur;

DECLARE @nErr int = (SELECT COUNT(*) FROM @err);
PRINT ' Indices reorg/rebuild        : ' + CAST(@okIdx  AS varchar);
PRINT ' Tablas con stats actualizadas: ' + CAST(@okStat AS varchar);
PRINT ' Objetos SALTEADOS por error  : ' + CAST(@nErr AS varchar);
SELECT objeto AS [Objeto salteado], fase, motivo AS [Motivo] FROM @err ORDER BY fase, objeto;
```

## Resultado validado (dev y prod)

Corrida sobre NEW_BYTES: optimizó **376 tablas**, salteó las **2 corruptas** (`TMP_Art`, `TMP_ArtSoloMaxIDCOMPRA`) listándolas por nombre y motivo, sin abortar. Mismo resultado en producción.

## Ver también
- [[Migracion_SQLServer_Dev]] — runbook completo de la migración.
