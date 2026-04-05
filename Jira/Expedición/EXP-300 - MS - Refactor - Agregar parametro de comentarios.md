---
jira_key: "EXP-300"
aliases: ["EXP-300"]
summary: "MS - Refactor - Agregar parametro de comentarios"
status: "CodeReview"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-05-29 06:49"
updated: "2023-05-31 17:35"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-300"
---

# EXP-300: MS - Refactor - Agregar parametro de comentarios

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-05-29 06:49 |
| Actualizado | 2023-05-31 17:35 |
| Etiquetas | ninguna |
| Jira | [EXP-300](https://bluinc.atlassian.net/browse/EXP-300) |

## Relaciones

- **Padre:** [[EXP-13]] Feat - Etiquetas y seguimiento
- **blocks:** [[EXP-299]] APP - Refactor - Agregar observaciones editables para los expedicionistas

## Descripcion

Considerando que existe en cada una de las APIs de los transportes (OCA,Andreani,Entregar,etc, transporte propio) un campo para poner observaciones, que a su vez, sale en la etiqueta, atenderemos el reclamo de [link](https://lioteam.atlassian.net/browse/SNB-759) donde se pide que agreguemos un campo para poner observaciones mas detalladas o de manera libre.

Este parámetro observaciones debe estar limitado en caracteres al máximo de caracteres permitidos por el transportista que menos caracteres permita.  

Ademas debe verse en las etiquetas emitidas por cada uno, incluida la genérica creada por nosotros.

De esta forma refactorizaremos 

```
{{API_URL}}/addTrackingOrder/nb
```

```
{
    "branch": "0002",
    "order": "10290322",
    "packageGroup": 1,
    "assignValue": false
    "comment": "lorem ipsum bla bla bla" <- Se agrega nuevo parametro opcional, puede estar o no
}
```

También se debe ajustar 

```
{{API_URL}}/getLabel/{etiqueta}/jpg
```

```
{{API_URL}}/getLabel/{etiqueta}/pdf
```

```
{{API_URL}}/getLabel/{etiqueta}/zpl
```

Para mostrar el parámetro observaciones en cada etiqueta
