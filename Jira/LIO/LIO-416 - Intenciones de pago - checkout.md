---
jira_key: "LIO-416"
aliases: ["LIO-416"]
summary: "Intenciones de pago - checkout"
status: "Selected for Development"
type: "Historia"
priority: "Medium"
assignee: "Catriel Mercurio"
reporter: "Emanuel Jesus Ferreyra"
created: "2025-08-08 17:16"
updated: "2025-08-12 09:50"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-416"
---

# LIO-416: Intenciones de pago - checkout

| Campo | Valor |
|-------|-------|
| Estado | Selected for Development (Por hacer) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Catriel Mercurio |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2025-08-08 17:16 |
| Actualizado | 2025-08-12 09:50 |
| Etiquetas | ninguna |
| Jira | [LIO-416](https://bluinc.atlassian.net/browse/LIO-416) |

## Relaciones

- **Subtarea:** [[LIO-422]] API - Feat - Crear intención de pago
- **Subtarea:** [[LIO-423]] API - Feat - Completar intención de pago
- **Subtarea:** [[LIO-440]] API - Feat - Autorizar intención de pago
- **Subtarea:** [[LIO-441]] API - Feat - Cancelación de intención
- **Subtarea:** [[LIO-442]] API - Feat - Listar intenciones de pago
- **has action item:** [[PED-1076]] API - Research - Ofrecer pagos con dinero en Wallet, en caso de que tenga dinero disponible

## Descripcion

### Endpoints principales

### **Flujo básico de un microservicio de Intenciones de Pago (MVP)**

- **Crear intención de pago (ID inicial)**

- **Endpoint:** `POST /payment-intents`




- **Completar intención de pago (payload final)**

- **Endpoint:** `PATCH /payment-intents/{id}`




- **Cancelación de intención**


- **Endpoint:** `POST /payment-intents/{id}/cancel`


- **Consulta y listado**

- **GET /payment-intents/{id}`** → detalle completo.


- **GET /payment-intents** con filtros → auditoría/backoffice.





---



### Opcionales / Extendidos

- `GET /payment-intents`

- Listar intenciones de pago (para panel de administración, debugging, etc.).




- `POST /payment-intents/{id}/retry`

- Reintentar el pago en caso de error (útil si falla por fondos insuficientes, por ejemplo).




- `POST /payment-intents/{id}/metadata`



- Agregar información adicional (útil para trazabilidad.).







### Tablas necesarias para completar esta feature.

### **1. PaymentIntents**

Guarda la intención y su estado en todo el ciclo de vida.

```
CREATE TABLE PaymentIntents (
    id UNIQUEIDENTIFIER PRIMARY KEY DEFAULT NEWID(),
    referenceNumber VARCHAR(100) NULL, -- referencia externa (orden, ticket, etc.)
    amount DECIMAL(18, 2) NULL, -- puede ser NULL al inicio
    currency VARCHAR(10) NOT NULL DEFAULT 'ARS',
    typeOperation VARCHAR(50) NOT NULL, -- pagar_orden, cargar_wallet, cobro_externo
    origin VARCHAR(50) NOT NULL, -- ecommerce, sistema_interno, etc.
    status VARCHAR(50) NOT NULL DEFAULT 'pending_incomplete', -- pending_incomplete, pending, authorized, failed, cancelled
    createdAt DATETIME NOT NULL DEFAULT GETDATE(),
    updatedAt DATETIME NULL,
    deletedAt DATETIME NULL
);

```

---

### **2. PaymentIntentMethods**

Permite almacenar métodos de pago asociados (pueden ser varios para un mismo intent).

```
CREATE TABLE PaymentIntentMethods (
    id INT IDENTITY(1,1) PRIMARY KEY,
    paymentIntentId UNIQUEIDENTIFIER NOT NULL,
    paymentMethodType VARCHAR(50) NOT NULL, -- tarjeta, transferencia, wallet, etc.
    details NVARCHAR(MAX) NULL, -- JSON con detalles: token, CBU, id externo, etc.
    amount DECIMAL(18, 2) NOT NULL,
    status VARCHAR(50) NOT NULL DEFAULT 'initiated', -- initiated, confirmed, failed
    createdAt DATETIME NOT NULL DEFAULT GETDATE(),
    FOREIGN KEY (paymentIntentId) REFERENCES PaymentIntents(id)
);

```

---

### **3. PaymentLogs**

Historial de eventos por trazabilidad y auditoría.

```
CREATE TABLE PaymentLogs (
    id INT IDENTITY(1,1) PRIMARY KEY,
    paymentIntentId UNIQUEIDENTIFIER NOT NULL,
    message NVARCHAR(500),
    status VARCHAR(50),
    createdAt DATETIME NOT NULL DEFAULT GETDATE(),
    FOREIGN KEY (paymentIntentId) REFERENCES PaymentIntents(id)
);
```





### Ejemplo Basico de Flujo.

### **Flujo básico de un microservicio de Intenciones de Pago (MVP)**

- **Crear intención de pago (ID inicial)**

- **Endpoint:** `POST /payment-intents`


- **Entradas mínimas:**

- `importe` (opcional si no se conoce aún)


- `moneda` (opcional si solo manejás una por defecto)


- `tipoOperacion` (`pagar_orden`, `cargar_wallet`, `cobro_externo`)


- `origen` (`ecommerce`, `sistema_interno`, etc.)




- **Respuesta:**

- `id_intencion` (UUID o autoincremental)


- `estado` = `pendiente_incompleto`





📌 *Esto solo reserva la “caja” de la intención para completarla después.*



---

- **Completar intención de pago (payload final)**

- **Endpoint:** `PATCH /payment-intents/{id}`


- **Entradas necesarias:**

- `importe` (si no estaba)


- `moneda`


- `metodo_pago` (tarjeta, transferencia, wallet, etc.)


- `detalles_metodo` (token de tarjeta, CBU, ID de medio externo, etc.)


- `datos_cliente` (nombre, email, etc. si aplica)




- **Validaciones:**

- El estado debe ser `pendiente_incompleto` para poder completar.


- Si ya está completo → error `409 Conflict`.




- **Cambio de estado:**

- De `pendiente_incompleto` a `pendiente` (lista para autorizar).







---

- **Autorización de pago**

- Se envía al gateway/medio de pago correspondiente.


- Si OK → `autorizado`


- Si falla → `fallido`





---

- **Cancelación de intención**

- **Endpoint:** `POST /payment-intents/{id}/cancel`


- Si estaba autorizado → liberar fondos.


- Estado final → `cancelado`.





---

- **Consulta y listado**

- **GET /payment-intents/{id}`** → detalle completo.


- **GET /payment-intents** con filtros → auditoría/backoffice.







### Casos de uso y escenarios para la Intención de Pago

### 1. Pago Completo con un solo medio

- Pago total de la orden con tarjeta de crédito o débito.


- Pago total con transferencia bancaria.


- Pago total usando saldo disponible en la wallet.



### 2. Pago Mixto (combinación de medios)

- Uso parcial del saldo wallet + resto con tarjeta.


- Uso parcial del saldo wallet + resto con transferencia bancaria.


- Combinación de dos tarjetas diferentes (menos común, pero posible).



### 3. Pago parcial de orden

- Se paga solo un porcentaje o monto parcial de la orden, saldo queda pendiente para pagar luego.


- Pago parcial con wallet y/o otro medio.



### 4. Recarga de saldo en Wallet (sin orden)

- Usuario o personal interno agrega saldo a la wallet.


- Intención de pago generada solo con monto, sin orden asociada.



### 5. Pago adicional o extra (fuera de orden)

- Pago por servicios extras, multas, intereses, etc.


- Intención de pago libre, no vinculada a orden ni wallet.



### 6. Creación de intención desde el sistema interno

- Usuario interno crea intención para pagar orden específica.


- Usuario interno crea intención para recargar wallet de un cliente.


- Usuario interno crea intención para pago libre (ej. anticipo, ajuste).



### 7. Estados de la intención de pago

- Pendiente (pending) → se espera confirmación de pago.


- Confirmada (confirmed) → pago autorizado y en proceso.


- Pagada (paid) → pago exitoso y liquidado.


- Fallida (failed) → pago rechazado o error.


- Cancelada (cancelled) → intención anulada por usuario o sistema.



### 8. Manejo de errores y rollback

- Si falla pago por tarjeta, debe liberarse el saldo usado en wallet.


- Si se cancela la orden, cancelar o anular intención asociada.



### 9. Consultas y reportes

- Consultar estado de intención de pago desde LO.


- Consultar historial de pagos y movimientos de wallet.
