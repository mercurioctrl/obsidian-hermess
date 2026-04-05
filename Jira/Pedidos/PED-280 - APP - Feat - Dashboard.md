---
jira_key: "PED-280"
aliases: ["PED-280"]
summary: "APP - Feat - Dashboard"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2023-11-24 08:12"
updated: "2025-03-29 17:08"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-280"
---

# PED-280: APP - Feat - Dashboard

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2023-11-24 08:12 |
| Actualizado | 2025-03-29 17:08 |
| Etiquetas | ninguna |
| Jira | [PED-280](https://bluinc.atlassian.net/browse/PED-280) |

## Relaciones

- **Padre:** [[PED-242 - Pestaña Estadisticas|PED-242]] Pestaña Estadisticas
- **is blocked by:** [[PED-424 - APP - Refactor - Dashboard - Tasa de conversión|PED-424]]   APP - Refactor - Dashboard - Tasa de conversión
- **relates to:** [[PED-981 - APP - Refactor - Dashboard - Visualizar mensaje de error del total facturado|PED-981]] APP - Refactor - Dashboard -> Visualizar mensaje de error del total facturado

## Descripcion

Crearemos un dashboard donde los vendedores puedan ver en un vistazo rápido sus parámetros y métricas mas relevantes.

En todos los casos, pre-inicializaremos los parámetros para verlos con un mes de distancia para atrás.

### Ejemplos:

[adjunto]
[adjunto]
[adjunto]
Como se aprecia en los ejemplos, hay distintos tipos de elementos.

- Histogramas


- Métricas (Son los cuadritos con un numero y una flecha que indica tendencia)


- Listas


- Ruedas de objetivos alcanzados



### ¿Que vamos a usar nosotros de todo esto?

En la primera linea pondremos cuadros de “Metricas”

- Ventas totales [link](https://lioteam.atlassian.net/browse/PED-282) 


- Ticket promedio [link](https://lioteam.atlassian.net/browse/PED-281) 


- Tasa de conversión [link](https://lioteam.atlassian.net/browse/PED-260) 


- Tasa de reactivacion de clientes [link](https://lioteam.atlassian.net/browse/PED-259) 


- Tasa de retención de clientes [link](https://lioteam.atlassian.net/browse/PED-246) 




Flecha de tendencia: Para poder mostrar esto, nos encargaremos de obtener por cada metrica, 2 valores. El del periodo en curso (Ultimos 30 dias) y el de el periodo anterior (30 dias precios, a el primer dia de estos 30)

[Esta historia continua]
