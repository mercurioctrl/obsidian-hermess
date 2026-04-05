---
jira_key: "EXP-421"
aliases: ["EXP-421"]
summary: "API - Refactor - Ajustar recurso de conteo para tambien contabilizar pesos y medidas"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-07-24 10:13"
updated: "2024-09-30 06:36"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-421"
---

# EXP-421: API - Refactor - Ajustar recurso de conteo para tambien contabilizar pesos y medidas

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-07-24 10:13 |
| Actualizado | 2024-09-30 06:36 |
| Etiquetas | ninguna |
| Jira | [EXP-421](https://bluinc.atlassian.net/browse/EXP-421) |

## Relaciones

- **Padre:** [[EXP-17]] Feat - Listar productos (Control de stock)
- **blocks:** [[EXP-422]] APP - Refactor - En el modulo de conteo se deben poder visualizar y editar tambien medidas y pesos
- **relates to:** [[EXP-423]] API - Ajustar recurso de conteo para tambien contabilizar pesos y medidas - Sugerencia de mejora en el mensaje de respuesta
- **has action item:** [[EXP-451]] API - Refactor-  Agregar al .env un parametro (true/false) para activar/desactivar la validacion de medidas antes de cargar un producto

## Descripcion

Se debe a la edicion del producto el peso y las medidas, para cuando se realiza el conteo, poder ir relevando las medidas exactas. 

Puede recibir cualquiera de los atributos, o todos. Si no recibo el parametro de conteo, ni toco esa tabla, solo la de las medidas (articulos).

- `weightAverage`


- `lengthAverage`


- `widthAverage`


- `highAverage`



```
PATCH {API_URL}/v1/items
```

```
[
  {
  "Id":"104964",
  "weightAverage": 34,
  "lengthAverage": 34,
  }
]
```
