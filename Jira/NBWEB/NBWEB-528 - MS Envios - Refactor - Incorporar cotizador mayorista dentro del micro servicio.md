---
jira_key: "NBWEB-528"
aliases: ["NBWEB-528"]
summary: "MS Envios - Refactor - Incorporar cotizador mayorista dentro del micro servicio de envios"
status: "En curso"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-04-10 13:52"
updated: "2023-04-14 10:28"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-528"
---

# NBWEB-528: MS Envios - Refactor - Incorporar cotizador mayorista dentro del micro servicio de envios

| Campo | Valor |
|-------|-------|
| Estado | En curso (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-04-10 13:52 |
| Actualizado | 2023-04-14 10:28 |
| Etiquetas | ninguna |
| Jira | [NBWEB-528](https://bluinc.atlassian.net/browse/NBWEB-528) |

## Relaciones

- **Padre:** [[NBWEB-507]] Refactor cotizacion de envios en el sitio

## Descripcion

Segun lo conversado en la daily, incorporaremos el nuevo endpoint de andreani, en un recurso diferenciado

```
{{API_URL}}/addTrackingOrder/nbDistributor
```

```
{
    "branch": "0002",
    "order": "10289017",
    "packageGroup": 1
}

```

Se busca utilizar los métodos para el contrato nuevo, con los endpoint nuevos.

En el caso de OCA, URBANO y otros, este endpoint actua de la misma forma que `{{API_URL}}/addTrackingOrder/nb`

Si necesitas que veamos algo de esto, avisame
