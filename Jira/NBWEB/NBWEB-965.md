---
jira_key: "NBWEB-965"
summary: "APP - Feat - Mostrar / Ocultar en el sitio la cotizacion del momento segun corresponda"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-04-16 14:28"
updated: "2025-04-21 10:40"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-965"
---

# NBWEB-965: APP - Feat - Mostrar / Ocultar en el sitio la cotizacion del momento segun corresponda

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-04-16 14:28 |
| Actualizado | 2025-04-21 10:40 |
| Etiquetas | ninguna |
| Jira | [NBWEB-965](https://bluinc.atlassian.net/browse/NBWEB-965) |

## Descripción

**Título:** Mostrar u ocultar cotización según respuesta del recurso `/v1/currencyQuote`

**Resumen:**
Se deberá consumir el recurso `GET /v1/currencyQuote` desde el frontend para mostrar, si corresponde, la cotización del dólar en el sitio.

**Detalles:**

- **Endpoint:** `GET {API_URL}/v1/currencyQuote`


- **Respuesta esperada:**

```
{   
"currencyQuote": 1235.56
} 
```



o, en caso de que no deba mostrarse:

```
{   
"currencyQuote": null
 }
```


Se debe ubicar en algún lugar de esta área


[attachment]




- **Comportamiento esperado:**

- Si el campo `currencyQuote` viene con un número válido, se muestra la cotización en el sitio en el lugar correspondiente.


- Si el campo `currencyQuote` es `null`, no se debe renderizar ningún elemento visual relacionado a la cotización.





**Notas:**

- Esta lógica permitirá que el backend pueda habilitar o deshabilitar dinámicamente la visibilidad de la cotización según el parámetro `quoteSiteShow`.


- No es necesario agregar controles manuales en el frontend, solo se debe responder a la existencia o ausencia del valor.
