---
jira_key: "EXP-280"
aliases: ["EXP-280"]
summary: "API - Refactor - Validar palabra clave, en el caso que esta exista en la tabla pedclit"
status: "Gamma"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-05-15 09:08"
updated: "2023-05-16 09:49"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-280"
---

# EXP-280: API - Refactor - Validar palabra clave, en el caso que esta exista en la tabla pedclit

| Campo | Valor |
|-------|-------|
| Estado | Gamma (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-05-15 09:08 |
| Actualizado | 2023-05-16 09:49 |
| Etiquetas | ninguna |
| Jira | [EXP-280](https://bluinc.atlassian.net/browse/EXP-280) |

## Relaciones

- **Padre:** [[EXP-258]] Feat - Autorizar Entrega mediante tarjeta de autorizacion
- **blocks:** [[EXP-281]] APP - Refactor - Validar palabra clave, en el caso que exista

## Descripcion

Vamos a incorporar el sistema ya existente de palabras clave, a este modal, donde se confirma la entrega del pedido.

Viendo como lo hacen, estaban saltando entre dos sistemas. En uno confirmaban y en el otro ponían la palabra clave.

Para esto agregaremos al recurso [link](https://lioteam.atlassian.net/browse/EXP-259) 

```
PATCH {API_URL}/v1/orders/{pedido}/hand
```

```
{
    autorizaUser: {token},
    secretKey: {secretKey} <--Agregamos la palabra clave
}
```

Solo es necesario validar en los casos que tengan `[NewBytes_DBF].[dbo].[pedclit].secret_key` distinto de NULL

Adicionalmente si la palabra clave es correcta marcaremos el usuario y momento de la inserción de la palabra

```
[secret_key_confirm_user]
[secret_key_confirm_date]
```



Modificar recurso para leer en el front

También modificaremos en 

```
GET {API_URL}/v1/orders/{pedido}
```

y agregaremos el parámetro `secretKey:true` cuando en pedclit no es nulo para poder saber si debemos o no mostrar el campo desde el front
