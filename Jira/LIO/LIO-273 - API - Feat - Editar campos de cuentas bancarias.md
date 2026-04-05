---
jira_key: "LIO-273"
aliases: ["LIO-273"]
summary: "API - Feat - Editar campos de  cuentas bancarias"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2025-03-13 15:05"
updated: "2025-03-19 15:17"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-273"
---

# LIO-273: API - Feat - Editar campos de  cuentas bancarias

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2025-03-13 15:05 |
| Actualizado | 2025-03-19 15:17 |
| Etiquetas | ninguna |
| Jira | [LIO-273](https://bluinc.atlassian.net/browse/LIO-273) |

## Relaciones

- **Padre:** [[LIO-231]] Billetera
- **has action item:** [[LIO-271]] APP - Feat - Visualización de la Billetera del Usuario

## Descripcion

Implementar PATCH para actualizar cuenta bancaria 

```
PATCH /wallet/bankAccount/{bankAccountId}
```

Este recurso debe permitir la actualización parcial de una cuenta bancaria existente. 

Los campos actualizables serán: `accountHolderName`, `documentNumber` , `bankAlias` , `default`

**Validaciones:**

- Verificar que el bankAccountId exista en la base de datos.


- Si se envía bankAlias, validar que no esté registrado en otra cuenta bancaria (manteniendo la unicidad).


- Actualizar solo los campos enviados en el cuerpo de la solicitud (parche parcial).


- Actualizar el campo updatedAt con la fecha y hora actuales (GETDATE()).



Ejemplo de Payload:

```
{
  "accountHolderName": "Juan Pérez Modificado",
  "bankAlias": "juanperez.nuevo",
  "default": true
}
```



**Ejemplo de respuesta (200 OK):**

```
{
  "id": "F03C6D7E-EB84-415B-A...",
  "clientId": "2",
  "accountHolderName": "Juan Pérez Modificado",
  "documentNumber": "30123456",
  "bankAlias": "juanperez.nuevo",
  "bankCBU": "2850590940090418135201",
  "default": true,
  "createdAt": "2024-02-28T12:00:00Z",
  "updatedAt": "2025-03-13T10:00:00Z"
}


```

**Errores comunes:**

- 400 Bad Request: Datos inválidos o mal formateados.


- 404 Not Found: No se encontró la cuenta bancaria con el bankAccountId proporcionado.


- 409 Conflict: El bankAlias ya está registrado en otra cuenta.





**Notas:**

-  No se permite modificar `bankCBU`, `clientId` mediante este endpoint.



- La actualización debe ser atómica y reflejar solo los cambios enviados en la solicitud.
