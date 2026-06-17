# Migración SQL Server Dev → Contenedor (host hermess)

**Fecha:** 2026-06-17 · **Autor:** Claude (deep work en terminal) · **Host:** `hermess-server` (`10.10.10.47`)

**Contexto:** Un Windows Server (entorno de desarrollo, refrescado desde backups de producción) andaba mal. Se migraron las 7 bases a un contenedor Docker SQL Server 2022 en el host `hermess`. Ver también [[Script-Optimizacion-SQLServer]] y [[MEMORIA]].

---

## Contenedor

| | |
|---|---|
| Nombre | `mssql-dev` |
| Imagen | `mssql-dev-fts:2022-cu25` (custom, con Full-Text horneado) |
| Base original | `mcr.microsoft.com/mssql/server:2022-latest` (Developer Edition) |
| Versión motor | SQL Server 2022 RTM-CU25 (16.0.4255.1) |
| Gestión | `~/mssql/docker-compose.yml` → `docker compose up -d / down` |
| Puerto | 1433 |
| Datos | volumen externo `mssql-data` → `/var/opt/mssql` (persistente) |
| Backups | bind `~/mssql/backups` → `/backups` (chmod 777 para que el uid mssql escriba) |
| Memoria | `mem_limit: 4608m` (contenedor) · `max server memory = 4096 MB` (en master) |

**Conexión:** `10.10.10.47,1433` · admin `sa` · logins de app `<usuario>` — **credenciales fuera de esta nota** (out-of-band con Catriel). Trust server certificate (cert autofirmado).

## Las 7 bases (todas ONLINE, compat 160)

| Base | Origen .bak | Notas |
|---|---|---|
| CS | CS.bak | log shrink 18→2 GB, SIMPLE |
| LO | LO.bak | full-text (categorias/marcas/vendedores), SIMPLE |
| NB_WEB | NB_WEB.bak | restaurada como `NB_beta`, **renombrada** a `NB_WEB` |
| NEW_BYTES | NEW_BYTES.bak | ⚠️ corrupción reparada — ver abajo |
| NewBytes_DBF | NewBytes_Dbf.bk | full-text (FP_Ciudades/articulo) |
| PRODUCTOS | PRODUCTOS.bak | la más chica |
| SEARCH_ENGINE_LO | SEARCH_ENGINE_LO.bak | log inflado 200 GB→2 GB (shrink en origen), full-text (items) |

## Trabajo realizado (cronológico)

1. **Restauración** de los 7 `.bak` con `RESTORE ... WITH MOVE` (nombres lógicos auto-detectados).
2. **Disco:** el `.bak` de SEARCH_ENGINE_LO traía un log de **200 GB** (recreado al tamaño original en restore). Se resolvió en el **origen** (`SET RECOVERY SIMPLE` + `CHECKPOINT` + `DBCC SHRINKFILE` → 2 GB) y re-backup. Aun así faltaba disco: el LV `/dev/ubuntu-vg/ubuntu-lv` era de 100 GB y el NVMe tenía ~136 GB sin asignar → `lvextend -l +100%FREE` + `resize2fs` → `/` pasó a **233 GB**. (sudo lo corre Catriel.)
3. **Logins:** el `master` original NO se migró (base de sistema). Quedaron usuarios huérfanos en todas las bases → se recrearon **22 logins** (app: web, loweb, progweb, ms-envio/estado/ticket/envios/bridge, NewBytes, entercommla, NB, nn + cuentas de devs) con `CHECK_POLICY=OFF` y password de dev único, re-mapeados con `ALTER USER ... WITH LOGIN`. 0 huérfanos restantes.
4. **Mantenimiento + compat 160:** las 6 bases sanas pasaron a `COMPATIBILITY_LEVEL=160`, `DBCC UPDATEUSAGE`, rebuild de índices y `UPDATE STATISTICS WITH FULLSCAN` (las stats venían NULL/viejas del restore).
5. **Tuning memoria:** `docker update --memory 4608m` + `sp_configure 'max server memory', 4096` (en caliente). El host tiene 7,6 GB; SQL topado a 4 GB de buffer pool deja ~3 GB para el OS.
6. **Full-Text Search:** la imagen oficial NO lo trae. Se agregó el repo `packages.microsoft.com/ubuntu/22.04/mssql-server-2022` (faltaba) e instaló `mssql-server-fts=16.0.4255.1-8` + restart. Lo usan CS, LO, NewBytes_DBF, SEARCH_ENGINE_LO. Los índices se repoblaron solos al arrancar.
7. **Permanencia:** `docker commit mssql-dev mssql-dev-fts:2022-cu25` + `docker-compose.yml`. Probado: `docker rm` + recrear conserva FTS, las 7 bases, compat 160 y memoria.

