---
jira_key: "PED-28"
aliases: ["PED-28"]
summary: "API - Feat - Listar direcciones del cliente"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-08-16 08:12"
updated: "2023-08-16 10:05"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-28"
---

# PED-28: API - Feat - Listar direcciones del cliente

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-08-16 08:12 |
| Actualizado | 2023-08-16 10:05 |
| Etiquetas | ninguna |
| Jira | [PED-28](https://bluinc.atlassian.net/browse/PED-28) |

## Relaciones

- **Padre:** [[PED-16 - Listar clientes|PED-16]] Listar clientes
- **blocks:** [[PED-30 - APP - Feat - AgregarEditar direcciones|PED-30]] APP - Feat - Agregar/Editar direcciones

## Descripcion

Crearemos un recurso que se utilizara para listar las direcciones del cliente, basandonos en el mismo esquema que hemos utilizado para la api y expedicion

```
GET {{API_URL}}/v1/shippingAddress/{clientId}
```

```
[
[
    {
        "direccion": "Alberdi 3234",
        "alphaCode": "BSAS",
        "telefono": "3423423424",
        "provincia": "CAPITAL FEDERAL ( CAP. FED. )",
        "codigoPostal": "1407",
        "idDirCli": "19337",
        "predeterminado": null
    },
    {
        "direccion": "Av. Independencia 3485",
        "alphaCode": "BSAS",
        "telefono": "13241412",
        "provincia": "CAPITAL FEDERAL ( CAP. FED. )",
        "codigoPostal": "1225",
        "idDirCli": "19338",
        "predeterminado": null
    },
]
```
