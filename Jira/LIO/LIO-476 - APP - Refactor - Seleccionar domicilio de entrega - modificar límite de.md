---
jira_key: "LIO-476"
aliases: ["LIO-476"]
summary: "APP - Refactor - Seleccionar domicilio de entrega -> modificar límite de caracteres a 100"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Guillermo Avila"
created: "2025-11-06 18:00"
updated: "2025-12-05 04:36"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-476"
---

# LIO-476: APP - Refactor - Seleccionar domicilio de entrega -> modificar límite de caracteres a 100

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Guillermo Avila |
| Creado | 2025-11-06 18:00 |
| Actualizado | 2025-12-05 04:36 |
| Etiquetas | ninguna |
| Jira | [LIO-476](https://bluinc.atlassian.net/browse/LIO-476) |

## Relaciones

- **Padre:** [[LIO-1]] Experiencia del Usuario (UX)
- **relates to:** [[LIO-368]] APP - Refactor - Seleccionar domicilio de entrega -> modificar límite de caracteres
- **relates to:** [[LIO-346]] APP - Refactor - Seleccionar domicilio de entrega -> Oportunidad de mejora en la validación de campos

## Descripcion

Realizaremos un refactor para que el total de caracteres de la dirección de envío (Avenida/Calle, Altura, Piso, Casa/Dpto) no supere los 100 caracteres.

Además, contemplaremos la posibilidad de que las direcciones previamente guardadas ya excedan este límite.

[adjunto]
Te comparto aquí información de la dirección del cliente en orden al que deben ser ingresados en el formulario.

```
Los Crisantemos esq. Boulevard del Bosque S/N (Mzna 30, Lote 3)
1
0
Casa
7600
MAR DEL PLATA , BUENOS AIRES
[Vacío]
```
