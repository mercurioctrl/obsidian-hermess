---
jira_key: "INV-52"
summary: "API  - Feat - Recurso para sugerir atributos"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-01-24 07:17"
updated: "2024-01-30 03:47"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-52"
---

# INV-52: API  - Feat - Recurso para sugerir atributos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-01-24 07:17 |
| Actualizado | 2024-01-30 03:47 |
| Etiquetas | ninguna |
| Jira | [INV-52](https://bluinc.atlassian.net/browse/INV-52) |

## Descripción

Basándonos en la tabla `PRODUCTOS.dbo.etiquetas`

Crearemos un nuevo recurso que sirve para sugerir atributos cuando **matchean con 2 o mas caracteres**

```
GET {api_url}/V1/attributes?search=di
```

```
[
  {
    "description": " Maximum Display Support"
  },
  {
    "description": "Built in Audio Port"
  },
  {
    "description": "Cantidad de discos"
  },
  {
    "description": "Compatibilidad con Dispotivos de Smart Home"
  },
  {
    "description": "Con dispenser de hielo"
  },
  {
    "description": "Con display digital"
  },
  {
    "description": "Con indicador de colector lleno"
  },
  {
    "description": "Con salida de audio"
  },
  {
    "description": "Conector eléctrico adicional"
  }
  
  ...
```
