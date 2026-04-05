---
jira_key: "LIO-241"
aliases: ["LIO-241"]
summary: "API - Feat - Gestion de informacion de cuentas bancarias para el cliente y su billetera"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-02-28 08:25"
updated: "2025-03-20 11:15"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-241"
---

# LIO-241: API - Feat - Gestion de informacion de cuentas bancarias para el cliente y su billetera

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-02-28 08:25 |
| Actualizado | 2025-03-20 11:15 |
| Etiquetas | ninguna |
| Jira | [LIO-241](https://bluinc.atlassian.net/browse/LIO-241) |

## Relaciones

- **Padre:** [[LIO-231 - Billetera|LIO-231]] Billetera
- **has action item:** [[LIO-271 - APP - Feat - Visualización de la Billetera del Usuario|LIO-271]] APP - Feat - Visualización de la Billetera del Usuario
- **relates to:** [[LIO-279 - API - Gestión de información de cuentas bancarias para el cliente y su|LIO-279]] API - Gestión de información de cuentas bancarias para el cliente y su billetera - No autorizado para crear cuenta bancaria con mi clientId
- **relates to:** [[LIO-286 - API - Refactor - Gestión de información de cuentas bancarias para el cliente y|LIO-286]] API - Refactor - Gestión de información de cuentas bancarias para el cliente y su billetera -> Normalización del número de documento

## Descripcion

Permite crear, consultar y actualizar la cuenta bancaria de un cliente dentro de la billetera.

- `accountHolderName`: Nombre completo del titular.


- `documentNumber`: DNI/CUIT/CUIL.


- `bankAlias` y `bankCBU` son opcionales, pero **uno de los dos debe estar presente**.


- `createdAt`** y **`updatedAt` registran la fecha de creación y modificación.



**Estructura orientativa: **

```
CREATE TABLE [NewBytes_DBF].[dbo].[clientsBankAccount] (
    id UNIQUEIDENTIFIER DEFAULT NEWID() PRIMARY KEY,
    clientId NOT NULL,
    accountHolderName NVARCHAR(255) NOT NULL,
    documentNumber NVARCHAR(20) NOT NULL,
    bankAlias NVARCHAR(50) NULL,
    bankCBU NVARCHAR(22) NULL,
    default TINYINT,
    createdAt DATETIME DEFAULT GETDATE(),
    updatedAt DATETIME DEFAULT GETDATE(),
    CONSTRAINT UQ_clientsBankAccount_clientId UNIQUE (clientId)
);
```

## **Crear una Cuenta Bancaria (**`POST /wallet/bankAccount`**)**

### **Descripción**

Registra la cuenta bancaria de un cliente. **Un cliente solo puede tener una cuenta registrada.**

```
POST /wallet/bankAccount
```

### **Ejemplo de solicitud**

```
{   
"clientId": "2",   
"accountHolderName": "Juan Pérez",   
"documentNumber": "30123456",   
"bankAlias": "juanperez.mp",   
"bankCBU": "2850590940090418135201" 
} 
```

### **Ejemplo de respuesta (201 Created)**

```
{   
"id": "34",   
"clientId": "2",   
"accountHolderName": "Juan Pérez",   
"documentNumber": "30123456",   
"bankAlias": "juanperez.mp",
"default": true,   
"bankCBU": "2850590940090418135201",   
"createdAt": "2024-02-28T12:00:00Z" 
}
```

### **Errores Comunes**

| Código | Descripción |
| --- | --- |
| `400 Bad Request` | Se debe proporcionar `bankAlias` o `bankCBU`. |
| `409 Conflict` | Ya existe una cuenta bancaria para el cliente. |

## **Consultar Cuenta Bancaria (**`GET /wallet/bankAccount/{bankAccountId opcional}`**)**

### **Descripción**

Obtiene la cuenta bancaria de un cliente, si se pasa el ID, es una especifica. Sino trae todas las del cliente.

### **Endpoint**

```
GET /wallet/bankAccount/{bankAccountId opcional} 
```

### **Ejemplo de respuesta (200 OK)**

```
{   
"id": "2",   
"clientId": "2",   
"accountHolderName": "Juan Pérez",   
"documentNumber": "30123456",   
"bankAlias": "juanperez.mp",
"default": true,   
"bankCBU": "2850590940090418135201",   
"createdAt": "2024-02-28T12:00:00Z",   
"updatedAt": "2024-02-28T12:00:00Z" 
} 
```

**Errores Comunes**

| Código | Descripción |
| --- | --- |
| `404 Not Found` | No se encontró la cuenta bancaria para el cliente. |

## **Eliminar Cuenta Bancaria (**`DELETE /wallet/bankAccount/{bankAccountId}`**)**

### **Descripción**

Elimina la cuenta bancaria de un cliente** con un softDelete (no se elimina de db)**

### **Endpoint**

```
DELETE /wallet/bankAccount/{bankAccountId} 
```

### **Ejemplo de respuesta (204 No Content)**

(Sin cuerpo en la respuesta)

Pasos para verificar.

- El usuario intenta eliminar su cuenta bancaria.


- El sistema **verifica si hay movimientos pendientes** (retiros/depositos en estado `pending`).


- **Si hay movimientos pendientes**, responde con **409 Conflict** y una lista de los movimientos.


- **Si no hay movimientos pendientes**, permite eliminar la cuenta.



### **Errores Comunes**

| Código | Descripción |
| --- | --- |
| `404 Not Found` | No se encontró la cuenta bancaria para eliminar. |
| `409 Not Found` | Existen movimiento pendientes relacionados a la cuenta, una vez terminado el proceso vuelva  intentarlo. |







Actualizacion 5/3/2025: 

- POST : El cliente puede tener varias cuentas bancarias creadas, (validacion basica: que tanto el alias como el cbu no se encuentren registrados )


- DELETE : No se puede eliminar un pedido que en movimientos de cuenta corriente tenga el campo pending en true.
