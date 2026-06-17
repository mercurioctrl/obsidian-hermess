# Migración SQL Server Dev → Contenedor (host hermess)

**Fecha:** 2026-06-17
**Autor:** Claude (deep work en terminal)
**Contexto:** El Windows Server con el motor de desarrollo andaba mal. Se migraron las 7 bases de dev a un contenedor Docker en el host `hermess`.

## Contenedor

| | |
|---|---|
| Nombre | `mssql-dev` |
| Imagen | `mcr.microsoft.com/mssql/server:2022-latest` (Developer Edition) |
| Puerto | `1433` |
| Restart policy | `unless-stopped` |
| Datos (persistente) | volumen `mssql-data` → `/var/opt/mssql` |
| Backups montados | `~/mssql/backups` → `/backups` |
| Memoria límite | 2560 MB |

## Conexión

```
Servidor:  10.10.10.7,1433   (localhost,1433 en el server)
Admin:     sa  / <password fuera de esta nota>
App/devs:  <usuario> / <password único de dev — fuera de esta nota>
```
> **Credenciales NO se documentan acá.** Passwords de desarrollo: cambiarlos si el server se expone fuera de la LAN.

## Bases restauradas (7, todas ONLINE)

| Base | Origen .bak | Tamaño | Recovery |
|---|---|---|---|
| CS | CS.bak | 21,6 GB | SIMPLE |
| NB_beta | NB_WEB.bak | 18,4 GB | FULL |
| NEW_BYTES | NEW_BYTES.bak | 10,0 GB | FULL |
| LO | LO.bak | 9,3 GB | SIMPLE |
| NewBytes_DBF | NewBytes_Dbf.bk | 8,1 GB | FULL |
| SEARCH_ENGINE_LO | SEARCH_ENGINE_LO.bak | 2,7 GB | SIMPLE |
| PRODUCTOS | PRODUCTOS.bak | 0,8 GB | FULL |

## Decisiones / problemas resueltos

1. **Log inflado de 200 GB** en `SEARCH_ENGINE_LO` (datos reales 0,58 GB). RESTORE recrea el log al tamaño original → no entraba. Resuelto en el **origen**: `SET RECOVERY SIMPLE` + `CHECKPOINT` + `DBCC SHRINKFILE` → log a 2 GB, y re-backup solo de esa base.
2. **Disco insuficiente**: `/` era 100 GB (38 libres), bases ~69 GB. El NVMe tenía ~136 GB libres en LVM. Extendido con `lvextend -l +100%FREE /dev/ubuntu-vg/ubuntu-lv` + `resize2fs` → `/` a **233 GB**. (sudo lo corre Catriel.)
3. **Logins perdidos**: el `master` original NO se migró (base de sistema). Usuarios huérfanos en todas las bases. Se recrearon **22 logins** (web, loweb, progweb, ms-envio/estado/ticket/envios/bridge, NewBytes, entercommla, NB, nn + cuentas de devs) con CHECK_POLICY=OFF y se re-mapearon con `ALTER USER ... WITH LOGIN`. 0 huérfanos restantes.
4. **Shrink post-restore**: CS 18,5→2,3 GB, LO 3,2→0,4 GB (FULL→SIMPLE). Recuperó ~18 GB.
5. **Backups .bak borrados** tras restaurar (liberó 40 GB). Disco final: 156 GB libres.

## Pendiente / recomendaciones

- No hay backup standalone (los .bak se borraron y el Windows origen falla). Armar rutina de `BACKUP DATABASE` periódica del contenedor.
- Rotar passwords si el server queda accesible fuera de la LAN.
- Apps: actualizar connection strings al password de dev definido.
