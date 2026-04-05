---
jira_key: "INV-127"
aliases: ["INV-127"]
summary: "API - Feat - Importar catalogo a partir de un archivo xlsx"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-09-12 07:08"
updated: "2024-09-26 02:28"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-127"
---

# INV-127: API - Feat - Importar catalogo a partir de un archivo xlsx

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-09-12 07:08 |
| Actualizado | 2024-09-26 02:28 |
| Etiquetas | ninguna |
| Jira | [INV-127](https://bluinc.atlassian.net/browse/INV-127) |

## Relaciones

- **Padre:** [[INV-125 - Importación de catálogos|INV-125]] Importación de catálogos
- **blocks:** [[INV-128 - APP - Feat - Formulario de carga masiva de productos a través de un archivo|INV-128]] APP - Feat - Formulario de carga masiva de productos a través de un archivo 
- **is blocked by:** [[INV-137 - API - Importar catalogo a partir de un archivo xlsx - Valores no coincidentes|INV-137]] API - Importar catalogo a partir de un archivo xlsx - Valores no coincidentes

## Descripcion

Lo que hace este importador es cargar en la tabla `[NewBytes_DBF].[dbo].[articulo]` los productos que provienen del mapeo

```
POST {API_URL}/import/xlsx
```

```
{
  "file": "excel_file.xlsx",
  "preview": "true",
  "currency": 1, //dolares o pesos, esto se usa para poder guardarlo en dolares de la forma correcta (si viene ne pesos, dividimos por el oficial)
  "distributor" 4, //Id del distribuidor [NewBytes_DBF].[dbo].[articulo].id_distribuidora
  "mapping": {
    "A": "mainImage",
    "B": "sku",
    "C": "title",
    "D": "brand",
    "E": "category",
    "F": "price",
    "G": "stock",
    "H": "iva",
    "I": "officialSiteUrl"
  }
}
```

**Si preview es TRUE**, no proceso el archivo, sino que solo extraigo los datos para que el front muestre una preview de las primeras 10 lineas para saber si están bien mapeadas las columnas

```
{
  "import_id": "12345",
  "status": "preview",
  "currency": "USD", 
  "distributorId": 4,
  "preview": [
    {
      "mainImage": "https://example.com/image1.jpg",
      "sku": "SKU12345",
      "title": "Product 1",
      "brand": "Brand A",
      "category": "Electronics",
      "price": 120.50,  // Se asume que la moneda es USD
      "stock": 25,
      "iva": 21.00,
      "officialSiteUrl": "https://example.com/product1"
    },
    {
      "mainImage": "https://example.com/image2.jpg",
      "sku": "SKU12346",
      "title": "Product 2",
      "brand": "Brand B",
      "category": "Appliances",
      "price": 89.99,   // Precio en USD después de conversión
      "stock": 10,
      "iva": 21.00,
      "officialSiteUrl": "https://example.com/product2"
    },
```

**Si preview  esta en FALSE o vacio proceso el archivo y guardo los datos en el sistema**

```
{
  "succces": true,
  "import_id": "12345",
  "message": "Se proceso de manera correcta",
  "problemas":[
    /// Aca podes reportar problemas de formato o items que no pudiste importar, etc
  ]
}
```

Es IMPORTANTE tener en cuenta que no se puede poner el mismo SKU para el mismo ID_Distribuidora, osea solo puede darse de alta un SKU para cada distribuidora

El stock, solo se guarda en `nstock_virtual` y en ninguna de las otras columnas
