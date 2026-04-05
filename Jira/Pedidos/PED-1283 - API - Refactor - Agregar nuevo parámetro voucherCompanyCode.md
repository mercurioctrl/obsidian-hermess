---
jira_key: "PED-1283"
aliases: ["PED-1283"]
summary: "API - Refactor - Agregar nuevo parámetro voucherCompanyCode"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2026-01-26 08:09"
updated: "2026-01-27 00:36"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1283"
---

# PED-1283: API - Refactor - Agregar nuevo parámetro voucherCompanyCode

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-26 08:09 |
| Actualizado | 2026-01-27 00:36 |
| Etiquetas | ninguna |
| Jira | [PED-1283](https://bluinc.atlassian.net/browse/PED-1283) |

## Relaciones

- **Padre:** [[PED-600]] Edicion/Alta de cliente
- **has action item:** [[PED-1284]] APP - Refactor - Agregar selector de empresa de facturación con nuevo parámetro
- **has action item:** [[LOCAPP-99]] API - Refactor - En vez de utilizar companyCode para saber a que CUIT facturar es voucherCompanyCode
- **has action item:** [[PED-1287]] API - Refactor - Agregar voucherCompanyCode para lectura
- **is cloned by:** [[PED-1288]] API - Review - Agregar nuevo parámetro voucherCompanyCode -> Clientes por migrar

## Descripcion

Para permitir que un usuario trabaje asociado a una única empresa sin perder la posibilidad de que un cliente tenga múltiples empresas de facturación, y sin generar problemas de filtrado, es necesario desambiguar el concepto de *company*.

Para ello se incorporará el nuevo parámetro
`[NewBytes_DBF].[dbo].[clientes].voucherCompanyCode`.

Como paso inicial, se migrarán los valores actuales de `companyCode` a `voucherCompanyCode`, de modo de contar con una configuración inicial consistente.

Luego se ajustará el recurso:

```
PATCH {API_URL}/v1/clients/{id}/params
```

```
{
  "currencyId": 1,
  "companyCode": 5,
  "voucherCompanyCode": 9,
  "salespersonId": 12,
  "specialPrice": 0,
  "paymentTerms": 0,
  "profile": 1
}

```

El endpoint deberá continuar aceptando el parámetro `companyCode` (existente y obligatorio de mantener) y además soportar el nuevo parámetro `voucherCompanyCode`, cuyo comportamiento es equivalente pero conceptualmente diferenciado.

---

### Criterios de aceptación

- Existe el campo `voucherCompanyCode` en la tabla
`[NewBytes_DBF].[dbo].[clientes]` (en dev y en produ).


- Todos los registros existentes tienen `voucherCompanyCode` inicializado con el valor previo de `companyCode`.


- El endpoint `PATCH /v1/clients/{id}/params` acepta el parámetro `voucherCompanyCode` sin afectar el funcionamiento actual.


- El endpoint continúa aceptando `companyCode` exactamente como antes, sin cambios de contrato ni regresiones.


- Es posible enviar `companyCode`, `voucherCompanyCode` o ambos en el payload, y los valores se persisten correctamente según lo enviado.


- No se generan errores de validación ni de filtrado al trabajar con clientes que tengan múltiples empresas de facturación.
