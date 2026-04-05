---
jira_key: "INV-120"
aliases: ["INV-120"]
summary: "APP - Refactor - Agregar parámetro sindicateContentImg"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2024-09-10 07:32"
updated: "2024-09-11 22:41"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-120"
---

# INV-120: APP - Refactor - Agregar parámetro sindicateContentImg

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2024-09-10 07:32 |
| Actualizado | 2024-09-11 22:41 |
| Etiquetas | ninguna |
| Jira | [INV-120](https://bluinc.atlassian.net/browse/INV-120) |

## Relaciones

- **Padre:** [[INV-27]] Productos
- **is blocked by:** [[INV-119]] API - Refactor - Agregar parámetro sindicateContentImg

## Descripcion

Agregaremos un parámetro a el listado y para editar (PATCH) donde sea posible agregar una URL que aloja una imagen (esto se encuentra en un servidor externo de imágenes, ej: [link](https://i.imgur.com/bzJgKy9.jpeg) )

Este parámetro se almacena en una tabla similar a 

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
            "sindicateContentImg":"https://i.imgur.com/bzJgKy9.jpeg" <---
            ...
        },
```

```
PATCH {API_URL}/item/{itemId}
```

```
{
  ...
  "sindicateContentImg":"https://i.imgur.com/bzJgKy9.jpeg"
}
```

Moveremos EAN y UPC al “lapiz de edición” ya que es obligatorio en otro paso desde expedición (cuando cargan los productos) y pondremos en su lugar este parámetro.

[adjunto]


La idea es usar el contenido sindicado que genera la marca para agregar aun mas valor aprovechando la imagen generada por las marcas y mejorar el brandeo producto por producto. 

[adjunto]
