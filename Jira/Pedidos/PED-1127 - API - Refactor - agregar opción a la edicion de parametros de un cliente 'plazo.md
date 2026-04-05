---
jira_key: "PED-1127"
aliases: ["PED-1127"]
summary: "API - Refactor - agregar opción a la edicion de parametros de un cliente 'plazo de pago'"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Marbe Moreno"
created: "2025-10-01 17:31"
updated: "2025-11-10 11:46"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1127"
---

# PED-1127: API - Refactor - agregar opción a la edicion de parametros de un cliente 'plazo de pago'

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Marbe Moreno |
| Creado | 2025-10-01 17:31 |
| Actualizado | 2025-11-10 11:46 |
| Etiquetas | ninguna |
| Jira | [PED-1127](https://bluinc.atlassian.net/browse/PED-1127) |

## Relaciones

- **Padre:** [[PED-16 - Listar clientes|PED-16]] Listar clientes
- **action item from:** [[PED-1128 - APP - MVP - Refactor - agregar opción a la edicion de parametros de un cliente|PED-1128]] APP - MVP - Refactor - agregar opción a la edicion de parametros de un cliente 'plazo de pago'
- **relates to:** [[PED-1169 - APP - MVP - Feat - Edición de parámetros del cliente|PED-1169]] APP - MVP - Feat - Edición de parámetros del cliente

## Descripcion

El refactor actual se realizo sobre la nueva feature:

```
PATCH {API_URL}/v1/clients/{clientId}/params
```

---

Agregaremos un nuevo parámetro tanto para leer como para editar el recurso `clients`

```
GET {API_URL}/v1/clients/{clientId}
```

```
{
    "clientId": 93384,
    "email": "lukas.r.0092@gmail.com",
    "provinceId": 0,
    "localityId": 0,
    "address": "Pedernera 2157  ",
    "cuil": "31089716",
    "clientName": "Andrea Borello",
    "commercialName": "Andrea Borello",
    "postalCode": "1824",
    "telephone": "1178877349",
    "telephone2": "",
    "typeDocument": 4,
    "category": 3,
    "whaPhone": "",
    "companyCode": 4,
    "profile": 1,
    "currencyId": 1,
    "salespersonId": 100,
    "specialPrice": 0
    "paymentTerms": 15 //--> Nuevo parametro Cantidad de dias (valor entero)
}
```

```
PATCH {API_URL}/v1/clients/{clientId}
```

```
{
    "paymentTerms": 15 //--> Nuevo parametro Cantidad de dias (valor entero)
}
```
