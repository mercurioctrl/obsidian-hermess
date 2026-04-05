---
jira_key: "LIO-206"
aliases: ["LIO-206"]
summary: "API - Feat - Leer y Editar objeto \"mi tienda\" o vendedores"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-02-03 06:40"
updated: "2025-02-12 10:31"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-206"
---

# LIO-206: API - Feat - Leer y Editar objeto "mi tienda" o vendedores

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-02-03 06:40 |
| Actualizado | 2025-02-12 10:31 |
| Etiquetas | ninguna |
| Jira | [LIO-206](https://bluinc.atlassian.net/browse/LIO-206) |

## Relaciones

- **Padre:** [[LIO-203 - Mi cuenta|LIO-203]] Mi cuenta
- **has action item:** [[LIO-207 - APP - Feat - Editar informacion de mi tienda|LIO-207]] APP - Feat - Editar informacion de "mi tienda"

## Descripcion

Basándonos en el objeto original de legacy ([https://api.libreopcion.com.ar/vendedores](https://api.libreopcion.com.ar/vendedores)), lo migraremos para poder leerlo y editarlo

```
GET {API_URL_v4}/myStore
```

```
{
    "email": "bsaspc@libreopcion.com",
    "telefono": "4-636-3407",
    "whatsapp": "",
    "web": "",
    "retiroPorLocal": true,
    "horarioAtencion": "0",
    "cp": "1407",
    "direccion": "Medina 351",
    "ciudad": {
        "id": 1,
        "nombre": "A. A. FERNANDEZ",
        "provincia_id": 20832,
        "total": 0
    },
    "provincia": {
        "id": 20832,
        "key": 20832,
        "nombre": "BUENOS AIRES",
        "pais_id": 0,
        "total": 0,
        "ciudad_defecto_id": 0
    },
    "pais": {
        "id": null,
        "nombre": null,
        "total": null
    },
    "mensajePedido": "Gracias por tu compra!",
    "utilidad": 22,
    "razonSocial": "",
    "ciudadID": 1,
    "provinciaID": 20832,
    "paisID": null,
    "estado": {
        "estado": 0
    },
    "id": 22,
    "nombre": "BsAsPC",
    "uri": "buenos-aires-pc",
    "key": 22,
    "img": "67950734a4fe424a34f619b9889c004e.jpeg",
    "esReseller": true,
    "total": 0,
    "activo": false
}
```

```
PATCH {API_URL_v4}/myStore
```

```
{
    "email": "bsaspc@libreopcion.com",
    "telefono": "4-636-3407",
    "whatsapp": "",
    "web": "",
    "retiroPorLocal": true,
    "horarioAtencion": "0",
    "cp": "1407",
    "direccion": "Av. Jujuy 1039",
    "mensajePedido": "Gracias por tu compra!",
    "utilidad": 22,
    "razonSocial": "",
    "ciudadID": 1,
    "provinciaID": 20832,
    "id": 22,
    "nombre": "BsAsPC",
    "uri": "buenos-aires-pc",
    "key": 22,
    "img": "67950734a4fe424a34f619b9889c004e.jpeg",
    "activo": false
}
```
