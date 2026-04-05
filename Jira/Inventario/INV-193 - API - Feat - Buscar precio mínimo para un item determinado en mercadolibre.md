---
jira_key: "INV-193"
aliases: ["INV-193"]
summary: "API - Feat - Buscar precio mínimo para un item determinado en mercadolibre"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-06-24 15:26"
updated: "2025-07-15 10:31"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-193"
---

# INV-193: API - Feat - Buscar precio mínimo para un item determinado en mercadolibre

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-06-24 15:26 |
| Actualizado | 2025-07-15 10:31 |
| Etiquetas | ninguna |
| Jira | [INV-193](https://bluinc.atlassian.net/browse/INV-193) |

## Relaciones

- **Padre:** [[INV-35]] Importadores/ Scrappers
- **relates to:** [[INV-189]] API - Refactor - Volver a conectar repositorio de búsqueda de imágenes a mercadolibre según research

## Descripcion

Crearemos un recurso que busca en el catalogo de Mercadolibre para encontrar un item determinado, encontrar el precio mas barato del mismo para un producto nuevo

En principio esto puede hacerse de dos formas con este recurso

- **Búsqueda Libre:** Se busca un producto en base a una “cadena”, nombre o SKU y este devuelve un objeto como el siguiente



```
GET {API_URL}/getPrice/string?search={string}
```

```
{
    "precio": 713378, <-- El precio mas bajo para ese item NUEVO
    "tienda": "Hardloots", <-- Este parametro peude estar o no, segun si esta para scrappear
    "titulo": " NOTEBOOK LENOVO AMD R3 7320U 16GB 512GB 15.6 FULL HD ", <-- Titulo del producto del cual se selecciono el precio
    "permalink": "https:\/\/www.hardgamers.com.ar\/product\/-431037134", <-- Url para ver la ficha del producto en ML
    "keyword": "LENOVO AMD R3 7320U", <-- Las keywords utilizadas para buscarlo
    "thumbnail": "https:\/\/static.nb.com.ar\/i\/nb_NOTEBOOK-LENOVO-v15-AMD-R3-7320U-16GB-512GB-15.6-FULL-HD_ver_10a0f609a5653d0b83ac70ac8ea93f9c.jpg" <-- La imagen principal del catalogo de donde tomamos el precio
}
```

- **Búsqueda por itemId:** Se busca un producto en base a su item ide en nuestro sistema. Para eso usaremos la tabla `[NewBytes_DBF].[dbo].[scrap_hg]` que ya dispone del parametro `search_keys` para nuestros itemId, y usaremos esas `keywords` para buscar el producto en ml



```
GET {API_URL}/getPrice/string?itemId={itemId}
```

```
{
    "precio": 713378, <-- El precio mas bajo para ese item NUEVO
    "tienda": "Hardloots", <-- Este parametro peude estar o no, segun si esta para scrappear
    "titulo": " NOTEBOOK LENOVO AMD R3 7320U 16GB 512GB 15.6 FULL HD ", <-- Titulo del producto del cual se selecciono el precio
    "permalink": "https:\/\/www.hardgamers.com.ar\/product\/-431037134", <-- Url para ver la ficha del producto en ML
    "keyword": "LENOVO AMD R3 7320U", <-- Las keywords utilizadas para buscarlo
    "thumbnail": "https:\/\/static.nb.com.ar\/i\/nb_NOTEBOOK-LENOVO-v15-AMD-R3-7320U-16GB-512GB-15.6-FULL-HD_ver_10a0f609a5653d0b83ac70ac8ea93f9c.jpg" <-- La imagen principal del catalogo de donde tomamos el precio
}
```

Ejemplo practico: Supongamos que quiero buscar el `itemId=119375` del cual sus `search_keys`son según nuestra tabla `9950X`

Entonces debemos buscar en 

```
https://listado.mercadolibre.com.ar/9950x#D[A:9950X]
```

De modo tal que terminaremos por seleccionar el que indicamos con una flecha. ¿Porque ese y no otros?

- Por ser  NUEVO y no usado del cual hay mas baratos.


- Por no ser Compra Internacional del cual hay mas baratos.



Es decir, se busca aquel con el cual uno compite directamente, por eso se dejan fuera los que vienen de afuera y están marcados como “compra internacional” o los usados.

[adjunto]
