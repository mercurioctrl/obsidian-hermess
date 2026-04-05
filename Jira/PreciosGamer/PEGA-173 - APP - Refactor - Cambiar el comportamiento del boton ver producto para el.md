---
jira_key: "PEGA-173"
aliases: ["PEGA-173"]
summary: "APP - Refactor - Cambiar el comportamiento del boton \"ver producto\" para el reseller \"MercadoLibre\""
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-01-15 12:02"
updated: "2025-01-16 12:41"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-173"
---

# PEGA-173: APP - Refactor - Cambiar el comportamiento del boton "ver producto" para el reseller "MercadoLibre"

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-01-15 12:02 |
| Actualizado | 2025-01-16 12:41 |
| Etiquetas | ninguna |
| Jira | [PEGA-173](https://bluinc.atlassian.net/browse/PEGA-173) |

## Relaciones

- **Padre:** [[PEGA-7 - Feat - Detalle del producto (Ficha)|PEGA-7]] Feat - Detalle del producto (Ficha)

## Descripcion

Dado que lo que busca en realidad es la opcion mas económica y por como funciona para los casos que son marketplace no esta  atado a una ficha especifica, cambiaremos el comportamiento del botón “Ver producto” para los casos donde el reller es “Mercado Libre” de tal forma que nos permita en lugar de ir al enlace que proviene del back, **hacer la búsqueda en mercadolibre mediante el titulo**

[adjunto]
Para el caso del ejemplo ([link](https://preciosgamer.com/procesador_gamer_amd_ryzen_7_5700x_y_3_4ghz_-_19084) )  cambiaremos el enlace por

[link](https://listado.mercadolibre.com.ar/procesador-gamer-amd-ryzen-7-5700x-y-3.4ghz#D%5BA:Procesador%20Gamer%20Amd%20Ryzen%207%205700x%20Y%203.4ghz%5D) 

```
https://listado.mercadolibre.com.ar/procesador-gamer-amd-ryzen-7-5700x-y-3.4ghz#D[A:Procesador%20Gamer%20Amd%20Ryzen%207%205700x%20Y%203.4ghz]

```

Es decir

```
https://listado.mercadolibre.com.ar/{TITULO}#D[A:{TITULO}]
```



[adjunto]
