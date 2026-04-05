---
jira_key: "COM-115"
aliases: ["COM-115"]
summary: "API - Review - Problema al ver del detalle de las oredenes"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-06-26 08:49"
updated: "2024-06-26 20:16"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-115"
---

# COM-115: API - Review - Problema al ver del detalle de las oredenes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-06-26 08:49 |
| Actualizado | 2024-06-26 20:16 |
| Etiquetas | ninguna |
| Jira | [COM-115](https://bluinc.atlassian.net/browse/COM-115) |

## Relaciones

- **Padre:** [[COM-38 - Ver orden de compra|COM-38]] Ver orden de compra

## Descripcion

```
GET 'https://gamma.api.purchases.lio.red/v1/providerOrder/11179'
```

Por alguna razón empezó a falla el recurso, asumo que tiene que ver con el remplazo de base de datos con que tal vez falta rellenar alguna tabla o algo. 



SQL Ejecutadas:

```
CREATE TABLE NEW_BYTES.dbo.ProductPosition (
    posicion NVARCHAR(50),
    category_id INT NOT NULL,
    descripcion NVARCHAR(MAX) NULL,
    derechos_exportacion DECIMAL(18, 2) NULL,
    arancel_externo_comun DECIMAL(18, 2) NULL,
    reintegros_extrazona DECIMAL(18, 2) NULL,
    derechos_importacion_extrazona DECIMAL(18, 2) NULL,
    reintegros_intrazona DECIMAL(18, 2) NULL,
    derechos_importacion_intrazona DECIMAL(18, 2) NULL,
    derechos_importacion_especifico_minimo DECIMAL(18, 2) NULL,
    unidad NVARCHAR(50) NULL,
    actualizado DATETIME NULL,
    activo BIT NULL,
    texto_partida NVARCHAR(MAX) NULL,
    pos_padre INT NULL,
    derecho_exportacion_adicional DECIMAL(18, 2) NULL,
    category_name NVARCHAR(255) NULL
);
```



```
CREATE TABLE NEW_BYTES.dbo.TaxPosition (
    posicion NVARCHAR(50),
    descripcion NVARCHAR(MAX) NULL,
    operacion NVARCHAR(50) NULL,
    subcluster NVARCHAR(50) NULL,
    product_position NVARCHAR(50) NOT NULL,
    valor DECIMAL(18, 2) NULL,
    cluster NVARCHAR(50) NULL
);
```



```
 ALTER TABLE NewBytes_DBF.dbo.articulo
ADD position NVARCHAR(50)
```
