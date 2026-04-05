---
jira_key: "COB-473"
aliases: ["COB-473"]
summary: "APP - Regularizar cuenta para administradores - Incidencias varias"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Guillermo Avila"
created: "2023-08-29 16:52"
updated: "2023-09-05 14:36"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-473"
---

# COB-473: APP - Regularizar cuenta para administradores - Incidencias varias

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Guillermo Avila |
| Creado | 2023-08-29 16:52 |
| Actualizado | 2023-09-05 14:36 |
| Etiquetas | ninguna |
| Jira | [COB-473](https://bluinc.atlassian.net/browse/COB-473) |

## Relaciones

- **blocks:** [[COB-453]] Feat - Regularizar cuenta para administradores

## Descripcion

**VALIDACIONES REQUERIDAS**

La entrada de texto **saldo correcto del cliente** no cuenta con las validaciones siguientes:

Límite de longitud máxima

[adjunto]
[adjunto]
---

**ERROR DE ENVÍO DEL ID DEL CLIENTE**

Al hacer una segunda regularización, sin recargar el modal del detalle del cliente, el `clientId` se manda en `null` lo que ocasiona un error en el BackEnd.

[adjunto]
---

**CAMBIO DE ESTRUCTURA DE OBJETO RESPUESTA**

Al hacer una regularización aparece el siguiente error

[adjunto]
Esto puede ser debido a que el objeto de respuesta del back cambio su estructura a la siguiente

```
{ 
  "status" : "success", 
  "message" : "La cuenta del cliente fue ajustada correctamente" 
}
```
