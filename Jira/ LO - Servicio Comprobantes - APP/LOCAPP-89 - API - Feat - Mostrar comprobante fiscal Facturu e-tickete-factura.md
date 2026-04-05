---
jira_key: "LOCAPP-89"
aliases: ["LOCAPP-89"]
summary: "API - Feat - Mostrar comprobante fiscal Facturu e-ticket/e-factura"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-10-17 12:03"
updated: "2025-12-05 03:36"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LOCAPP-89"
---

# LOCAPP-89: API - Feat - Mostrar comprobante fiscal Facturu e-ticket/e-factura

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-10-17 12:03 |
| Actualizado | 2025-12-05 03:36 |
| Etiquetas | ninguna |
| Jira | [LOCAPP-89](https://bluinc.atlassian.net/browse/LOCAPP-89) |

## Relaciones

- **Padre:** [[LOCAPP-88]] FactUru
- **has action item:** [[LOCAPP-81]]  APP - MVP -Feat - Crear maqutacion para eticket y efactura (voucher) FACTURU 
- **has action item:** [[LOCAPP-80]] MVP - Vouchers para LASET (eticket, efactura,packingList "PL", SLI)

## Descripcion

Exponer un endpoint para **recuperar el comprobante uruguayo** (e-Ticket) en formato JSON, tomando como fuente nuevas tablas de persistencia:

- `[NewBytes_DBF].[dbo].[FP_FactWebCliEncabezado_Uy]`


- `[NewBytes_DBF].[dbo].[FP_FactWebCliDetalle_Uy]`



Se intentará **reutilizar lógica** existente separándola por `companyCode` en un repositorio ya existente. Si no es posible, se crearán componentes específicos para UY.

```
GET {API_URL}/v2/FUy/{nroComprobante}/{token}
```

```
{
  "cabecera": {
    "tipoComprobante": "e-Ticket",
    "formaPago": "Crédito",
    "moneda": "USD",
    "nroFactura": "0001",
    "tipoSerie": "A",
    "empresa": {
      "nombre": "LASET SOCIEDAD ANÓNIMA",
      "direccion": "PRADINES CLEMENTE 1795",
      "ciudad": "MONTEVIDEO",
      "rut": "217502910019"
    },
    "cliente": {
      "nombre": "EMAP SA",
      "rut": "PY 80046875-9",
      "direccion": "Av Carlos A. Lopez c/Adrian Jara, Ciudad del Este, Paraguay",
      "email": "juanperez@gmail.com"
    },
    "fechas": {
      "fechaVencimiento": "2025-01-01",
      "fechaEmision": "2025-01-01"
    }
  },
  "productos": [
    {
      "cantidad": 1,
      "sku": "1234567890",
      "descripcion": "Producto 1",
      "precio": 100
    }
  ],
  "totales": {
    "subtotalGravado": 92000,
    "subtotalNoGravado": 92000,
    "iva": 19320,
    "total": 111320,
    "noFacturable": 10000,
    "totalAPagar": 101320
  },
  "pie": {
    "fechaEmision": "2025-01-01",
    "CAE": "1234567890",
    "rango": "2601-3600",
    "codSeguridad": "1234567890",
    "fechaVencimientoCae": "2025-01-01",
    "urlQR": "https://www.lasetcorp.com/",
    "adenda": "Bienes enajenados en el Exterior   \nCondición de Venta: FCA  \nNro de Referencia: PI-PY-427  \nNro de PL: #MSI 11086987  \nForma de Pago: 30 días fecha de factura\n\nBank:  Ocean Bank  \nBank Address: 780 NW 42nd Ave, Miami Florida 33162, USA  \nABA: 066011392  \nSWIFT: OCBKUS3M  \nBeneficiary Name: Laset Sociedad Anonima  \nBeneficiary Address: Pradines Clemente 1795 (CP 11500)  \nBeneficiary Account #: 2538098205"
  }
}

```

La adenda podemos tomarla de `[NB_WEB].[dbo].[addendum]` ver ( ver [https://bluinc.atlassian.net/browse/PED-1120](https://bluinc.atlassian.net/browse/PED-1120))

la condición de venta de la adenda (incoterm) sale de [link](https://bluinc.atlassian.net/browse/PED-1122)
