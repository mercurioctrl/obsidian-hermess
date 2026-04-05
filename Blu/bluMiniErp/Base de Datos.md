# Base de Datos

MySQL 8. 47 migraciones. 22 tablas principales.

## Diagrama de relaciones

```
usuarios
   |
   +- gastos (usuario_id)
   +- presupuestos (created_by, nullable)
   +- proyectos (created_by, nullable)
   +- bancos_cajas (usuario_id, nullable)

etiquetas
   +- presupuesto_etiqueta (etiqueta_id)

clientes
   +- presupuestos (cliente_id)
   |     +- items_presupuesto (presupuesto_id, cascade)
   |     +- movimientos_cuenta (presupuesto_id, nullable)
   |     +- presupuesto_etiqueta (presupuesto_id)
   |     +- proyectos (presupuesto_id, unique, nullable)
   |           +- gastos (proyecto_id, nullable)
   |           +- proyecto_empleado (proyecto_id)
   |           +- proyecto_adjuntos (proyecto_id, cascade)
   |           +- proyecto_jira_boards (proyecto_id, cascade)
   |           +- pruebas_ejecucion (proyecto_id)
   |                 +- hitos_ejecucion (prueba_ejecucion_id)
   +- movimientos_cuenta (cliente_id)

empleados
   +- pagos_personal (empleado_id)
   |     +- bancos_cajas (banco_caja_id)
   +- proyecto_empleado (empleado_id)

bancos_cajas
   +- gastos (banco_caja_id)
   +- pagos_personal (banco_caja_id)
```

Ver detalles de cada modelo en [[Backend - Modelos]].

## Tablas

### `usuarios`
| Columna | Tipo | Notas |
|---------|------|-------|
| id | bigint PK | |
| nombre | varchar(200) | |
| email | varchar(150) | unique |
| password | varchar | hashed |
| rol | enum | ADMIN, USUARIO |
| activo | boolean | default true |
| permisos | json | nullable. Ver [[Modulo Permisos]] |
| created_at, updated_at | timestamps | |

### `clientes`
| Columna | Tipo | Notas |
|---------|------|-------|
| id | bigint PK | |
| nombre | varchar(200) | |
| email | varchar(150) | nullable |
| telefono | varchar(50) | nullable |
| empresa | varchar(200) | nullable |
| cuit_dni | varchar(30) | nullable |
| direccion | varchar(300) | nullable |
| moneda_default | enum | ARS, USD |
| notas | text | nullable |
| activo | boolean | default true |
| created_at, updated_at | timestamps | |

### `presupuestos`
| Columna | Tipo | Notas |
|---------|------|-------|
| id | bigint PK | |
| numero | varchar(20) | unique, auto-generado |
| cliente_id | FK -> clientes | |
| fecha | date | |
| estado | enum | BORRADOR, ENVIADO, APROBADO, RECHAZADO, CANCELADO, FACTURADO, COBRADO |
| moneda | enum | ARS, USD |
| tasa_cambio | decimal(10,4) | nullable |
| subtotal | decimal(10,2) | |
| descuento | decimal(10,2) | default 0 |
| descuento_tipo | enum | PORCENTAJE, FIJO |
| iva_monto | decimal(10,2) | |
| total | decimal(10,2) | |
| banco_caja_cobro_id | FK -> bancos_cajas | nullable |
| vigencia_dias | int | |
| observaciones | text | nullable |
| created_by | FK -> usuarios | nullable |
| created_at, updated_at | timestamps | |

