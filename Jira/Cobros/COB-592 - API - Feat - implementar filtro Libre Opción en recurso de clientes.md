---
jira_key: "COB-592"
aliases: ["COB-592"]
summary: "API - Feat - implementar filtro Libre Opción en recurso de clientes"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2025-12-10 09:50"
updated: "2025-12-16 12:01"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-592"
---

# COB-592: API - Feat - implementar filtro Libre Opción en recurso de clientes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2025-12-10 09:50 |
| Actualizado | 2025-12-16 12:01 |
| Etiquetas | ninguna |
| Jira | [COB-592](https://bluinc.atlassian.net/browse/COB-592) |

## Relaciones

- **action item from:** [[SNB-3443]] Agregar Libre Opcion para las empresas en Cobros /deudas

## Descripcion

El sistema debera permitir el filtrado por el nuevo companyCode para Libre Opcion el cual se inicializara desde el .env del microservicio de pedidos. el cual toma como referencia el creado en la tabla FP_Empresas.

```
GET /v1/clients?currentPage=1&companyCode=12
```



Se debe utilizar la variable de entonro `COMPANY_CODE_LO` para que el microservicio sea capaz de resolver la consulta retornando todos los clientes que son de Libre Opción.



Ademas se agrego un nuevo parametro que retorna el id de cliente LO. *(esto es solo como informacion extra)*

```json
{
    "response": [
        {
            "clientId": 91991,
            "clientName": "mauro romo",
            "clientBusinessName": "mauro romo",
            "clientTaxNumber": "42411294",
            "clientPerception": 0,
            "limitCheckBalanceAmount": 0,
            "usedCheckBalanceAmount": 0,
            "limitBalanceAmount": 0,
            "usedBalanceAmount": -1029.61,
            "desactive": false,
            "salespersonName": "Opcion Libre",
            "sellerId": 100,
            "companyCode": 4,
            "clientLo": 309202 ---> NUEVO
        },...
  ]
}
```



El id correspondiente a LO, se puede obtener del recurso:

```
GET /v1/companies?show=1
```

```json
[
  ...,
  {
        "id": 12,
        "description": "Libre Opción"
    }
]
```
