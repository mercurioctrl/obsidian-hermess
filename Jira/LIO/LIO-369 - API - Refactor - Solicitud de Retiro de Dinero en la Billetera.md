---
jira_key: "LIO-369"
aliases: ["LIO-369"]
summary: "API - Refactor - Solicitud de Retiro de Dinero en la Billetera "
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2025-06-11 09:51"
updated: "2025-07-02 10:42"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-369"
---

# LIO-369: API - Refactor - Solicitud de Retiro de Dinero en la Billetera 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2025-06-11 09:51 |
| Actualizado | 2025-07-02 10:42 |
| Etiquetas | ninguna |
| Jira | [LIO-369](https://bluinc.atlassian.net/browse/LIO-369) |

## Relaciones

- **Padre:** [[LIO-231]] Billetera

## Descripcion

**Correcciones en el endpoint de retiro de dinero POST /cash-out de V4.**

- **Adaptar a nueva estructura de base de datos**:

- Actualizar el código para utilizar el campo 

```
clients_bank_account_hash
```

en lugar de 

```
clients_bank_account_id
```

para adaptarse a los cambios en la estructura de la tabla 

```
PendingCashOut
```




- Modificar el método **prepareData()** para incluir correctamente el nuevo campo en la preparación de datos.




- **Modificar el código de transacción**:

- Se cambió el código de transacción 

```
TR_CODIGO
```

de 26 (Depósito en Banco) a 8 (salidas varias) en el método **createMovement()** para asegurar que se registre correctamente en la tabla de movimientos.




- **Mejora en la gestión de IDs**:

- Se implementó el almacenamiento del ID de cuenta corriente (**ctaCteId**) después de crear un movimiento para asegurar que esté disponible en llamadas posteriores.


- Se mejoró el método **insert()** para manejar mejor los parámetros SQL utilizando consultas preparadas con nombres de parámetros para mayor seguridad y claridad.
