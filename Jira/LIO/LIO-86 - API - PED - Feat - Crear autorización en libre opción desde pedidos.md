---
jira_key: "LIO-86"
aliases: ["LIO-86"]
summary: "API - PED - Feat - Crear autorización en libre opción desde pedidos"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-08-09 09:05"
updated: "2024-08-16 03:36"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-86"
---

# LIO-86: API - PED - Feat - Crear autorización en libre opción desde pedidos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-08-09 09:05 |
| Actualizado | 2024-08-16 03:36 |
| Etiquetas | ninguna |
| Jira | [LIO-86](https://bluinc.atlassian.net/browse/LIO-86) |

## Relaciones

- **Padre:** [[LIO-28]] El sitio debe funcionar correctamente, sin puntos grises o cosas que no se entienden
- **blocks:** [[LIO-87]] APP - Feat - Pantalla de autologin (similar como se trabajo en NB)

## Descripcion

```
POST {API_URL}/v1/getLoWebAuthorization
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

Es muy parecido o igual a lo que se hizo en NB pero usa otras tablas obviamente
