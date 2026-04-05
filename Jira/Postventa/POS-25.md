---
jira_key: "POS-25"
summary: "API - Feat - Asignar técnico "
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-07-18 10:14"
updated: "2022-10-04 11:37"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-25"
---

# POS-25: API - Feat - Asignar técnico 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-07-18 10:14 |
| Actualizado | 2022-10-04 11:37 |
| Etiquetas | ninguna |
| Jira | [POS-25](https://bluinc.atlassian.net/browse/POS-25) |

## Descripción

Se trata del recurso encargado de designar a la persona responsable de testear un ingreso de mercaderia

```
PATCH {API_URL}/v1/aftersales/{afterSaleId}
```

Carga útil:

```
{
  agentId: 6
}
```

Lo que se requiere es marcar que ‘agente’ seguirá el caso para eso le pasamos `agentId`, de la lista que proviene de [link](https://lioteam.atlassian.net/browse/POS-26) 

En caso de que las columnas tengan otra clave para vincularse con el agente, poner la adecuada que este vinculada a agentId (si tenes dudas con esto consultame  )
