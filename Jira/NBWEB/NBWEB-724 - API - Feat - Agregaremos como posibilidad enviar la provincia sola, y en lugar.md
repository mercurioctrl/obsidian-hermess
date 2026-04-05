---
jira_key: "NBWEB-724"
aliases: ["NBWEB-724"]
summary: "API - Feat - Agregaremos como posibilidad enviar la provincia sola, y en lugar de placeId, enviaremos placeTxt"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-04-26 09:18"
updated: "2024-05-01 14:04"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-724"
---

# NBWEB-724: API - Feat - Agregaremos como posibilidad enviar la provincia sola, y en lugar de placeId, enviaremos placeTxt

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-04-26 09:18 |
| Actualizado | 2024-05-01 14:04 |
| Etiquetas | ninguna |
| Jira | [NBWEB-724](https://bluinc.atlassian.net/browse/NBWEB-724) |

## Relaciones

- **Padre:** [[NBWEB-602]] Sitio Web
- **blocks:** [[NBWEB-725]] API - Refactor - Validar direccion completa en caso de tener direccion de envio y dar respuesta en consecuencia
- **relates to:** [[NBWEB-728]] API - Agregar dirección - Oportunidad de mejora en la búsqueda de coincidencias

## Descripcion

Utilizaremos el recurso según lo conversado ayer, para admitir la posiblidad de que en el dropshipping envíen la localidad en modo texto

```
{
        "direccion": "alguna Eze",
        "telefono": "1530510267",
        "codigoPostal": "1407",
        "predeterminado": null,
        "provinceId" : 2,
        "placeString": "ABASTO"
}
```
