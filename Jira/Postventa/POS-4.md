---
jira_key: "POS-4"
summary: "API - Feat - Listar ingresos de postventa"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-07-13 14:25"
updated: "2022-10-04 09:55"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-4"
---

# POS-4: API - Feat - Listar ingresos de postventa

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-07-13 14:25 |
| Actualizado | 2022-10-04 09:55 |
| Etiquetas | ninguna |
| Jira | [POS-4](https://bluinc.atlassian.net/browse/POS-4) |

## Descripción

Se trata del recurso basico  que permite listar las postventas propiamente dichas, una vez que se pasaron desde el preingreso, o bien se crearon directamente.

```
GET {API_URL}/v1/aftersales
```

Retorna

```json
[{

aftersaleId : 3244,
clientId: 23423,
clientName: 'Nombre del cliente',
admissionDate: '12-10-2021 00:00',
status: 'Sin Revisar',
dispatched: true,
dispatchedDate: '12-10-2021 00:00',
agentName: 'Nombre agente soporte tecnico',
agentId: 'Nombre agente soporte tecnico',
'elapsedTimeTesting': '24m',
'elapsedTime': '25h'

},
{

aftersaleId : 3244,
clientId: 23423,
clientName: 'Nombre del cliente',
admissionDate: '12-10-2021 00:00',
status: 'Sin Revisar',
dispatched: true,
dispatchedDate: '12-10-2021 00:00',
agentName: 'Nombre agente soporte tecnico',
agentId: 'Nombre agente soporte tecnico',
'elapsedTimeTesting': '24m',
'elapsedTime': '25h'

}]
```

 Se deben utilizar principalmente las tablas 

`ST_RMACABECERA` y `ST_RMADETALLE`

pero puede haber mas, en ese caso podemos verlo.
