---
jira_key: "PED-1264"
aliases: ["PED-1264"]
summary: "APP - Refactor - Mostrar selector de bancos solo cuando se indica para el metodo de pago seleccionado"
status: "Finalizada"
type: "Subtarea"
priority: "Low"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2026-01-14 08:43"
updated: "2026-01-29 09:34"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1264"
---

# PED-1264: APP - Refactor - Mostrar selector de bancos solo cuando se indica para el metodo de pago seleccionado

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Low |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-14 08:43 |
| Actualizado | 2026-01-29 09:34 |
| Etiquetas | ninguna |
| Jira | [PED-1264](https://bluinc.atlassian.net/browse/PED-1264) |

## Relaciones

- **Padre:** [[PED-1257]] Repositorio Bancos y medios de pago
- **action item from:** [[PED-1262]] API - Refactor - Agregar el filtro companyCode  al repositorio de metodos de pago y parámetro que indica si es o no un banco

## Descripcion

Siguiendo lo realizado en [link](https://bluinc.atlassian.net/browse/PED-1262)  mostraremos el selector de banco, solo cuando lo indica el medio de pago para evitar harcodeos y facilitar la configuración en empresas múltiples.

```
..
    {
        "id": 3,
        "description": "Dep\u00f3sito en Banco",
        "authorizedExit": "NO",
        "mustInformBank": "SI",
        "directCurrentAccount": "NO",
        "idInPaymentMethods": 7,
        "visible": true,
        "interest": 0,
        "successStatus": "",
        "successStatusDetailConvert": "",
        "companyCode": 4,
        "requiresBank": true <-- ESTE
    },
...
```
