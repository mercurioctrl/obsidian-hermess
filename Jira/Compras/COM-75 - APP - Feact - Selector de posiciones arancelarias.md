---
jira_key: "COM-75"
aliases: ["COM-75"]
summary: "APP - Feact - Selector de posiciones arancelarias"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2024-03-22 08:34"
updated: "2024-05-24 21:11"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-75"
---

# COM-75: APP - Feact - Selector de posiciones arancelarias

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2024-03-22 08:34 |
| Actualizado | 2024-05-24 21:11 |
| Etiquetas | ninguna |
| Jira | [COM-75](https://bluinc.atlassian.net/browse/COM-75) |

## Relaciones

- **Padre:** [[COM-38 - Ver orden de compra|COM-38]] Ver orden de compra
- **blocks:** [[COM-88 - API - Feat - Patch para agregar posiciones arancelarias externas a las locales|COM-88]] API - Feat - Patch para agregar posiciones arancelarias externas a las locales o en su defecto agregar la descripcion de las posiciones arancelarias a la orden
- **is blocked by:** [[COM-91 - API - Feat - Listar categorías|COM-91]] API - Feat - Listar categorías

## Descripcion

Tal como lo hablamos en la daily, incluiremos en la columna de posiciones arancelarias un selector que usaremos con los recursos de [link](https://lioteam.atlassian.net/browse/COM-71) .

[adjunto]
- Si la posición ya esta cargada, la mostraremos cargada en el selector 


- Si la posición no esta, o es incorrecta, tengo que podes buscarla entre las posiciones que ya tengo en mi sistema con el recurso ({{API_URL}}/v1/tariffPosition?position=3810.10.20.000H)  (Ver en postman) ya sea por posición o descripción


- Si no encuentro la posición, levantare un modal que me permita agregarla utilizando el recurso {{API_URL}}/v1/tariffPositionExternal?search=8471.60.53.000Q (Ver en postman)
