---
jira_key: "PED-493"
aliases: ["PED-493"]
summary: "API - Feat - Mejorar performance para ver la cuenta en ciertos clientes"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-01-17 09:08"
updated: "2024-01-26 05:03"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-493"
---

# PED-493: API - Feat - Mejorar performance para ver la cuenta en ciertos clientes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-01-17 09:08 |
| Actualizado | 2024-01-26 05:03 |
| Etiquetas | ninguna |
| Jira | [PED-493](https://bluinc.atlassian.net/browse/PED-493) |

## Relaciones

- **Padre:** [[PED-54 - Cuenta corriente de clientes|PED-54]] Cuenta corriente de clientes

## Descripcion

Basándonos en la consulta en producción, del siguiente recurso, para el siguiente cliente

```
GET {API_URL}/v1/currentAccount/23124
```

Buscaremos estrategias para cumplir *la regla de los dos segundos*

Detectaremos los elementos que estén demorando la entrega del recurso y buscaremos soluciones o alternativas.

Puede ser tanto como se ejecuta la consulta a la base de datos, como programáticas.

Cualquier cosa lo vemos
