---
jira_key: "PED-746"
aliases: ["PED-746"]
summary: "API - Refactor - Los clientes que son \"extentos\" generan pedidos con IVA = 0 como suelen hacerlo los de \"exportacion\""
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-06-19 11:01"
updated: "2024-06-19 19:57"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-746"
---

# PED-746: API - Refactor - Los clientes que son "extentos" generan pedidos con IVA = 0 como suelen hacerlo los de "exportacion"

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-06-19 11:01 |
| Actualizado | 2024-06-19 19:57 |
| Etiquetas | ninguna |
| Jira | [PED-746](https://bluinc.atlassian.net/browse/PED-746) |

## Relaciones

- **Padre:** [[PED-34 - Generar Editar ordenes|PED-34]] Generar / Editar ordenes
- **blocks:** [[SNB-2009 - FACTURA EXENTA SALE CON RETENCION DE IVA|SNB-2009]] FACTURA EXENTA SALE CON RETENCION DE IVA

## Descripcion

Esto quiere decir que siempre que hablemos de un cliente que es exento, como cuando lo hacemos de un exportador (tiera del fuego), marcaremos en cero `[NewBytes_DBF].[dbo].[pedclil].niva`
Utilizaremos para las pruebas el cliente 

21126 - OBRA SOCIAL DEL PERSONAL DE LA SANIDAD ARGENTINA

Es decir todos los clientes que su condición impositiva sea:    4 - Exento / No Gravado
