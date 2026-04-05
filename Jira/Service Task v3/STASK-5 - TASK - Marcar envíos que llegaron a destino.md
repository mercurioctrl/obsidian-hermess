---
jira_key: "STASK-5"
aliases: ["STASK-5"]
summary: "TASK - Marcar envíos que llegaron a destino"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-09-13 11:44"
updated: "2025-02-19 11:06"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/STASK-5"
---

# STASK-5: TASK - Marcar envíos que llegaron a destino

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-09-13 11:44 |
| Actualizado | 2025-02-19 11:06 |
| Etiquetas | ninguna |
| Jira | [STASK-5](https://bluinc.atlassian.net/browse/STASK-5) |

## Relaciones

- **Padre:** [[STASK-3]] Crear notificaciones
- **has action item:** [[STASK-6]] TASK - Marcar envíos que llegaron a destino - Oportunidad de mejora -> Guardar tiempo desde que lo tomo el currier hasta que lo entregaron
- **has action item:** [[STASK-13]] TASK - Marcar envíos que llegaron a destino - Oportunidad de mejora en la fecha almacenada

## Descripcion

```
PATCH {{API_URL}}/v1/syncUp/markAsDelivered
```

*lleva token

Agregaremos el parámetro `[NewBytes_DBF].[dbo].[pedclit].delivered` (datetime) para marcar con una fecha cuando pudimos comprobar con este proceso cuando el mismo ya le llego a los clientes.



Para esto

Crearemos una un tarea para ejecutar a través de un cron (syncUp) que se encargue de recorrer todos los pedidos que tengan un `[NewBytes_DBF].[dbo].[pedclit].medioEnvioId`, tracking y `[NewBytes_DBF].[dbo].[pedclit].delivered` en `NULL`.

y ejecutaremos el seguimiemiento para cada uno, de esta forma recorreremos el array de los estados de envío buscando una señal, palabra o indicador que nos permita determinar sin errores que el mismo llego a destino.

**Por ejemplo en OCA:**

- Estado De Visita Online (sin Motivo) - Tucuman

OCA - Tucuman

Pje Lopez 3192, Tucuman, Tucuman

09-09-2024 18:46


- **Entregado** - Tucuman **<------ Palabra Entregado**

OCA - Tucuman

Pje Lopez 3192, Tucuman, Tucuman

09-09-2024 18:46



**Por ejemplo ANDREANI:**

- El envío está viajando a la sucursal responsable de la entrega

20-08-2024 03:47


- Tu envío llegó a la sucursal a cargo de la entrega. Suscribite al servicio de notificaciones y te enviaremos novedades por e-mail

21-08-2024 04:52


- En el día de hoy estaremos visitando el domicilio de entrega

21-08-2024 08:03


- El envío **fue entregado <------ fue entregado**

21-08-2024 14:41



**Por ejemplo ENTREGAR:**

- Entregado Cobrado

Jujuy 1039, CABA, CABA

07-09-2024 12:00


- **ENTREGADO <------ Palabra Entregado**

Entregar

Av. Jujuy 1039, Capital Federal

09-09-2024 09:18





Esto se hace sobre este repositorio que es nuevo [link](https://github.com/New-Bytes/service-task-v3)  (y esta en gamma tambien)
