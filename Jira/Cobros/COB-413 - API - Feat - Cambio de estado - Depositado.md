---
jira_key: "COB-413"
aliases: ["COB-413"]
summary: "API - Feat - Cambio de estado -> Depositado"
status: "Gamma"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-04-24 12:08"
updated: "2023-04-28 07:44"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-413"
---

# COB-413: API - Feat - Cambio de estado -> Depositado

| Campo | Valor |
|-------|-------|
| Estado | Gamma (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-04-24 12:08 |
| Actualizado | 2023-04-28 07:44 |
| Etiquetas | ninguna |
| Jira | [COB-413](https://bluinc.atlassian.net/browse/COB-413) |

## Relaciones

- **Padre:** [[COB-183 - Feat - Listar cheques|COB-183]] Feat - Listar cheques

## Descripcion

En esta historia agregaremos la logica detras del chueque al cambiar el estado [link](https://lioteam.atlassian.net/browse/COB-407) . 

```
PATCH {API_URL}/v1/checks/
```

Cuando cambia de “Recibido” de “Depositado” es necesario hacer que el monto de los cheques, pase a la entidad bancaria correspondiente y figure entre los movimientos como un deposito

Para esto se introdujo un selector dentro del modal

[adjunto]
Que genera la siguiente carga util

```
[
   {
      "checkId":328542,
      "newStatus":2,
      "bankId":72
   },
   {
      "checkId":328541,
      "newStatus":2,
      "bankId":72
   }
]
```

Por lo tanto, introducimos el nuevo parametro `bankId` que nos permite **donde imputaremos la sumatoria total de los cheques que estamos cambiando de estado.**

Con eso podemos escribir la tabla `[NEW_BYTES].[dbo].[BA_BP_MOVIMIENTOS_ENTRADAS]` para agregar el dinero a la cuenta bancaria. Se debe observar que en la tabla , ya existen columnas tipo “`ME_Numero_Cheque`" que hacen referencia a los chques y deben incorporarse (vver casos viejos)

Hay mas informacion sobre como se leen y escriben los bancos aca:[link](https://lioteam.atlassian.net/browse/COB-208)
