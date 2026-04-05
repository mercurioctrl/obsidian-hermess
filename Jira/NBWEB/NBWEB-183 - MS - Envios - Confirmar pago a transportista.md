---
jira_key: "NBWEB-183"
aliases: ["NBWEB-183"]
summary: "MS - Envios - Confirmar pago a transportista"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-05-13 09:07"
updated: "2022-11-09 11:31"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-183"
---

# NBWEB-183: MS - Envios - Confirmar pago a transportista

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-05-13 09:07 |
| Actualizado | 2022-11-09 11:31 |
| Etiquetas | ninguna |
| Jira | [NBWEB-183](https://bluinc.atlassian.net/browse/NBWEB-183) |

## Relaciones

- **Padre:** [[NBWEB-76]] API - Implementar MS envios

## Descripcion

Solo debe poder ejecutar este recurso quien tenga rol ‘Administrador’

```
PUT {{API_URL}}/v1/shipping/makePayment
```

Request

```
{
  deilverysId [
  23,45,32
  ]
}
```



Se trata de un recurso para marcar los envíos que ya se cancelaron con el transportista. Suiele hacerse siempre en intervalos desde el un back office así que le pasamos los ide de los envíos.
