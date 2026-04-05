---
jira_key: "LIO-74"
aliases: ["LIO-74"]
summary: "API - Refactor - Corregir ruta al formato del nuevo servidor de imagenes"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-07-23 12:35"
updated: "2024-07-23 21:03"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-74"
---

# LIO-74: API - Refactor - Corregir ruta al formato del nuevo servidor de imagenes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-07-23 12:35 |
| Actualizado | 2024-07-23 21:03 |
| Etiquetas | ninguna |
| Jira | [LIO-74](https://bluinc.atlassian.net/browse/LIO-74) |

## Relaciones

- **Padre:** [[LIO-28 - El sitio debe funcionar correctamente, sin puntos grises o cosas que no se|LIO-28]] El sitio debe funcionar correctamente, sin puntos grises o cosas que no se entienden

## Descripcion

Al abrir los correos de libre opcion observamos que estan llegando mal las imagenes, el logo, los productos, etc.

Esto se debe a que cambio el formato de la ruta

[adjunto]
En el mail figura asi

[https://static.libreopcion.com/img/w/100/b2045eb1ea2612ec2049af2a0e2f945b.jpeg](https://static.libreopcion.com/img/w/100/b2045eb1ea2612ec2049af2a0e2f945b.jpeg) (formato viejo que ya no funciona)

Cuando deberia tener este formato para esa imagen

[https://static.libreopcion.com/i/lio_mail_size_w100_b2045eb1ea2612ec2049af2a0e2f945b.jpeg](https://static.libreopcion.com/i/lio_mail_size_w100_b2045eb1ea2612ec2049af2a0e2f945b.jpeg)
