---
jira_key: "COM-130"
aliases: ["COM-130"]
summary: "API - Refactor - Agregar nuevo parametro al repositorio de impuestos"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-08-05 14:22"
updated: "2024-08-08 04:24"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-130"
---

# COM-130: API - Refactor - Agregar nuevo parametro al repositorio de impuestos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-08-05 14:22 |
| Actualizado | 2024-08-08 04:24 |
| Etiquetas | ninguna |
| Jira | [COM-130](https://bluinc.atlassian.net/browse/COM-130) |

## Relaciones

- **Padre:** [[COM-98 - Repositorio de impuestos por posicionar arancelaria|COM-98]] Repositorio de impuestos por posicionar arancelaria
- **blocks:** [[COM-131 - APP - Refactor- Agregar nuevo parámetro al repositorio de impuestos|COM-131]] APP - Refactor- Agregar nuevo parámetro al repositorio de impuestos 
- **blocks:** [[COM-132 - APP - Refactor - Agregar al modal del detalle de la orden los impuestos que son|COM-132]] APP - Refactor - Agregar al modal del detalle de la orden los impuestos que son prorrateables abajo

## Descripcion

Agregaremos un parámetro destinado a saber que impuestos deben prorratearse en todos los items de un pedido determinado en lugar de afectar a un item puntual 

Tambien agregaremos un filtro para mostrar todos(cuando no envio el filtro)/true/false

```
GET {API_URL}v1/tariffTax?distribute=true/false
```

```
POST {API_URL}v1/tariffTax
```

```
[
    {
        "acronym": "RT",
        "description": "RETENCIONES",
        "taxExclusive": false,
        "distribute": true/false,
    }
  ]
```



```
PATCH {API_URL}v1/tariffTax
```

```
[
    {
        "id": 4,
        "description": "RETENCIONES",
        "taxExclusive": false,
        "distribute": true/false,
    }
  ]
```
