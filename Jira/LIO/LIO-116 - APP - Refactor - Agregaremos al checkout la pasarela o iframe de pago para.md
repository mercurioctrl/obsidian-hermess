---
jira_key: "LIO-116"
aliases: ["LIO-116"]
summary: "APP - Refactor - Agregaremos al checkout la pasarela o iframe de pago para GETNET"
status: "En curso"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2024-10-29 08:34"
updated: "2024-10-30 18:17"
labels: ["esperandoDependencia"]
jira_url: "https://bluinc.atlassian.net/browse/LIO-116"
---

# LIO-116: APP - Refactor - Agregaremos al checkout la pasarela o iframe de pago para GETNET

| Campo | Valor |
|-------|-------|
| Estado | En curso (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2024-10-29 08:34 |
| Actualizado | 2024-10-30 18:17 |
| Etiquetas | esperandoDependencia |
| Jira | [LIO-116](https://bluinc.atlassian.net/browse/LIO-116) |

## Relaciones

- **Padre:** [[LIO-8 - Proceso pago sencillo y competitiva a nivel financiamiento|LIO-8]] Proceso pago sencillo y competitiva a nivel financiamiento
- **action item from:** [[LIO-117 - API - Feat - Getnent crear intención de pago|LIO-117]] API - Feat - Getnent crear intención de pago
- **action item from:** [[LIO-97 - Resarch - Revisar la documentacion para poder implementar plataforma de pagos|LIO-97]] Resarch - Revisar la documentacion para poder implementar plataforma de pagos GETNET (santander) dentro del sitio (sin salir) para pago con tarjeta y promociones bancarias

## Descripcion

Según lo conversado ayer utilizaremos el recurso

```
POST {{API_URL}}/v4/intentionToPayGetnet
```

Para completar la pasarela de pago
