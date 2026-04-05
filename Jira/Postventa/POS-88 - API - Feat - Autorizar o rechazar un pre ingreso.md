---
jira_key: "POS-88"
aliases: ["POS-88"]
summary: "API - Feat - Autorizar o rechazar un pre ingreso"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-08-26 09:41"
updated: "2022-10-14 09:35"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-88"
---

# POS-88: API - Feat - Autorizar o rechazar un pre ingreso

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-08-26 09:41 |
| Actualizado | 2022-10-14 09:35 |
| Etiquetas | ninguna |
| Jira | [POS-88](https://bluinc.atlassian.net/browse/POS-88) |

## Relaciones

- **Padre:** [[POS-87 - Feat - Autorizar y rechazar un preingreso|POS-87]] Feat - Autorizar y rechazar un preingreso
- **blocks:** [[POS-89 - APP - Feat - Autorizar o rechazar un preingreso|POS-89]] APP - Feat - Autorizar o rechazar un preingreso

## Descripcion

Esta historia se trata sobre agregar un acción para rechazar el pre ingreso.

```
PATCH {API_URL}/v1/rejectPreAfterSales
```

Payload:

```
{
    "preAfterSaleId":30,
    "reason": "Motivo escrito por un tecnico "
}
```

Se debe agregar a la tabla  correspondiente la columna rejected y una tabla aparte para los motivos (Solo `id`, `preAftersalesId` y `reason`).

Al realizar, debe enviarse un correo al cliente con los datos para reconocer el pre ingreso y los motivos de su rechazo
