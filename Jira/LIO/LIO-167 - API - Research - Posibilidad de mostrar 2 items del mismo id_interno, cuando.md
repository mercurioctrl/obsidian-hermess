---
jira_key: "LIO-167"
aliases: ["LIO-167"]
summary: "API - Research - Posibilidad de mostrar 2 items del mismo id_interno, cuando estos tienen un titulo diferente"
status: "Backlog"
type: "Subtarea"
priority: "High"
assignee: "Catriel Mercurio"
reporter: "Catriel Mercurio"
created: "2024-12-17 09:41"
updated: "2026-02-18 11:21"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-167"
---

# LIO-167: API - Research - Posibilidad de mostrar 2 items del mismo id_interno, cuando estos tienen un titulo diferente

| Campo | Valor |
|-------|-------|
| Estado | Backlog (Por hacer) |
| Tipo | Subtarea |
| Prioridad | High |
| Asignado | Catriel Mercurio |
| Reportado por | Catriel Mercurio |
| Creado | 2024-12-17 09:41 |
| Actualizado | 2026-02-18 11:21 |
| Etiquetas | ninguna |
| Jira | [LIO-167](https://bluinc.atlassian.net/browse/LIO-167) |

## Relaciones

- **Padre:** [[LIO-166]] Catalogos y sincronizaciones

## Descripcion

Siguiendo el ejemplo creado para esto en [https://gamma.libreopcion.com/procesador_amd_am4_ryzen_7_5700g?o=rel&ver_mas_vendedores=1](https://gamma.libreopcion.com/procesador_amd_am4_ryzen_7_5700g?o=rel&ver_mas_vendedores=1) donde se inserto un producto igual al otro, de otro vendedor que puso otro titulo.

La idea seria ir a un esquema como cuando esto se podía, pero bien hecho. 

Empezando por que cuando un titulo difiere, no lo agrupe obteniendo el siguiente resultado.

[adjunto]
El resultado es que al cambiar el titulo, se desplaza al vendedor fuera de la agrupación.

Esto se hace en el sycnup por supuesto, lo cual le agrega algo de complejidad… la idea seria ver si es posible y que limitaciones tiene para despues extender la idea a otros parametros como envios gratis o cosas asi (donde algunos vendedores pueden tenerlos y otros no)
