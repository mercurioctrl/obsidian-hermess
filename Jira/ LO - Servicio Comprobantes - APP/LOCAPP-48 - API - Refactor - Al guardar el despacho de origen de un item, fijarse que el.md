---
jira_key: "LOCAPP-48"
aliases: ["LOCAPP-48"]
summary: "API - Refactor - Al guardar el despacho de origen de un item, fijarse que el formato sea el correcto, sino no gurdarlo"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-05-29 07:17"
updated: "2024-06-04 14:48"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LOCAPP-48"
---

# LOCAPP-48: API - Refactor - Al guardar el despacho de origen de un item, fijarse que el formato sea el correcto, sino no gurdarlo

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-05-29 07:17 |
| Actualizado | 2024-06-04 14:48 |
| Etiquetas | ninguna |
| Jira | [LOCAPP-48](https://bluinc.atlassian.net/browse/LOCAPP-48) |

## Relaciones

- **Padre:** [[LOCAPP-23 - Generar un comprobante|LOCAPP-23]] Generar un comprobante

## Descripcion

Dado que me encontre casos, donde en compras locales Dani marca en el numero de despacho el nombre del lugar donde lo compro

ver ejemplos:

```
select nroDespacho from  [NewBytes_DBF].[dbo].[FP_FactWebCliDetalle]  
WHERE (LEN(nroDespacho) <> 20 and LEN(nroDespacho) <> 13) AND nroDespacho IS NOT NULL
```

Y como eso no puede figurar en la factura, me vi en la obligacion de correr la siguiente query (habia muchos)

```
UPDATE [NewBytes_DBF].[dbo].[FP_FactWebCliDetalle] SET nroDespacho = NULL
WHERE (LEN(nroDespacho) <> 20 and LEN(nroDespacho) <> 13) AND nroDespacho IS NOT NULL
```

Estaría bueno que si no cumplen con esos criterios, osea si no tienen los 20 caracteres o los 13 caracteres que puede tener el formato de este numero, no se guarden.

O bien si se guardan, hacer una limpieza posterior a cada guardado como hice con esa query para que no queden los datos que sabemos que son erroneos por no cumplir la mascara.
