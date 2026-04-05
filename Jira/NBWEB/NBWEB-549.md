---
jira_key: "NBWEB-549"
summary: "API - Feat - Listar clientes"
status: "Code Review"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-05-29 07:14"
updated: "2023-06-07 11:16"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-549"
---

# NBWEB-549: API - Feat - Listar clientes

| Campo | Valor |
|-------|-------|
| Estado | Code Review (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-05-29 07:14 |
| Actualizado | 2023-06-07 11:16 |
| Etiquetas | ninguna |
| Jira | [NBWEB-549](https://bluinc.atlassian.net/browse/NBWEB-549) |

## Descripción

Se debe construir el siguiente recurso paginable (usando offset y limit como hicimos en recursos anteriores)

```
GET {API_URL}/v1/cms/customers?id={clientId}&clientName={clientName}
```

```
[
  {
    "id": 77160,
    "clientName": "ECHANIZ HERMANOS SOCIEDAD ANONIMA",
    "clientComercialName": "Echaniz hnos",
    "discount": 1.0,
    "priceList": 1.0,
    "defaultCurrency": 1,
    "ccoddiv": "DOL",
    "brokerage": 0,
    "userBlack": null,
    "userBlackpercentage": 5000000.0,
    "profile": 1,
    "company": 4,
    "sellerId": 41,
    "lastNameSeller": "Sheridaim",
    "sellerName": "Natalia"
  },
  {
    "id": 77159,
    "clientName": "TEBES ANDRES SEBASTIAN",
    "clientComercialName": "Servi.com",
    "discount": 1.0,
    "priceList": 1.0,
    "defaultCurrency": 1,
    "ccoddiv": "DOL",
    "brokerage": 0,
    "userBlack": null,
    "userBlackpercentage": 5000000.0,
    "profile": 1,
    "company": 4,
    "sellerId": 41,
    "lastNameSeller": "Sheridaim",
    "sellerName": "Natalia"
  },]
```

Repositorio de ejemplo:

```
        SELECT
        top(10)
        ID_CLIENTE as id,
        cnomcli as clientName,
        cnomcom as clientComercialName,
        ndto as discount,
        ntarifapp as priceList, 
        ID_DIVISA as defaultCurrency,
        ccoddiv,
        intermediacion as brokerage,
        usuarioBlack as userBlack,
        superOfertaDto as userBlackpercentage,
        perfil as profile,
        CODEMP as company,
        clientes.ID_VENDEDOR as sellerId,
        agentes.cnbrage as lastNameSeller,
        agentes.capeage as sellerName
        FROM [NewBytes_DBF].[dbo].[clientes]
        LEFT JOIN NB_WEB.dbo.usuarios_nb ON clientes.ID_CLIENTE = usuarios_nb.codigoFP
        LEFT JOIN NewBytes_DBF.dbo.agentes ON agentes.ccodage = clientes.ccodage
        where subCuenta IS NULL
        order by ccodcli desc
```

- Esta lista debe poder ordenarse por ID de cliente, descendente a menos que se indique lo contrario (tal vez lo piden mas adelante)


- Se debe poder filtrar por nombre de cliente según el parámetro `clientName` (debe buscar tanto en `clientName` como en `clientComercialName`)


- Se debe poder filtrar por id de cliente según el parámetro `clientId`


- Se debe paginar de a 30 resultados inicialmente, a menos que se especifique lo contrario
