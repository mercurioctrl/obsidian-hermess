---
jira_key: "PED-29"
aliases: ["PED-29"]
summary: "API - Feat - Editar direcciones del cliente"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-08-16 08:16"
updated: "2024-01-04 15:48"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-29"
---

# PED-29: API - Feat - Editar direcciones del cliente

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-08-16 08:16 |
| Actualizado | 2024-01-04 15:48 |
| Etiquetas | ninguna |
| Jira | [PED-29](https://bluinc.atlassian.net/browse/PED-29) |

## Relaciones

- **Padre:** [[PED-16 - Listar clientes|PED-16]] Listar clientes
- **blocks:** [[PED-30 - APP - Feat - AgregarEditar direcciones|PED-30]] APP - Feat - Agregar/Editar direcciones
- **is blocked by:** [[PED-445 - API - Editar direcciones del cliente - Error al actualizar|PED-445]] API - Editar direcciones del cliente - Error al actualizar

## Descripcion

```
  {
        "address": "Benedetto 91",
        "localityId": "0001",
        "provinceId":  2,
        "postalCode": "1439",
        "telephone": "11232232221",
        "IdDirCli": "23077",
        "predeterminado": null
    }
```

Retorna

```
{
  succes:true
}
```
