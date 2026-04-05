---
jira_key: "LIO-248"
aliases: ["LIO-248"]
summary: "API - Feat -  Recurso para Solicitar un Retiro de Dinero en la Billetera"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-03-06 12:05"
updated: "2025-03-20 15:39"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-248"
---

# LIO-248: API - Feat -  Recurso para Solicitar un Retiro de Dinero en la Billetera

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-03-06 12:05 |
| Actualizado | 2025-03-20 15:39 |
| Etiquetas | ninguna |
| Jira | [LIO-248](https://bluinc.atlassian.net/browse/LIO-248) |

## Relaciones

- **Padre:** [[LIO-231 - Billetera|LIO-231]] Billetera
- **has action item:** [[LIO-271 - APP - Feat - Visualización de la Billetera del Usuario|LIO-271]] APP - Feat - Visualización de la Billetera del Usuario

## Descripcion

## Requerimientos

- **El monto a retirar debe ser menor o igual al saldo disponible** en **GET {API_V4}/wallet/balance**.


- **Se debe seleccionar una cuenta bancaria válida** del usuario.


- Se generará un **registro en la tabla** `[NEW_BYTES].[dbo].[MC_CCORRIENTES_MOVIMIENTOS]` en estado **pending**.


- Se insertará la solicitud en `[NEW_BYTES].[dbo].[PendingCashOut]` con los siguientes campos:

- `userIdLo` → Usuario que solicita el retiro.


- `clientsBankAccountId` → ID de la cuenta bancaria seleccionada.


- `bankCBU` y `bankAlias` → Se almacenan por si la cuenta cambia en el futuro.


- `output_concept_id` → Se usará un concepto especial llamado **"Retiros Billetera Libre Opción"**.


- `pending` → Se marca como `1` hasta que se complete el retiro.





Agregar el Concepto "Retiros Billetera Libre Opción" en `[NEW_BYTES].[dbo].[OutputConcepts]` llamado “Retiros Billetera Libre Opción”

## **Estructura de la Tabla **`[NEW_BYTES].[dbo].[PendingCashOut]`** (Modificada con nuevos campos)**

```
ALTER TABLE [NEW_BYTES].[dbo].[PendingCashOut] 
ADD 
    userIdLo UNIQUEIDENTIFIER NOT NULL,
    clientsBankAccountId UNIQUEIDENTIFIER NOT NULL,
    bankCBU NVARCHAR(22) NULL,
    bankAlias NVARCHAR(50) NULL;

```

```
POST {API_V4}/wallet/cash-out
```

### **Carga util**

| Parámetro | Tipo | Requerido | Descripción |
| --- | --- | --- | --- |
| `amount` | `decimal(18,2)` | ✅ Sí | Monto a retirar (Debe ser menor o igual al saldo disponible). |
| `clientsBankAccountId` | `UUID` | ✅ Sí | ID de la cuenta bancaria asociada del usuario. |

### **Ejemplo de Solicitud**

```
{
  "amount": 15000.00,
  "clientsBankAccountId": 432
}
```

## Ejemplo de Respuesta Exitosa (201 Created)

```
{
  "id": 34e,
  "userIdLo": 32,
  "amount": 15000.00,
  "clientsBankAccountId": 432,
  "bankCBU": "2850590940090418135201",
  "bankAlias": "juanperez.mp",
  "output_concept_id": "retiros billetera libre opcion",
  "pending": 1,
  "createdAt": "2024-02-28T12:00:00Z"
}

```

### **Errores Comunes**

| Código | Descripción |
| --- | --- |
| `400 Bad Request` | El monto excede el saldo disponible. |
| `400 Bad Request` | La cuenta bancaria seleccionada no existe o no pertenece al usuario. |
| `409 Conflict` | Ya existe un retiro pendiente para este usuario. |
| `500 Internal Server Error` | Error inesperado al registrar la solicitud. |

## **Flujo Completo**

- **El usuario solicita un retiro** mediante **POST /wallet/cash-out**.


- **El sistema valida:**

- Que **el usuario tiene saldo suficiente**.


- Que **la cuenta bancaria es válida**.


- Que **no hay un retiro pendiente**.




- **Se crea un registro en **`[NEW_BYTES].[dbo].[PendingCashOut]` con el retiro en estado `pending`.


- **Se crea un movimiento en **`[NEW_BYTES].[dbo].[MC_CCORRIENTES_MOVIMIENTOS]` marcándolo como pendiente.
