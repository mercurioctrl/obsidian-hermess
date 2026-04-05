---
jira_key: "NBWEB-201"
summary: "FIX - Pre ingreso de postventa - Se agregan parametros al request"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-05-24 10:55"
updated: "2022-06-26 21:27"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-201"
---

# NBWEB-201: FIX - Pre ingreso de postventa - Se agregan parametros al request

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-05-24 10:55 |
| Actualizado | 2022-06-26 21:27 |
| Etiquetas | ninguna |
| Jira | [NBWEB-201](https://bluinc.atlassian.net/browse/NBWEB-201) |

## Descripción

Modificar

```
POST {{API_URL}}/v1/postventa
```

Agregamos un parámetros que es un array de seriales

llamado secondarySerials

```json
[
        {
          serialNumber: 'WE4791013661',
          serialDetail: {
            clientId: '016050',
            saleDate: '2015-12-24 09:16:27.090',
            warranty: 1,
            elapsedMonths: '77',
            referSale: '0002-00296114',
            productId: '1945',
            productDescription: 'TECLADO_GENIUS_06B',
            purchasePrice: '5.71012800000',
            currentWarranty: false,
            buyer: false,
          },
        },
]
```

quedando configurado el recurso de la siguiente manera

```json
{
  contactNumber: '+54 9 11 30958675' 
  detail: [
    {
    productId: 2345,
    serialNumber: '423423fds3243fsd',
    failTypeId: 3,
    quantity :2,
    failDescription: 'It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English.',
    invoiceNumber: 'A00030048948',
    img: [ {
        "id": "257659",
        "filename": "eb4fc89a3b443ae8ff7a622d14a3428b.png",
        "url": "http://static.nb.com.ar/img/eb4fc89a3b443ae8ff7a622d14a3428b.png"
    },
    {
        "id": "257671",
        "filename": "eb81cc64c07459ee95474a9f4a4a4a0c.png",
        "url": "http://static.nb.com.ar/img/eb81cc64c07459ee95474a9f4a4a4a0c.png"
    }
    ,
    secondarySerial : [
        {
          serialNumber: 'WE4791013661',
          serialDetail: {
            clientId: '016050',
            saleDate: '2015-12-24 09:16:27.090',
            warranty: 1,
            elapsedMonths: '77',
            referSale: '0002-00296114',
            productId: '1945',
            productDescription: 'TECLADO_GENIUS_06B',
            purchasePrice: '5.71012800000',
            currentWarranty: false,
            buyer: false,
          },
          {
          serialNumber: 'WE4791013662',
          serialDetail: {
            clientId: '016050',
            saleDate: '2015-12-24 09:16:27.090',
            warranty: 1,
            elapsedMonths: '77',
            referSale: '0002-00296114',
            productId: '1945',
            productDescription: 'TECLADO_GENIUS_06B',
            purchasePrice: '5.71012800000',
            currentWarranty: false,
            buyer: false,
          },
          {
          serialNumber: 'WE4791013663',
          serialDetail: {
            clientId: '016050',
            saleDate: '2015-12-24 09:16:27.090',
            warranty: 1,
            elapsedMonths: '77',
            referSale: '0002-00296114',
            productId: '1945',
            productDescription: 'TECLADO_GENIUS_06B',
            purchasePrice: '5.71012800000',
            currentWarranty: false,
            buyer: false,
          },
        },
]]
    }

  ]
}
```
