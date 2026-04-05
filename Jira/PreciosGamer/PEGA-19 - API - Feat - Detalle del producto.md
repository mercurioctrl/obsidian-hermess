---
jira_key: "PEGA-19"
aliases: ["PEGA-19"]
summary: "API - Feat - Detalle del producto"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-11-15 17:20"
updated: "2024-06-26 14:23"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-19"
---

# PEGA-19: API - Feat - Detalle del producto

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-11-15 17:20 |
| Actualizado | 2024-06-26 14:23 |
| Etiquetas | ninguna |
| Jira | [PEGA-19](https://bluinc.atlassian.net/browse/PEGA-19) |

## Relaciones

- **Padre:** [[PEGA-7 - Feat - Detalle del producto (Ficha)|PEGA-7]] Feat - Detalle del producto (Ficha)
- **blocks:** [[PEGA-20 - APP - Feat - Detalle del producto|PEGA-20]] APP - Feat - Detalle del producto
- **relates to:** [[PEGA-71 - API - Detalle del producto - Mejora en los parámetros de precios|PEGA-71]] API - Detalle del producto - Mejora en los parámetros de precios
- **is blocked by:** [[PEGA-94 - API - Detalle del producto - Ultimo precio no visible|PEGA-94]] API - Detalle del producto - Ultimo precio no visible

## Descripcion

```
GET {API_URL}/v1/itemDetail/{id del item}
```

```
[
{
id:35243,
resellerId: 1,
resellerDescription: LibreOpcion,
brandid:2,
brandDescription: 'Asus',
description: 'teclado Inalabrico Asus'
price: 3243,
lastPrice: 3231,
destinyUrl: 'https://www.libreopcion.com/teclado-mecanico-ducky-one-3-daybreak-sf-teclas-azulesinterruptor-rojo-silencioso-ingles-pbt-doble-disparo-sin-costuras-estuche-superior-azul-estuche-P690968?catalogue=1'
defaultimgUrl: 'https://cache-static.libreopcion.com/img/teclado_mecanico_ducky_one_3_daybreak_sf_teclas_azulesinterruptor_rojo_silencioso_ingles_pbt_doble_disparo_sin_costuras_estuche_superior_azul_estuche_ad203cbc938014de9f8b61a191d6010d.jpg'
images:[],
histogram:[] // aca mas adelante agregaremos un refactor para completar el array, basicamente son pares de fechas y precios
}
]
```
