---
jira_key: "NBWEB-110"
aliases: ["NBWEB-110"]
summary: "APP - Maquetado y desarrollo Postventa"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2022-04-11 13:48"
updated: "2022-06-26 21:24"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-110"
---

# NBWEB-110: APP - Maquetado y desarrollo Postventa

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2022-04-11 13:48 |
| Actualizado | 2022-06-26 21:24 |
| Etiquetas | ninguna |
| Jira | [NBWEB-110](https://bluinc.atlassian.net/browse/NBWEB-110) |

## Relaciones

- **Padre:** [[NBWEB-99 - API - Precarga postventa|NBWEB-99]] API - Precarga postventa
- **relates to:** [[NBWEB-100 - API - Buscar por serial para formulario de postventa|NBWEB-100]] API - Buscar por serial para formulario de postventa
- **relates to:** [[NBWEB-104 - API - Pre ingreso de postventa|NBWEB-104]] API - Pre ingreso de postventa
- **relates to:** [[NBWEB-108 - Carga de imagenes|NBWEB-108]] Carga de imagenes
- **blocks:** [[NBWEB-193 - APP - Agregar un suggest box con description de producto al formulario de alta|NBWEB-193]] APP - Agregar un suggest box  con description de producto al formulario de alta de post venta
- **relates to:** [[NBWEB-201 - FIX - Pre ingreso de postventa - Se agregan parametros al request|NBWEB-201]] FIX - Pre ingreso de postventa - Se agregan parametros al request

## Descripcion

Haciendo uso de los recursos de la API maquetar y desarrollar el formulario de ingreso de postventa

```
POST {{API_URL}}/v1/postventa/image
```

Retorna

```json
{ 
"id":"257638", //id de la imagen en el servidor de imagenes 
"filename":"dbe70dfcf6c29852ccab46901d912e38.png", //nombre de la imagen en el servidor de imagenes 
"url":"http:\/\/static.nb.com.ar\/img\/dbe70dfcf6c29852ccab46901d912e38.png" //ruta completa de la imagen 
}
```

---

Para obtener y validar el serial

```
GET {{API_URL}}/v1/postventa/serial/{serial}
```

Retorna:

```
{ 
 clientId: 2, 
 saleDate: '22-12-2021 00:00',
 warranty: 36, //son meses totales de la garantia 
 elapsedMonths: 9, meses transcurridos desde la compra 
 referSale: '0002-32432433', numero de pedido de la compra 
 productoId: 2412, 
 productDescription: 'Descripcion del producto', 
 purchasePrice : 455,4, // preci de compra 
 currentWarranty: true, // si la garantia aun esta vigente 
 buyer:true //en caso de que la cuenta del cliente sea la misma que lo compro 
}
```

---

Para enviar la informacion del formulario completa

```
POST {{API_URL}}/v1/postventa
```

**Request:**

```
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
    img:[{
        "id": "257659",
        "filename": "eb4fc89a3b443ae8ff7a622d14a3428b.png",
        "url": "http://static.nb.com.ar/img/eb4fc89a3b443ae8ff7a622d14a3428b.png"
    },
    {
        "id": "257671",
        "filename": "eb81cc64c07459ee95474a9f4a4a4a0c.png",
        "url": "http://static.nb.com.ar/img/eb81cc64c07459ee95474a9f4a4a4a0c.png"}]
    
    },
       {
    productId: 2345,
    serialNumber: '423423fds3243fsd',
    failTypeId: 3,
    quantity :2,
    failDescription: 'It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English.',
    invoiceNumber: 'A00030048948',
    img: null
    
    }
  ]
}
```

---
