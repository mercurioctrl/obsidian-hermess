---
jira_key: "PED-45"
summary: "API - Feat - Integración con Padrones de AFIP por documento de cliente"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-08-22 10:19"
updated: "2023-09-11 09:34"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-45"
---

# PED-45: API - Feat - Integración con Padrones de AFIP por documento de cliente

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-08-22 10:19 |
| Actualizado | 2023-09-11 09:34 |
| Etiquetas | ninguna |
| Jira | [PED-45](https://bluinc.atlassian.net/browse/PED-45) |

## Descripción

Según el recurso [link](https://lioteam.atlassian.net/browse/PED-50) 

Se debe formalizar un objeto compatible según los datos que se obtienen directamente del padrón de AFIP para completar la informacion de un cliente que estamos dando de alta o editando.

Para esto debemos buscar que parámetros son el equivalente de nuestros parámetros internos (Si queres avísame y te doy una mano con esto para saber cual es cual o como se hacen los switches)

```
GET {API_URL}/v1/clients/afip/{taxId}
```

```
{
    "clientName": "COLONEL CLAUDIO LIVIO",
    "commercialName": "Mercurio",
    "clientAddress": "ANDRES FERREYRA 2685",
    "clientCity": "",
    "cityCode": "3678",
    "postalCode": "1678",
    "taxId": "20-13131339-0",
    "contactName": "Claudio ",
    "invoiceSeries": "A",
    "taxId": "6",
    "addressDirection": "0",
    "email": "mercurioweb@yahoo.com.ar",
    "postalCodeId": null,
    "countryId": "7",
    "cityId": "3681",
    "provinceId": "2",
}
```
