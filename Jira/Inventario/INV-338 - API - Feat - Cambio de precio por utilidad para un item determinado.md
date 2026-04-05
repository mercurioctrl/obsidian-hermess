---
jira_key: "INV-338"
aliases: ["INV-338"]
summary: "API - Feat - Cambio de precio por utilidad para un item determinado"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2026-02-10 12:22"
updated: "2026-02-26 16:52"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-338"
---

# INV-338: API - Feat - Cambio de precio por utilidad para un item determinado

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2026-02-10 12:22 |
| Actualizado | 2026-02-26 16:52 |
| Etiquetas | ninguna |
| Jira | [INV-338](https://bluinc.atlassian.net/browse/INV-338) |

## Relaciones

- **Padre:** [[INV-199 - Control de Stock Stock en general Control de Precios|INV-199]] Control de Stock / Stock en general  / Control de Precios
- **has action item:** [[INV-340 - APP - Feat - Cambio de utilidad para un item determinado|INV-340]] APP - Feat - Cambio de utilidad para un item determinado

## Descripcion

Como sistema backend, necesito un endpoint que permita actualizar los márgenes de utilidad y descuentos de artículos, recalculando automáticamente sus precios según el tipo de lista

```
PATCH /itemsPrice
```

### Payload (JSON)

```
{
  "itemId": 104150,
  "type": "PL",
  "value": 31
}

```

---

## OBJETIVO

Crear un endpoint REST moderno que:

- Actualice porcentajes de utilidad/descuento por tipo de lista


- Valide utilidad mínima según reglas de negocio


- Recalcule precio final automáticamente


- Maneje lógica especial para resellers (LO1/LO2)


- Registre auditoría de cambios


- Retorne precio actualizado



---

## REQUISITOS FUNCIONALES

### RF1 — Tipos de lista soportados

PL → Precio Lista → PORC_GANAN_ESTIP → npvp1
PLI → Precio Lista Incrementado → PORC_GANAN_ESTIP2 → npvp1
LO1 → Lista Oficial 1 → PORC_GANAN_ESTIPLO → nplo
LO2 → Lista Oficial 2 → PORC_GANAN_ESTIPLO1 → nplo
MAY1 → Mayorista 1 → PORC_GANAN_ESTIP3 → npvp5
MAY2 → Mayorista 2 → PORC_GANAN_ESTIP4 → npvp5
PML → Marketplace → PORC_GANAN_ESTIPMK1 → npvp3
PCAM → Precio Cambio → PORC_GANAN_ESTIP6 → npvp6
CF → Cliente Final → PORC_GANAN_ESTIPCF → npvp4
DT2 → Descuento 2 → ndto2
DT3 → Descuento 3 → ndto3

---

### RF2 — Validación de utilidad mínima

**utilidad_total = valor_nuevo + utilidad_base**

SI utilidad_total < minUtility → ERROR

**Excepciones**

- minUtilityExclude = 1


- Familia = 65


- Tipos: PML, PCAM, CF



**Mensaje de error:**

> "La utilidad mínima es de {minUtility}%, agregue {diferencia} para poder continuar"


**minUtility** proviene de la tabla de parámetros del sistema:

`NEW_BYTES.dbo.PV_PARAMETROS_VARIOS`

SQL representativo:

```
SELECT
    (({COLUMNA_A_CAMBIAR}) - P.minUtility) AS valor,
    P.minUtility
FROM
    NEW_BYTES.dbo.ST_GANANCIA_ESTIPULADA_ARTICULOS B
LEFT JOIN
    NEW_BYTES.dbo.PV_PARAMETROS_VARIOS P ON 1 = 1  -- JOIN cruzado (1 sola fila)
LEFT JOIN
    NewBytes_DBF.dbo.articulo ON articulo.cRef = B.ID_ARTICULO
WHERE
    B.ID_ARTICULO = '{id_articulo}'
    AND ccodfam <> 65
    AND minUtilityExclude <> 1  -- Esta columna está en articulo

```

---

### RF3 — Cálculo de precios

**precio_nuevo = costo_promedio + (costo_promedio * utilidad_total / 100)**

Caso especial PML:

**precio_pml_ars = npvp3 * cotizacion_pesoslo * (1 + ivaVenta/100)**

---

### RF4 — Lógica especial Resellers (LO1 / LO2)

- Actualizar costo base en CS.productos


- Recalcular utilidad de cada reseller


- Aplicar incrementos de costo por usuario


- Recalcular utilidades


- Ejecutar SP de descuentos si dtoDelay = 'SI'



---

### RF5 — Auditoría

```
INSERT historial_precios (fecha, agente, ID_ARTICULO, columna_precio)
```

---

### RF6 — Modo solo validación

Si `onlyValidate = true`:

- Validar utilidad mínima


- NO guardar cambios


- Retornar `{ "validation": "ok" }`



Payload ejemplo:

```
{
  "itemId": 104150,
  "type": "PL",
  "value": 31,
  "onlyValidate": true
}
```

---

## REQUISITOS TÉCNICOS

### Response OK (contrato con alias)

> Se devuelve eco del request (`itemId`, `type`, `value`) y los campos deben respetar **alias**.


```
{
  "success": true,
  "data": {
    "itemId": 104150,
    "type": "PL",
    "value": 31,
    "previous": {
      "unitPrice": 1150.0,
      "pl": 25.0
    },
    "current": {
      "unitPrice": 1234.56,
      "pl": 31.0,
      "pli": 5.0,
      "may1": 15.0,
      "may2": 10.0,
      "pml": 0.0,
      "lo1": 20.0,
      "lo2": 8.0,
      "dt2": 0.0,
      "dt3": 0.0,
      "pcam": 0.0,
      "mk1": 0.0,
      "cost": 100.0,
      "fob": 0.0,
      "loCost": 0.0,
      "mayPrice": 0.0,
      "priceLoReseller": 0.0,
      "PVP": 0.0,
      "mlPrice": 0.0,
      "IINT": 0.0
    },
    "currency": "USD",
    "updatedAt": "2026-02-10T15:30:00Z",
    "affectedResellers": 15
  }
}

```

> Nota: `PVP` e `IINT` se mantienen como están en tu snippet (alias en mayúscula). Si querés estandarizar casing (p.ej. `pvp`, `iint`), eso sería **cambiar alias con AS** y lo hago, pero acá los respeté tal cual.


---

### Error utilidad mínima

```
{
  "success": false,
  "error": {
    "code": "MIN_UTILITY_NOT_MET",
    "message": "La utilidad mínima es de 25%, agregue 5.3 para poder continuar"
  }
}

```

---

## Convenciones de nombres

### API (externo)

- `itemId`


- `type`


- `value`


- `onlyValidate` (opcional)



### DB (interno)

- articulo.ID_ARTICULO


- articulo.cRef


- articulo.ncosteprom


- articulo.npvp1 / nplo / npvp5 / npvp3 / npvp4 / npvp6


- articulo.ndto2 / ndto3


- ST_GANANCIA_ESTIPULADA_ARTICULOS.{PORC_*}



---

## 2) Datos de ejemplo base (constantes para todos los casos)

### Articulo

Articulo ID: 104150

```
SELECT *
FROM NewBytes_DBF.dbo.articulo
WHERE ID_ARTICULO = 104150;
```

ncosteprom = 100.00
cRef = '[[ART-104150]]'
ivaVenta = 21.00

---

### Ganancia estipulada

```
SELECT *
FROM NEW_BYTES.dbo.ST_GANANCIA_ESTIPULADA_ARTICULOS
WHERE ID_ARTICULO = '[[ART-104150]]';

```

PORC_GANAN_ESTIP = 25
PORC_GANAN_ESTIP2 = 5
PORC_GANAN_ESTIPLO = 20
PORC_GANAN_ESTIPLO1 = 8
PORC_GANAN_ESTIP3 = 15
PORC_GANAN_ESTIP4 = 10

---

### Cotizacion pesos

```
SELECT COTIZACION
FROM NEW_BYTES.dbo.MS_COTIZACIONES
WHERE NOMBRE = 'PESOSLO';

```

COTIZACION = 1200.00

---

### Utilidad minima

```
SELECT minUtility
FROM NEW_BYTES.dbo.PV_PARAMETROS_VARIOS;

```

minUtility = 20.00

---

## 3) Reglas globales (aplican a todos los tipos)

### Regla de validacion (cuando aplica)

utilidad_total = utilidad_base + utilidad_complementaria

Validar:
(utilidad_total - minUtility) >= 0

---

### Formula general de recalculo (cuando aplica)

precio_nuevo_usd = ncosteprom + (ncosteprom * utilidad_total / 100)

---

### Caso especial PML (retorno ARS con IVA)

precio_pml_ars_con_iva = npvp3 * cotizacion_pesoslo * (1 + ivaVenta/100)

---

## 4) Matriz de comportamiento por tipo (legacy confirmado)

### Mapeo de utilidad_total y campo precio

| Tipo | Valida min | utilidad_total (DB) | Campo precio (DB) | Retorna |
| --- | --- | --- | --- | --- |
| PL | Si | PORC_GANAN_ESTIP + PORC_GANAN_ESTIP2 | npvp1 | USD |
| PLI | Si | PORC_GANAN_ESTIP + PORC_GANAN_ESTIP2 | npvp1 | USD |
| LO1 | Si | PORC_GANAN_ESTIPLO + PORC_GANAN_ESTIPLO1 | nplo | USD |
| LO2 | Si | PORC_GANAN_ESTIPLO + PORC_GANAN_ESTIPLO1 | nplo | USD |
| MAY1 | Si | PORC_GANAN_ESTIP3 + PORC_GANAN_ESTIP4 | npvp5 | USD |
| MAY2 | Si | PORC_GANAN_ESTIP3 + PORC_GANAN_ESTIP4 | npvp5 | USD |
| PML | No | PORC_GANAN_ESTIP3 + PORC_GANAN_ESTIP4 + PORC_GANAN_ESTIPMK1 | npvp3 | ARS con IVA |
| PCAM | No | PORC_GANAN_ESTIP6 | npvp6 | USD |
| CF | No | PORC_GANAN_ESTIPCF | npvp4 | USD |
| DT2 | No | - | ndto2 | - |
| DT3 | No | - | ndto3 | - |

---

### Mapeo de columna que se actualiza segun type

type=PL -> ST_GANANCIA_ESTIPULADA_ARTICULOS.PORC_GANAN_ESTIP
type=PLI -> ST_GANANCIA_ESTIPULADA_ARTICULOS.PORC_GANAN_ESTIP2
type=LO1 -> ST_GANANCIA_ESTIPULADA_ARTICULOS.PORC_GANAN_ESTIPLO
type=LO2 -> ST_GANANCIA_ESTIPULADA_ARTICULOS.PORC_GANAN_ESTIPLO1
type=MAY1 -> ST_GANANCIA_ESTIPULADA_ARTICULOS.PORC_GANAN_ESTIP3
type=MAY2 -> ST_GANANCIA_ESTIPULADA_ARTICULOS.PORC_GANAN_ESTIP4
type=PML -> ST_GANANCIA_ESTIPULADA_ARTICULOS.PORC_GANAN_ESTIPMK1
type=PCAM -> ST_GANANCIA_ESTIPULADA_ARTICULOS.PORC_GANAN_ESTIP6
type=CF -> ST_GANANCIA_ESTIPULADA_ARTICULOS.PORC_GANAN_ESTIPCF
type=DT2 -> articulo.ndto2
type=DT3 -> articulo.ndto3

---

## 5) Flujos por tipo (paso a paso, copy/paste)

Para todos los casos se asume itemId=104150, ncosteprom=100, minUtility=20, cotizacion=1200, ivaVenta=21.

> En todos los requests: **PATCH /itemsPrice** y payload JSON con `itemId`, `type`, `value`.


---

### 5.1) PL

Request

```
PATCH /itemsPrice

```

```
{
  "itemId": 104150,
  "type": "PL",
  "value": 31
}

```

Validacion (aplica)

utilidad_total = value + PORC_GANAN_ESTIP2
utilidad_total = 31 + 5 = 36

36 - 20 = 16 >= 0

SQL representativo:

```
SELECT ((31 + 5) - 20) AS valor;

```

Update utilidad

```
UPDATE B
SET B.PORC_GANAN_ESTIP = 31
FROM NewBytes_DBF.dbo.articulo A
INNER JOIN NEW_BYTES.dbo.ST_GANANCIA_ESTIPULADA_ARTICULOS B
  ON A.cRef = B.ID_ARTICULO
WHERE A.ID_ARTICULO = 104150;

```

Recalculo precio (npvp1)

npvp1 = 100 + (100 * (31 + 5) / 100) = 136.00

SQL representativo:

```
UPDATE A
SET A.npvp1 = A.ncosteprom + (A.ncosteprom * (31 + 5) / 100)
FROM NewBytes_DBF.dbo.articulo A
WHERE A.ID_ARTICULO = 104150;

```

Historial (aplica)

```
INSERT INTO NB_WEB.dbo.historial_precios (fecha, agente, ID_ARTICULO, npvp1)
VALUES (GETDATE(), 123, 104150, 136.00);

```

Response (alias)

```
{
  "success": true,
  "data": {
    "itemId": 104150,
    "type": "PL",
    "value": 31,
    "current": {
      "unitPrice": 136.0
    }
  }
}

```

---

### 5.2) PLI

Request

```
{
  "itemId": 104150,
  "type": "PLI",
  "value": 8
}

```

Validacion (aplica)

utilidad_total = PORC_GANAN_ESTIP + value
utilidad_total = 31 + 8 = 39

39 - 20 = 19 >= 0

Update utilidad

```
UPDATE B
SET B.PORC_GANAN_ESTIP2 = 8
FROM NewBytes_DBF.dbo.articulo A
INNER JOIN NEW_BYTES.dbo.ST_GANANCIA_ESTIPULADA_ARTICULOS B
  ON A.cRef = B.ID_ARTICULO
WHERE A.ID_ARTICULO = 104150;

```

Recalculo precio (npvp1)

npvp1 = 100 + (100 * (31 + 8) / 100) = 139.00

Response (alias)

```
{
  "success": true,
  "data": {
    "itemId": 104150,
    "type": "PLI",
    "value": 8,
    "current": {
      "unitPrice": 139.0
    }
  }
}

```

---

### 5.3) LO1 (resellers)

Request

```
{
  "itemId": 104150,
  "type": "LO1",
  "value": 22
}

```

Validacion (aplica)

utilidad_total = value + PORC_GANAN_ESTIPLO1
utilidad_total = 22 + 8 = 30

30 - 20 = 10 >= 0

Update utilidad

```
UPDATE B
SET B.PORC_GANAN_ESTIPLO = 22
FROM NewBytes_DBF.dbo.articulo A
INNER JOIN NEW_BYTES.dbo.ST_GANANCIA_ESTIPULADA_ARTICULOS B
  ON A.cRef = B.ID_ARTICULO
WHERE A.ID_ARTICULO = 104150;

```

Recalculo precio (nplo)

nplo = 100 + (100 * (22 + 8) / 100) = 130.00

Actualizar costo base:

```
UPDATE CS.dbo.productos
SET costo_cliente = 130.00
WHERE id_interno = 104150;

```

Historial (aplica)

```
INSERT INTO NB_WEB.dbo.historial_precios (fecha, agente, ID_ARTICULO, nplo)
VALUES (GETDATE(), 123, 104150, 130.00);

```

Response (alias)

```
{
  "success": true,
  "data": {
    "itemId": 104150,
    "type": "LO1",
    "value": 22,
    "current": {
      "loCost": 130.0
    }
  }
}

```

---

### 5.4) LO2 (resellers incremental)

Request

```
{
  "itemId": 104150,
  "type": "LO2",
  "value": 10
}

```

Validacion (aplica)

utilidad_total = PORC_GANAN_ESTIPLO + value
utilidad_total = 22 + 10 = 32

32 - 20 = 12 >= 0

Update utilidad

```
UPDATE B
SET B.PORC_GANAN_ESTIPLO1 = 10
FROM NewBytes_DBF.dbo.articulo A
INNER JOIN NEW_BYTES.dbo.ST_GANANCIA_ESTIPULADA_ARTICULOS B
  ON A.cRef = B.ID_ARTICULO
WHERE A.ID_ARTICULO = 104150;

```

Recalculo precio (nplo)

nplo = 100 + (100 * (22 + 10) / 100) = 132.00

Response (alias)

```
{
  "success": true,
  "data": {
    "itemId": 104150,
    "type": "LO2",
    "value": 10,
    "current": {
      "loCost": 132.0
    }
  }
}

```

---

### 5.5) MAY1

Request

```
{
  "itemId": 104150,
  "type": "MAY1",
  "value": 18
}

```

Validacion (aplica)

utilidad_total = value + PORC_GANAN_ESTIP4
utilidad_total = 18 + 10 = 28

28 - 20 = 8 >= 0

Update utilidad

```
UPDATE B
SET B.PORC_GANAN_ESTIP3 = 18
FROM NewBytes_DBF.dbo.articulo A
INNER JOIN NEW_BYTES.dbo.ST_GANANCIA_ESTIPULADA_ARTICULOS B
  ON A.cRef = B.ID_ARTICULO
WHERE A.ID_ARTICULO = 104150;

```

Recalculo precio (npvp5)

npvp5 = 100 + (100 * (18 + 10) / 100) = 128.00

Response (alias)

```
{
  "success": true,
  "data": {
    "itemId": 104150,
    "type": "MAY1",
    "value": 18,
    "current": {
      "mayPrice": 128.0
    }
  }
}

```

---

### 5.6) MAY2

Request

```
{
  "itemId": 104150,
  "type": "MAY2",
  "value": 12
}

```

Update utilidad

```
UPDATE B
SET B.PORC_GANAN_ESTIP4 = 12
FROM NewBytes_DBF.dbo.articulo A
INNER JOIN NEW_BYTES.dbo.ST_GANANCIA_ESTIPULADA_ARTICULOS B
  ON A.cRef = B.ID_ARTICULO
WHERE A.ID_ARTICULO = 104150;

```

Recalculo precio (npvp5)

npvp5 = 100 + (100 * (18 + 12) / 100) = 130.00

Response (alias)

```
{
  "success": true,
  "data": {
    "itemId": 104150,
    "type": "MAY2",
    "value": 12,
    "current": {
      "mayPrice": 130.0
    }
  }
}

```

---

### 5.7) PML

Request

```
{
  "itemId": 104150,
  "type": "PML",
  "value": 15
}

```

Validacion

No valida utilidad minima

Update utilidad

```
UPDATE B
SET B.PORC_GANAN_ESTIPMK1 = 15
FROM NewBytes_DBF.dbo.articulo A
INNER JOIN NEW_BYTES.dbo.ST_GANANCIA_ESTIPULADA_ARTICULOS B
  ON A.cRef = B.ID_ARTICULO
WHERE A.ID_ARTICULO = 104150;

```

Recalculo precio base (npvp3 USD)

utilidad_total = MAY1 + MAY2 + PML = 18 + 12 + 15 = 45
npvp3 = 100 + 45 = 145.00

Retorno ARS con IVA

precio_ars = 145.00 * 1200 * 1.21 = 210540.00

Response (alias)

```
{
  "success": true,
  "data": {
    "itemId": 104150,
    "type": "PML",
    "value": 15,
    "current": {
      "mlPrice": 210540.0
    }
  }
}

```

---

### 5.8) PCAM

Request

```
{
  "itemId": 104150,
  "type": "PCAM",
  "value": 35
}

```

Validacion

No valida utilidad minima

Update utilidad

```
UPDATE B
SET B.PORC_GANAN_ESTIP6 = 35
FROM NewBytes_DBF.dbo.articulo A
INNER JOIN NEW_BYTES.dbo.ST_GANANCIA_ESTIPULADA_ARTICULOS B
  ON A.cRef = B.ID_ARTICULO
WHERE A.ID_ARTICULO = 104150;

```

Recalculo precio (npvp6)

npvp6 = 100 + (100 * 35 / 100) = 135.00

Response (alias)

```
{
  "success": true,
  "data": {
    "itemId": 104150,
    "type": "PCAM",
    "value": 35,
    "current": {
      "pcam": 35.0
    }
  }
}

```

---

### 5.9) CF

Request

```
{
  "itemId": 104150,
  "type": "CF",
  "value": 40
}

```

Validacion

No valida utilidad minima

Update utilidad

```
UPDATE B
SET B.PORC_GANAN_ESTIPCF = 40
FROM NewBytes_DBF.dbo.articulo A
INNER JOIN NEW_BYTES.dbo.ST_GANANCIA_ESTIPULADA_ARTICULOS B
  ON A.cRef = B.ID_ARTICULO
WHERE A.ID_ARTICULO = 104150;

```

Recalculo precio (npvp4)

npvp4 = 100 + (100 * 40 / 100) = 140.00

Historial

```
INSERT INTO NB_WEB.dbo.historial_precios (fecha, agente, ID_ARTICULO, npvp4)
VALUES (GETDATE(), 123, 104150, 140.00);

```

Response (alias)

```
{
  "success": true,
  "data": {
    "itemId": 104150,
    "type": "CF",
    "value": 40
  }
}

```

---

### 5.10) DT2

Request

```
{
  "itemId": 104150,
  "type": "DT2",
  "value": 15
}

```

Reglas:

- no valida


- no recalcula


- no historial



Update:

```
UPDATE NewBytes_DBF.dbo.articulo
SET ndto2 = 15
WHERE ID_ARTICULO = 104150;

```

Response:

```
{
  "success": true,
  "data": {
    "itemId": 104150,
    "type": "DT2",
    "value": 15,
    "current": {
      "dt2": 15.0
    }
  }
}

```

---

### 5.11) DT3

Request

```
{
  "itemId": 104150,
  "type": "DT3",
  "value": 20
}

```

Update:

```
UPDATE NewBytes_DBF.dbo.articulo
SET ndto3 = 20
WHERE ID_ARTICULO = 104150;

```

Response:

```
{
  "success": true,
  "data": {
    "itemId": 104150,
    "type": "DT3",
    "value": 20,
    "current": {
      "dt3": 20.0
    }
  }
}

```

---

## 6) Punto de control (consistencia)

Este punto es importante para no migrar un bug sin querer:

En el caso PLI, LO2 y MAY2:

- value representa el componente incremental


- la validacion debe sumar base + incremental


- el precio se recalcula con base + incremental



En el caso PL, LO1 y MAY1:

- value representa el componente base


- la validacion debe sumar value + incremental vigente


- el precio se recalcula con base + incremental



---

## CRITERIOS DE ACEPTACIÓN

- Actualiza los 11 tipos de precio


- Valida utilidad mínima con excepciones


- Recalcula precios correctamente


- Maneja lógica resellers


- Registra historial


- Soporta modo solo validación


- Maneja transacciones


- Tests > 80%



---

### Snippet de SELECT (alias base, sin cambiar columnas internas)

```
SELECT
    a.ID_ARTICULO                                          AS itemId,
    fob.FOB                                                AS fob,
    ROUND(a.NCOSTEPROM, 2)                                 AS cost,
    ROUND(a.npvp1, 2)                                      AS unitPrice,
    ROUND(a.npvp5, 2)                                      AS mayPrice,
    ROUND(a.NPLO, 2)                                       AS loCost,
    lop.LOP_EnLo                                           AS priceLoReseller,
    ROUND(pvp.precio, 2)                                   AS PVP,
    ROUND(a.npvp3 * c.CotId1 * (a.ivaVenta / 100.0 + 1), 2) AS mlPrice,
    ROUND(g.PORC_GANAN_ESTIP, 2)                            AS PL,
    ROUND(g.PORC_GANAN_ESTIP2, 2)                           AS PLI,
    ROUND(g.PORC_GANAN_ESTIP3, 2)                           AS MAY1,
    ROUND(g.PORC_GANAN_ESTIPMK1, 2)                         AS PML,
    ROUND(g.PORC_GANAN_ESTIP4, 2)                           AS MAY2,
    ROUND(a.NDTO2, 2)                                       AS DT2,
    ROUND(a.NDTO3, 2)                                       AS DT3,
    ROUND(g.PORC_GANAN_ESTIPLO, 2)                          AS LO1,
    ROUND(g.PORC_GANAN_ESTIPLO1, 2)                         AS LO2,
    ROUND(g.PORC_GANAN_ESTIPMK1, 2)                         AS MK1,
    ROUND(g.PORC_GANAN_ESTIP6, 2)                           AS PCAM,
    ROUND(a.internalTax, 2)                                 AS IINT
;
```
