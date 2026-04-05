---
jira_key: "EXP-43"
aliases: ["EXP-43"]
summary: "APP - Feat - Ingresar nuevos seriales a un producto, dentro de un pedido"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2022-11-07 18:54"
updated: "2023-06-21 07:11"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-43"
---

# EXP-43: APP - Feat - Ingresar nuevos seriales a un producto, dentro de un pedido

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2022-11-07 18:54 |
| Actualizado | 2023-06-21 07:11 |
| Etiquetas | ninguna |
| Jira | [EXP-43](https://bluinc.atlassian.net/browse/EXP-43) |

## Relaciones

- **Padre:** [[EXP-11]] Feat - Serializar entrada de mercadería

## Descripcion

Se trata de un formulario que tiene el cuerpo formado por un textarea que separa los seriales con un salto de linea a través de la tecla enter (esto hace la pistola).

Se debe incluir un contador, que tenga en cuenta la cantidad de seriales que ya tome y que informa el recurso [link](https://lioteam.atlassian.net/browse/EXP-39). Con cada linea, descuento uno de mi contador; ejemplo: 34/100 para decir que tome 34 de los 100 que debo tomar.

[adjunto]
Ademas posee un botón para guardar los cambios.

Una vez que se presiona el botón guardar mostrar el mensaje: “Esta seguro que desea agregar xx números de serie del producto xx en el pedido de compra xxx” Si | No

Luego construiremos con los datos la siguiente carga útil o payload:

```
[
  {
    mode:list, //indica el modo para la lista
    "serials": [
        'FAT43939393933',
        'FAT43939393933',
        'FAT43939393933',
        'FAT43939393933',
        'FAT43939393933',
        'FAT43939393933',
        'FAT43939393933',
    ]
}
]
```

y se la enviaremos al recurso [link](https://lioteam.atlassian.net/browse/EXP-42)
