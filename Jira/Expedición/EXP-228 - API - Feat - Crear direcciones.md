---
jira_key: "EXP-228"
aliases: ["EXP-228"]
summary: "API - Feat - Crear direcciones"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-03-06 09:27"
updated: "2023-05-16 09:56"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-228"
---

# EXP-228: API - Feat - Crear direcciones

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-03-06 09:27 |
| Actualizado | 2023-05-16 09:56 |
| Etiquetas | ninguna |
| Jira | [EXP-228](https://bluinc.atlassian.net/browse/EXP-228) |

## Relaciones

- **Padre:** [[EXP-218 - Etiquetas para envíos que no las generan (genericas de ahora en mas)|EXP-218]] Etiquetas para envíos que no las generan (genericas de ahora en mas)
- **relates to:** [[EXP-227 - API - Feat -Crear direccion para el cliente|EXP-227]] API - Feat -Crear direccion para el cliente
- **blocks:** [[EXP-222 - APP - Feat - Modal para crear etiqueta de envío generica|EXP-222]] APP - Feat - Modal para crear etiqueta de envío generica

## Descripcion

Basándose en [link](https://lioteam.atlassian.net/browse/EXP-227)  se debe agregar el recurso para poder listar las direcciones en caso de necesitar generar una etiqueta desde expedición si el vendedor no lo hizo.

Es insólito, pero a veces ocurre y traba todo cuando tenes que volver para atrás y que el vendedor lo vuelve a hacer, sobre todo si ya tenes ahi el transporte, moto o lo que sea.



```
{{API_URL}}/v1/shipments/createAddress
```

Payload: 

```
{
        "address": "Benedetto 9",
        "telefono": "1530510267",
        "localityId": "BSAS",
        "provinceId":  1,
        "postalCode": "1439",
        "telephone": "1123223222",
        "clientId": 25955 
}
```
