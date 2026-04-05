---
jira_key: "NBWEB-86"
aliases: ["NBWEB-86"]
summary: "Ms - envios Integracion completa de Motos y Mini Flete"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-04-05 08:38"
updated: "2022-07-01 17:40"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-86"
---

# NBWEB-86: Ms - envios Integracion completa de Motos y Mini Flete

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-04-05 08:38 |
| Actualizado | 2022-07-01 17:40 |
| Etiquetas | ninguna |
| Jira | [NBWEB-86](https://bluinc.atlassian.net/browse/NBWEB-86) |

## Relaciones

- **Padre:** [[NBWEB-76 - API - Implementar MS envios|NBWEB-76]] API - Implementar MS envios

## Descripcion

Se debe integrar de manera completa la moto y el miniflete dentro del mismo flujo que tienen los demás envíos.

Para ambos casos se debe poder parametrizar costo y precio de estos servicios.

Estos servicios deben funcionar con un mini sistema de clave publica y privada, pudiendo ser la clave publica el mismo numero de brunch y orderNumber

Ademas se deben crear recursos para poder cargar un Transportista, de modo tal de poder asignarle los envios propiamente dichos y luego poder liquidarle el costo en intervalos de tiempo. Para eso tambien debe existir una columna para marcar aquellos viajes que ya fueron liqudados por caja, dentro de la empresa.
