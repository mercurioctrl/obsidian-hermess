---
jira_key: "INV-174"
aliases: ["INV-174"]
summary: "API - Refactor - Incorporar parámetro \"obligatorio\" para un atributo según la categoría de NB (Capa 1) si corresponde"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-01-20 12:54"
updated: "2025-01-29 11:06"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-174"
---

# INV-174: API - Refactor - Incorporar parámetro "obligatorio" para un atributo según la categoría de NB (Capa 1) si corresponde

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-01-20 12:54 |
| Actualizado | 2025-01-29 11:06 |
| Etiquetas | ninguna |
| Jira | [INV-174](https://bluinc.atlassian.net/browse/INV-174) |

## Relaciones

- **Padre:** [[INV-27 - Productos|INV-27]] Productos
- **has action item:** [[INV-176 - APP - Refactor- Marcar atributos como obligatorios|INV-176]] APP - Refactor- Marcar atributos como obligatorios 

## Descripcion

Basándonos en lo que intentamos hacer en [link](https://lioteam.atlassian.net/browse/INV-147)  haremos el cambio para poder hacerlo referenciado a la CAPA1 este era el espíritu original de la feature, pero por un mal entendido se hizo directo desde libreopcion.

Para esto usaremos la columna `categoriaIdNb` en lugar de `categoriaId` para poder referenciarlo directamente a CAPA1

De esta forma podemos ver un ejemplo de uso donde por ejemplo al abrir un producto ejemplo como ser “119740 - MOTHER ASUS (LGA1700) PRIME H610M-K D4 CSM” que pertenece a la categoría “14 - MOTHER ASUS“  veríamos en la tabla `[PRODUCTOS].[dbo].[componentsAttributes]` algo como lo siguiente

| `categoriaId` | `atributo` | `categoriaIdNb` |
| --- | --- | --- |
| 12 | Socket | 14 |
| 12 | Ranuras RAM | 14 |
| 12 | Tipo de RAM | 14 |
| 12 | Factor de forma | 14 |

```
GET {API_URL}/item/119740
```

Debiera devolver algo como esto

```
[
    {
        "title": "MOTHER ASUS (LGA1700) PRIME H610M-K D4 CSM",
        "sku": "PRIME H610M-K D4-CSM",
        "id": 119740,
        "category": "MOTHER ASUS                   ",
        "categoryId": 14,
        "brand": 65,
        "brandId": "ASUS",
        "brandImage": "https://static.nb.com.ar/img/69acebab5be930f60c54ba745b9ff4a6.jpg",
        "mainImage": "http://static.nb.com.ar/img/83c6af61dd41b26bb20476caef7318b5.jpg",
        "stock": 44.0,
        "warranty": "12 meses",
        "description": null,
        "attributes": [
            {
                "name": "Socket",
                "value": "1151",
                "id": 798990,
                "required": 1 << -- Viene obligatorio
            },
            {
                "name": "Ranuras RAM",
                "value": 2,
                "id": 798989,
                "required": 1 << -- Viene obligatorio
            },
            {
                "name": "Tipo de RAM",
                "value": "DDR5",
                "id": 798991,
                "required": 1 << -- Viene obligatorio
            },
            {
                "name": "Factor de forma",
                "value": "",
                "id": 798988,
                "required": 1 << -- VACIO porque y no esta, Viene obligatorio <----
            },
            {
                "name": "Ranuras de expansión",
                "value": "1 x pcie 3.0 x1 slot,1 x pcie 4.0 x16 slot",
                "id": 798992,
                "required": 0
            },
            {
                "name": "Aplicaciones",
                "value": "PC",
                "id": 798986,
                "required": 0
            },
            {
                "name": "Marca",
                "value": "Asus",
                "id": 798987,
                "required": 0
            },
            {
                "name": "Línea",
                "value": "Prime",
                "id": 798993,
                "required": 0
            },
            {
                "name": "Socket",
                "value": "1700",
                "id": 798996,
                "required": 0
            },
            {
                "name": "Procesadores soportados",
                "value": "12va Gen Intel Core Pentium Gold Celeron",
                "id": 798997,
                "required": 0
            },
            {
                "name": "Formato de memoria RAM",
                "value": "DIMM",
                "id": 798998,
                "required": 0
            },
            {
                "name": "Módulos de memoria RAM",
                "value": "2",
                "id": 798999,
                "required": 0
            },
            {
                "name": "Modelo",
                "value": "H610M-K D4",
                "id": 798995,
                "required": 0
            },
            {
                "name": "Tipo de memoria RAM",
                "value": "DDR4",
                "id": 799000,
                "required": 0
            },
            {
                "name": "Capacidad máxima soportada de la memoria RAM",
                "value": "64 GB",
                "id": 798994,
                "required": 0
            }
        ],
        "images": [
            {
                "checksum": "http://static.nb.com.ar/img/83c6af61dd41b26bb20476caef7318b5.jpg",
                "order": 0
            },
            {
                "checksum": "http://static.nb.com.ar/img/a20e7bbe8364454f3141f7db5205638a.jpg",
                "order": 1
            },
            {
                "checksum": "http://static.nb.com.ar/img/3b993bfbbbd5d368e901d17cd2c3c211.jpg",
                "order": 2
            },
            {
                "checksum": "http://static.nb.com.ar/img/810a5c86e1777b80ee38fa9499ea343c.jpg",
                "order": 3
            },
            {
                "checksum": "http://static.nb.com.ar/img/446dc8f4dccf94884c0f59f6df1e2c96.jpg",
                "order": 4
            },
            {
                "checksum": "http://static.nb.com.ar/img/b7868d90dfc14372929497e45f822dbd.jpg",
                "order": 5
            }
        ],
        "ean": "4711081565529",
        "upc": null,
        "videoId": null,
        "companyCode": 4,
        "companyName": "NB DISTRIBUIDORA MAYORISTA SRL",
        "officialSiteUrl": "https://www.asus.com/latin/motherboards-components/motherboards/prime/prime-h610m-k-d4/techspec/",
        "sindicateContentImg": "https://i.imgur.com/E1V3ASr.jpeg",
        "iva": 10.5,
        "notSerializable": 0,
        "iaDescription": "¡Claro! El MOTHER ASUS (LGA1700) PRIME H610M-K D4 CSM es una placa base de alta calidad diseñada para ofrecer un rendimiento confiable y estable en tu sistema. Aquí tienes una descripción detallada de sus características y beneficios:\n\n1. **Compatibilidad LGA1700**: Esta placa base es compatible con los procesadores Intel de 12ª generación, lo que te permite disfrutar de un rendimiento potente y eficiente.\n\n2. **Diseño robusto**: El diseño de alta calidad de la placa base ASUS Prime H610M-K D4 CSM garantiza una durabilidad excepcional y una larga vida útil, lo que la convierte en una excelente inversión a largo plazo.\n\n3. **Soporte para memoria DDR4**: Con soporte para memoria DDR4, esta placa base te permite disfrutar de una velocidad de transferencia de datos más rápida y una mayor capacidad de memoria para tus aplicaciones y juegos.\n\n4. **Conectividad completa**: Con múltiples puertos USB, puertos SATA y ranuras PCIe, esta placa base te ofrece una conectividad completa para tus periféricos y dispositivos de almacenamiento.\n\n5. **Tecnología ASUS de última generación**: Equipada con tecnologías exclusivas de ASUS como ASUS OptiMem y ASUS Fan Xpert, esta placa base garantiza un rendimiento optimizado y una refrigeración eficiente en todo momento.\n\nEn resumen, el MOTHER ASUS (LGA1700) PRIME H610M-K D4 CSM es una excelente opción para aquellos que buscan una placa base fiable, duradera y con un rendimiento excepcional para sus sistemas de computación. ¡No dudes en adquirirla para potenciar tu experiencia informática!",
        "national": 0
    }
]
```

Ver el caso que dice `<< -- VACIO porque y no esta, Viene obligatorio <----`
