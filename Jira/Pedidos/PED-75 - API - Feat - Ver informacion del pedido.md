---
jira_key: "PED-75"
aliases: ["PED-75"]
summary: "API - Feat - Ver informacion del pedido"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-09-17 21:20"
updated: "2024-01-02 17:06"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-75"
---

# PED-75: API - Feat - Ver informacion del pedido

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-09-17 21:20 |
| Actualizado | 2024-01-02 17:06 |
| Etiquetas | ninguna |
| Jira | [PED-75](https://bluinc.atlassian.net/browse/PED-75) |

## Relaciones

- **Padre:** [[PED-8]] Listar ordenes de compra
- **blocks:** [[PED-76]] APP - Feat - Ver informacion del pedido
- **is blocked by:** [[PED-421]] API - Ver información del pedido - Obtener WhatsApp

## Descripcion

Existe en la actualidad una herramienta muy utilizada, porque permite obtener de una forma simple y fácil de compartir el contenido del pedido y otros detalles específicos que al cliente le interesan como un resumen rápido.

Se debe mostrar algo exactamente como estos ejemplos, respetando cada linea, y agrando una linea por cada producto.

**Ejemplo 1**

```
Información del pedido 0002 - 10328553

Cliente: Libre Opcion (032103)
Vendedor: Web Sistema
Cotización: 398.41

1 - PARLANTE TRUST TYTAN 2.0 GXT608  21,00% | 94,61 | 94,61
1 - SERVICIO DE TRANSPORTE  21,00% | 4,53 | 4,53
1 - COSTO FINANCIERO  21,00% | 7,10 | 7,10

Total: u$s 106,25 | $ 42.329,28
Total Final: u$s 128,56 | $ 51.218,43
```



**Ejemplo 2 (con percepcion y ya realizado el remito)**

```
Información del remito X000200566068
Orden 0002 - 10328553

Cliente: COMERCIALIZADORA ARVEN S.A.S. (031311)
Vendedor: Soto Lautaro
Cotización: 395.0

1 - TECLADO Y MOUSE TRUST TREZO WIRELESS ECO ES  10,50% | 44,08 | 44,08

Total: u$s 44,08 | $ 17.409,63
Percepcion: 1.5 (u$s0.66 $261.14)
Total Final: u$s 49,36 | $ 19.498,78

```

```
GET {API_URL}/v1/aboutOrder/{branch y order}
```

**Consulta ostentativa **

```sql
SELECT albclil.*, albclit.cnumped, albclil.cDetalle as cdetalle, albclil.cDetalle as cDetalle, albclil.ncanent as ncanped
  FROM [NewBytes_DBF].[dbo].[albclit]
  LEFT JOIN [NewBytes_DBF].[dbo].[albclil] On albclil.ID_NROREMCLI_ENC = albclit.ID_NROREMCLI_ENC
  WHERE albclit.cnumalb = ? AND albclit.cnumsuc = ?
```
