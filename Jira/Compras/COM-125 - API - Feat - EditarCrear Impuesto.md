---
jira_key: "COM-125"
aliases: ["COM-125"]
summary: "API - Feat - Editar/Crear Impuesto"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-07-02 08:44"
updated: "2024-07-05 10:06"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-125"
---

# COM-125: API - Feat - Editar/Crear Impuesto

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-07-02 08:44 |
| Actualizado | 2024-07-05 10:06 |
| Etiquetas | ninguna |
| Jira | [COM-125](https://bluinc.atlassian.net/browse/COM-125) |

## Relaciones

- **Padre:** [[COM-98]] Repositorio de impuestos por posicionar arancelaria
- **blocks:** [[COM-126]] APP - Feat - Editar / Crear impuesto
- **relates to:** [[COM-127]] API - Editar/Crear Impuesto - Sugerencia de mejora en el mensaje impuesto repetido

## Descripcion

Crearemos un recurso para poder crear nuevos impuestos y editarlos

```
POST {API_URL}v1/tariffTax
```

```
[
    {
        "acronym": "RT",
        "description": "RETENCIONES",
        "taxExclusive": false
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
        "taxExclusive": false
    }
  ]
```

¿le agregarías la posibilidad de unirlo al impuesto que viene de las posiciones arancelarias?