## NEW_BYTES — corrupción de metadata

`DBCC CHECKDB` encontró corrupción de **catálogo de sistema** (`sysschobjs`, `sysidxstats`, `sysobjvalues`) + 1 tabla real (`ST_DETALLE_STOCK`). Nivel mínimo: `REPAIR_ALLOW_DATA_LOSS`.

- Se sacó backup de seguridad (`NEW_BYTES_pre-repair.bak`) y se corrió `REPAIR_ALLOW_DATA_LOSS` (single-user) → reparó toda la corrupción real (índices de sistema reconstruidos, ST_DETALLE_STOCK OK, 5,4M filas leyéndose bien).
- **Quedaron 2 tablas TMP basura de 2013** (`TMP_Art`, `TMP_ArtSoloMaxIDCOMPRA`, partition IDs `...106624` / `...041088`) con particiones huérfanas que **no se pueden dropear** y hacen que **CHECKDB no complete** (Msg 608/602). Se decidió **dejar la base así** (es funcional). Para un CHECKDB 100% limpio habría que migrar las tablas buenas a una base nueva.
- Su mantenimiento se corre **excluyendo esas 2 tablas** y sin `DBCC UPDATEUSAGE`.

**⚠️ La corrupción viene de PRODUCCIÓN:** al correr el script de optimización en prod aparecieron las **mismas 2 tablas con los mismos partition IDs**. Producción es **SQL Server 2012 SP4 Enterprise**. Corrupción de metadata = señal de **hardware con fallas** (disco/memoria). Pendiente: `DBCC CHECKDB` completo en prod para ver si se extendió a datos reales, y revisar salud de discos del Windows.

## Exposición a internet (UniFi)

- Controlador UniFi: `10.10.10.7:8443` (Network clásico self-hosted).
- Topología: **doble NAT** pero el USG está en **DMZ** del módem ISP → todo el tráfico entrante llega al USG.
- IP pública: `190.189.93.116` (**dinámica** → conviene DDNS).
- Regla creada por API: port-forward **`SQL-dev-41433`** (externo 41433 → `10.10.10.47:1433`, TCP, abierta a cualquier origen porque Catriel se conecta desde IPs variables).
- Blindaje: puerto no estándar + password de `sa` rotado a uno fuerte.

## Pendientes

1. 🔴 **Rutina de backups** — NO hay copias de las 7 bases (todo en un disco). Lo más urgente.
2. 🟠 **Rotar passwords** de los logins de app (siguen débiles y SQL está expuesto a internet).
3. 🟡 **DDNS** para el dominio (IP pública dinámica).
4. 🟡 **DBCC CHECKDB en producción** + revisar hardware del Windows (origen de la corrupción).
5. ⚪ Agendar el [[Script-Optimizacion-SQLServer|script de optimización]] como job semanal de SQL Agent en prod.

## Ver también
- [[Script-Optimizacion-SQLServer]] — script resiliente de optimización (apto prod, saltea tablas corruptas).
- [[MEMORIA]] — índice de infraestructura de Claude.
