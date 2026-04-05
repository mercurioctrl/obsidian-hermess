---
jira_key: "PED-1148"
aliases: ["PED-1148"]
summary: "API - Review - Agregar al repositorio de clientes los balances de cuentas (Revision de datos respecto a api de caja y redondeo)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-10-08 07:17"
updated: "2025-11-11 10:44"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1148"
---

# PED-1148: API - Review - Agregar al repositorio de clientes los balances de cuentas (Revision de datos respecto a api de caja y redondeo)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-10-08 07:17 |
| Actualizado | 2025-11-11 10:44 |
| Etiquetas | ninguna |
| Jira | [PED-1148](https://bluinc.atlassian.net/browse/PED-1148) |

## Relaciones

- **Padre:** [[PED-54 - Cuenta corriente de clientes|PED-54]] Cuenta corriente de clientes

## Descripcion

```
GET {API_URL}/v1/clients?balanceState={balanceState}
```

Durante las pruebas del repositorio de **Cuentas Corrientes y Balance de Clientes**, se observó que los resultados presentan una leve diferencia respecto al repositorio de **Caja**, ya que el primero parece traer más registros que el segundo.

Es importante entender la causa de esta diferencia para determinar si:

- En **Caja** están faltando registros, o


- En **Cuentas Corrientes / Pedidos** se están incluyendo registros de más.



El objetivo final es que ambos repositorios reflejen la misma información contable para unificar los resultados visibles en las aplicaciones de backoffice y reportes.

---

### 💡 Oportunidad de mejora

Se detectó además una posible mejora en la **precisión de los cálculos**:

- Actualmente, los valores se estiman con más de dos decimales, lo que genera inconsistencias visuales como saldos tipo `-0.00000034` o `0.004324324`.


- Se propone **redondear los cálculos a dos decimales** para evitar mostrar microdiferencias y representar correctamente el saldo real del cliente (deudor, acreedor o neutro).
