---
jira_key: "PEGA-14"
summary: "API - Feat - Listar productos"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-11-15 17:17"
updated: "2024-05-08 15:47"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-14"
---

# PEGA-14: API - Feat - Listar productos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-11-15 17:17 |
| Actualizado | 2024-05-08 15:47 |
| Etiquetas | ninguna |
| Jira | [PEGA-14](https://bluinc.atlassian.net/browse/PEGA-14) |

## Descripción

```
GET {API_URL}/v1/items/{terminosDeBusqueda}
```

Los catálogos son todos los recursos que entregan listados de productos. Si no tengo parámetros al respecto debo paginar. (Ponerse de acuerdo con marbe sobre si haran una recarga infinita de productos).

Es importante que este recurso funcione muy rapido, alrededor de 1 segundo como maximo

El recurso devuelve básicamente un array de objetos, donde cada objeto es un producto determinado con los siguientes atributos.

```json
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
},
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
},
]
```
