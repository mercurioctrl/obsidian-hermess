---
jira_key: "NBWEB-136"
summary: "API -  Agregar envio"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-04-25 16:07"
updated: "2022-06-26 21:33"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-136"
---

# NBWEB-136: API -  Agregar envio

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-04-25 16:07 |
| Actualizado | 2022-06-26 21:33 |
| Etiquetas | ninguna |
| Jira | [NBWEB-136](https://bluinc.atlassian.net/browse/NBWEB-136) |

## Descripción

---

Una vez que que tenemos los datos de cotización para la direccion favorita del cliente

Se debe agregar el envio al pedido propiamente dicho, utilizando el recurso

```
PATCH {{API_URL}}/v1/carrito/agregarEnvio
```

Ruequest

```
{
  codigoPostalFavorito:1439,
  mediodeEnvioId:34
}
```



Una vez ejecutado el recurso, se debe crear un ítem agregado en el carrito (con id y cref `102048`) que contenga la leyenda “Servicio de Transporte” por el total cotizado en el recurso

```
GET {{API_URL}}/v1/carrito/calcularEnvioPara/{codigoPostalFavorito}
```

Para ese medio de envio.

Es decir, que por detrás, es necesario re cotizar.
