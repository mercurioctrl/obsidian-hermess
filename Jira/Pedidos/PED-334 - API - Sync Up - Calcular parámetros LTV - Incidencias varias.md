---
jira_key: "PED-334"
aliases: ["PED-334"]
summary: "API - Sync Up - Calcular parámetros LTV - Incidencias varias"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Guillermo Avila"
created: "2023-12-14 15:37"
updated: "2023-12-18 14:13"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-334"
---

# PED-334: API - Sync Up - Calcular parámetros LTV - Incidencias varias

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Guillermo Avila |
| Creado | 2023-12-14 15:37 |
| Actualizado | 2023-12-18 14:13 |
| Etiquetas | ninguna |
| Jira | [PED-334](https://bluinc.atlassian.net/browse/PED-334) |

## Relaciones

- **blocks:** [[PED-298 - API - Feat - Sync Up - Calcular parametros LTV|PED-298]] API - Feat - Sync Up - Calcular parametros LTV

## Descripcion

1. Al consultar la tabla `[NewBytes_DBF].[dbo].[clientesLtv]` utilizando como prueba el cliente `2261` me aparece como que su valor promedio de compra es de 32.25, sin embargo, al consultar de manera aparte los movimientos del cliente, me da un total promedio de 50.551, por lo que no se está calculando correctamente el valor promedio de compra.

[adjunto]
2. Utilizando los mismos datos de prueba, me aparece que la frecuencia de compra del cliente es de 0, sin embargo, puedo observar que se realizaron dos compras en los últimos dos años.

[adjunto]
3. Me pareciera que la operación que se realiza para obtener el LTV es incorrecta debido que al sustituir los números en la fórmula el resultado es otro.

```
LTV = (Valor promedio de compra) X (Frecuencia de Compra) X (Duración De La Relación)
```

```
0 = (32.255400) (0) (13)
```

[adjunto]
