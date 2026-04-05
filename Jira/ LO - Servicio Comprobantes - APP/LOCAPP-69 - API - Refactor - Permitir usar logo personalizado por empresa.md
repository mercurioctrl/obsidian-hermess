---
jira_key: "LOCAPP-69"
aliases: ["LOCAPP-69"]
summary: "API - Refactor - Permitir usar logo personalizado por empresa"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-06-03 08:25"
updated: "2025-06-22 20:07"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LOCAPP-69"
---

# LOCAPP-69: API - Refactor - Permitir usar logo personalizado por empresa

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-06-03 08:25 |
| Actualizado | 2025-06-22 20:07 |
| Etiquetas | ninguna |
| Jira | [LOCAPP-69](https://bluinc.atlassian.net/browse/LOCAPP-69) |

## Relaciones

- **Padre:** [[LOCAPP-68 - Cabecera e informacion complementaria|LOCAPP-68]] Cabecera e informacion complementaria

## Descripcion

Se debe realizar un refactor sobre el recurso:

```
GET {API_URL}/v2/F/{nroComprobante}/{token}
```

para incorporar la funcionalidad de mostrar un logo personalizado por empresa emisora del comprobante

```
...
"neto105": "0,00",
"iva105": "0,00",
"neto0": "0,00",
"iva0": "0,00",
"iibbPerception": "0,00",
"internalTax": "0,00",
"perceptionCabaCharged": "0,00",
"perceptionArbaCharged": "0,00"
},
"pie": {
"cae": "75208714963986",
"vencimientoCae": "30/05/2025"
},
"recursos": {
"logoEmpresa": <<--- SERIA ESTE CAMPO

....
```

Hacer que cada empresa registrada en la base de datos tenga su propio logo en los comprobantes emitidos, sin alterar la lógica actual relacionada a logos de tienda o de Libre Opción.

- Modificar el recurso mencionado para que, al renderizar un comprobante, se obtenga el logo desde la tabla: `[NewBytes_DBF].[dbo].[FP_Empresas]`



- Se debe agregar una nueva columna a esa tabla:



```
invoiceLogo VARCHAR(255) NULL
```

que almacenará la ruta del logo personalizado.

- Si el campo `invoiceLogo` de la empresa emisora está **completo**, se usará esa imagen como logo en el comprobante.


- Si el campo invoiceLogo es nulo, se deberá usar el logo predeterminado:

```
/img/60198d50831f5c4fbe0f0e24cc7cc687.png
```




- No se debe modificar la lógica relacionada a logos de tienda ni a Libre Opción. Solo afecta al logo superior de la empresa emisora.


- Verificar que la ruta del logo exista y sea accesible. Si falla, usar también el logo predeterminado.


- No alterar la lógica ni los parámetros actuales del endpoint.



### Criterios de aceptación:

- Comprobantes muestran el logo correspondiente si la empresa tiene `invoiceLogo` definido.


- Comprobantes usan el logo predeterminado si el campo es nulo o la ruta es inválida.


- Las tiendas y Libre Opción siguen mostrando sus logos sin cambios.


- El nuevo campo `invoiceLogo` está correctamente agregado a la tabla.
