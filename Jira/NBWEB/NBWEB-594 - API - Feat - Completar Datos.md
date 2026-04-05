---
jira_key: "NBWEB-594"
aliases: ["NBWEB-594"]
summary: "API - Feat - Completar Datos"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Guillermo Avila"
reporter: "Catriel Mercurio"
created: "2023-11-16 10:19"
updated: "2024-04-16 12:15"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-594"
---

# NBWEB-594: API - Feat - Completar Datos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Guillermo Avila |
| Reportado por | Catriel Mercurio |
| Creado | 2023-11-16 10:19 |
| Actualizado | 2024-04-16 12:15 |
| Etiquetas | ninguna |
| Jira | [NBWEB-594](https://bluinc.atlassian.net/browse/NBWEB-594) |

## Relaciones

- **Padre:** [[NBWEB-592]] Sección Completar Datos
- **blocks:** [[NBWEB-593]] APP - Feat - Completar Datos

## Descripcion

Guardaremos los datos provenientes de [link](https://lioteam.atlassian.net/browse/NBWEB-593) en la tabla `[NewBytes_DBF].[dbo].[clientes]`

```
PATCH {API_URL}/v1/client
```

Las columnas donde se guardan los datos respectivamente (cualquier duda consultarme) son:

```
      ,[cnomcli]
      ,[niva]
      ,[cnomcom]
      ,[cdircli]
      ,[ccodpobl]
      ,[cptlcli]
      ,[ctfo1cli]
      ,[cdnicif]
      ,[cdireccion]
      ,[ID_CIUDAD]
      ,[ID_PROVINCIA]
      ,[www]
      ,[whaPhone]
```

Adicionalmetne, debemos guardar en Brevo automaticamente el Whatsaap, asociado al cliente si es que existe, y si no es asi, lo crearemos.
