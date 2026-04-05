---
jira_key: "EXP-445"
aliases: ["EXP-445"]
summary: "API - Refactor - Cuando se ejecuta la acción de devolución por faltante (que envía el stock a control)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-09-13 12:39"
updated: "2024-10-01 09:26"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-445"
---

# EXP-445: API - Refactor - Cuando se ejecuta la acción de devolución por faltante (que envía el stock a control)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-09-13 12:39 |
| Actualizado | 2024-10-01 09:26 |
| Etiquetas | ninguna |
| Jira | [EXP-445](https://bluinc.atlassian.net/browse/EXP-445) |

## Relaciones

- **Padre:** [[EXP-424]] Controles de stock al despachar
- **relates to:** [[EXP-454]] API - Devolución por faltante - Oportunidad de mejora en la visualización del correo

## Descripcion

Cuando se ejecuta [link](https://lioteam.atlassian.net/browse/EXP-426)  y se envía el stock a control se debe enviar un correo a 

[gerencia@nb.com.ar](mailto:gerencia@nb.com.ar) y [logistica@nb.com.ar](mailto:logistica@nb.com.ar)  (estos mail si no estan en el .env hay que agregarlos como mails estandar de los sectores)

Con el mensaje:

---

Asunto: Se realizo CRÉDITO por FALTANTE

El usuario **{nombreUser}** acredito 

**{cantidad}**  - **{idDelProducoto}** - **{nombreDelProducto}** 

**{cantidad}**  - **{idDelProducoto}** - **{nombreDelProducto}** 



Se enviara a control de stock, porque lo marco como un faltante.
