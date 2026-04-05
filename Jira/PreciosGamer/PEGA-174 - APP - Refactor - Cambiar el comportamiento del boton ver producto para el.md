---
jira_key: "PEGA-174"
aliases: ["PEGA-174"]
summary: "APP - Refactor - Cambiar el comportamiento del boton \"ver producto\" para el reseller \"LibreOpcion\""
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-01-15 12:13"
updated: "2025-01-16 12:41"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-174"
---

# PEGA-174: APP - Refactor - Cambiar el comportamiento del boton "ver producto" para el reseller "LibreOpcion"

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-01-15 12:13 |
| Actualizado | 2025-01-16 12:41 |
| Etiquetas | ninguna |
| Jira | [PEGA-174](https://bluinc.atlassian.net/browse/PEGA-174) |

## Relaciones

- **Padre:** [[PEGA-7]] Feat - Detalle del producto (Ficha)

## Descripcion

Dado que lo que busca en realidad es la opcion mas económica y por como funciona para los casos que son marketplace no esta  atado a una ficha especifica, cambiaremos el comportamiento del botón “Ver producto” para los casos donde el reller es “Mercado Libre” de tal forma que nos permita en lugar de ir al enlace que proviene del back, **hacer la búsqueda en libreopcion mediante el titulo**

Para el caso del ejemplo ([link](https://preciosgamer.com/placa_de_video_zotac_gtx_1630_4gb_gddr6_ultra_compact_-_21089)  )  cambiaremos el enlace por

[link](https://libreopcion.com.ar/placa_de_video_zotac_gtx_1630_4gb_gddr6_ultra_compact?o=rel&ver_mas_vendedores=1) 

```
https://libreopcion.com.ar/placa_de_video_zotac_gtx_1630_4gb_gddr6_ultra_compact?o=rel&ver_mas_vendedores=1
```

Es decir

```
https://libreopcion.com.ar/{TITULO}?o=rel&ver_mas_vendedores=1
```
