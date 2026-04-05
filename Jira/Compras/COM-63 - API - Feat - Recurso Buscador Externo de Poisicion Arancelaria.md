---
jira_key: "COM-63"
aliases: ["COM-63"]
summary: "API - Feat - Recurso Buscador Externo de Poisicion Arancelaria"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2024-02-28 12:45"
updated: "2024-03-02 14:19"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-63"
---

# COM-63: API - Feat - Recurso Buscador Externo de Poisicion Arancelaria

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2024-02-28 12:45 |
| Actualizado | 2024-03-02 14:19 |
| Etiquetas | ninguna |
| Jira | [COM-63](https://bluinc.atlassian.net/browse/COM-63) |

## Relaciones

- **Padre:** [[COM-1 - Bases y repositorios|COM-1]] Bases y repositorios

## Descripcion

Se implementa recurso con conexion externa para obtener posiciones arancelarias.

Ejemplo de busqueda: `monitor`

```
/v1/tariffPosition?search=monitor
```



Respuesta.

```
[{
        "posicion": "8528.72.00.990T",
        "descripcion": "Los demás",
        "derechos_exportacion": "0.00",
        "arancel_externo_comun": "20.00",
        "reintegros_extrazona": "7.00",
        "derechos_importacion_extrazona": "20.00",
        "reintegros_intrazona": "7.00",
        "derechos_importacion_intrazona": "0.00",
        "derechos_importacion_especifico_minimo": null,
        "unidad": "07",
        "actualizado": "2023-10-27",
        "activo": 0,
        "texto_partida": "Los demás Los demás Los demás en colores Aparatos receptores de televisión ...",
        "bk": null,
        "bit": null,
        "la": 1,
        "dumping": 0,
        "secciones_id": null,
        "pos_padre": "852872009",
        "derecho_exportacion_adicional": null
    }]
```
