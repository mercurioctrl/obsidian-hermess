---
jira_key: "NBWEB-208"
aliases: ["NBWEB-208"]
summary: "APP - Feat - Maquetar y Conectar tickets"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2022-05-26 11:26"
updated: "2022-06-26 21:29"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-208"
---

# NBWEB-208: APP - Feat - Maquetar y Conectar tickets

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2022-05-26 11:26 |
| Actualizado | 2022-06-26 21:29 |
| Etiquetas | ninguna |
| Jira | [NBWEB-208](https://bluinc.atlassian.net/browse/NBWEB-208) |

## Relaciones

- **Padre:** [[NBWEB-99]] API - Precarga postventa
- **is blocked by:** [[NBWEB-205]] API - Enviar mensaje a un messageChannel
- **is blocked by:** [[NBWEB-257]] API - Refactor -  Leer mensajes de unm messageChannel
- **is blocked by:** [[NBWEB-204]] API - Crear un message channel con permalink

## Descripcion

El recurso consta de dos url de acceso:

La primero, cuando no estoy logueado, me permite a través del tocken leer el ticket y contestarlo de igual manera (ver [link](https://lioteam.atlassian.net/browse/NBWEB-205) )

```
{{APP_URL}}/postventa/2026/messageChannel/{token}
```



La segunda es cuando estoy logueado, que no necesito el token

```
{{APP_URL}}/v1/postventa/2026/messageChannel
```



Si no existe la informacion, debo mostrar un boton, para comenzar la conversación (ver [link](https://lioteam.atlassian.net/browse/NBWEB-204) )

[adjunto]
Se trata de un sistema clasico de tickets, al que por ahora no podran agregarse imagenes (mas alla de las que se agregaron en principio al crear el issue de postventa)
