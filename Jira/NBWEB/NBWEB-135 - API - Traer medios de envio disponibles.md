---
jira_key: "NBWEB-135"
aliases: ["NBWEB-135"]
summary: "API -  Traer medios de envio disponibles"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-04-25 16:07"
updated: "2022-06-26 21:33"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-135"
---

# NBWEB-135: API -  Traer medios de envio disponibles

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-04-25 16:07 |
| Actualizado | 2022-06-26 21:33 |
| Etiquetas | ninguna |
| Jira | [NBWEB-135](https://bluinc.atlassian.net/browse/NBWEB-135) |

## Relaciones

- **Padre:** [[NBWEB-11]] API - Implementar Cotizadores de envio

## Descripcion

```
GET {{API_URL}}/v1/carrito/calcularEnvioPara/{codigoPostalFavorito}
```

Utilizando el recurso en [link](https://lioteam.atlassian.net/browse/NBWEB-80) se debe cotizar el carrito activo, utilizando el código postal del envío marcado como favorito
