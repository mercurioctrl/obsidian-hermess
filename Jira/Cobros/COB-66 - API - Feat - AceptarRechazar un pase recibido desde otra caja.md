---
jira_key: "COB-66"
aliases: ["COB-66"]
summary: "API - Feat - Aceptar/Rechazar un pase recibido desde otra caja"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-08-26 10:25"
updated: "2022-10-20 17:11"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-66"
---

# COB-66: API - Feat - Aceptar/Rechazar un pase recibido desde otra caja

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-08-26 10:25 |
| Actualizado | 2022-10-20 17:11 |
| Etiquetas | ninguna |
| Jira | [COB-66](https://bluinc.atlassian.net/browse/COB-66) |

## Relaciones

- **Padre:** [[COB-12 - Feat - Procesar pases de caja|COB-12]] Feat - Procesar pases de caja
- **blocks:** [[COB-88 - APP - Refactor - Agregar checkboxes|COB-88]] APP - Refactor - Agregar checkboxes

## Descripcion

Esta accion puede ser masiva. Osea aplicarse a varios identificadores de pase… 



Esta acción se trata sobre aceptar o rechazar un pase, osea que en principio se debe chequear que la cuenta que esta aceptando o rechazando sea efectivamente la destinataria del mismo.

Por otra parte, no se debe poder pasar estados para atras. Es decir un pase nace Abierto (status 1), y puede pasar a aceptado (2) o rechazaro (3) y asi.

El recurso sera el siguiente

```
PATCH {{API_URL}}/v1/passes/trade/
```

Payload

```
[{
  passesId:234,
  statusId:2
},
{
  passesId:233,
  statusId:2
},
{
  passesId:232,
  statusId:2
}]
```

Consultame sobre esto y lo vemos bien