Ver flujo de estados en [[Reglas de Negocio#Presupuestos - Flujo de estados]].

### `items_presupuesto`
| Columna | Tipo | Notas |
|---------|------|-------|
| id | bigint PK | |
| presupuesto_id | FK -> presupuestos | cascade delete |
| descripcion | varchar(300) | |
| cantidad | decimal(10,2) | |
| precio_unitario | decimal(10,2) | |
| iva_porcentaje | decimal(5,2) | 0, 10.5, 21 |
| iva_monto | decimal(10,2) | calculado en Model::booted() |
| subtotal | decimal(10,2) | calculado |
| orden | int | |

Ver [[Reglas de Negocio#IVA en Presupuestos]] para detalle del calculo.

### `proyectos`
| Columna | Tipo | Notas |
|---------|------|-------|
| id | bigint PK | |
| presupuesto_id | FK -> presupuestos | nullable, unique |
| cliente_id | bigint | desnormalizado |
| nombre | varchar(300) | |
| estado | varchar | en_progreso, pausado, completado, cancelado |
| fecha_inicio | date | nullable |
| fecha_fin_est | date | nullable |
| notas | text | nullable |
| created_by | FK -> usuarios | nullable |
| created_at, updated_at | timestamps | |

### `proyecto_jira_boards`
Un proyecto puede vincularse a multiples tableros Jira (relacion 1:N).

| Columna | Tipo | Notas |
|---------|------|-------|
| id | bigint PK | |
| proyecto_id | FK -> proyectos | cascade delete |
| jira_project_key | varchar(50) | ej: "ASUS" |
| jira_project_name | varchar(200) | nullable |
| unique(proyecto_id, jira_project_key) | | |

### `movimientos_cuenta`
Representa el debe/haber de clientes. **NO es flujo de caja real.** Ver [[Reglas de Negocio#Cuenta Corriente vs Gastos]].

| Columna | Tipo | Notas |
|---------|------|-------|
| id | bigint PK | |
| cliente_id | FK -> clientes | |
| tipo | enum | CARGO, PAGO, AJUSTE_POSITIVO, AJUSTE_NEGATIVO |
| monto | decimal(10,2) | |
| moneda | enum | ARS, USD |
| descripcion | varchar(300) | |
| presupuesto_id | FK -> presupuestos | nullable |
| tasa_cambio | decimal(10,4) | nullable |
| fecha | datetime | |

### `gastos`
Salidas reales de dinero. Siempre requiere `banco_caja_id`. Ver [[Reglas de Negocio#IVA en Gastos]].

| Columna | Tipo | Notas |
|---------|------|-------|
| id | bigint PK | |
| tipo | enum | OPERATIVO, RETIRO, PROYECTO |
| descripcion | varchar(300) | |
| precio_unitario | decimal(12,2) | |
| cantidad | unsigned int | default 1 |
| iva_porcentaje | decimal(5,2) | default 0. Valores: 0, 10.5, 21, 27 |
| iva_monto | decimal(12,2) | calculado |
| monto | decimal(10,2) | calculado: (precio_unitario x cantidad) + iva_monto |
| moneda | enum | ARS, USD |
| fecha | datetime | |
| categoria | varchar(100) | string plano, NO relacion |
| proyecto_id | FK -> proyectos | nullable |
| usuario_id | FK -> usuarios | |
| tasa_cambio | decimal(10,4) | nullable |
| banco_caja_id | FK -> bancos_cajas | requerido |
| realizado | boolean | default false |

### `bancos_cajas`
| Columna | Tipo | Notas |
|---------|------|-------|
| id | bigint PK | |
| tipo | enum | BANCO, CAJA |
| nombre | varchar(200) | |
| descripcion | text | nullable |
| usuario_id | FK -> usuarios | nullable (CAJA tiene usuario, BANCO no) |
| moneda | enum | ARS, USD |
| saldo_inicial | decimal(10,2) | |
| saldo_actual | decimal(10,2) | ajustado automaticamente |
| activo | boolean | default true |

Ver [[Reglas de Negocio#Bancos y Cajas - Saldo automatico]] para ajustes.

### `movimientos_banco_caja`
Registro historico de todos los movimientos de saldo.

| Columna | Tipo | Notas |
|---------|------|-------|
| id | bigint PK | |
| banco_caja_id | FK -> bancos_cajas | cascade delete |
| tipo | enum | INGRESO, EGRESO, RETIRO, TRANSFERENCIA_IN, TRANSFERENCIA_OUT, GASTO, COBRO |
| monto | decimal(12,2) | siempre positivo |
| saldo_posterior | decimal(12,2) | |
| descripcion | varchar(500) | |
| referencia_id | bigint unsigned | nullable |
| created_at | timestamp | |

### `empleados`
Ver [[Modulo Personal]] para detalle completo.

| Columna | Tipo | Notas |
|---------|------|-------|
| id | bigint PK | |
| nombre | varchar(200) | |
| cargo | varchar(100) | nullable |
| email | varchar(150) | nullable |
| telefono | varchar(50) | nullable |
| salario_base | decimal(10,2) | default 0 |
| moneda_salario | varchar(3) | ARS o USD |
| tipo_contrato | enum | TIEMPO_COMPLETO, MEDIO_TIEMPO, CONTRATO, DIRECTOR, FREELANCE |
| fecha_ingreso | date | nullable |
| activo | boolean | default true |
| notas | text | nullable |

### `proyecto_empleado` (pivot)
Sin timestamps. Ver [[Errores Comunes#withTimestamps en la relacion proyecto_empleado]].

### `pagos_personal`
| Columna | Tipo | Notas |
|---------|------|-------|
| id | bigint PK | |
| empleado_id | FK -> empleados | cascade delete |
| tipo | enum | SUELDO, BONO, AGUINALDO |
| monto | decimal(10,2) | |
| moneda | varchar(3) | |
| fecha | date | |
| descripcion | varchar(300) | nullable |
| banco_caja_id | FK -> bancos_cajas | |

### `pruebas_ejecucion` (Activaciones)
| Columna | Tipo | Notas |
|---------|------|-------|
| id | bigint PK | |
| proyecto_id | FK -> proyectos | |
| numero | int | auto-incremental por proyecto |
| periodo_desde | date | nullable |
| periodo_hasta | date | nullable |
| notas | text | nullable |
| descripcion_ia | text | nullable. Ver [[Backend - API#Evidencias]] |
| descripcion_ia_cant_hitos | unsigned int | nullable |

### `hitos_ejecucion`
| Columna | Tipo | Notas |
|---------|------|-------|
| id | bigint PK | |
| prueba_ejecucion_id | FK -> pruebas_ejecucion | cascade delete |
| orden | int | |
| descripcion | text | |
| categoria_servicio | varchar(200) | nullable |
| actividad_especifica | varchar(300) | nullable |
| qc | decimal(10,2) | Cantidad Comprometida |
| qe | decimal(10,2) | Cantidad Ejecutada |
| qb | decimal(10,2) | QB = QC - QE |
| fecha | date | nullable |
| estado | varchar(50) | Ok / Pendiente Blu / Pendiente Cliente / En Progreso / Cancelado |
| jira_issue_key | varchar(50) | nullable |
| jira_issue_summary | varchar(500) | nullable |

### `etiquetas`
| Columna | Tipo | Notas |
|---------|------|-------|
| id | bigint PK | |
| nombre | varchar(100) | unique |
| color | varchar(7) | hex color |

Ver [[Reglas de Negocio#Etiquetas de Presupuestos]].

### `configuracion`
Tabla singleton. Contiene credenciales de [[Medios de Pago]] (MP, Stripe, Mercury) y Jira.

### `mercadopago_movimientos`
Persistencia local de movimientos de MercadoPago. Ver [[Medios de Pago#MercadoPago]].

### `proyecto_adjuntos`
Enlaces y archivos adjuntos de un proyecto. Ver [[Backend - API#Proyectos]].

---

## Ver tambien

- [[Backend - Modelos]] - Modelos Eloquent con fillable, casts y relaciones
- [[Backend - API]] - Endpoints que operan sobre estas tablas
- [[Reglas de Negocio]] - Logica de dominio sobre los datos
- [[Stack e Infraestructura]] - Configuracion de MySQL en Docker
