---
jira_key: "LIO-174"
aliases: ["LIO-174"]
summary: "API - Refactor - Nuevo parámetros y filtros para el repositorio categorías"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-01-19 19:25"
updated: "2025-01-27 04:43"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-174"
---

# LIO-174: API - Refactor - Nuevo parámetros y filtros para el repositorio categorías

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-01-19 19:25 |
| Actualizado | 2025-01-27 04:43 |
| Etiquetas | ninguna |
| Jira | [LIO-174](https://bluinc.atlassian.net/browse/LIO-174) |

## Relaciones

- **Padre:** [[LIO-173 - Categorias|LIO-173]] Categorias

## Descripcion

Agregaremos algunas funciones útiles para la composición de menúes mas complejos

```
GET {API_URL}/v4/cabecera-categorias?homeShow={1|0|null}
```

## Nuevas columnas `[LO].[dbo].[categorias]`

- homeShow: Es un parámetro para saber si debe mostrarse o no en la home 


- directUrl: Parámetro para albergar directamente una url de búsqueda del tipo `https://libreopcion.com.ar/memorias-flash?ver_mas_vendedores=1&freeshipping=1` o cualquier otra



## Retorna

```
[
{
"id": 1732,
"nombre": "Accesorios y Periféricos",
"hijos": [
{
"id": 1,
"nombre": "Mouse",
"img": "icon-mouse.svg",
"directUrl": "https://libreopcion.com.ar/memorias-flash" <-- NUEVO
},
{
"id": 30,
"nombre": "Mousepad",
"img": "icon-mousepad.svg"
"directUrl": "https://libreopcion.com.ar/mousepad" <-- NUEVO
},
{
"id": 4,
"nombre": "Parlantes",
"img": "icon-parlantes.svg"
"directUrl": null <-- NUEVO
},
},
{
"id": 117,
"nombre": "Micrófonos",
"img": "icon-microfono.svg"
"directUrl": null <-- NUEVO
},
{
"id": 3,
"nombre": "Teclados",
"img": "icon-teclado.svg"
"directUrl": null <-- NUEVO
},
{
"id": 5,
"nombre": "Auriculares",
"img": "icon-auriculares.svg"
},
{
"id": 2,
"nombre": "Webcams",
"img": "icon-webcam.svg"
},
{
"id": 195,
"nombre": "Mochilas",
"img": "icon-mochilas.svg"
...
```



Desestimar la parte anterior - Refactor 



Vamos a cambiar la forma de trabajar con las tabla de categorías, tanto para las categorias padres y las hijas.



Si una categoría es padre, utilizaremos el campo** categoria_padre = 0 **



Si una categoría es hija, utilizaremos el campo **categoria_padre = {id_categoria_padre}**



Ejemplo 

Categoria padre :  



[adjunto]
Categoria hija:





[adjunto]
`Sum up : `

Accesorios y perifericos 

                 →    Mouse
