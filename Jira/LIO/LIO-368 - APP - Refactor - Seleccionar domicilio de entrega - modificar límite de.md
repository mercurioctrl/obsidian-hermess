---
jira_key: "LIO-368"
aliases: ["LIO-368"]
summary: "APP - Refactor - Seleccionar domicilio de entrega -> modificar límite de caracteres"
status: "Finalizada"
type: "Tarea"
priority: "Low"
assignee: "Marbe Moreno"
reporter: "Guillermo Avila"
created: "2025-06-05 14:39"
updated: "2025-11-06 18:01"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-368"
---

# LIO-368: APP - Refactor - Seleccionar domicilio de entrega -> modificar límite de caracteres

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Low |
| Asignado | Marbe Moreno |
| Reportado por | Guillermo Avila |
| Creado | 2025-06-05 14:39 |
| Actualizado | 2025-11-06 18:01 |
| Etiquetas | ninguna |
| Jira | [LIO-368](https://bluinc.atlassian.net/browse/LIO-368) |

## Relaciones

- **Padre:** [[LIO-1]] Experiencia del Usuario (UX)
- **relates to:** [[LIO-346]] APP - Refactor - Seleccionar domicilio de entrega -> Oportunidad de mejora en la validación de campos
- **relates to:** [[LIO-476]] APP - Refactor - Seleccionar domicilio de entrega -> modificar límite de caracteres a 100

## Descripcion

Realizaremos un refactor para que el total de caracteres de la dirección de envío (calle, altura, piso, casa) no superen los 60 caracteres.

```
Dirección: 01234567890123456789012345678901234567890123456789 01234567, 01234567890 012345, 012345 CP: 2100, 9 DE ABRIL, BUENOS AIRES. 
```

[adjunto]
[adjunto]
[adjunto]
