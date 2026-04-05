---
jira_key: "POS-238"
aliases: ["POS-238"]
summary: "API - Feat - Eliminar deposito (logico)"
status: "Gamma"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-03-08 12:23"
updated: "2023-03-14 10:16"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-238"
---

# POS-238: API - Feat - Eliminar deposito (logico)

| Campo | Valor |
|-------|-------|
| Estado | Gamma (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-03-08 12:23 |
| Actualizado | 2023-03-14 10:16 |
| Etiquetas | ninguna |
| Jira | [POS-238](https://bluinc.atlassian.net/browse/POS-238) |

## Relaciones

- **Padre:** [[POS-231 - Repositorios|POS-231]] Repositorios

## Descripcion

```
PATCH {API_URL}/v1/providerWarehouse
```

Carga útil:

```
{
    "id": 1
}
```

La eliminación es lógica, se debe marcar una columna en la tabla para este fin (si no existe agregarla)
