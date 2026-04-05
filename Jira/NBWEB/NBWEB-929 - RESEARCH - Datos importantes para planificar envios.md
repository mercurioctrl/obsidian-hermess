---
jira_key: "NBWEB-929"
aliases: ["NBWEB-929"]
summary: "RESEARCH - Datos importantes para planificar envios"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-11-25 07:46"
updated: "2025-01-21 15:59"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-929"
---

# NBWEB-929: RESEARCH - Datos importantes para planificar envios

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-11-25 07:46 |
| Actualizado | 2025-01-21 15:59 |
| Etiquetas | ninguna |
| Jira | [NBWEB-929](https://bluinc.atlassian.net/browse/NBWEB-929) |

## Relaciones

- **Padre:** [[NBWEB-423]] Logistica Envios
- **has action item:** [[STASK-6]] TASK - Marcar envíos que llegaron a destino - Oportunidad de mejora -> Guardar tiempo desde que lo tomo el currier hasta que lo entregaron
- **has action item:** [[STASK-8]] API - Feat - Task - Relevamiento de datos para evaluar tiempos logisticos

## Descripcion

Lo que queremos es evaluar que requerimientos necesitamos para evaluar las siguiente informacion, tanto por pedido como por zonas.

Se busca dar cuenta de que datos se necesitara. como los recolectaremos, y donde se guardaran. 

- Costos y tarifas por zona


- Tiempo de entrega por zona


- Fiabilidad por zona (Entregas exitosas vs perdidas, etc)





**Research:**

- **Microservicios Afectados:**

- **API Envios:** Generar etiquetas.


- **API Pedidos:**

- Al asignar transportista. 


- Para la autorización del transportista.




- **API LO y NB:** También involucradas en la asignación del transportista.


- API Cobros ?: → *comentarle a catri si al liquidar desde caja se debe marcar este momento.*







*Nota: Rastrear y analizar el proceso completo de envío para identificar si es que existe el cuello de botella interno.*



- Comparar los tiempos reales de envío contra los tiempos estimados prometidos, y medir la eficiencia y cumplimiento de los transportistas.


- **Proceso:**


- **PASO 1:** Cotización del envío: Se registra el tiempo estimado en una nueva tabla asociada a la orden y sucursal.


- **PASO 2:** Autorización: Se marca un tiempo en la tabla cuando el pedido es autorizado para envío.


- **PASO 3:** Generación de etiqueta: Se registra otro tiempo en la tabla al generar la etiqueta.


- **PASO 4:** Seguimiento periódico al transportista: Se actualiza la tabla con la fecha final de entrega una vez que el pedido es recibido por el cliente.





- **Datos a Capturar:**

- **Fechas y horas claves: **Cotización, autorización, generación de etiqueta, entrega final.


- Tiempos estimados prometidos para la entrega.


- **Zona geográfica** (`zoneId`) asociada al envío.


- Transportista asignado y tiempos promedios por transportista y zona.







- **Análisis y Métricas que se lograrian obtener:**

- **Tiempo total de envío real:** Fecha/hora de inicio hasta la entrega final.


- **Cumplimiento de estimaciones:** Comparar tiempo real vs. estimado.


- **Estadísticas:** Por transportista y zona geográfica (promedios y cumplimiento).


- **Identificación de retrasos:** Listar envíos que exceden tiempos estimados.


- **Alertas:** Automatizar notificaciones para envíos con retrasos significativos.







Sugiero generar una tabla nueva, podrias llamarse ShippingTracking que mediante order y branch. se pueda obtener esta información.

EJ:

```
CREATE TABLE shipping_tracking (
    id INT IDENTITY(1,1) PRIMARY KEY,              -- Identificador único para cada registro
    order_id BIGINT NOT NULL,                      -- Número de orden
    branch CHAR(4) NOT NULL,                       -- Código de sucursal
    code_postal INT NOT NULL,                      -- Identificador de la zona
    carrier NVARCHAR(100) NOT NULL,                -- Nombre del transportista
    estimated_time INT NOT NULL,                   -- Tiempo estimado de entrega en minutos
    quoted_at DATETIME NOT NULL,                   -- 1 - Fecha y hora de cotización
    authorized_at DATETIME NULL,                   -- 2 - Fecha y hora de autorización
    label_generated_at DATETIME NULL,              -- 3 - Fecha y hora de generación de etiqueta
    delivered_at DATETIME NULL,                    -- 4 - Fecha y hora de entrega
    created_at DATETIME DEFAULT GETDATE(),         -- Fecha de creación del registro
    updated_at DATETIME DEFAULT GETDATE()          -- Última fecha de actualización
);

```

al tener las fechas marcas asi: 

```
    quoted_at DATETIME NOT NULL,                   -- 1 - Fecha y hora de cotización
    authorized_at DATETIME NULL,                   -- 2 - Fecha y hora de autorización
    label_generated_at DATETIME NULL,              -- 3 - Fecha y hora de generación de etiqueta
    delivered_at DATETIME NULL,                    -- 4 - Fecha y hora de entrega
```

se puede entender en el proceso interno donde esta la demora.
