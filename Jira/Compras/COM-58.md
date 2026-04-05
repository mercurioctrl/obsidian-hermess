---
jira_key: "COM-58"
summary: "API - Ver detalle de un proveedor - Descripción de localidad faltante"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2024-02-20 18:07"
updated: "2024-02-21 15:47"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-58"
---

# COM-58: API - Ver detalle de un proveedor - Descripción de localidad faltante

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2024-02-20 18:07 |
| Actualizado | 2024-02-21 15:47 |
| Etiquetas | ninguna |
| Jira | [COM-58](https://bluinc.atlassian.net/browse/COM-58) |

## Descripción

Al consultar el detalle de un proveedor no aparece la descripción de la localidad.

[attachment]
[attachment]
Dato extra:
No existe relación para obtener la ciudad.

```
public function getProviderById(int $id): array
    {
        $get = "SELECT
                  ...
                FROM [NewBytes_DBF].[dbo].[FP_Proveedores]
                LEFT JOIN NewBytes_DBF.dbo.FP_Paises as Country ON Country.Id_Pais = FP_Proveedores.Id_Pais
                      <------------------------------**
                WHERE ID_PROVEEDOR = :id ";
    }
```
