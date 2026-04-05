---
jira_key: "EXP-179"
aliases: ["EXP-179"]
summary: "API - Refactor - Agregar direccion de envio al objeto cliente dentro de la volanta"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-01-25 10:16"
updated: "2023-02-23 16:04"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-179"
---

# EXP-179: API - Refactor - Agregar direccion de envio al objeto cliente dentro de la volanta

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-01-25 10:16 |
| Actualizado | 2023-02-23 16:04 |
| Etiquetas | ninguna |
| Jira | [EXP-179](https://bluinc.atlassian.net/browse/EXP-179) |

## Relaciones

- **Padre:** [[EXP-137 - Feat - Volanta operativa|EXP-137]] Feat - Volanta operativa
- **blocks:** [[SNB-511 - NUEVO SISTEMA EXPEDICION DIRECCIONES|SNB-511]] NUEVO SISTEMA EXPEDICION  DIRECCIONES
- **blocks:** [[EXP-180 - MS - Refactor - Agregar direccion de envio al objeto cliente dentro de la|EXP-180]] MS - Refactor - Agregar direccion de envio al objeto cliente dentro de la volanta
- **blocks:** [[EXP-181 - APP - Refactor - Agregar dirección de envío al objeto cliente dentro de la|EXP-181]] APP - Refactor - Agregar dirección de envío al objeto cliente dentro de la volanta

## Descripcion

Con el objetivo de mostrar los datos a donde se enviaran los transportes dentro de la volanta, agregaremos para el cliente la informacion que tenemos disponible en 

```
SELECT [ccodcli]
      ,[cidendir]
      ,[cnomcom]
      ,[cdircli]
      ,[cpobcli]
      ,[ccodpobl]
      ,[cptlcli]
      ,[ctfo1cli]
      ,[cnaccli]
      ,[IdDirCli]
      ,[eliminar]
  FROM [NB_WEB].[dbo].[dircli]
  WHERE ccodcli = ?
```

Agregaremos

- ciudad


- provincia


- codigo postal


- direccion


- telefono y persona de contacto
