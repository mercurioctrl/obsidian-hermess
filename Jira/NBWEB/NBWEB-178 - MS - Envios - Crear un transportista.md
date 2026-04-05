---
jira_key: "NBWEB-178"
aliases: ["NBWEB-178"]
summary: "MS - Envios - Crear un transportista"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-05-13 07:47"
updated: "2022-07-01 17:40"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-178"
---

# NBWEB-178: MS - Envios - Crear un transportista

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-05-13 07:47 |
| Actualizado | 2022-07-01 17:40 |
| Etiquetas | ninguna |
| Jira | [NBWEB-178](https://bluinc.atlassian.net/browse/NBWEB-178) |

## Relaciones

- **Padre:** [[NBWEB-76]] API - Implementar MS envios

## Descripcion

Solo con rol administrador

```
POST {{API_URL}}/v1/shipper
```

Request

```
{
  description: 'Nombre del transportista' // ej: Moto Ned Flanders
  type: 1 // este es un id, para una futura tablas de tipos. Hoy no es necesaria, pero dejarlo en la estructur es util. Por ahora siempre es 1.
}
```
