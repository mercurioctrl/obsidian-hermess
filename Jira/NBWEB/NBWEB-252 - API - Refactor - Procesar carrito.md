---
jira_key: "NBWEB-252"
aliases: ["NBWEB-252"]
summary: "API - Refactor - Procesar carrito"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-06-10 13:55"
updated: "2022-06-10 14:09"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-252"
---

# NBWEB-252: API - Refactor - Procesar carrito

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-06-10 13:55 |
| Actualizado | 2022-06-10 14:09 |
| Etiquetas | ninguna |
| Jira | [NBWEB-252](https://bluinc.atlassian.net/browse/NBWEB-252) |

## Relaciones

- **Padre:** [[NBWEB-50]] Sitio Web
- **Subtarea:** [[NBWEB-580]] API - Feat - Carrito -> Cerrar ventas y mostrar un mensaje según se indico en el cms

## Descripcion

```
POST {{API_URL}}/v1/carrito/procesar
```

mediopagoid se llama ahora mediodepagoid

Crear story para eze para arreglar bug.... mediodepagoid y debe llamarse mediodepagoid...

Ademas no debo mostrar un 200 en caso de que falle la creacion

– refactor producto de lo conversado con  en la daily --



asi se envia actualmente



```
{"note":"","medioPagoId":11,"codigoPostalFavorito":"6360","mediodeEnvioId":4041}
```
