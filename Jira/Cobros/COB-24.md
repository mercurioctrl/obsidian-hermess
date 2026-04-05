---
jira_key: "COB-24"
summary: "API - Feat - Sistema de permisos"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-07-17 19:49"
updated: "2022-10-13 09:01"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-24"
---

# COB-24: API - Feat - Sistema de permisos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-07-17 19:49 |
| Actualizado | 2022-10-13 09:01 |
| Etiquetas | ninguna |
| Jira | [COB-24](https://bluinc.atlassian.net/browse/COB-24) |

## Descripción

Se debe integrar un sistema de permisos con el cual proteger y restringir las aplicaciones o incluso funciones especificas.

La clave o permiso para ingresar al sistema es `cobros` y debe devolver 1 al ser consultado para hacer login.

Para esto debe utilizarse la tabla `NB_WEB.dbo.permisos_agente`.



Ejemplo: La tabla `NB_WEB.dbo.permisos_agente` contiene diferentes columnas que otorgan permisos generales y particulares.

[attachment]
###### En esta imagen, se columnas del mismo subsitema. La general llamada `clientes` es la que permite hacer login en el sistema de clientes y obtener acceso básico.

###### Mientras que las siguientes (`clientes_solicitudes`, `clientes_clientes,` `clientes_pedidos`) otorgan permisos mas específicos dentro del sistema de clientes.

Supongamos que yo, una vez dentro del sistema de clientes quisiera realizar un pedido, entonces mi función de permisos debe devolver 1 al consultar por la clave `clientes_pedidos` para ese usuario.
