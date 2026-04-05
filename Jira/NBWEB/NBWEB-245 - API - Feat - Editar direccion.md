---
jira_key: "NBWEB-245"
aliases: ["NBWEB-245"]
summary: "API - Feat - Editar direccion"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-06-08 14:55"
updated: "2022-07-03 09:31"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-245"
---

# NBWEB-245: API - Feat - Editar direccion

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-06-08 14:55 |
| Actualizado | 2022-07-03 09:31 |
| Etiquetas | ninguna |
| Jira | [NBWEB-245](https://bluinc.atlassian.net/browse/NBWEB-245) |

## Relaciones

- **Padre:** [[NBWEB-2 - API - Mi cuenta|NBWEB-2]] API - Mi cuenta
- **relates to:** [[NBWEB-255 - APP - Feat - Mis Direcciones de envio|NBWEB-255]] APP - Feat - Mis Direcciones de envio
- **relates to:** [[NBWEB-285 - APP - Feat - Mi cuenta - Listar direcciones|NBWEB-285]] APP - Feat - Mi cuenta - Listar direcciones

## Descripcion

```
PATCH {{API_URL}}/v1/miCuenta/shippingAddress
```

```

[
    {
        "direccion": "alguna de prueba 124",
        "telefono": "1530510267",
        "localidad": "CIUDAD DE BUENOS AIRES        ",
        "provincia": "BUENOS AIRES ( BS. AS )       ",
        "codigoPostal": "1407",
        "IdDirCli": "18063",
        "predeterminado": null,
        
    }
]
{
  succes:true
}
```
