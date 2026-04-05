---
jira_key: "INV-197"
aliases: ["INV-197"]
summary: "API - Refactor - Objeto \"item, leer y escribir atributos de distribuidora"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-09-02 08:27"
updated: "2025-09-03 19:06"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-197"
---

# INV-197: API - Refactor - Objeto "item, leer y escribir atributos de distribuidora

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-09-02 08:27 |
| Actualizado | 2025-09-03 19:06 |
| Etiquetas | ninguna |
| Jira | [INV-197](https://bluinc.atlassian.net/browse/INV-197) |

## Relaciones

- **Padre:** [[INV-27]] Productos
- **action item from:** [[INV-198]] API - Feat - Crear la tabla [NewBytes_DBF].[dbo].[distributor] y exponer repositorio REST con GET/POST/PATCH/DELETE para administrar distribuidoras.
- **has action item:** [[INV-200]] APP - Feat - Cambiar atributo "distributor" y poder filtrarlo en el repositorio "items"

## Descripcion

Luego agregaremos al objeto items la posibilidad de leer el `distributorId` y `distributorDescription` podremos “joinear” la tabla que acabamos de crear con el atributo `[NewBytes_DBF].[dbo].[distributor].id_distribuidora`(`distributorId`)

```
GET {API_URL}/item/{itemId}
```

```
{
    "list": [
        {
            "title": "NOTEBOOK LENOVO V15 AMD R7 7730U 8GB 512GB 15.6 FULL HD",
            "sku": "82YY0029AR",
            "id": 119748,
            "category": "NOTEBOOKS Y PORTATILES",
            "categoryId": 26,
            "brand": "LENOVO                                            ",
            "brandId": 29,
            "brandImage": "https://static.nb.com.ar/img/a46eec123386583d50a8629a8359114e.jpg",
            "mainImage": "http://static.nb.com.ar/img/be0f15fbf2f5b28cb250589f7ff177b0.jpg",
            "stock": 9.0,
            "warranty": "12 meses",
            "description": null,
            "attributes": 18,
            "distributorId": 1,  <<--- Se agrega
            "distributorDescription": "NB"  <<--- Se agrega
            "images": [
                {
                    "checksum": "http://static.nb.com.ar/img/be0f15fbf2f5b28cb250589f7ff177b0.jpg",
                    "order": 0
                },
                {
                    "checksum": "http://static.nb.com.ar/img/c49b77246b8be535915e6aae3af685f1.jpg",
                    "order": 1
                }
            ],
            "ean": null,
            "upc": "198153768561",
            "videoId": null,
            "companyCode": 4,
            "companyName": "NB DISTRIBUIDORA MAYORISTA SRL",
            "officialSiteUrl": null,
            "sindicateContentImg": null,
            "iva": 10.5,
            "notSerializable": 0,
            "iaDescription": "¡Claro! El producto NOT LENOVO AMD R7 7730U 8GB 512GB 15.6 FULL HD con SKU 82YY0029AR es una laptop potente y versátil que ofrece un rendimiento excepcional para tus necesidades diarias de computación. Aquí te dejo una descripción detallada de sus características y beneficios:\n\n- **Procesador AMD R7 7730U:** Equipado con un potente procesador AMD R7 7730U, esta laptop te brinda la velocidad y eficiencia necesarias para realizar múltiples tareas, ejecutar aplicaciones exigentes y disfrutar de un rendimiento fluido en todo momento.\n\n- **Memoria RAM de 8GB:** Con 8GB de memoria RAM, esta laptop garantiza una experiencia multitarea sin problemas, permitiéndote trabajar en varias aplicaciones a la vez sin que la velocidad se vea comprometida.\n\n- **Capacidad de almacenamiento de 512GB:** Con una amplia capacidad de almacenamiento de 512GB, tendrás espacio más que suficiente para guardar tus archivos, documentos, fotos, videos y programas favoritos sin preocuparte por quedarte sin espacio.\n\n- **Pantalla Full HD de 15.6 pulgadas:** Disfruta de una experiencia visual inmersiva con la pantalla Full HD de 15.6 pulgadas, que ofrece colores vibrantes y detalles nítidos para una calidad de imagen excepcional al ver películas, trabajar en diseño gráfico o jugar videojuegos.\n\n- **Diseño elegante y portátil:** Con un diseño elegante y portátil, esta laptop es ideal para llevar contigo a todas partes, ya sea para trabajar desde casa, en la oficina o mientras te desplazas. Su tamaño compacto y peso ligero la hacen perfecta para usuarios en movimiento.\n\nEn resumen, el NOT LENOVO AMD R7 7730U 8GB 512GB 15.6 FULL HD con SKU 82YY0029AR es una excelente opción para aquellos que buscan un equilibrio perfecto entre rendimiento, almacenamiento y portabilidad en una laptop. ¡No dudes en adquirirla y experimentar todo lo que tiene para ofrecer!",
            "national": 1,
            "subheadline": null
        },
        {
            "title": "PROCESADOR AMD (AM4) RYZEN 5 5500X3D",
            "sku": "100-100001504WOF",
            "id": 121137,
            "category": "PROCESADORES",
            "categoryId": 3,
            "brand": "AMD                                               ",
            "brandId": 43,
            "brandImage": "https://static.nb.com.ar/img/266f407b98b3c0721710b6c651d4108f.jpg",
            "mainImage": "http://static.nb.com.ar/img/b6b4bafb9eb0e73e21eca6f84ffc69fe.png",
            "stock": 540.0,
            "warranty": "36 meses",
            "description": null,
            "attributes": 10,
```

### 

```
PATCH {API_URL}/item/{id}
```

**Carga útil:**

```
{
  "distributorId": 3
}
```
