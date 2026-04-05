---
jira_key: "COM-175"
aliases: ["COM-175"]
summary: "API - Feat - Crear una factura de compra"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-03-17 07:22"
updated: "2025-06-01 23:40"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-175"
---

# COM-175: API - Feat - Crear una factura de compra

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-03-17 07:22 |
| Actualizado | 2025-06-01 23:40 |
| Etiquetas | ninguna |
| Jira | [COM-175](https://bluinc.atlassian.net/browse/COM-175) |

## Relaciones

- **Padre:** [[COM-174 - Crear factura de compra|COM-174]] Crear factura de compra
- **relates to:** [[COM-189 - API - Crear una factura de compra - Posibles datos faltantes|COM-189]] API - Crear una factura de compra -> Posibles datos faltantes

## Descripcion

Son varios pasos… Leela tranqui trata de relacionarlo con los otros recursos de compra (el de orden y el de ingresos) y después si queres charlamos y vemos si estas de acuerdo con todo lo descrpito.

Se debe desarrollar un endpoint en el backend que permita registrar un comprobante de proveedor en la base de datos. Este recurso recibirá los datos de la factura, sus ítems y los impuestos asociados, validará la información y la persistirá en las tablas correspondientes.

```
POST {API_URL}/v1/providerVoucher
```

**Carga útil**

```
{
  "providerId": "123456",
  "voucherNumber": "0000123456789",
  "accountingDate": "2025-03-17", <-- Fecha contable, osea la del comprobante
  "deposito": "DEP001",
  "paymentMethodId": 3, --- ver comprobantes en facptrot para ver de donde sale
  "currencyPrefix": "USD",
  "paymentBranch": "SUC001",
  "type": 1,
  "currencyAmount": 1.2,
  "FOB": 1500.50,
  "providerOrder": "ALB12345", <-- nnumalb
  "items": [
             {
                "id": 172,
                "title": "FLETE CAMIONETA",
                "sku": "",
                "price": {
                    "value": 13740,
                    "iva": 21,
                    "finalPrice": 16625.4
                },
                "warranty": "",
                "amount": 3,
                "position": null,
                "taxPosition": null,
                "amountEntered": "120.000"
            },
  ],
  "tariffTax": [
     {
        "id": 16,
        "acronym": "IVA AD",
        "description": "IVA ADICIONAL ALICUOTA REDUCIDA",
        "taxExclusive": false,
        "distribute": true
    },
    {
        "id": 29,
        "acronym": "GPR0409",
        "description": "Gprueba0409",
        "taxExclusive": false,
        "distribute": true
    },
  ]
}

```

### **Pasos del proceso en backend**

- **Validación de datos:**

- `ProveedorID` debe ser un número de 6 caracteres.


- `voucherNumber` debe ser un número de 13 caracteres.


- `detallesItem` e `impActivos` deben ser arrays válidos.




- **Verificación en la base de datos:**

- Buscar si ya existe un comprobante con `CSUFAC = voucherNumber` y `CCODPRO = ProveedorID` en la tabla `FACPROT`.


- Si existe, devolver error 409 (Conflict).


- Si no existe, generar un nuevo número de factura (`CNUMFAC`).




- **Registrar la cabecera del comprobante en **`FACPROT`**.**


- **Actualizar la tabla **`albprot`** si hay un **`nnumalb`** para marcarlo como facturado.**


- **Registrar los detalles del comprobante en **`FACPROL`**.**


- **Registrar los impuestos en **`FACPROI`**.**



### **Tablas afectadas**

#### **Tabla: **`FACPROT` *(Cabecera del comprobante de proveedor)*

| Campo | Tipo | Descripción |
| --- | --- | --- |
| `CNUMFAC` | INT | Número de factura (autogenerado). |
| `CSUFAC` | VARCHAR(13) | voucherNumber del proveedor. |
| `CCODPRO` | VARCHAR(6) | Código del proveedor. |
| `DFECFAC` | DATETIME | Fecha de la factura. |
| `DFECCONT` | DATETIME | Fecha contable. |
| `CCODALM` | VARCHAR(10) | Código de almacén. |
| `CCODPAGO` | VARCHAR(10) | Código de pago. |
| `CCODDIV` | VARCHAR(3) | Código de divisa. |
| `CNUMSUCPAG` | VARCHAR(10) | Sucursal de pago. |
| `NTIPOCOMP` | INT | Tipo de compra. |
| `NVALDIV` | FLOAT | Valor de la divisa. |
| `FOB` | FLOAT | Valor FOB (si aplica). |

#### **Tabla: **`FACPROL` *(Detalles del comprobante de proveedor)*

| Campo | Tipo | Descripción |
| --- | --- | --- |
| `CSERIE` | CHAR(1) | Serie del comprobante (Ej: "A"). |
| `CNUMFAC` | INT | Número de factura (relación con `FACPROT`). |
| `CREF` | VARCHAR(20) | Código de referencia del producto. |
| `CDETALLE` | VARCHAR(255) | Descripción del producto. |
| `NPREUNIT` | FLOAT | Precio unitario. |
| `NIVA` | FLOAT | IVA aplicado. |
| `NCANENT` | INT | Cantidad de unidades. |
| `LCONTROL` | BIT | Control interno (por defecto 'false'). |
| `LSINIMPINT` | BIT | Sin impuesto interno (por defecto 'true'). |
| `LMODIF` | BIT | Modificado (por defecto 'false'). |

#### **Tabla: **`FACPROI` *(Impuestos aplicados a la factura)*

| Campo | Tipo | Descripción |
| --- | --- | --- |
| `CSERIE` | CHAR(1) | Serie del comprobante. |
| `CNUMFAC` | INT | Número de factura (relación con `FACPROT`). |
| `CCODIMP` | VARCHAR(10) | Código del impuesto. |
| `CDESCRIP` | VARCHAR(255) | Descripción del impuesto. |
| `NPORCTASA` | FLOAT | Porcentaje de la tasa. |
| `NIMPBASE` | FLOAT | Base imponible. |
| `LCALCUAUTO` | BIT | Cálculo automático (por defecto 'false'). |
| `NBASE` | INT | Base de cálculo (por defecto '1'). |

### **Casos de uso**

✅ **Caso exitoso**

- Se envía un `POST` con datos válidos.


- Se genera el número de factura.


- Se inserta la cabecera en `FACPROT`.


- Se agregan los detalles en `FACPROL`.


- Se agregan los impuestos en `FACPROI`.


- Respuesta: `201 Created` con el número de factura generado.



❌ **Errores posibles**

- `400 Bad Request`: Datos faltantes o incorrectos.


- `409 Conflict`: El comprobante ya existe.


- `500 Internal Server Error`: Fallo en la base de datos.



### **Respuesta esperada**

✅ **Éxito (**`201 Created`**)**

```
{
  "message": "Factura registrada exitosamente",
  "CNUMFAC": 10045
}
```

❌ **Error (**`409 Conflict`**)**

```
{
  "error": "El numero de factura ya existe para este proveedor"
}

```
