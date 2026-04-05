---
jira_key: "EXP-44"
aliases: ["EXP-44"]
summary: "API - Feat - Ingresar nuevos seriales POR INTERVALO a un producto, dentro de un pedido"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-11-07 22:24"
updated: "2023-06-21 07:11"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-44"
---

# EXP-44: API - Feat - Ingresar nuevos seriales POR INTERVALO a un producto, dentro de un pedido

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-11-07 22:24 |
| Actualizado | 2023-06-21 07:11 |
| Etiquetas | ninguna |
| Jira | [EXP-44](https://bluinc.atlassian.net/browse/EXP-44) |

## Relaciones

- **Padre:** [[EXP-11 - Feat - Serializar entrada de mercadería|EXP-11]] Feat - Serializar entrada de mercadería

## Descripcion

Este recurso es una extensión de [link](https://lioteam.atlassian.net/browse/EXP-42).

```
POST {API_URL}/v1/providersOrders/{providerOrderId}/serials/{itemId}
```

Payload:

```
[
  {
    mode:interval, //indica el modo para la lista
    "serials": [
        'MMFE8YT000095',
        'MMFE8YT000105'
    ]
}
]
```



Se trata de un recurso que nos permite dar de alta una lista de seriales a partir de dos string, uno de inicio y uno final.

**Ejemplo**:

Siendo` startSerial = MMFE8YT000095` y ` endSerial = MMFE8YT000105`

Deberemos dar de alta los siguientes seriales:

```
MMFE8YT000095
MMFE8YT000096
MMFE8YT000097
MMFE8YT000098
MMFE8YT000099
MMFE8YT000100
MMFE8YT000101
MMFE8YT000102
MMFE8YT000103
MMFE8YT000104
MMFE8YT000105
```

El truco consiste en aislar la parte que es un string de la parte que es numérica y poder incrementar el numero al mismo tiempo que lo iteramos.

Probar con un caso como el del ejemplo, que es un alfanumérico puro con caracteres y letras desordenados
