---
jira_key: "EXP-93"
aliases: ["EXP-93"]
summary: "API - Feat - Agregar codigo unico a un item"
status: "Gamma"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-11-22 13:41"
updated: "2022-12-15 09:54"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-93"
---

# EXP-93: API - Feat - Agregar codigo unico a un item

| Campo | Valor |
|-------|-------|
| Estado | Gamma (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-11-22 13:41 |
| Actualizado | 2022-12-15 09:54 |
| Etiquetas | ninguna |
| Jira | [EXP-93](https://bluinc.atlassian.net/browse/EXP-93) |

## Relaciones

- **Padre:** [[EXP-17]] Feat - Listar productos (Control de stock)
- **blocks:** [[EXP-95]] APP - Feat - Agregar codigo universal a un producto

## Descripcion

Esta historia sirve para armar un formulario para completar el objeto, en caso de que este incompleto con alguno de los códigos únicos que luego utilizaremos

```
PATCH {API_URL}/v1/items/{IDiTEM}
```

```
{
gtin:883412740920
ean:0012345678905
isbn: 9788481300185
upc:012345678905
}
```

Cualquiera de ellos que este presente sirve, con que este uno es suficiente
