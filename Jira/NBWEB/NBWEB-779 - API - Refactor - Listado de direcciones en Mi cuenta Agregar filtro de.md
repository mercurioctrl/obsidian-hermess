---
jira_key: "NBWEB-779"
aliases: ["NBWEB-779"]
summary: "API - Refactor - Listado de direcciones en \"Mi cuenta\": Agregar filtro de dropshipping y mostrar el parametro en el objeto"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-07-23 13:49"
updated: "2024-07-25 18:08"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-779"
---

# NBWEB-779: API - Refactor - Listado de direcciones en "Mi cuenta": Agregar filtro de dropshipping y mostrar el parametro en el objeto

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-07-23 13:49 |
| Actualizado | 2024-07-25 18:08 |
| Etiquetas | ninguna |
| Jira | [NBWEB-779](https://bluinc.atlassian.net/browse/NBWEB-779) |

## Relaciones

- **Padre:** [[NBWEB-610]] API - Refactor - Agregar internalTax a los montos finales de las ordenes dentro de Mi Cuenta
- **is blocked by:** [[NBWEB-778]] API - Refactor - Al procesar una compra que tiene marcado "Dropshipping" entonces debo marcar la direccion como "Dropshipping"
- **blocks:** [[NBWEB-780]] APP - Refactor - Listado de direcciones en "Mi cuenta": Agregar filtro de dropshipping y mostrar el listado según el filtro
- **is blocked by:** [[NBWEB-787]] API - Mis direcciones -> Filtro por dropshipping - Agregar parámetro y filtrado

## Descripcion

```
GET {API_URL}/v1/miCuenta/shippingAddress?dropShipping=true
```

Agregaremos el filtro `dropShipping` al repositorio

Si `dropShipping=true` entonces muestro aquellos que tienen en la base de datos `dropShipping=true`

Si `dropShipping=false` muestro los que `dropShipping != true (incluidos null)`

Si `dropShipping=null` muestro todos los casos



Adicionalmente agregaremos el parámetro al objeto


```
[
    {
        "direccion": "Alberdi 3234",
        "alphaCode": "BSAS",
        "telefono": "3423423424",
        "provincia": "CAPITAL FEDERAL ( CAP. FED. )",
        "codigoPostal": "1407",
        dropShipping=true, <<---
        "idDirCli": "19337",
        "predeterminado": "19337"
    },
    {
        "direccion": "Alberdi 3234",
        "alphaCode": "BSAS",
        "telefono": "3423423424",
        dropShipping=false <---
        "provincia": "CAPITAL FEDERAL ( CAP. FED. )",
        "codigoPostal": "1407",
        "idDirCli": "19337",
        "predeterminado": "19337"
    },
```
