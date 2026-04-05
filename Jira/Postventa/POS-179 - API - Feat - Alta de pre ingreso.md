---
jira_key: "POS-179"
aliases: ["POS-179"]
summary: "API - Feat - Alta de pre ingreso "
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-10-11 11:50"
updated: "2022-10-18 14:12"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-179"
---

# POS-179: API - Feat - Alta de pre ingreso 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-10-11 11:50 |
| Actualizado | 2022-10-18 14:12 |
| Etiquetas | ninguna |
| Jira | [POS-179](https://bluinc.atlassian.net/browse/POS-179) |

## Relaciones

- **Padre:** [[POS-178]] Feat - Crear un pre ingreso manual
- **blocks:** [[POS-180]] APP - Feat - Modal alta de pre ingreso

## Descripcion

```
GET {API_URL}/v1/preAftersales
```

Se trata del recurso necesario para dar de alta un pre ingreso en el caso puntual de que el cliente se ve imposibilitado para hacerlo desde el sitio.

Como tal requiere todos los campos necesarios para crear un preingreso

```
{
  contactNumber: '+54 9 11 30958675'
  clientId: 32423,
  detail: [
    {
    productId: 2345,
    serialNumber: '423423fds3243fsd',
    failTypeId: 3,
    quantity :2,
    failDescription: 'It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English.',
    invoiceNumber: 'A00030048948',
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
        },
]]
    }

  ]
}
```
