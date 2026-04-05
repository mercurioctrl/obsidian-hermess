---
jira_key: "NBWEB-955"
aliases: ["NBWEB-955"]
summary: "API - Refactor - Desdoblar cotización libre opción"
status: "Finalizada"
type: "Tarea"
priority: "Highest"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-03-07 11:59"
updated: "2025-03-10 19:31"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-955"
---

# NBWEB-955: API - Refactor - Desdoblar cotización libre opción

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Highest |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-03-07 11:59 |
| Actualizado | 2025-03-10 19:31 |
| Etiquetas | ninguna |
| Jira | [NBWEB-955](https://bluinc.atlassian.net/browse/NBWEB-955) |

## Relaciones

- **Padre:** [[NBWEB-599]] CMS

## Descripcion

Desdoblaremos la cotización de libreopcion para poder hacer descuentos sobre la cotización, pero sin nunca perder la cotización original en la pantalla. 
Para esto agregaremos un nuevo parametro en 
`[NEW_BYTES].[dbo].[MS_COTIZACIONES].COTIZACION_SHOW_LO`la cual usaremos para guardar la cotizacion y mostrarla en los siguientes recursos.

```
GET /v1/cms/currencyQuote
```

Pasaría a traer `COTIZACION_SHOW_LO` en vez de `COTIZACION` solo para el caso con `ID=3`
y al hacer la modificacion de PESOSLO (id=3) modificaremos tambien `COTIZACION_SHOW_LO` y luego correremos el mismo el descuento como lo hacemos en [link](https://lioteam.atlassian.net/browse/NBWEB-954)  para modificar la cotización real COTIZACION (esto solo se hace en `id=3`)

```
PATCH /v1/cms/currencyQuote
```

```
   {
        "id": 3,
        "description": "PESOSLO",
        "currency": 1034.99,
        "CurrencyQuoteMax": 9999,
        ....
```

```
Una vez actualizado, corremos:

UPDATE [NEW_BYTES].[dbo].[MS_COTIZACIONES]
SET COTIZACION = COTIZACION_SHOW_LO * (100 - (SELECT quoteDiscountLo FROM [NEW_BYTES].[dbo].[PV_PARAMETROS_VARIOS]))
WHERE id = 3;
```





Actuzalición:

El calculo debe ser el siguente:

```
select COTIZACION = COTIZACION_SHOW_LO -  (  (SELECT quoteDiscountLo FROM [NEW_BYTES].[dbo].[PV_PARAMETROS_VARIOS]))
from [NEW_BYTES].[dbo].[MS_COTIZACIONES]
WHERE id = 3; --> Libre opcion unicamente
```

Siendo un valor nominal, por ejemplo si COTIZACION_SHOW_LO es 1000 (editado)  Y quoteDiscountLo = 5 quedaria COTIZACION = 995
