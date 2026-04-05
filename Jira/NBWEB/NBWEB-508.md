---
jira_key: "NBWEB-508"
summary: "API - Feat - Bultos por unidad"
status: "Code Review"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-11-25 10:26"
updated: "2022-11-28 10:27"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-508"
---

# NBWEB-508: API - Feat - Bultos por unidad

| Campo | Valor |
|-------|-------|
| Estado | Code Review (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-11-25 10:26 |
| Actualizado | 2022-11-28 10:27 |
| Etiquetas | ninguna |
| Jira | [NBWEB-508](https://bluinc.atlassian.net/browse/NBWEB-508) |

## Descripción

Introduciremos el concepto de bulto por unidad, de esta forma podremos hacer cotizaciones mas precisas y mas cercanas a lo que sucede después en el deposito cuando los arman realmente.

Trabajaremos sobre los recursos 

```
GET {{API_URL}}/cart/nb/8004029/cp/1682/{Direccion}
```

```
GET {{API_URL}}/cart/nb/8004029/cp/1439
```

```
GET {{API_URL}}/order/nb/0002-10217160/cp/1407
```

Del servicio de envíos

Lo que haremos sera agregar un parámetro `packagePerUnit` que nos permita, al multiplicarse por la cantidad de unidades del producto que lo posee, obtener la cantidad de bultos.

Si la cantidad de bultos nos da un numero decimal (ej 3.4) entonces redondeamos para arriba (4)

En principio pondermos el nuevo parametro en la tabla `NewBytes_DBF.dbo.ariculos`
