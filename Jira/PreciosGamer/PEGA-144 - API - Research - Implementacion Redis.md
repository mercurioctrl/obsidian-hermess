---
jira_key: "PEGA-144"
aliases: ["PEGA-144"]
summary: "API - Research - Implementacion Redis"
status: "Finalizada"
type: "Tarea"
priority: "Lowest"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-11-12 15:53"
updated: "2024-11-22 00:50"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-144"
---

# PEGA-144: API - Research - Implementacion Redis

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Lowest |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-11-12 15:53 |
| Actualizado | 2024-11-22 00:50 |
| Etiquetas | ninguna |
| Jira | [PEGA-144](https://bluinc.atlassian.net/browse/PEGA-144) |

## Relaciones

- **Padre:** [[PEGA-2 - Catalogos y Buscador|PEGA-2]] Catalogos y Buscador

## Descripcion

Configurar Redis y realizar una prueba con nuestras principales consultas en Laravel. Queremos ver cuánto impacto puede tener esta mejora y si logramos reducir la carga de la base de datos, optimizar el uso de sesiones y mejorar la experiencia del usuario en este proyecyo que tiene datos y es muy pesado y  si la prueba es exitosa ver de como lo trasladariamos a libre opcion u otro proyecto donde sea importante la velocidad.

Si condisderas que queres hacer pruebas en produ directo (porque tiene otra db y otra velocidad) te paso acceso

Al probar Redis, podríamos encontrar una forma de llevar nuestra aplicación al siguiente nivel en términos de rapidez y eficiencia pero ademas nos sirve para probar la herramienta en este caso de uso que es mas bien simple y luego pasar a aplicarlo en apis mas complejas.
