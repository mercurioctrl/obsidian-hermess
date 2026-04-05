---
jira_key: "PED-444"
aliases: ["PED-444"]
summary: "API - Feat - Unir pedido a otro envio "
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-01-04 14:21"
updated: "2024-01-09 18:04"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-444"
---

# PED-444: API - Feat - Unir pedido a otro envio 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-01-04 14:21 |
| Actualizado | 2024-01-09 18:04 |
| Etiquetas | ninguna |
| Jira | [PED-444](https://bluinc.atlassian.net/browse/PED-444) |

## Relaciones

- **Padre:** [[PED-123]] Feat - Liquidar pedido
- **blocks:** [[PED-447]] APP - Feat - Unir pedido a otro envío (pedido)

## Descripcion

Lo primero que haremos es crear una tabla nueva

`[NewBytes_DBF].[dbo].[albclitJoinShipping]`

- id (auto)


- ID_NROREMCLI_ENC_HOST


- ID_NROREMCLI_ENC


- date (hora y fecha de insercion)



---

Lo que haremos sera agregar a esa tabla, cada uno de los pedidos que salen juntos. Para esto utilizaremos (crearemos) el siguiente recurso

```
POST {{API_URL}}/v1/orders/joinShipping
```

```
{
  host: 'X001000021834',
  guest: 'X001000021832'
}
```

El parámetro `host` es el que guardaremos en ID_NROREMCLI_ENC_HOST

El parámetro `guest` es el que guardaremos en ID_NROREMCLI_ENC

Para poder hacer esto SIEMPRE se debe verificar que el `host` no solo este liquidado, sino que tenga un envio vigente.. sino no se puede adjuntarle mas mercadería al mismo envio
