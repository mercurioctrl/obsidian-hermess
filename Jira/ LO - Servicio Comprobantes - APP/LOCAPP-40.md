---
jira_key: "LOCAPP-40"
summary: "API - Faet - Generar comprobante (fc,nc,db) a un tercero, para un cliente determinado"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-04-22 13:57"
updated: "2024-04-29 16:03"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LOCAPP-40"
---

# LOCAPP-40: API - Faet - Generar comprobante (fc,nc,db) a un tercero, para un cliente determinado

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-04-22 13:57 |
| Actualizado | 2024-04-29 16:03 |
| Etiquetas | ninguna |
| Jira | [LOCAPP-40](https://bluinc.atlassian.net/browse/LOCAPP-40) |

## Descripción

Refactorizaremos el recurso 

```
POST {{API_URL}}/v2/CreateVoucher
```

tanto en su versión para emitir desde un pedido, como uno manual para enviar un nuevo objeto (third)

En el objeto enviaremos los siguientes datos que luego guardaremos donde se considere mas oportuno (tener en cuenta que tambien usaremos esos campos para los comprobantes normales, y así lograr que los comprobantes persistan los cambios aunque el cliente cambie).

- Cuit


- Razon social


- niva


- direccion


- provincia


- ciudad


- tipo de documento
