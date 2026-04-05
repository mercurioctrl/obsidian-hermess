---
jira_key: "INV-54"
aliases: ["INV-54"]
summary: "API - Feat - Sugerir valor en base a un atributo determinado y el item"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-01-24 07:26"
updated: "2024-01-30 03:54"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-54"
---

# INV-54: API - Feat - Sugerir valor en base a un atributo determinado y el item

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-01-24 07:26 |
| Actualizado | 2024-01-30 03:54 |
| Etiquetas | ninguna |
| Jira | [INV-54](https://bluinc.atlassian.net/browse/INV-54) |

## Relaciones

- **Padre:** [[INV-27]] Productos
- **blocks:** [[INV-53]] APP - Feat- Sugerir atributos cuando estamos creando uno

## Descripcion

Basándonos en la tabla `PRODUCTOS.dbo.etiquetas`

Crearemos un nuevo recurso que sirve para sugerir valores de atributos que filtra enviando el id del articulo  cuando **matchean con 2 o mas caracteres**

```
GET {api_url}/V1/attributesValues?search=di$itemId=102312
```

```
[
  {
    "nombre": "Puertos",
    "valor": "USB 3.0 x1 + USB 2.0 x1 + Audio Frontal Ac97"
  },
  {
    "nombre": "Marca",
    "valor": "Western Digital"
  },
  {
    "nombre": "Modelo",
    "valor": "Dasher medium"
  },
  {
    "nombre": "Material del mouse pad",
    "valor": "Poliuretano no resbaladizo"
  },
  {
    "nombre": "Tamaño de mouse pad",
    "valor": "extendido"
  },
  {
    "nombre": "Puertos",
    "valor": "4 PUERTOS USB (2.0/3.0*) + Audio"
  },
  {
    "nombre": "Modelo",
    "valor": "Firefly Cloth Edition"
  },
  
  ...
```
