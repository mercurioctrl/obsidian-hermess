---
jira_key: "PEGA-201"
summary: "API - Feat - Crear Syncup para importar catalogo de resellers por feet xml"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2025-06-24 11:07"
updated: "2025-07-08 10:41"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-201"
---

# PEGA-201: API - Feat - Crear Syncup para importar catalogo de resellers por feet xml

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2025-06-24 11:07 |
| Actualizado | 2025-07-08 10:41 |
| Etiquetas | ninguna |
| Jira | [PEGA-201](https://bluinc.atlassian.net/browse/PEGA-201) |

## Descripción

Se debe implementar la sincronización automática y masiva de catálogos XML de resellers, junto con varios ajustes relacionados al proceso de importación de feeds.

#### Endpoint público

```
POST /catalog/sync-all/{SYNC_TOKEN?}?resellerId=<reseller_code>
```



- Autenticación mediante la variable de entorno `SYNC_TOKEN` (ruta o query‐string).


- Permite filtrar por un único reseller mediante `resellerId`** ** optimizando recursos. (esto es opcional) 


- Recorre `reseller_catalog_feeds `con `status = 'active'`, valida que hayan transcurrido al menos `XML_RESELLER_SYNC_INTERVAL`



minutos desde `last_sync_at`y ejecuta la sincronización.

- Devuelve un resumen con feeds procesados, insertados, errores, etc.

```json
{
    "message": "Sincronización masiva completada",
    "data": [
        {
            "feed_url": "https://try.com.ar/wp-content/uploads/woo-feed/google/xml/hardgamers.xml",
            "reseller_code": 3048,
            "status": "success",
            "inserted": 1297,
            "updated": 0,
            "skipped": 1297,
            "errors": [],
            "total_products": 2594
        }
    ]
}
```



### Variables de entorno  / usadas

- `SYNC_TOKEN` – token de seguridad para el nuevo endpoint.


- `XML_RESELLER_SYNC_INTERVAL` – intervalo (min) entre sincronizaciones de un mismo feed.



### Objetivo.

Automatizar la actualización periódica de catálogos XML sin necesidad de login de reseller, garantizando la integridad del historial de precios.
