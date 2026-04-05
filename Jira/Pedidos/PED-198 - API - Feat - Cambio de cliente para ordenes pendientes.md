---
jira_key: "PED-198"
aliases: ["PED-198"]
summary: "API - Feat - Cambio de cliente para ordenes pendientes"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-10-31 10:29"
updated: "2024-11-20 15:44"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-198"
---

# PED-198: API - Feat - Cambio de cliente para ordenes pendientes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-10-31 10:29 |
| Actualizado | 2024-11-20 15:44 |
| Etiquetas | ninguna |
| Jira | [PED-198](https://bluinc.atlassian.net/browse/PED-198) |

## Relaciones

- **Padre:** [[PED-34]] Generar / Editar ordenes
- **blocks:** [[PED-199]] APP - Feat - Cambio de cliente para ordenes pendientes
- **relates to:** [[PED-217]] API - Review - Revisar al cambiar el cliente de una orden y luego abrir el detalle de la orden, desaparece el nombre del cliente
- **is blocked by:** [[PED-250]] API - Cambio de cliente para ordenes pendientes - Incidencias varias
- **relates to:** [[PED-877]] API - Cambio de cliente para ordenes pendientes - Error al intentar cambiar de cliente

## Descripcion

```
PATCH {API_URL}/v1/order/changeClient
```

```
{
  order:
  branch:
  newClientId:
}
```

Esta opción sirve para poder cambiar la titularidad (clientId) de una orden, en caso de que aun este pendiente (`cestado=P`) 

Criterios de aceptacion

- Se debe cambiar tanto `ID_CLIENTE` como `ccodcli` en `[NewBytes_DBF].[dbo].[pedclit]`


- Se deben actualizar todos los precios para la lista de precios del nuevo cliente


- Solo debe poder hacerse cuando` cestado = 'P'`
