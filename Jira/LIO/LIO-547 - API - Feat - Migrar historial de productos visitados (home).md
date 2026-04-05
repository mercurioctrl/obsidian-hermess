---
jira_key: "LIO-547"
aliases: ["LIO-547"]
summary: "API - Feat - Migrar historial de productos visitados (home)"
status: "Selected for Development"
type: "Subtarea"
priority: "Medium"
assignee: "Sin asignar"
reporter: "Catriel Mercurio"
created: "2026-02-23 07:47"
updated: "2026-02-23 16:42"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-547"
---

# LIO-547: API - Feat - Migrar historial de productos visitados (home)

| Campo | Valor |
|-------|-------|
| Estado | Selected for Development (Por hacer) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Sin asignar |
| Reportado por | Catriel Mercurio |
| Creado | 2026-02-23 07:47 |
| Actualizado | 2026-02-23 16:42 |
| Etiquetas | ninguna |
| Jira | [LIO-547](https://bluinc.atlassian.net/browse/LIO-547) |

## Relaciones

- **Padre:** [[LIO-537]] Migración de repositorios previa deprecación de la api legacy

## Descripcion

Migrar historial de productos visitados. Este endpoint retorna el historial de navegación del usuario autenticado, devolviendo los últimos productos que visitó en el sitio.
  Se utiliza para alimentar secciones tipo "Vistos recientemente" en la home o en páginas de detalle de producto.

```
GET /productos/{cantidad}/historial 
```

  Funcionamiento conceptual

- Se identifica al usuario a través del token de autenticación.


- Se consulta la tabla de visitas (productosVisitas) para obtener los últimos productos que el usuario navegó, eliminando
duplicados por producto_id y ordenando del más reciente al más antiguo.


- Si el usuario tiene menos de 5 visitas registradas, se retorna un array vacío (no se muestra la sección).


- Con los IDs de los productos visitados, se consulta el detalle completo de cada uno incluyendo precios, estados, envíos, cuotas,
marca y vendedor.


- Importante: la query de detalle utiliza mostrarOcultos = true, lo que significa que no filtra por stock ni por activo — solo
excluye productos con ocultar = 1. Esto es intencional: el historial muestra lo que el usuario vio aunque el producto ya no esté
disponible.



Requiere autenticación: Si — se extrae el [usuario.id](http://usuario.id) desde el token JWT.

---

##  Parametros

** cantidad:** Limite maximo de productos a retornar. Ejemplo: 10

---

## Respuestas

### 200 OK — Con historial suficiente

Array de objetos ProductoDTO. Puede tener entre 1 y {cantidad} elementos.

```
[
    {
      "id": 1234,
      "idInterno": 5678,
      "calificacion": 5,
      "limiteCompra": 99999,
      "esNativo": true,
      "imagenPrincipal": "abc123checksum",
      "titulo": "Monitor LG 27\" Full HD",
      "estados": {
        "stock": true,
        "revision": false,
        "rechazado": false,
        "usado": false,
        "preventa": false,
        "instantFlash": false
      },
      "precios": {
        "precioLO": 180000,
        "precioLista": 198000,
        "precioSinDescuento": 180000,
        "cotizacion": 1050.00,
        "descuentoLO": 0,
        "descuentoDolares": 0
      },
      "cuotas": { },
      "envios": {
        "activo": true,
        "gratis": false,
        "rapido": false,
        "codigoPostalOrigen": "",
        "cotizar": false
      },
      "marca": {
        "id": 3177,
        "nombre": "LG",
        "img": "checksum-logo",
        "activa": true,
        "uri": "lg",
        "svg": "images/logos/marcas/lg.svg"
      },
      "vendedor": {
        "id": 1,
        "nombre": "LibreOpcion",
        "uri": "libreopcion",
        "esReseller": false,
        "cp": "1234"
      }
    }
  ]
```

200 OK — Historial insuficiente (menos de 5 visitas)

```
 []
```

No hay codigos de error especificos para este endpoint. Devuelve [] en lugar de un 4xx cuando no hay datos suficientes.

## Queries utilizadas

## Query 1 — Obtener visitas del usuario

```
  SELECT TOP 100
      id,
      producto_id
  FROM [LO].[dbo].[productosVisitas]
  WHERE usuario_id = ?
  GROUP BY
      id,
      producto_id
  ORDER BY id DESC;
```

 Parametro: usuario_id del token autenticado.
  Nota: Trae hasta 100 visitas y agrupa por producto_id para evitar repetidos. Si el resultado tiene menos de 5 filas, se corta el
  flujo y retorna [].

## Query 2 — Obtener detalle de los productos visitados

```
  SELECT TOP {cantidad}

      -- Identificadores
      [productos].id,
      [productos].id_interno AS idInterno,
      [productos].vendedorID AS idVendedor,
      COALESCE([productosValoracionCalculada].valoracion, 0) AS calificacion,
      [productos].titulo,
      CASE WHEN [productos].maxUniPromo > 0 THEN [productos].maxUniPromo ELSE 99999 END AS limiteCompra,
      [productos].id_interno AS esNativo,

      -- Envios
      CASE
          WHEN [productos].id_interno IS NOT NULL THEN (SELECT COUNT(*) FROM [LO].[dbo].[mediosEnvio] WHERE activo = 1 AND eliminado
  = 0)
          WHEN [vendedores].IDcliente IS NOT NULL THEN (SELECT COUNT(*) FROM [LO].[dbo].[vendedoresMediosEnvio])
          ELSE 1
      END AS envioActivo,
      [productos].envioRapido,
      [productos].envioGratis,

      -- Marca
      [productos].id_marca AS marcaId,
      [marcas].nombre AS marcaNombre,
      COALESCE((SELECT checksum FROM [PRODUCTOS].[dbo].[fotos] WHERE id = [marcas].logo_id), '') AS marcaImagen,

      -- Estados
      [productos].usado,
      [productos].preventa,
      [productos].instantFlash,

      -- Precios
      [productos].descuento,
      (floor(
          CASE WHEN COALESCE([productos].costo_cliente, 0) > 0
              THEN {cotizacion} * [productos].precioDolar
              ELSE [productos].precioImportado * (
                  CASE WHEN [productos].precioImportadoDolar = 1 THEN {cotizacion} ELSE 1 END
              )
          END
      )) * (1 - ([productos].descuento / 100)) AS precio,
      (floor(
          CASE WHEN COALESCE([productos].costo_cliente, 0) > 0
              THEN {cotizacion} * [productos].precioDolar
              ELSE [productos].precioImportado * (
                  CASE WHEN [productos].precioImportadoDolar = 1 THEN {cotizacion} ELSE 1 END
              )
          END
      )) AS precioSinDescuento

  FROM [CS].[dbo].[productos]

  -- JOIN para preservar el orden original de IDs del historial
  JOIN (
      SELECT
          CA = ROW_NUMBER() OVER (ORDER BY (SELECT NULL)),
          CB = v.value('(./text())[1]', 'INT')
      FROM (VALUES (CONVERT(xml, '<x>' + REPLACE('{ids_csv}', ',', '</x><x>') + '</x>'))) x(n)
      CROSS APPLY n.nodes('x') node(v)
  ) B ON [productos].id = B.CB

  LEFT JOIN [LO].[dbo].[marcas]
      ON [marcas].id = [productos].id_marca AND [marcas].eliminada = 0
  LEFT JOIN [LO].[dbo].[productosValoracionCalculada]
      ON [productosValoracionCalculada].idFabricante = [productos].ID_fabricante
  LEFT JOIN [LO].[dbo].[vendedores]
      ON [productos].vendedorID = [vendedores].id
  LEFT JOIN [LO].[dbo].[ciudades]
      ON [ciudades].id = [vendedores].ciudadID
  LEFT JOIN [LO].[dbo].[provincias]
      ON [provincias].id = [vendedores].provinciaID
  LEFT JOIN [NewBytes_DBF].[dbo].[articulo]
      ON [productos].id_interno = [articulo].id_articulo
  LEFT JOIN [NewBytes_DBF].[dbo].[stocks]
      ON [articulo].ID_ARTICULO = [stocks].ID_ARTICULO

  WHERE
      [productos].ocultar <> 1              -- unico filtro activo (mostrarOcultos = true)
      AND [productos].id IN ({ids_csv})

  ORDER BY B.CA;                            -- preserva orden del historial

  Nota sobre filtros: A diferencia de otros endpoints de productos, este no filtra por activo, stock, revision ni rechazado. Solo
  excluye productos marcados como ocultar = 1. Es comportamiento intencional.

```

**Nota sobre filtros: **A diferencia de otros endpoints de productos, este no filtra por activo, stock, revision ni rechazado. Solo excluye productos marcados como ocultar = 1. Es comportamiento intencional.
