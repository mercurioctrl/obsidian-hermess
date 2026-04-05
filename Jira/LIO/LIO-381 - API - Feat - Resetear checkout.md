---
jira_key: "LIO-381"
aliases: ["LIO-381"]
summary: "API - Feat - Resetear checkout"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-07-08 16:27"
updated: "2025-08-08 18:28"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-381"
---

# LIO-381: API - Feat - Resetear checkout

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-07-08 16:27 |
| Actualizado | 2025-08-08 18:28 |
| Etiquetas | ninguna |
| Jira | [LIO-381](https://bluinc.atlassian.net/browse/LIO-381) |

## Relaciones

- **Padre:** [[LIO-373 - Seguridad del checkout y protección de transacciones|LIO-373]] Seguridad del checkout y protección de transacciones
- **blocks:** [[LIO-383 - APP - Refactor - Implementar reseteo de checkout al expirar o volver al inicio|LIO-383]] APP - Refactor - Implementar reseteo de checkout al expirar o volver al inicio del mismo
- **relates to:** [[LIO-417 - API - Research - Resetear checkout - Expirado constante|LIO-417]] API - Research - Resetear checkout -> Expirado constante

## Descripcion

Crearemos un recurso que sirve solo a los fines de reiniciar el checkout

```
PATCH {API_URL}/pedidos/checkout/{idPedido}/reset
```

Este recurso toma ese checkout iniciado (validar `LO.dbo.pedidosCabecera.confirmado=0`)

Y reinicia sus características agregadas durante el proceso como ser

- Precio


- Descuento o tarjeta de descuento


- Opciones de envio


- Opciones de pago







Se requiere la siguiente variable de entorno:

```
# Time max checkout in minute
TIME_MAX_CHECKOUT=1
```
