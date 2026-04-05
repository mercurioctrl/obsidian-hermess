---
jira_key: "COB-474"
aliases: ["COB-474"]
summary: "API - Regularizar cuenta para administradores - Incidencias varias"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2023-08-30 01:08"
updated: "2023-09-05 15:17"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-474"
---

# COB-474: API - Regularizar cuenta para administradores - Incidencias varias

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2023-08-30 01:08 |
| Actualizado | 2023-09-05 15:17 |
| Etiquetas | ninguna |
| Jira | [COB-474](https://bluinc.atlassian.net/browse/COB-474) |

## Relaciones

- **blocks:** [[COB-453 - Feat - Regularizar cuenta para administradores|COB-453]] Feat - Regularizar cuenta para administradores

## Descripcion

**AJUSTE DE SALDO INCORRECTO**

Este es el saldo del **Cliente 26806 - MERCURIO CATRIEL EDUARDO** antes de realizar el ajuste, la query para consultar el saldo es obtenida de la función `getAccountBalance()`

[adjunto]
Se intenta hacer la regularización

[adjunto]
Y podemos observar en la siguiente captura que la cuenta del cliente no se regularizo a $0. Esto es debido a que el subtotal, antes de realizar el ajuste, en el front es de -22,05 y no de 1.0 lo que provoca que el ajuste no se realice de manera correcta.

[adjunto]
---

**VALIDACIONES REQUERIDAS**

El parámetro `adjustToAmount` no cuenta con la validación de Límite de longitud máxima y el parámetro `supportingText` con un mínimo de 50 caracteres.

[adjunto]
---

**DESCRIPCIÓN DEL MOVIMIENTO**

Falta añadir la leyenda de "regularización" en la observación indicando el origen del movimiento.

[adjunto]
---

**MODELO DEL OBJETO DE RESPUESTA**

El objeto de respuesta actual es este:

[adjunto]
Sin embargo, debería tener la siguiente estructura:

```
{
  "status" : "success",
  "message" : "La cuenta del cliente fue ajustada correctamente"
}
```
