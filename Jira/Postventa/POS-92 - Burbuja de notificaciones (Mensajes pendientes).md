---
jira_key: "POS-92"
aliases: ["POS-92"]
summary: "Burbuja de notificaciones (Mensajes pendientes)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Ezequiel manzano"
created: "2022-08-29 12:57"
updated: "2022-10-18 14:18"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-92"
---

# POS-92: Burbuja de notificaciones (Mensajes pendientes)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Ezequiel manzano |
| Creado | 2022-08-29 12:57 |
| Actualizado | 2022-10-18 14:18 |
| Etiquetas | ninguna |
| Jira | [POS-92](https://bluinc.atlassian.net/browse/POS-92) |

## Relaciones

- **Padre:** [[POS-90 - Canal de mensajería|POS-90]] Canal de mensajería

## Descripcion

Se trata de informarle al usuario logeado que tiene mensajes pendientes en los canales de mensajerías.

Yo había pensado en ponerle algo similar a esto:

[adjunto]
para informarle que tiene un mensaje sin leer en algun canal, para esto utilizamos el recurso

```
{{API_URL}}/v1/messageChannels/pendingsBuble
```

Que nos devuelve algo así: 

[adjunto]
Con esto sabemos que pre-ingreso tiene mensajes pendientes y cuantos. Mi idea era armar un mensajito de este estilo 

“Tienes {amountMessages} pendiente/s en el pre-ingreso {postsaleInboundId}” (y que lo redirija a la pantalla de mensajes creadas en el [link](https://lioteam.atlassian.net/browse/POS-91) )

Obvio que en todo esto podes hacer lo q vos quieras yo solamente te traspaso como lo pensé 

Cualquier duda me preguntas
