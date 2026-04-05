---
jira_key: "LIO-286"
aliases: ["LIO-286"]
summary: "API - Refactor - Gestión de información de cuentas bancarias para el cliente y su billetera -> Normalización del número de documento"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Guillermo Avila"
created: "2025-03-20 11:15"
updated: "2025-03-20 15:12"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-286"
---

# LIO-286: API - Refactor - Gestión de información de cuentas bancarias para el cliente y su billetera -> Normalización del número de documento

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Guillermo Avila |
| Creado | 2025-03-20 11:15 |
| Actualizado | 2025-03-20 15:12 |
| Etiquetas | ninguna |
| Jira | [LIO-286](https://bluinc.atlassian.net/browse/LIO-286) |

## Relaciones

- **Padre:** [[LIO-231 - Billetera|LIO-231]] Billetera
- **relates to:** [[LIO-241 - API - Feat - Gestion de informacion de cuentas bancarias para el cliente y su|LIO-241]] API - Feat - Gestion de informacion de cuentas bancarias para el cliente y su billetera

## Descripcion

Realizaremos dos refactorizaciones para que antes de insertar o actualizar el número de documento en la base de datos, se eliminen caracteres no numéricos.

```
POST {{API_URL}}/v4/wallet/bankAccount
```

```
PATCH {{API_URL}}/v4/wallet/bankAccount/{bankAccountId}
```

[adjunto]
