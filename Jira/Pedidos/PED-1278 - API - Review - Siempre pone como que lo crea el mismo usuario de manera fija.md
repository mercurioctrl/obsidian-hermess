---
jira_key: "PED-1278"
aliases: ["PED-1278"]
summary: "API - Review - Siempre pone como que lo crea el mismo usuario de manera fija (parece estar harcodeado)"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2026-01-23 09:24"
updated: "2026-01-26 12:28"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1278"
---

# PED-1278: API - Review - Siempre pone como que lo crea el mismo usuario de manera fija (parece estar harcodeado)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-23 09:24 |
| Actualizado | 2026-01-26 12:28 |
| Etiquetas | ninguna |
| Jira | [PED-1278](https://bluinc.atlassian.net/browse/PED-1278) |

## Relaciones

- **Padre:** [[PED-1186]] Sistema de reservas de salas de reuniones (vista semanal)
- **relates to:** [[PED-1270]] API - Review - Listar reservas en un rango (para semana) - Agregar nombre de usuario -> Usuario guardado no coincidente

## Descripcion

Al ejecutar el recurso 

```
POST /v1/rooms/1/reservations
```

Utiliza siempre el userId `55` que siquiera es un usuario interno, así que asumo que debe estar harcodeado.

Si bien se que el responsable se encuentra de vacaciones, podrías darme una mano para que sea el usuario que crea la request el que se guarda?
