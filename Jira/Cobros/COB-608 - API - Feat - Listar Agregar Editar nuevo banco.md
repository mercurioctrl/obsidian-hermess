---
jira_key: "COB-608"
aliases: ["COB-608"]
summary: "API - Feat - Listar / Agregar / Editar nuevo banco "
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2026-02-04 07:11"
updated: "2026-02-13 10:50"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-608"
---

# COB-608: API - Feat - Listar / Agregar / Editar nuevo banco 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2026-02-04 07:11 |
| Actualizado | 2026-02-13 10:50 |
| Etiquetas | ninguna |
| Jira | [COB-608](https://bluinc.atlassian.net/browse/COB-608) |

## Relaciones

- **Padre:** [[COB-9 - API - Feat - Listar bancos|COB-9]] API - Feat - Listar bancos
- **has action item:** [[COB-609 - APP - Feat - Listar Agregar Editar nuevo banco|COB-609]] APP - Feat - Listar  Agregar / Editar nuevo banco

## Descripcion

La tabla `NEW_BYTES.dbo.BA_BP_CAJA_CBANCARIAS` almacena las cuentas bancarias del sistema.
Hoy no existe un endpoint propio para gestionarla (solo se consume indirectamente desde `BankRepository`).

Se debe exponer un CRUD **sin delete**:

---

## Tablas involucradas

| Tabla | Rol | Columnas relevantes |
| --- | --- | --- |
| `NEW_BYTES.dbo.BA_BP_CAJA_CBANCARIAS` | Principal | `Id_Caja_Cuenta` (PK), `Id_Banco` (FK), `Descripcion`, `companyCode` |
| `NEW_BYTES.dbo.BANCOS` | Nombre del banco | `Id_Banco` (PK), `DESCRIPCION` |
| `NewBytes_DBF.dbo.FP_Empresas` | Nombre empresa | `codemp` (PK), `cnombre` |

---

## 🔌 Endpoints

| Método | Ruta | Acción |
| --- | --- | --- |
| GET | `/bank-accounts` | Listar cuentas |
| POST | `/bank-accounts` | Crear cuenta |
| PUT | `/bank-accounts/{accountId}` | Editar cuenta |

---

# Listar cuentas bancarias

### GET `/bank-accounts`

**Reglas**

- Devuelve todas las cuentas.


- Join con bancos y empresas.


- Filtro `companyCode`.


- Filtro `bankName`.


- Filtro `bankId`.


- Orden: `Id_Caja_Cuenta DESC`.


- Respuesta: array directo (`BaseController::success()`).



### Requests

```
GET /bank-accounts
GET /bank-accounts?bankName={bankName}&companyCode={companyCode}&bankId={bankId}
```

### Response 200

```
[
  {
    "accountId": 12,
    "description": "Cuenta Corriente Galicia",
    "bankId": 3,
    "bankName": "Banco Galicia",
    "companyCode": 4,
    "companyName": "New Bytes S.A."
  },
  {
    "accountId": 11,
    "description": "Caja de Ahorro Santander",
    "bankId": 7,
    "bankName": "Banco Santander",
    "companyCode": null,
    "companyName": null
  }
]

```

---

# Crear cuenta bancaria

```
POST /bank-accounts
```

**Validaciones**

- Requeridos: `bankId`, `description`


- Opcional: `companyCode`


- Validar existencia en tablas:

- `bankId` → BANCOS


- `companyCode` → FP_Empresas





### Request

```
{
  "bankId": 3,
  "description": "Cuenta Corriente Galicia",
  "companyCode": 4
}

```

### Response 201

```
{
  "success": true,
  "message": "Cuenta bancaria creada exitosamente",
  "data": {
    "accountId": 15,
    "description": "Cuenta Corriente Galicia",
    "bankId": 3,
    "bankName": "Banco Galicia",
    "companyCode": 4,
    "companyName": "New Bytes S.A."
  }
}

```

### ❌ Error banco inválido

```
{
  "errors": {
    "status": 422,
    "title": "El banco indicado no existe"
  }
}
```

### ❌ Error empresa inválida

```
{
  "errors": {
    "status": 422,
    "title": "La empresa indicada no existe"
  }
}
```

---

# Editar cuenta bancaria

```
PUT /bank-accounts/{accountId}
```

**Campos editables**

- `description`


- `bankId`


- `companyCode`



Edición parcial permitida.

**Validaciones**

- Cuenta existe → 404 si no.


- bankId válido → 422.


- companyCode válido → 422.



### Request

```
{
  "description": "Cuenta Corriente Galicia — Empresa Principal",
  "companyCode": 5
}
```

### Response 200

```
{
  "success": true,
  "message": "Cuenta bancaria actualizada exitosamente",
  "data": {
    "accountId": 12,
    "description": "Cuenta Corriente Galicia — Empresa Principal",
    "bankId": 3,
    "bankName": "Banco Galicia",
    "companyCode": 5,
    "companyName": "Otra Empresa S.A."
  }
}
```

### Error 404

```
{
  "errors": {
    "status": 404,
    "title": "Cuenta bancaria no encontrada"
  }
}

```
