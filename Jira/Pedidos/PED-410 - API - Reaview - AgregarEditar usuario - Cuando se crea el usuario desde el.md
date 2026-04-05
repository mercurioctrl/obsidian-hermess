---
jira_key: "PED-410"
aliases: ["PED-410"]
summary: "API - Reaview - Agregar/Editar usuario -> Cuando se crea el usuario desde el modal por primera vez debo marcar como \"correo verificado\" la cuenta"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-12-28 16:28"
updated: "2023-12-29 12:34"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-410"
---

# PED-410: API - Reaview - Agregar/Editar usuario -> Cuando se crea el usuario desde el modal por primera vez debo marcar como "correo verificado" la cuenta

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-12-28 16:28 |
| Actualizado | 2023-12-29 12:34 |
| Etiquetas | ninguna |
| Jira | [PED-410](https://bluinc.atlassian.net/browse/PED-410) |

## Relaciones

- **Padre:** [[PED-16 - Listar clientes|PED-16]] Listar clientes

## Descripcion

Al crear un usuario por primeara vez para la web, desde pedidos, debemos asegurarnos que el tilde 

`[NB_WEB].[dbo].[usuarios_nb].correoConfirmado`

quede marcado en 1, para asegurarnos que pueda usar la cuenta sin problemas.
