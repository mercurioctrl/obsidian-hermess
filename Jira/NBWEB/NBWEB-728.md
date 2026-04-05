---
jira_key: "NBWEB-728"
summary: "API - Agregar dirección - Oportunidad de mejora en la búsqueda de coincidencias"
status: "Finalizada"
type: "Tarea"
priority: "Low"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2024-05-01 14:03"
updated: "2024-05-02 11:24"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-728"
---

# NBWEB-728: API - Agregar dirección - Oportunidad de mejora en la búsqueda de coincidencias

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Low |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2024-05-01 14:03 |
| Actualizado | 2024-05-02 11:24 |
| Etiquetas | ninguna |
| Jira | [NBWEB-728](https://bluinc.atlassian.net/browse/NBWEB-728) |

## Descripción

Al ingresar la localidad como cadena de texto “agua hedionda“ con el código de población 0138 me registra el código de población 0139 - AGUA LINDA. 
Entiendo que las coincidencias no son exactas, sin embargo, creo que podemos mejorarlo.

[attachment]
```
{
    "direccion": "Locality string Postman",
    "telefono": "9112345679",
    "placeId": "0139",
    "codigoPostal": "2200",
    "predeterminado": null,
    "provinceId" : 14,
    "placeString": "agua hedionda"
}
```
