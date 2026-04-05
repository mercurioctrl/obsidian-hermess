---
jira_key: "NBWEB-236"
aliases: ["NBWEB-236"]
summary: "API - Feat - Agregar direccion"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-06-07 11:01"
updated: "2022-07-03 09:31"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-236"
---

# NBWEB-236: API - Feat - Agregar direccion

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-06-07 11:01 |
| Actualizado | 2022-07-03 09:31 |
| Etiquetas | ninguna |
| Jira | [NBWEB-236](https://bluinc.atlassian.net/browse/NBWEB-236) |

## Relaciones

- **Padre:** [[NBWEB-2 - API - Mi cuenta|NBWEB-2]] API - Mi cuenta
- **relates to:** [[NBWEB-285 - APP - Feat - Mi cuenta - Listar direcciones|NBWEB-285]] APP - Feat - Mi cuenta - Listar direcciones

## Descripcion

```
POST {{API_URL}}/v1/miCuenta/shippingAddress
```

```
[
    {
        "direccion": "alguna de prueba 124",
        "telefono": "1530510267",
        "placeId": 1,
        "provinceId": 4,
        "codigoPostal": "1407",
        "predeterminado": null,
        
    }
]
```

```
{
  succes:true
}
```
