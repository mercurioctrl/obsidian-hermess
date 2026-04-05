---
jira_key: "INV-85"
aliases: ["INV-85"]
summary: "APP - Refactor - Obtener sugerencia de descripción auto generada con IA"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2024-07-17 10:25"
updated: "2024-07-20 21:13"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-85"
---

# INV-85: APP - Refactor - Obtener sugerencia de descripción auto generada con IA

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2024-07-17 10:25 |
| Actualizado | 2024-07-20 21:13 |
| Etiquetas | ninguna |
| Jira | [INV-85](https://bluinc.atlassian.net/browse/INV-85) |

## Relaciones

- **Padre:** [[INV-80 - Descripciones|INV-80]] Descripciones
- **is blocked by:** [[INV-84 - API - Refactor - Incorporar codigo para autogenerar descripciones con IA|INV-84]] API - Refactor - Incorporar codigo para autogenerar descripciones con IA

## Descripcion

Crearemos un formulario para obtener una sugerencia basándonos en el recurso [link](https://lioteam.atlassian.net/browse/INV-84) 

Debe ser fácil de generar, con la menor cantidad de clics posibles se debe mostrar la sugerencia y poder guardarla remplazando la descripción actual.

Se debe mostrar un boton par editar antes de guardar.

Se debe poder introducir informacion en cualquier formato con el parámetro `characteristics`

Tengo 10 niveles posibles de determinismo siendo:
- 0.0 (determinista): La salida es muy predecible y siempre selecciona las palabras más probables.

- 1.0 (alta aleatoriedad): La salida es más creativa y menos predecible, eligiendo entre una variedad más amplia de opciones posibles.



```
POST {API_URL}/v1/suggestDescription
```

```
 {
    "characteristics": informacion copiada asi nomas de lo sitios oficiales,
    "itemId": 118865,
    "temperature": 0.2
  },
```
