---
jira_key: "PED-810"
aliases: ["PED-810"]
summary: "APP - Feat - Notificaciones (primeras pruebas)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2024-08-29 08:08"
updated: "2024-09-23 13:59"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-810"
---

# PED-810: APP - Feat - Notificaciones (primeras pruebas)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2024-08-29 08:08 |
| Actualizado | 2024-09-23 13:59 |
| Etiquetas | ninguna |
| Jira | [PED-810](https://bluinc.atlassian.net/browse/PED-810) |

## Relaciones

- **Padre:** [[PED-809]] Notificaciones
- **action item from:** [[PED-829]] APP - Refactor - Al recibir notificacion se debe poder abrir los reportes si el link contiene el parametro

## Descripcion

Buscaremos integrar un esquema de notificaciones (en principio) basado en firebase para utilizar para distintas cosas como  reportes, notificaciones entre departamentos, recordatorios o avisos.

Para haremos una primera prueba de integraciones en la aplicacion de PEDIDOS

Usaremos [https://console.firebase.google.com/u/0/?hl=es-419&pli=1](https://console.firebase.google.com/u/0/?hl=es-419&pli=1)

con la cuenta 

[integraciones@nb.com.ar](mailto:integraciones@nb.com.ar) (la clave es la de siempre, pero sino pedimela por chat)

```
npm install firebase
```

Lo primero que  haremos sera configurar y crear alguna notificación de prueba para poder recibirla.

Luego avanzaremos a Leer las respuestas recibidas en soporte para notificarlas hasta que sean respondidas cada intervalos regualres de tiempo
