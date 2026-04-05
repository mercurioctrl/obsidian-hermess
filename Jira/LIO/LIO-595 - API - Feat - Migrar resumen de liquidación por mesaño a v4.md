---
jira_key: "LIO-595"
aliases: ["LIO-595"]
summary: "API - Feat - Migrar resumen de liquidación por mes/año a v4"
status: "Ready for QA"
type: "Subtarea"
priority: "Medium"
assignee: "Franco Callipo"
reporter: "Catriel Mercurio"
created: "2026-03-31 17:30"
updated: "2026-04-01 17:48"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-595"
---

# LIO-595: API - Feat - Migrar resumen de liquidación por mes/año a v4

| Campo | Valor |
|-------|-------|
| Estado | Ready for QA (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Franco Callipo |
| Reportado por | Catriel Mercurio |
| Creado | 2026-03-31 17:30 |
| Actualizado | 2026-04-01 17:48 |
| Etiquetas | ninguna |
| Jira | [LIO-595](https://bluinc.atlassian.net/browse/LIO-595) |

## Relaciones

- **Padre:** [[LIO-537]] Migración de repositorios previa deprecación de la api legacy
- **has action item:** [[LIO-597]] APP - Feat - Migrar resumen de liquidacion por mes/año a v4
- **has action item:** [[LIO-592]] APP Mobile - Feat - Migrar liquidaciones v3-legacy a LO-v4

## Descripcion

Migrar el endpoint `GET /liquidaciones/resumen/{mes}/{anio}` desde la API v3 a la API v4 (Laravel), permitiendo consultar el resumen de liquidación de meses anteriores para vendedores.

---

### **Description**

Actualmente en v4 existen los endpoints:

- `GET /liquidaciones/resumen-actual`


- `GET /liquidaciones/meses-previos`



Falta migrar el endpoint que permite consultar el resumen de un mes específico anterior, utilizado cuando el vendedor selecciona un mes desde el frontend.

Este endpoint debe replicar el comportamiento de v3, incluyendo el cálculo combinado de productos **nativos y no nativos (UNION ALL)**.

---

### **Objective**

Permitir que frontend y app de vendedores consuman el resumen mensual histórico desde v4 sin depender de v3.

---

### **Scope**

#### Incluye

- Endpoint: `GET /api/liquidaciones/resumen/{mes}/{anio}`


- Arquitectura: Controller → Service → Repository


- Queries de:

- Productos nativos


- Productos no nativos (UNION ALL)




- Resolución de `vendedorId` desde JWT



---

### **Endpoint**

`GET /api/liquidaciones/resumen/{mes}/{anio}`

---

### **Request**

| Campo | Valor |
| --- | --- |
| Método | GET |
| Auth | Bearer Token (JWT) |
| Path Params | `mes` (string, ej: "Septiembre"), `anio` (string, ej: "2025") |
| Query Params | - |
| Body | - |

---

### **Response (200)**

```
{
  "ganancia": 15234.50,
  "comision": 1200.00,
  "ventasGanancia": 48500.00,
  "ventasComision": 12300.00,
  "total": 14034.50,
  "mes": "Septiembre",
  "año": "2025"
}
```

#### Sin datos

```
{
  "ganancia": 0.0,
  "comision": 0.0,
  "ventasGanancia": 0.0,
  "ventasComision": 0.0,
  "total": 0.0,
  "mes": "Septiembre",
  "año": "2025"
}
```

---

### **Errores**

| Código | Descripción |
| --- | --- |
| 401 | Token inválido o expirado |
| 400 | Usuario no es vendedor |
| 500 | Error interno |

---

### **Business Rules**

-  Solo usuarios con perfil **vendedor** 


-  Filtrado por mes usando `DATENAME(MONTH, fechaCreacion)` 


-  Ganancia neta ≥ 0 



#### Fórmulas

- `ganancia` = nativos + no nativos 


- `comision` = suma de ambos 


- `ventasGanancia` = solo nativos 


- `ventasComision` = solo no nativos 


- `total` = ganancia - comision 



---

### **DB Involucrada**

#### LO

- `pedidosDetalle` 


- `pedidosDetalleLiquidacion` 


- `pedidosCabeceraVendedor` 


- `pedidosCabecera` 


- `vendedores` 



#### NewBytes_DBF

- `pedclit` 



---

### **Joins Clave**

```
PD -> PDL
PD -> PCV
PCV -> PC
PCV -> PED (solo nativos)
```

---

### **Consideraciones**

-  A diferencia de `resumen-actual`, este endpoint incluye **nativos + no nativos** 


- `SUM()` puede devolver NULL → manejar con `ISNULL` o `?? 0` 


-  Dependencia del idioma del SQL Server (mes en español) 


-  Case sensitivity depende del collation 



---

### **Acceptance Criteria**

-  Devuelve datos correctos para vendedor autenticado 


-  Coincide con v3 para mismo período 


- `total = ganancia - comision` 


-  Sin datos → valores en `0.0` 


-  Usuario no vendedor → 400 


-  Sin token → 401 


-  Incluye UNION ALL (nativos + no nativos) 


-  Ruta protegida con `token.auth` 


-  Respeta estructura v4 existente 



---

### **QA Notes**

-  Comparar v3 vs v4 (mismo vendedor y mes) 


-  Probar: 

-  Mes con datos 


-  Mes sin datos 


-  Mes inválido (`Sept`, `September`) 




-  Validar seguridad (sin token / rol incorrecto) 


-  Validar `ventasComision` (debe tener valor real)
