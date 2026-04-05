---
jira_key: "INV-128"
aliases: ["INV-128"]
summary: "APP - Feat - Formulario de carga masiva de productos a través de un archivo "
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2024-09-12 07:29"
updated: "2024-09-21 19:01"
labels: ["esperandoDependencia"]
jira_url: "https://bluinc.atlassian.net/browse/INV-128"
---

# INV-128: APP - Feat - Formulario de carga masiva de productos a través de un archivo 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2024-09-12 07:29 |
| Actualizado | 2024-09-21 19:01 |
| Etiquetas | esperandoDependencia |
| Jira | [INV-128](https://bluinc.atlassian.net/browse/INV-128) |

## Relaciones

- **Padre:** [[INV-125 - Importación de catálogos|INV-125]] Importación de catálogos
- **is blocked by:** [[INV-127 - API - Feat - Importar catalogo a partir de un archivo xlsx|INV-127]] API - Feat - Importar catalogo a partir de un archivo xlsx
- **is blocked by:** [[INV-126 - API - Feat - Obtener esquema estándar del mapeo de columnas|INV-126]] API - Feat - Obtener esquema estándar del mapeo de columnas 
- **blocks:** [[INV-132 - APP - Refactor - Agregar selector de empresa (companyCode) en el modal de|INV-132]] APP - Refactor - Agregar selector de empresa (companyCode) en el modal de importacion
- **relates to:** [[INV-138 - APP - Formulario de carga masiva de productos a través de un archivo -|INV-138]] APP - Formulario de carga masiva de productos a través de un archivo - Sugerencia de mejora al recibir un error en la previsualización 
- **relates to:** [[INV-140 - APP - Formulario de carga masiva de productos a través de un archivo -|INV-140]] APP - Formulario de carga masiva de productos a través de un archivo - Cotización enviada no coincidente

## Descripcion

Agregaremos un accionable para “Importar catalogo” que despliega un modal 

[adjunto]
El modal es similar al siguiente esquema 


```
+---------------------------------------------------+
|           Importar archivo Excel                  |
+---------------------------------------------------+
| [Seleccionar archivo]                             |
+---------------------------------------------------+
|  Columna  |  Campo                                 |
|-----------|----------------------------------------|
|     A     |  [ mainImage        v ]                |
|     B     |  [ sku             v ]                |
|     C     |  [ title           v ]                |
|     D     |  [ brand           v ]                |
|     E     |  [ category        v ]                |
|     F     |  [ price           v ]                |
|     G     |  [ stock           v ]                |
|     H     |  [ iva             v ]                |
|     I     |  [ officialSiteUrl v ]                |
+---------------------------------------------------+
|  Moneda   |  [ USD / ARS       v ]                |
+---------------------------------------------------+
|  Distribuidor |  [ ID distribuidor  v ]           |
+---------------------------------------------------+
| [ ] Previsualización                              |
+---------------------------------------------------+
|                  [ SUBMIT ]                       |
+---------------------------------------------------+

```

Y ejecuta [link](https://lioteam.atlassian.net/browse/INV-127) 

Hay un parametro importante que es `preview` que sirve para tener una vista previoa del mapeo para saber si estas conectando bien las columnas con los datos.

Por otro lado, tambien existe un esquema que te permite plantear el formulario al principio de manera estandar, aunque el usuario puede cambiarlo moviendo los elementos.

Por ejemplo: Si la columnas H tiene mapeado IVA, podes (mediante un select) cambiar IVA a la columna G

No puede asignar la misma letra a dos columnas distintas

El mapeo entandar se obtiene de aca [link](https://lioteam.atlassian.net/browse/INV-126)
