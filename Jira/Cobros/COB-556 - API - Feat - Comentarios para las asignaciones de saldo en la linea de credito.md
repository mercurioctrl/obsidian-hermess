---
jira_key: "COB-556"
aliases: ["COB-556"]
summary: "API - Feat - Comentarios para las asignaciones de saldo en la linea de credito"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-04-16 14:18"
updated: "2025-04-25 03:06"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-556"
---

# COB-556: API - Feat - Comentarios para las asignaciones de saldo en la linea de credito

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-04-16 14:18 |
| Actualizado | 2025-04-25 03:06 |
| Etiquetas | ninguna |
| Jira | [COB-556](https://bluinc.atlassian.net/browse/COB-556) |

## Relaciones

- **Padre:** [[COB-374]] Feat - Editar estado crediticio de la cuenta del cliente
- **has action item:** [[SNB-3010]] OBSERVACIONES EN FICHA DE LINEA DE CREDITO

## Descripcion

Persistir observaciones en la asignación de línea de crédito

```
PATCH {API_URL}/v1/assignedCredit
```


Se permite enviar un comentario u observación a través del parámetro "comment" dentro del body del request.

Es necesario investigar si estas observaciones se están guardando actualmente, y en caso de que no sea así:

- Crear una tabla destinada al almacenamiento de observaciones/comentarios asociados a la asignación de línea de crédito.
Esta tabla deberá guardar al menos:

- `id` (autoincremental)


- `clientId` (INT)


- `comment` (TEXT)


- `created_at` (DATETIME)




- Asegurar que cada vez que se reciba un comentario en el recurso `PATCH /v1/assignedCredit`, este se registre en la nueva tabla.


- Crear un nuevo recurso de consulta para obtener las observaciones previas de un cliente específico:



```
GET {API_URL}/v1/assignedCredit/comments/{clientId} 
```





Este recurso deberá devolver un array con los comentarios históricos del cliente ordenados por fecha descendente, por ejemplo:

```
[   
  {     
    "date": "2025-04-16T14:00:00",     
    "comment": "este es un comentario de prueba",
    "created_at": uSUARIO
  },
  {     
    "date": "2025-03-10T10:30:00",    
    "comment": "Observación anterior",
    "created_at": uSUARIO 
  } 
]
```



**Notas técnicas:**

- Revisar si ya existe alguna lógica o tabla relacionada a comentarios en líneas de crédito.


- El cambio no debe afectar el comportamiento actual del recurso `PATCH`, solo se adiciona lógica de persistencia.



Si cuando lo lees tenes alguna idea diferente lo vemos
