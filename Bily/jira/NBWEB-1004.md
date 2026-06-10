---
jira_key: NBWEB-1004
status: Code Review
assignee: Guillermo Avila
assignee_email: null
reporter: Guillermo Avila
priority: Medium
issuetype: Subtarea
project: NBWEB
updated: "2025-10-20T10:34:03.001-0300"
created: "2025-10-08T18:46:46.936-0300"
url: "https://bluinc.atlassian.net/browse/NBWEB-1004"
tags: [jira, NBWEB, code-review]
sprint: Sprint 3 Q3 1/7
---

# NBWEB-1004 · API - Refactor - Recurso para leer precios -> Actualizar objeto de respuesta

[NBWEB-1004 en Jira](https://bluinc.atlassian.net/browse/NBWEB-1004)

## Descripción

Un cliente reportó que el recurso de precios no le está mostrando el valor correcto. Al analizar el caso, detectamos que el recurso que utiliza es una versión antigua, lo que ocasiona discrepancias en la información recibida.

Para resolver esta situación, realizaremos una refactorización al recurso `/v1/prices`, con el objetivo de actualizarlo y mejorar su funcionalidad. Entre los cambios contemplados se encuentran:

- Eliminación de advertencias existentes.
- Inclusión de nuevas claves en el objeto de respuesta, manteniendo la estructura original y asegurando compatibilidad con las implementaciones actuales.



```
{{API_URL}}/v1/prices
```

```
{
    "id": 2062,
    "sku": "SMWVB",
    "currencyQuote": 1310,
    "value": 128.36127,        
    "iva": 21,
    "internalTax": 0, <------------------------------ **SE AGREGA**
    "percepcion": null, <---------------------------- **SE AGREGA**            
    "utility": null, <------------------------------- **SE AGREGA**        
    "finalPrice": 155.3171367,              
    "finalPriceWithUtility": 155.31714, <------------ **SE AGREGA**        
}
```

## Comentarios (2)

### @Emanuel Jesus Ferreyra — 2025-10-17 16:49:08

@@Guillermo Avila  lo veo bien 👌 , creo que solo agregaria un comentario en el PR de las variables de entorno COMPANY_CODES y la creacion del procedimiento almacenado 'NewBytes_DBF.dbo.GetItemsByPrices'. para cuando se pase a Prod, se tenga encuenta estos ajustes.

### @Guillermo Avila — 2025-10-20 10:34:03

De acuerdo Ema, así lo haré, ¡muchas gracias!

---
_Sincronizado por jira-sidecar el 2026-06-07 22:27:37 UTC._
