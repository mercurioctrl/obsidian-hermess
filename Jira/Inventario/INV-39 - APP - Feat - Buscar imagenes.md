---
jira_key: "INV-39"
aliases: ["INV-39"]
summary: "APP - Feat - Buscar imagenes"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2023-10-20 17:28"
updated: "2023-11-07 08:22"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-39"
---

# INV-39: APP - Feat - Buscar imagenes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2023-10-20 17:28 |
| Actualizado | 2023-11-07 08:22 |
| Etiquetas | ninguna |
| Jira | [INV-39](https://bluinc.atlassian.net/browse/INV-39) |

## Relaciones

- **Padre:** [[INV-38 - Feat - Buscar imagenes en repositorios remotos|INV-38]] Feat - Buscar imagenes en repositorios remotos

## Descripcion

Agregaremos un “accionable” en alguna parte de la barra de imagenes que nos permita desplegar un modal que mostrara

- Un input de texto con el nombre del producto


- El resultado del siguiente recurso 


```
{{API_URL}}/getImages/string?title={titulo del producto}
```



[adjunto]
Esto devuelve un resutlado del siguiente tipo

```
[
    {
        "Meli": [
            "http://http2.mlstatic.com/D_928642-MLA47847420037_102021-F.jpg",
            "http://http2.mlstatic.com/D_683821-MLA51325230641_082022-F.jpg",
            "http://http2.mlstatic.com/D_875563-MLA51325230643_082022-F.jpg",
            "http://http2.mlstatic.com/D_835553-MLA51325236484_082022-F.jpg",
            "http://http2.mlstatic.com/D_662985-MLA51325304037_082022-F.jpg",
            "http://http2.mlstatic.com/D_720792-MLA51325230530_082022-F.jpg",
            "http://http2.mlstatic.com/D_932517-MLU69973925307_062023-F.jpg"
        ]
    },
    {
        "NewEgg": [
            "https://c1.neweggimages.com/ProductImage/19-113-664-V01.jpg",
            "https://c1.neweggimages.com/ProductImage/B1MBS2111150RBMLI2E.jpg",
            "https://c1.neweggimages.com/ProductImage/B1MBS2111150RBMI5BC.jpg",
            "https://c1.neweggimages.com/ProductImage/B1MBS2111150RBMRV3C.jpg",
            "https://c1.neweggimages.com/ProductImage/B1MBS2111150RBMBY49.jpg",
            "https://c1.neweggimages.com/ProductImage/B1MBS2111150RBMBY98.jpg",
            "https://c1.neweggimages.com/ProductImage/B1MBS2111150RBMSG0C.jpg"
        ]
    }
]
```

Debemos mostrar todas las imágenes, y agregar en cada una de ella un accionable que nos permitirá agregarla como imagen, como si fuese una subida desde nuestro equipo.
