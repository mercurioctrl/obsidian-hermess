---
jira_key: "PED-784"
aliases: ["PED-784"]
summary: "API - Refactor - Obtener productos para los cuales el cliente tiene una utilidad extra (se debe poder leer,editar y eliminar)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-08-01 10:00"
updated: "2024-08-11 16:21"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-784"
---

# PED-784: API - Refactor - Obtener productos para los cuales el cliente tiene una utilidad extra (se debe poder leer,editar y eliminar)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-08-01 10:00 |
| Actualizado | 2024-08-11 16:21 |
| Etiquetas | ninguna |
| Jira | [PED-784](https://bluinc.atlassian.net/browse/PED-784) |

## Relaciones

- **Padre:** [[PED-600 - EdicionAlta de cliente|PED-600]] Edicion/Alta de cliente
- **blocks:** [[PED-789 - APP - Feat - Agregar herramienta para listar,crear, eliminar utilidades extra|PED-789]] APP - Feat - Agregar herramienta para listar,crear, eliminar utilidades extra para un producto y cliente determinado

## Descripcion

Según lo realizado en [link](https://lioteam.atlassian.net/browse/PED-781) 

```
GET {API_URL}/v1/userItems/{clientId}?description={string para buscar en itemDescription}&categoryId={categoryId}
```

```
[
  {
    "id": 1,
    "clientId": 19227,
    "itemId": 116467,
    "itemDescription": "ACCESORIOS EVGA BRACKET IO INTEL LGA1700 RETENTION KIT",
    "utility": 20.0
  }
]
```

```
[NewBytes_DBF].[dbo].[userItems]
```
