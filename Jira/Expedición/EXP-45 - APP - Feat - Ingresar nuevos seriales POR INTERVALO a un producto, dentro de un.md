---
jira_key: "EXP-45"
aliases: ["EXP-45"]
summary: "APP - Feat - Ingresar nuevos seriales POR INTERVALO a un producto, dentro de un pedido"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2022-11-07 22:25"
updated: "2023-06-21 07:11"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-45"
---

# EXP-45: APP - Feat - Ingresar nuevos seriales POR INTERVALO a un producto, dentro de un pedido

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2022-11-07 22:25 |
| Actualizado | 2023-06-21 07:11 |
| Etiquetas | ninguna |
| Jira | [EXP-45](https://bluinc.atlassian.net/browse/EXP-45) |

## Relaciones

- **Padre:** [[EXP-11 - Feat - Serializar entrada de mercadería|EXP-11]] Feat - Serializar entrada de mercadería
- **blocks:** [[EXP-186 - APP - Feat - Serializar salida por intervalos|EXP-186]] APP - Feat - Serializar salida por intervalos

## Descripcion

Esta feature utiliza [link](https://lioteam.atlassian.net/browse/EXP-44)

Referencia horrible del sistema anterior

[adjunto]
Se trata de un recurso que nos permite dar de alta una lista de seriales a partir de dos string, uno de inicio y uno final.

**Ejemplo**:

Siendo` startSerial = MMFE8YT000095` y `endSerial = MMFE8YT000105`

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

A partir de dos input de entrada para un string se debe generar la siguiente carga util

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
