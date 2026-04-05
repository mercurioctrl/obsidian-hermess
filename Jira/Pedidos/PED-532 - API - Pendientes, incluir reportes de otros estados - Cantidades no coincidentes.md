---
jira_key: "PED-532"
aliases: ["PED-532"]
summary: "API - Pendientes, incluir reportes de otros estados - Cantidades no coincidentes"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2024-02-06 01:31"
updated: "2024-02-19 15:58"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-532"
---

# PED-532: API - Pendientes, incluir reportes de otros estados - Cantidades no coincidentes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2024-02-06 01:31 |
| Actualizado | 2024-02-19 15:58 |
| Etiquetas | ninguna |
| Jira | [PED-532](https://bluinc.atlassian.net/browse/PED-532) |

## Relaciones

- **Padre:** [[PED-252]] Integración Soporte (Jira)
- **blocks:** [[PED-524]] API- Feat - Al igual que se hizo con el estado "waiting for customer" contaremos aquellso reportes que estan en otros estados

## Descripcion

Cuando consulto el listado de reportes, noto que las cantidades no coinciden con los pendientes.

[adjunto]
[adjunto]
Este es un ejemplo, sin embargo, favor de verificar los demás estados:

- Finalizada


- Waiting For Customer


- Work in progress


- Waiting for support



---

Actualización 07/02/24
Ahora lo busque desde Jira con diferente token, las cantidades que no me resultaron coincidentes fueros `done` y `total`.
Si estoy buscándolas de manera incorrecta, házmelo saber Eze por favor.

[adjunto]
[adjunto]
[adjunto]
---

Actualización 09/02/24
Los parámetros `done` y `total` me aparecen con cantidades de diferencia de uno, te comparto la selección de filtros que estoy utilizando.
[Navegador de incidencias - Jira (atlassian.net)](https://lioteam.atlassian.net/issues/?jql=reporter%20in%20(712020%3Ac5277df7-ee2e-45ee-94cf-1d474c0c69f6)%20AND%20project%20%3D%20SNB%20AND%20status%20in%20(Canceled%2C%20Closed%2C%20Done%2C%20Resolved)%20ORDER%20BY%20summary%20ASC)

[adjunto]
[adjunto]
