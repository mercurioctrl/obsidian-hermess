---
jira_key: "PED-1053"
aliases: ["PED-1053"]
summary: "API - Refactor - Agregar seteo para nueva lista E de precios"
status: "Finalizada"
type: "Subtarea"
priority: "High"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-07-17 09:53"
updated: "2025-07-18 10:33"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1053"
---

# PED-1053: API - Refactor - Agregar seteo para nueva lista E de precios

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | High |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-07-17 09:53 |
| Actualizado | 2025-07-18 10:33 |
| Etiquetas | ninguna |
| Jira | [PED-1053](https://bluinc.atlassian.net/browse/PED-1053) |

## Relaciones

- **Padre:** [[PED-600]] Edicion/Alta de cliente

## Descripcion

Revisaremos si es necesario algun cambio para cuando en `profile` seteamos valor 5, para la nueva lista E

```
PATCH {API_URL}/v1/clients/{clientId}
```

```
{
    "clientId": 83681,
    "email": "ezequielferrari712@gmail.com",
    "provinceId": 0,
    "localityId": 0,
    "address": "Gral. Urquiza 379 planta alta ",
    "cuil": "32814789",
    "clientName": "Ezequiel Maronna iralour",
    "commercialName": "Ezequiel Maronna iralour",
    "postalCode": "1617",
    "telephone": "1127182069",
    "telephone2": "",
    "typeDocument": 4,
    "category": 3,
    "whaPhone": "",
    "companyCode": 4,
    "profile": 5, <--- Eso es lo que ahora debe ser sensible al valor 5
    "currencyId": 1,
    "salespersonId": 33,
    "specialPrice": 0
}
```

[adjunto]
