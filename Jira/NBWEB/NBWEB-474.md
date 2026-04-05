---
jira_key: "NBWEB-474"
summary: "INTEL Campaña gamer Call of Duty W"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-08-24 09:31"
updated: "2022-08-24 14:32"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-474"
---

# NBWEB-474: INTEL Campaña gamer Call of Duty W

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-08-24 09:31 |
| Actualizado | 2022-08-24 14:32 |
| Etiquetas | ninguna |
| Jira | [NBWEB-474](https://bluinc.atlassian.net/browse/NBWEB-474) |

## Descripción

Se requiere que el recurso de catalogo:

```
{API_URL}/v1/?product_id={Id_de_producto}
```

Pueda retornar un conjunto de productos, en lugar de uno solo. Esto permitirá hacer acciones mas especificas, de un conjunto de productos muy exacto, y que esto tenga su propio link.

**¿como podría ser?**

```
{API_URL}/v1/?product_id={Id_de_producto},{Id_de_producto},{Id_de_producto},{Id_de_producto}
```

Tal vez podemos usar el mismo parametro, pero que funcione tanto para uno solo, como para varios si se los paso separados por una coma.

Contame que te parece si lo hacemos así, o bien si se te ocurre una forma mejor.

---

Catri! tal como hablamos personalmenta, la idea es poder subir un banner a la home de LO y que este banner linkee a un filtro de intel donde solo aparezcan estos productos: 

i5 11400 (111351)

i7 11700 (109539)

i7 11700F (115899)

i7 11700F (109181)

I7 12700K (115776)

i9 12900k (115777)

se puede?
