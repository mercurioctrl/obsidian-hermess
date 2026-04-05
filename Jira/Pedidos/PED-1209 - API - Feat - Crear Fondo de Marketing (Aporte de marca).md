---
jira_key: "PED-1209"
aliases: ["PED-1209"]
summary: "API - Feat - Crear Fondo de Marketing (Aporte de marca)"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Franco Callipo"
reporter: "Catriel Mercurio"
created: "2026-01-05 06:53"
updated: "2026-01-16 09:57"
labels: ["esperandoDependencia"]
jira_url: "https://bluinc.atlassian.net/browse/PED-1209"
---

# PED-1209: API - Feat - Crear Fondo de Marketing (Aporte de marca)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Franco Callipo |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-05 06:53 |
| Actualizado | 2026-01-16 09:57 |
| Etiquetas | esperandoDependencia |
| Jira | [PED-1209](https://bluinc.atlassian.net/browse/PED-1209) |

## Relaciones

- **Padre:** [[PED-1208]] Gestión de Aportes y Gastos de Marketing
- **has action item:** [[PED-1219]] APP - Feat - Form Crear Fondo
- **is cloned by:** [[PED-1251]] API - Review - Crear Fondo de Marketing (Aporte de marca) - Diferencias en CreatedAt, CreateByUserId y respuesta del error

## Descripcion

**Qué hay que hacer**

- Crear un fondo asociado a `NB_WEB.dbo.marcas(id)` con moneda ARS/USD, monto, vencimiento opcional y notas.


- Al crear el fondo, crear su fila en `Marketing_FundStats` con totales en 0



```
POST /v1/marketing/funds
```

### **Ejemplo request (payload)**

```
{
  "brandId": 12,
  "name": "ASUS - Q1 2026 - USD 5000",
  "currencyId": 1,
  "amountOriginal": 5000.00,
  "expiresAt": "2026-03-31T23:59:59-03:00",
  "notes": "Aporte trimestral para campañas"
}

```

**Ejemplo response (201)**

```
{
  "id": 101,
  "brandId": 12,
  "name": "ASUS - Q1 2026 - USD 5000",
  "currencyId": 1 si es dolar / 2 si es peso segun tabla NesBytes_DBF.dbo.FP_Monedas,
  "amountOriginal": 5000.00,
  "expiresAt": "2026-03-31T23:59:59-03:00",
  "notes": "Aporte trimestral para campañas",
  "createdAt": "2026-01-05T06:12:00-03:00"
}

```

**SQL Server**

- `NB_WEB.dbo.Marketing_Funds` 


- `NB_WEB.dbo.Marketing_FundStats`

**SQL Server (tabla) — **`Marketing_Funds`

- `Id` (int, identity, PK)


- `BrandId` (int, NOT NULL) *(o referencia a tabla de marcas existente)*


- `Name` (varchar(120), NOT NULL) *(ej. “ASUS – Q1 2025 – USD 5.000”)*


- `CurrencyId` (int) *( 2 ‘ARS’ |  1 ‘USD’)*


- `AmountOriginal` (decimal(18,2), NOT NULL) *(monto aportado)*


- `ExpiresAt` (datetime2, NULL)


- `Notes` (varchar(400), NULL)


- `CreatedAt` (datetime2, NOT NULL, default sysdatetime())


- `CreatedByUserId` (int, NULL)


- Índices sugeridos:

- `IX_Marketing_Funds_BrandId_Currency` (`BrandId`, `Currency`)


- `IX_Marketing_Funds_ExpiresAt` (`ExpiresAt`)







**SQL Server (tabla) — **`Marketing_Actions`

- `Id` (int, identity, PK)


- `Name` (varchar(120), NOT NULL) *(ej. Hot Sale)*


- `Description` (varchar(600), NULL)


- `StartAt` (datetime2, NULL)


- `EndAt` (datetime2, NULL)


- `CreatedAt` (datetime2, NOT NULL, default sysdatetime())


- `CreatedByUserId` (int, NULL)


- Índice:

- `IX_Marketing_Actions_Name` (`Name`)





**Criterios de aceptación**

- Valida `BrandId` existente en `NB_WEB.dbo.marcas(id)`.


- Valida `currencyId`  es 1 si es dolar / 2 si es peso segun tabla NesBytes_DBF.dbo.FP_Monedas


- Crea `Marketing_Funds` y su fila en `Marketing_FundStats` (Allocated/Spent = 0).


- Responde `201` con el registro creado.


- Rechaza invalidaciones con `400` y mensaje claro (moneda/monto/marca).
