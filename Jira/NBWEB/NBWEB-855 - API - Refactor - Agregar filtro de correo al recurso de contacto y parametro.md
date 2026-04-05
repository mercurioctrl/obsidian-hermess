---
jira_key: "NBWEB-855"
aliases: ["NBWEB-855"]
summary: "API - Refactor - Agregar filtro de correo al recurso de contacto y parametro para visualizar la vCard aunque no se muestre en la seccion de contacto"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-08-29 08:06"
updated: "2024-10-03 10:33"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-855"
---

# NBWEB-855: API - Refactor - Agregar filtro de correo al recurso de contacto y parametro para visualizar la vCard aunque no se muestre en la seccion de contacto

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-08-29 08:06 |
| Actualizado | 2024-10-03 10:33 |
| Etiquetas | ninguna |
| Jira | [NBWEB-855](https://bluinc.atlassian.net/browse/NBWEB-855) |

## Relaciones

- **Padre:** [[NBWEB-498 - Oportunidades de mejora|NBWEB-498]] Oportunidades de mejora
- **has action item:** [[NBWEB-892 - APP - Refactor - Cambiaremos el recurso que lee las vCard para filtrar|NBWEB-892]] APP - Refactor - Cambiaremos el recurso que lee las vCard para filtrar especificamente por el email deseado en lugar de traer todo el repo (esto ademas nos permite obtener aquellos que no figuran en contactos)

## Descripcion

Refactorizaremos el recurso 

```
GET {API_URL}/v1/contact/agents
```

para agregar un recurso de filtrado

```
GET {API_URL}/v1/contact/agents?email=daltamiranda@nb.com.ar
```

```
    {
        "roleAgent": "Gerente",
        "whatsappAgent": "(+54911) 7082-0099",
        "phoneAgent": "(5411) 4011-8813",
        "nameAgent": "Dario Altamiranda",
        "emailAgent": "daltamiranda@nb.com.ar"
    },
```

Ademas agregaremos una columna a la tabla `[NewBytes_DBF].[dbo].[agentes]` el parámetro `vCard (true/false)`

De esta forma podremos decir que si usamos el filtro `email=daltamiranda@nb.com.ar`

No correremos la limitación `[NewBytes_DBF].[dbo].[agentes].sitio=1` que sirve solo para saber que se muestra en el sitio en la sección  [link](https://www.nb.com.ar/contacto)  

Y podríamos obtener a través del enlace de vCard [link](https://www.nb.com.ar/vcard/aaltamiranda@nb.com.ar)  todos aquellos que tienen `vCard` activado aunque no tengan  `sitio` activado.

Sitio solo sirve para saber cuales tengo que mostrar en el sitio cuando no le paso un filtro especifico

```
GET {API_URL}/v1/contact/agents
```
