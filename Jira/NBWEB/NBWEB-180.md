---
jira_key: "NBWEB-180"
summary: "MS - Envios - Crear Envio"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-05-13 08:09"
updated: "2022-07-01 17:40"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-180"
---

# NBWEB-180: MS - Envios - Crear Envio

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-05-13 08:09 |
| Actualizado | 2022-07-01 17:40 |
| Etiquetas | ninguna |
| Jira | [NBWEB-180](https://bluinc.atlassian.net/browse/NBWEB-180) |

## Descripción

Solo con rol administrador

```
POST {{API_URL}}/v1/shipping
```

Request

```
{
  shipperId: 3 //id del transportista
  deliveryAddress : 'Direccion de entrega'
  deliveryZipCode: 'Codig Postal destino'
  town: "localidad de entrega"
  province: "provincia de entrega"
  publicKey: "Es un string, que suele ser un numero de pedido u orden del sitio de origen"
}
```



La clave privada debe ser una palabra en español, que se puede elegir de manera aleatoria desde un diccionario que encontremos en cualquier formato.
