---
jira_key: "COM-254"
aliases: ["COM-254"]
summary: "API - MVP - Refactor - Listar repositorio de impuestos/gastos -> Agregar companyCode y companyDescription"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Guillermo Avila"
created: "2025-11-20 15:03"
updated: "2025-12-05 05:46"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-254"
---

# COM-254: API - MVP - Refactor - Listar repositorio de impuestos/gastos -> Agregar companyCode y companyDescription

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Guillermo Avila |
| Creado | 2025-11-20 15:03 |
| Actualizado | 2025-12-05 05:46 |
| Etiquetas | ninguna |
| Jira | [COM-254](https://bluinc.atlassian.net/browse/COM-254) |

## Relaciones

- **Padre:** [[COM-98]] Repositorio de impuestos por posicionar arancelaria
- **relates to:** [[COM-233]] API - MVP - Agregar filtro de empresa a la pestaña de impuestos/gasto (tariffTax)
- **relates to:** [[COM-99]] API - Feat - Listar repositorio de impuestos para posiciones arancelarias

## Descripcion

Realizaremos una refactorización en el recurso que obtiene los “Impuestos/Gastos” para agregar los campos `companyCode` y `companyDescription`. El objetivo es que el frontend pueda utilizar estas claves para mostrarlas al momento de editar un impuesto/gasto.

```
{{API_URL}}/v1/tariffTax
```

```
{
	{
		"id": 11,
		"acronym": "c",
		"description": "Coima",
		"taxExclusive": false,
		"distribute": false,
        "companyCode": <------------------ SE AGREGA
        "companyDescription"  <----------- SE AGREGA
	},
...
}
```

[adjunto]
