---
jira_key: "PED-1208"
aliases: ["PED-1208"]
summary: "Gestión de Aportes y Gastos de Marketing"
status: "Finalizada"
type: "Epic"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2026-01-05 06:51"
updated: "2026-01-20 17:25"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1208"
---

# PED-1208: Gestión de Aportes y Gastos de Marketing

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Epic |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-05 06:51 |
| Actualizado | 2026-01-20 17:25 |
| Etiquetas | ninguna |
| Jira | [PED-1208](https://bluinc.atlassian.net/browse/PED-1208) |

## Relaciones

*Sin relaciones*

## Descripcion

## **Objetivo del sistema**

**El objetivo de este MVP es ordenar, registrar y auditar los aportes económicos que realizan las marcas para acciones de marketing, y tener trazabilidad clara de:**

- **cuánto aporta cada marca**


- **en qué acciones se usa ese aporte**


- **cuánto se gastó efectivamente**


- **qué saldo queda disponible**



**Todo el sistema está pensado para trabajar de forma contable, soportando pesos y dólares, con tipo de cambio propio por cada movimiento.**

Documento MVP  

---

## Recursos de la API – resumen funcional

### POST /v1/marketing/funds

Crea un fondo de marketing asociado a una marca (`marcas.id`).
Representa un aporte presupuestario, no un gasto.
Define moneda (ARS/USD), monto original y vencimiento opcional.
Inicializa el control de asignado y gastado en cero.
Es el punto de partida de todo el sistema.

### GET /v1/marketing/funds

Lista los fondos existentes, filtrables por marca, moneda y vigencia.
Devuelve no solo el aporte original sino también lo asignado, gastado y los saldos disponibles por fondo.
Permite saber cuánto presupuesto queda por fondo sin recalcular movimientos.
Se usa para inspección detallada (fondo por fondo) y auditoría operativa.

### **GET /v1/marketing/brands**

Lista las marcas que tienen fondos y devuelve los **totales agregados por marca** (y por moneda), incluyendo: aportado total, asignado total, gastado total y saldos disponibles.
Evita que el front tenga que agrupar o recorrer páginas de fondos para responder “cuánto tengo por marca”.
Es el recurso principal para dashboards de disponibilidad por marca.
Soporta filtros típicos como vigencia (`activeOnly`), moneda (`currency`) y búsqueda por referencia (`q`).

### POST /v1/marketing/actions

Crea una acción de marketing (ej. Hot Sale, Black Friday).
La acción no tiene dinero propio, solo agrupa gastos.
Puede tener fechas o ser atemporal.
Sirve como contenedor lógico para presupuestos y movimientos.

### GET /v1/marketing/actions

Lista acciones con su presupuesto asignado y gasto real por moneda.
Permite filtrar por marca indirectamente (acciones financiadas por fondos de esa marca).
Muestra cuánto se asignó, cuánto se gastó y cuánto queda por acción.
Es la vista de control de ejecución de campañas.

### POST /v1/marketing/allocations

Asigna un monto de un fondo a una acción (presupuesto máximo).
Reserva presupuesto antes de gastar, evitando sobreuso del fondo.
Actualiza los totales del fondo y de la acción en la misma transacción.
Define el límite operativo contra el cual se validan los gastos.

### POST /v1/marketing/movements

Registra un gasto real imputado a una acción y un fondo.
Guarda monto original, moneda, tipo de cambio usado y monto final descontado.
Valida que no se exceda el fondo ni la asignación correspondiente.
Es la única operación que consume dinero real.

### GET /v1/marketing/movements

Lista los movimientos para auditoría y análisis.
Permite filtrar por marca, fondo, acción y rango de fechas.
Muestra el gasto original y su impacto real en el fondo.
Es el respaldo contable y trazable del sistema.

---

## Cómo se espera que se use la herramienta (flujo completo)

### 1) La marca aporta dinero

Se crea uno o más fondos (`POST /funds`) que representan presupuestos disponibles (ARS/USD).

### 2) Se define qué se va a hacer

Se crean acciones (`POST /actions`) que representan campañas o iniciativas.

### 3) Se reserva presupuesto antes de gastar

Desde los fondos se asignan montos a acciones (`POST /allocations`), fijando límites claros por acción.

### 4) Se registran los gastos reales

Cada gasto se carga como movimiento (`POST /movements`), con su tipo de cambio real si aplica (FX por movimiento).

### 5) Se controla y audita

- Para ver **disponibilidad por marca (dashboard)**: `GET /v1/marketing/brands`


- Para ver el detalle **fondo por fondo**: `GET /v1/marketing/funds?brandId=...`


- Para ver ejecución de campañas: `GET /v1/marketing/actions`


- Para auditar gastos y conversiones: `GET /v1/marketing/movements`



---

## Idea clave del diseño

- Los fondos no se gastan directamente → primero se asignan.


- Las acciones no tienen dinero propio → solo consumen lo asignado.


- El tipo de cambio se fija por movimiento, no se recalcula jamás.


- Todo es trazable, auditable y consistente **sin vistas** ni “magia oculta”; los totales operativos se exponen por endpoints (en particular `GET /marketing/brands` para agregados por marca).
