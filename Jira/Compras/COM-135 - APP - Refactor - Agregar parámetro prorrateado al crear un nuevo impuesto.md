---
jira_key: "COM-135"
aliases: ["COM-135"]
summary: "APP - Refactor - Agregar parámetro prorrateado al crear un nuevo impuesto"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Guillermo Avila"
created: "2024-08-08 04:02"
updated: "2024-08-15 03:35"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-135"
---

# COM-135: APP - Refactor - Agregar parámetro prorrateado al crear un nuevo impuesto

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Guillermo Avila |
| Creado | 2024-08-08 04:02 |
| Actualizado | 2024-08-15 03:35 |
| Etiquetas | ninguna |
| Jira | [COM-135](https://bluinc.atlassian.net/browse/COM-135) |

## Relaciones

- **Padre:** [[COM-98]] Repositorio de impuestos por posicionar arancelaria
- **blocks:** [[COM-131]] APP - Refactor- Agregar nuevo parámetro al repositorio de impuestos 

## Descripcion

- Al crear un nuevo impuesto, agregaremos la opción de seleccionar si es o no prorrateado.



```
POST {API_URL}/v1/tariffTax
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

[adjunto]
- En el listado de impuestos agregaremos el filtro `distribute` el cual muestra el listado de impuestos que están o no prorrateados



```
GET {API_URL}/v1/tariffTax?distribute=true/false
```
