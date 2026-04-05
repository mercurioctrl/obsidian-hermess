---
jira_key: "PEGA-43"
aliases: ["PEGA-43"]
summary: "TASK - Obtener productos por reseller en hardgamers"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-11-28 09:01"
updated: "2022-12-01 13:17"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-43"
---

# PEGA-43: TASK - Obtener productos por reseller en hardgamers

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-11-28 09:01 |
| Actualizado | 2022-12-01 13:17 |
| Etiquetas | ninguna |
| Jira | [PEGA-43](https://bluinc.atlassian.net/browse/PEGA-43) |

## Relaciones

- **Padre:** [[PEGA-26 - API - Feat - Recoger catalogos por resellermarketplace|PEGA-26]] API - Feat - Recoger catalogos por reseller/marketplace

## Descripcion

Este ejecutable puede funcionar de cualquier forma, el único requisito es que pueda correr a partir de un cron y recibir comandos o parametros

Utilizando algún mecanismo de scrapping obtendremos los datos necesarios para llenar [link](https://lioteam.atlassian.net/browse/PEGA-41)con todos los productos del catalogo de hardgamers.

Es importante crear una “instancia” de importación en [link](https://lioteam.atlassian.net/browse/PEGA-42)que nos permita correr este “importador” para cada reseller por separado.

Esto nos dará un discrecional extra a la hora de configurar la prioridad que tienen los distintos reseller, ya que la velocidad con la que realizan cambios de precio es mas o menos dinámica y varia de caso a caso.

Si bien no existe un id aun en esta instancia, para los resellers (que si existe una vez procesado el catalogo) utilizaremos el campo descripción para identificarlos de la siguiente forma:

HG Gezatek

HG Maximus

HG Full4ard

Y asi para cada uno.
