---
jira_key: "LIO-296"
aliases: ["LIO-296"]
summary: "API - Review - Revisar inconveniente en query luego de los refactor"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Catriel Mercurio"
reporter: "Catriel Mercurio"
created: "2025-03-25 08:51"
updated: "2025-09-04 10:18"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-296"
---

# LIO-296: API - Review - Revisar inconveniente en query luego de los refactor

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Catriel Mercurio |
| Reportado por | Catriel Mercurio |
| Creado | 2025-03-25 08:51 |
| Actualizado | 2025-09-04 10:18 |
| Etiquetas | ninguna |
| Jira | [LIO-296](https://bluinc.atlassian.net/browse/LIO-296) |

## Relaciones

- **Padre:** [[LIO-261 - Implementar Redis|LIO-261]] Implementar Redis

## Descripcion

Desde hace unos días note que al ingresar a la sección de “precios relámpago” no obtenía resultados, al examinar la query parece tener un inconveniente que se manifiesta en varios de los repositorios.

{API_URL}/v4/search?search=&offset=0&pp=if{API_URL}/v4/brands?pp=if{API_URL}/v4/onlyResellers?pp=if{API_URL}/v4/category?pp=if```
{
"errors": {
"status": 500,
"title": "SQLSTATE[HY000]: General error: 20018 Invalid column name 'ranking'. [20018] (severity 16) [ SELECT\n\n         I.*\n        FROM SEARCH_ENGINE_LO.dbo.items AS I\n         \n        WHERE 1 = 1\n         AND instant_flash = 1\n           ORDER BY ranking DESC, mayConversion DESC  OFFSET 0 rows FETCH next 30 rows only] (Connection: sqlsrv, SQL:  SELECT\n\n         I.*\n        FROM SEARCH_ENGINE_LO.dbo.items AS I\n         \n        WHERE 1 = 1\n         AND instant_flash = 1\n           ORDER BY ranking DESC, mayConversion DESC  OFFSET 0 rows FETCH next 30 rows only)",
"file": "/var/www/app/vendor/laravel/framework/src/Illuminate/Database/Connection.php",
"line": 829
}
}
```
