---
jira_key: "PEGA-44"
aliases: ["PEGA-44"]
summary: "TASK - Obtener productos por reseller en MercadoLibre AR"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-12-12 09:33"
updated: "2022-12-14 09:46"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-44"
---

# PEGA-44: TASK - Obtener productos por reseller en MercadoLibre AR

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-12-12 09:33 |
| Actualizado | 2022-12-14 09:46 |
| Etiquetas | ninguna |
| Jira | [PEGA-44](https://bluinc.atlassian.net/browse/PEGA-44) |

## Relaciones

- **Padre:** [[PEGA-26]] API - Feat - Recoger catalogos por reseller/marketplace

## Descripcion

Este ejecutable puede funcionar de cualquier forma, el único requisito es que pueda correr a partir de un cron y recibir comandos o parametros

Utilizando algún mecanismo de scrapping obtendremos los datos necesarios para llenar [link](https://lioteam.atlassian.net/browse/PEGA-41)con todos los productos del catalogo de hardgamers.

Es importante crear una “instancia” de importación en [link](https://lioteam.atlassian.net/browse/PEGA-42)que nos permita correr este “importador” para cada reseller por separado.

Basados en la misma lógica que [link](https://lioteam.atlassian.net/browse/PEGA-43) se debe obtener La búsqueda para ese producto dentro de mercado libre.

En este caso el reseller es MercadoLibre (Sin distinción por vendedor).

Lo que deberemos tomar es el producto nuevo, mas barato.



Sobre las tareas de importación:

Pueden hacerse sobre los títulos obtenidos en `HG`

Pueden hacerse sobre las búsquedas en si del sitio.
