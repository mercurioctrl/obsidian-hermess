---
jira_key: "PED-169"
aliases: ["PED-169"]
summary: "API - Ordenes - Incidencias varias"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2023-10-25 23:56"
updated: "2023-10-26 14:38"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-169"
---

# PED-169: API - Ordenes - Incidencias varias

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2023-10-25 23:56 |
| Actualizado | 2023-10-26 14:38 |
| Etiquetas | ninguna |
| Jira | [PED-169](https://bluinc.atlassian.net/browse/PED-169) |

## Relaciones

- **blocks:** [[PED-8]] Listar ordenes de compra

## Descripcion

**Error al seleccionar un pedido**
Al seleccionar aleatoriamente pedidos me aparecen diversos errores, por ejemplo, `0002-10314428`, me aparece el siguiente error.

```
Cannot assign null to property App\\Dto\\Order\\OrderDetailDto::$sellerIdCreator of type string
```

[adjunto]

`0000-10314741`

```
"Cannot assign null to property App\\Dto\\Order\\OrderDetailDto::$clientName of type string"
```

[adjunto]
Habría que manejar el error, devolver un mensaje y código de estado http predeterminado al usuario.


---

**Error en el cálculo de la paginación**
Me aparece que son 4,002 registros, entre 500 registros por página me da un total de 8, al seleccionar la página a partir de la 6 ya no me aparece ningún registro.

[adjunto]
