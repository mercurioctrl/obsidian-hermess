---
jira_key: "NBWEB-943"
summary: "API - Feat - Task - Relevamiento de datos para evaluar tiempos logisticos "
status: "Tareas por hacer"
type: "Tarea"
priority: "Medium"
assignee: "Sin asignar"
reporter: "Catriel Mercurio"
created: "2025-01-21 14:42"
updated: "2025-01-21 15:57"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-943"
---

# NBWEB-943: API - Feat - Task - Relevamiento de datos para evaluar tiempos logisticos 

| Campo | Valor |
|-------|-------|
| Estado | Tareas por hacer (Por hacer) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Sin asignar |
| Reportado por | Catriel Mercurio |
| Creado | 2025-01-21 14:42 |
| Actualizado | 2025-01-21 15:57 |
| Etiquetas | ninguna |
| Jira | [NBWEB-943](https://bluinc.atlassian.net/browse/NBWEB-943) |

## Descripción

Siguiendo lo desarrollado en el research ( [link](https://lioteam.atlassian.net/browse/NBWEB-929) ) y lo conversado, haremos un recurso de syncpUp para evaluar la duracion de las distintas etapas logísticas desde la compra realizada en el sitio web, hasta que el correo puede entregarlo.

El recurso lo trabajaremos en el servicio o repositorio [link](https://github.com/New-Bytes/service-task-v3) 

Si bien esto esta pensado para poder evaluar sobre todo las cadenas logísticas de las empresas de correo (OCA, Andreani, Entregar, etc) tambien sirve par evaluar los procesos internos para cualquier orden.

```
PATCH {{API_URL}}/v1/syncUp/updateLogisticPeriods?token={tokenEnVariablesDeEntorno}
```

## ¿Que hace el recurso?

El recurso se ejecuta periódicamente (Por ejemplo cada 5 minutos) busca completar pendientes en la tabla `shipping_tracking`

Es decir que todas o casi todas las claves `branch - order` tendrán su consecuente en la tabla  `shipping_tracking`. De esta forma sabemos que si no esta, debemos agregarlo como primera medida y luego ya es cuestión de evaluar su estado y otras “flags” para completar hasta donde pueda con fechas y horarios (y otros).Z     

## 1 - `promise_quoted_at` (guarda nuestra promesa de entrega en los sitios)

Fecha y hora donde teóricamente informamos se entregaría. Este es un dato que debemos tratar parecido a como hacemos con los tamaños de bulto, es decir que al momento de procesarse la compra debemos tenerlo disponible, seguramente via front para almacenar y de ahi podremos tomarlo mas tarde para convertirlo a DATETIME y guardar en `shipping_tracking`.`promise_quoted_at`

## 2 - `ordered_at` (guarda la fecha de la compra)

Fecha de la orden (Esta puede tomarse directo de pedclit y es cuando el cliente/vendedor hace la orden)

## 3 - `ordered_proccess_at` (evalúa al vendedor)

Fecha de liquidación, esto es el momento en el que ventas ya hizo su parte y dejo listo el pedido para ser cobrado o directamente armado.

## 4 - `authorized_at` (evalúa a cobranzas)

Fecha y hora de autorización, es decir que fue pagado (o tiene autorización de despacho sin pago) y ya puede ser preparado. Es el punto donde ya tienen autorizado armarlo en expedición.

 Esta es la fecha donde primera vez leíste que el pedido esta en estado autorizado o posterior:  Osea, `id_status == 2 || id_status == 11 || id_status == 10`

Importante: Si al momento de registrar` authorized_at` aun no esta `ordered_proccess_at`, se marcan con la misma fecha porque el proceso entre ambas fue muy rápido

## 5- `build_at` (evalúa al expedicionista)

Fecha del momento en el que detectamos la primera vez que el pedido se encuentra en alguno de los siguientes estados `id_status == 4`

Importante: Si al momento de registrar` build_at` aun no esta `authorized_at`, se marcan con la misma fecha porque el proceso entre ambas fue muy rápido

## 6 -`label_generated_at` (evalúa al expedicionista)

Fecha de creación de la etiqueta, muestra en momento en el que se genero la etiqueta para que la misma pueda ser recogida por el correo

## 7 - `dispatched_at`  (evalúa el tiempo desde que esta preparado a que lo retira el correo)

Fecha del momento en el que detectamos la primera vez que el pedido se encuentra en alguno de los siguientes estados `id_status == 16 || id_status == 15 || id_status == 14 || id_status == 13 || id_status == 3`

Importante: Si al momento de registrar` dispatched_at` aun no esta `build_at` o `authorized_at`, se marcan con la misma fecha porque el proceso entre ambas fue muy rápido

## **8 - **`delivered_at` (evalúa al correo externo)

Esta fecha se obtiene apoyándose en la tarea de [link](https://lioteam.atlassian.net/browse/STASK-5) y se trata de cuando finalmente detectamos que fue entregado por el correo



**Tabla de referencia de estados** `[NEW_BYTES].[dbo].[MS_STATUS_REMITO]`

```
1	Pendientes a Autorizar
2	Autorizados. Pendiente a despachar
4	Armado Finalizado
3	Despachado, Pendiente a Cobrar
9	A Facturar Sin Autorizar
11	Serializado
10	Parcialmente Serializado
12	Facturado Por No Autorizado
13	Entregado Cobrado
14	Entregado, Pendiente a cobrar
15	Acreditacion completa
16	Entregado. Acreditacion parcial
```

```
CREATE TABLE shipping_tracking (
    id INT IDENTITY(1,1) PRIMARY KEY,              -- Identificador único para cada registro
    order_id BIGINT NOT NULL,                      -- Número de orden
    branch CHAR(4) NOT NULL,                       -- Código de sucursal
    code_postal INT NOT NULL,                      -- Identificador de la zona
    carrier NVARCHAR(100) NOT NULL,                -- Nombre del transportista
    estimated_time INT NOT NULL,                   
    promise_quoted_at
    quoted_at DATETIME NOT NULL,
    ordered_proccess_at                   
    authorized_at DATETIME NULL,
    build_at
    dispatched_at                  
    label_generated_at DATETIME NULL,              
    delivered_at DATETIME NULL,                    
    created_at DATETIME DEFAULT GETDATE(),         -- Fecha de creación del registro
    updated_at DATETIME DEFAULT GETDATE()          -- Última fecha de actualización
);
```
