---
jira_key: "LIO-222"
aliases: ["LIO-222"]
summary: "APP - Refactor/Research - Bajar TBT del sitio"
status: "Finalizada"
type: "Subtarea"
priority: "High"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-02-13 12:27"
updated: "2025-03-16 17:44"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-222"
---

# LIO-222: APP - Refactor/Research - Bajar TBT del sitio

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | High |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-02-13 12:27 |
| Actualizado | 2025-03-16 17:44 |
| Etiquetas | ninguna |
| Jira | [LIO-222](https://bluinc.atlassian.net/browse/LIO-222) |

## Relaciones

- **Padre:** [[LIO-9]] Optimización

## Descripcion

Me gustaría volver a repasar algunas cuestiones de performance
Una de las cosas que podemos revisar para reducir los bloqueos y tiempos al ingresar a la home son las sugerencias que hace el propio Lighouse
En especial las dos primeras


[adjunto]
Segun vi en algun research veloz sacando en limpio repasaria para empezar estas cositas, si hay que simplificar algun diseño en pos de sacar elementos me parece bien tambien, lo podemos charlar.

-  Revisar code-splitting y lazy-loading en Vue.


-  Optimizar dependencias y analizar el bundle con webpack-bundle-analyzer


-  Revisa watchers y computed properties, usa debounce si es necesario.


-  Reduce el número de elementos DOM y evita renders innecesarios.



Todo lo que investigues y cada puntito que se logre bajar  de cualquier forma vale la pena   

Actualmente la puntuación que me da a mi es esta

[adjunto]
