---
jira_key: "POS-251"
aliases: ["POS-251"]
summary: "API - Feat - Mandar productos a recupero"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-03-27 16:53"
updated: "2023-04-17 09:40"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-251"
---

# POS-251: API - Feat - Mandar productos a recupero

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-03-27 16:53 |
| Actualizado | 2023-04-17 09:40 |
| Etiquetas | ninguna |
| Jira | [POS-251](https://bluinc.atlassian.net/browse/POS-251) |

## Relaciones

- **Padre:** [[POS-235 - Postventa Proveedores Recepcion|POS-235]] Postventa Proveedores Recepcion
- **blocks:** [[POS-252 - APP - Feat - Mandar productos a recupero|POS-252]] APP - Feat - Mandar productos a recupero

## Descripcion

(hablar con juan) Según lo conversado en la daily, se agregara un recurso para enviar a recupero la mercadería. Es decir, ponerlo en la lista “Recuperos” de donde luego se hacen otras acciones como “Enviar al proveedor” o “Enviar al deposito”.

```
{{API_URL}}/v1/afterSales/{afterSaleDetailId}/finalized/recovery
```

Responde.

```
{
    "success": true,
    "msg": "El item ha sido enviado a recupero"
}
```

Y se deberia ver el item en la pestaña de recupero
