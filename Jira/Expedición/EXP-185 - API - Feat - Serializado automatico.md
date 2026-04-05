---
jira_key: "EXP-185"
aliases: ["EXP-185"]
summary: "API - Feat - Serializado automatico"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-01-26 10:20"
updated: "2025-02-18 22:44"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-185"
---

# EXP-185: API - Feat - Serializado automatico

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-01-26 10:20 |
| Actualizado | 2025-02-18 22:44 |
| Etiquetas | ninguna |
| Jira | [EXP-185](https://bluinc.atlassian.net/browse/EXP-185) |

## Relaciones

- **Padre:** [[EXP-15 - Feat - Serializar salida|EXP-15]] Feat - Serializar salida
- **has action item:** [[EXP-480 - API - Serializado automático - Serial disponible marcado como ya en uso|EXP-480]] API - Serializado automático - Serial disponible marcado como ya en uso

## Descripcion

Es MUY importante que esta feature se haga con el menor consumo de recursos que los medios que utilizamos permitan.

Lo que se busca con esta feature, es lograr que puedan tomar cualquier serial (sin identificar producto ni nada, solo el pedido y el serial).

```
POST {API_URL}/v1/orders/{pedido}/serials
```

**Carga útil**

```
[
  {
    "serials": [
        'FAT43939393933'
    ]
}
]
```

Las verificaciones a realizar son las siguientes

- El pedido no debe estar despachado ni completo.


- El pedido debe contener el ítem al cual pertenece el serial y a su vez, el mismo aun debe estar incompleto.


- El serial no debe estar utilizado.



En caso de no cumplirse alguno de los criterios, entonces devolveremos una respuesta como la del siguiente ejemplo pero precisando en el mensaje específicamente cual de los problemas se presento.



```
{
  succes: false,
  massage: "El pedido esta completo"
  /"El producto no se encuentra en el pedido."
  /"Ese serial no se encuentra en la base de datos"
  /"El serial ya fue utilizado en otro pedido"
}
```

Estas tres validaciones pueden hacerse con una sola query y evaluando los datos de la misma.

En caso de que las condiciones están dadas, el serial se guarda en el pedido y se bloquea como hacemos siempre. Devolveremos:

```
{
  succes: true,
  massage: "Ok",
  serializedQuantity:5,
  itemDiscoveryId :53454 //este es el item que "adivinamos" es, en base al pedido y el serial
}
```
