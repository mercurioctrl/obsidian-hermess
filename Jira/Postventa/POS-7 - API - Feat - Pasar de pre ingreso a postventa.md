---
jira_key: "POS-7"
aliases: ["POS-7"]
summary: "API - Feat - Pasar de pre ingreso a postventa"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-07-14 14:26"
updated: "2022-10-04 09:31"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-7"
---

# POS-7: API - Feat - Pasar de pre ingreso a postventa

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-07-14 14:26 |
| Actualizado | 2022-10-04 09:31 |
| Etiquetas | ninguna |
| Jira | [POS-7](https://bluinc.atlassian.net/browse/POS-7) |

## Relaciones

- **Padre:** [[POS-5]] API - Feat - Enviar correo con el preingreso de postventa

## Descripcion

```
POST {API_URL}/v1/processPreAfterSales
```

Se debe generar un fichero que sirva para procesar (a través de un token o similar) una solicitud o pre ingreso de mercadería para covnertirla en un ingreso.

Es decir  

Pasasr los preingresos a `ST_RMACABECERA` y `ST_RMADETALLE`
