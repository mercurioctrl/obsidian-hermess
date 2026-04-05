---
jira_key: "NBWEB-613"
aliases: ["NBWEB-613"]
summary: "APP - Feat - Mi cuenta -> Listas de precios"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2024-01-18 07:21"
updated: "2024-01-26 02:52"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-613"
---

# NBWEB-613: APP - Feat - Mi cuenta -> Listas de precios

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2024-01-18 07:21 |
| Actualizado | 2024-01-26 02:52 |
| Etiquetas | ninguna |
| Jira | [NBWEB-613](https://bluinc.atlassian.net/browse/NBWEB-613) |

## Relaciones

- **Padre:** [[NBWEB-610 - API - Refactor - Agregar internalTax a los montos finales de las ordenes dentro|NBWEB-610]] API - Refactor - Agregar internalTax a los montos finales de las ordenes dentro de Mi Cuenta

## Descripcion

Utilizando los siguientes recursos:

```
GET {{API_URL}}/v1/miCuenta/readToken
```

```
GET {{API_URL}}/v1/priceListExcel/{token}
```

```
GET GET {{API_URL}}/v1/priceListCsv/{token}
```

Crearemos una nueva sección dentro de mi cuenta que exponga dentro de un input las dos direcciones para descargar el archivo **Excel** y el **Csv**.





---

**Descarga tu lista de precio actualizada **

Utiliza los siguientes recursos para descargar tu lista de pecios actualizada cuando quieras. Siempre que los utilices de la forma que se indica mas abajo, no requieren login y estarán siempre disponibles con precios actualizados para tu cuenta.

Estos recursos son únicos de tu cuenta, no los compartas ni compartas el token que viene con ellos.



[input con url y boton copiar para el csv]

[input con url y boton copiar para el xlsx]

---
