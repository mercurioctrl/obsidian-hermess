---
jira_key: "SNB-196"
aliases: ["SNB-196"]
summary: "agujero de seguridad informado por cliente"
status: "Resuelta"
type: "Support"
priority: "Medium"
assignee: "Catriel Mercurio"
reporter: "Julián Ramiro Albarracín"
created: "2022-07-12 14:04"
updated: "2023-01-11 15:22"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/SNB-196"
---

# SNB-196: agujero de seguridad informado por cliente

| Campo | Valor |
|-------|-------|
| Estado | Resuelta (Listo) |
| Tipo | Support |
| Prioridad | Medium |
| Asignado | Catriel Mercurio |
| Reportado por | Julián Ramiro Albarracín |
| Creado | 2022-07-12 14:04 |
| Actualizado | 2023-01-11 15:22 |
| Etiquetas | ninguna |
| Jira | [SNB-196](https://bluinc.atlassian.net/browse/SNB-196) |

## Relaciones

*Sin relaciones*

## Descripcion

Mientras tanto, te quería informar sobre un agujero de seguridad que ayer detecté en su nuevo sitio web.
La vulnerabilidad es que al consultar un comprobante (factura) de mi cuenta, puedo consultar también cualquier otro comprobante de otros clientes con solo modificar el nro. en el link.

Ejemplo de link a la última Factura mia:
[link](https://comprobantes.lio.red/?F=478671&show=1) 

Ejemplo de poder ver cualquier otra factura (solo le sumé 1 al ID):
[link](https://comprobantes.lio.red/?F=478672&show=1) 

Esto es algo muy obvio y serio, espero que este agujero lo puedan tapar pronto.

[1:37 p. m., 12/7/2022] Vallmitjana 11656: También quiero informar que ayer en casa armé un carrito de compras y hoy desde el laburo entré al sitio y el carrito está vacío.
