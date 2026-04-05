---
jira_key: "COB-554"
aliases: ["COB-554"]
summary: "API - Feat - Mover cheques simultáneamente de una caja a otra caja"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2025-03-11 13:27"
updated: "2025-03-14 05:56"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-554"
---

# COB-554: API - Feat - Mover cheques simultáneamente de una caja a otra caja

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2025-03-11 13:27 |
| Actualizado | 2025-03-14 05:56 |
| Etiquetas | ninguna |
| Jira | [COB-554](https://bluinc.atlassian.net/browse/COB-554) |

## Relaciones

- **Padre:** [[COB-195]] Feat - Pases de cheques

## Descripcion

Tomando como base la tarea [link](https://lioteam.atlassian.net/browse/COB-197) 

se debe completar la implementación que permite el pase simultaneo de cheques entre cajas.



Al realizar pase de cheques de forma simultanea 

Routes/PassesRoute.php

```
$app->post('/checkTrade', CheckTrade::class)->add(PermissionAdminMiddleware::class);
```

Ejemplo de payload:

```
{
   "amount": "39588.55", --> total de todos los cheques
   "comment": "test  3",
   "origin": "CAJA1",
   "destiny": "CAJA3",
   "paymentMethodId": 15,
   "payloadChecks": [ --> multiples id  de cheques
      "330733",
      "330735"
   ]
}
```



Debe quedar registrado en log_operaciones cada cheque y importes por separados.

ej: movimiento de caja. 

[adjunto]


ej: movimiento de pase por ser aceptado.

[adjunto]
