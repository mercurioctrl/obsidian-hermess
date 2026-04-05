---
jira_key: "NBWEB-92"
aliases: ["NBWEB-92"]
summary: "Conmutadores"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2022-04-05 10:25"
updated: "2022-06-21 21:34"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-92"
---

# NBWEB-92: Conmutadores

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2022-04-05 10:25 |
| Actualizado | 2022-06-21 21:34 |
| Etiquetas | ninguna |
| Jira | [NBWEB-92](https://bluinc.atlassian.net/browse/NBWEB-92) |

## Relaciones

- **Padre:** [[NBWEB-61]] Buscador
- **is blocked by:** [[NBWEB-28]] Cambio de datos de usuario
- **is blocked by:** [[NBWEB-106]] Agregar parametros (conmutadores) al objeto user

## Descripcion

Se trata de los conmutadores de precio y stock y moneda

**Condición de IVA**: Este conmutador quita y agrega el iva al precio que se esta mostrando. Los parametros para el calculo se encuentra en el objeto del item.

**Stock:** Muestra los productos que están en stock, o bien todos los productos (ver el recurso en postman, que tiene un parámetro para filtrar esto)

**Divisa**: El conmutador de divisa solo opera multiplicando a el precio original (en dolares)  por la cotizacion. Esto debe aplicar tanto cuando veo el precio “sin iva”, como cuando lo veo “final”.
