---
jira_key: "PED-1054"
aliases: ["PED-1054"]
summary: "APP - Refactor - Agregar seteo para nueva lista E de precios"
status: "Finalizada"
type: "Subtarea"
priority: "Highest"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-07-17 09:53"
updated: "2025-07-18 10:33"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1054"
---

# PED-1054: APP - Refactor - Agregar seteo para nueva lista E de precios

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Highest |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-07-17 09:53 |
| Actualizado | 2025-07-18 10:33 |
| Etiquetas | ninguna |
| Jira | [PED-1054](https://bluinc.atlassian.net/browse/PED-1054) |

## Relaciones

- **Padre:** [[PED-600]] Edicion/Alta de cliente

## Descripcion

Agregaremos la nueva LISTA E (5)

Ademas, cambiaremos unpoco la forma en que lo mostramos

Ahora

- Perfil 0


- Perfil 1


- Perfil 2


- Perfil 3


- Perfil 4



Despues

Ahora

- Perfil A - 1


- Perfil B - 2


- Perfil C - 3


- Perfil D - 4


- Perfil E - 5
(EL PERFIL  0 YA NO LO MOSTRAREMOS POR EL MOMENMTO)



---

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
