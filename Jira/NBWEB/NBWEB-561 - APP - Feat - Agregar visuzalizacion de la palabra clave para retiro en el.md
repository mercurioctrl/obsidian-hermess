---
jira_key: "NBWEB-561"
aliases: ["NBWEB-561"]
summary: "APP - Feat - Agregar visuzalizacion de la palabra clave para retiro en el apartado Mi cuenta > Postventa"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Guillermo Avila"
reporter: "Catriel Mercurio"
created: "2023-07-19 12:28"
updated: "2024-04-16 12:17"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-561"
---

# NBWEB-561: APP - Feat - Agregar visuzalizacion de la palabra clave para retiro en el apartado Mi cuenta > Postventa

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Guillermo Avila |
| Reportado por | Catriel Mercurio |
| Creado | 2023-07-19 12:28 |
| Actualizado | 2024-04-16 12:17 |
| Etiquetas | ninguna |
| Jira | [NBWEB-561](https://bluinc.atlassian.net/browse/NBWEB-561) |

## Relaciones

- **Padre:** [[NBWEB-559 - Palabra clave visible por el usuario para el apartaado Mi cuenta Postventa|NBWEB-559]] Palabra clave visible por el usuario para el apartaado Mi cuenta > Postventa

## Descripcion

De la misma forma que se hizo para los pedidos, agregaremos en el recurso

```
{API_URL}/v1/miCuenta/postventa
```

el parametro `secretKey` para que el ususario pueda ver la palabra clave de retiro en el caso de que exista



Este es un ejemplo ilustrativo de como se realizo lo mismo para la seccion de pedidos

[adjunto]
