---
jira_key: "INV-117"
aliases: ["INV-117"]
summary: "API - Refactor - Agregar parametro url oficial del producto officialSiteUrl"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-09-10 07:01"
updated: "2024-09-11 21:34"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-117"
---

# INV-117: API - Refactor - Agregar parametro url oficial del producto officialSiteUrl

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-09-10 07:01 |
| Actualizado | 2024-09-11 21:34 |
| Etiquetas | ninguna |
| Jira | [INV-117](https://bluinc.atlassian.net/browse/INV-117) |

## Relaciones

- **Padre:** [[INV-27]] Productos
- **blocks:** [[INV-118]] APP - Refactor - Agregar parametro url oficial del producto officialSiteUrl

## Descripcion

Agregaremos un parámetro a el listado y para editar (PATCH) donde sea posible agregar la url del sito oficial, esto no solo es útil para los clientes, sino que lo retomaremos mas adelanta para enviar una IA a buscar la informacion directamente en caso de que sea posible.

Este parámetro ya fue usado en algún momento y lo retomaremos con otra ubicación (antes se guardaba en `[NB_WEB].[dbo].[WebArtComplement].link` , hoy deprecada) pero le asignaremos una ubicación en `[NewBytes_DBF].[dbo].[articulo].officialSiteUrl`

```
GET {API_URL}/item/{itemId}
```

```
{
    "list": [
        {
            "title": "TECLADO GAMER DUCKY SESALWWT1",
            "sku": "DKON1967ST-SESALWWT1",
            "id": 111699,
            "category": "TECLADOS                      ",
            "categoryId": 34,
            "officialSiteUrl":"https://www.razer.com/es-es/gaming-laptops/razer-blade-14" <---
            ...
        },
```

```
PATCH {API_URL}/item/{itemId}
```

```
{
  "officialSiteUrl":"https://www.razer.com/es-es/gaming-laptops/razer-blade-14"
}
```
