---
jira_key: "PED-41"
aliases: ["PED-41"]
summary: "API - Feat - Crear autorizacion en la api de ordenes"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-08-21 19:50"
updated: "2023-08-22 13:09"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-41"
---

# PED-41: API - Feat - Crear autorizacion en la api de ordenes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-08-21 19:50 |
| Actualizado | 2023-08-22 13:09 |
| Etiquetas | ninguna |
| Jira | [PED-41](https://bluinc.atlassian.net/browse/PED-41) |

## Relaciones

- **Padre:** [[PED-40]] Login automático como cliente
- **blocks:** [[PED-43]] APP - Feat - Pedir autorizacion y redirigir 
- **blocks:** [[PED-42]] API - Feat - Login mediante autorizacion en el sitio web 

## Descripcion

```
POST {API_URL}/v1/getWebAuthorization
```

```
{
  clientId: 34234
}
```

Retorna:

```
{
    "status": "success",
    "data": [
        {
            "token": "d25cedf7ae63c2702cb2b30d194a78f2",
            "expirationDate": "02/12/1987 12:37"
        }
    ]
}
```

## ¿Que hace?

Lo que haremos es crear un token de autorización en una tabla, junto a una fecha de expirar, el id de cliente, el id del agente y otros datos que se necesiten en la implementacion que pidió el token. El token dura 5 minutos (Este parámetro esta entre las variables de entorno)
