---
jira_key: "COM-35"
aliases: ["COM-35"]
summary: "API - Listar ordenes de compra - Depósitos no coincidentes"
status: "Finalizada"
type: "Error"
priority: "Highest"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Guillermo Avila"
created: "2024-02-16 13:04"
updated: "2024-02-19 17:24"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-35"
---

# COM-35: API - Listar ordenes de compra - Depósitos no coincidentes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Highest |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Guillermo Avila |
| Creado | 2024-02-16 13:04 |
| Actualizado | 2024-02-19 17:24 |
| Etiquetas | ninguna |
| Jira | [COM-35](https://bluinc.atlassian.net/browse/COM-35) |

## Relaciones

- **Padre:** [[COM-8]] Ordenes de compra
- **blocks:** [[COM-22]] API - Refactor - Listar ordenes de compra ->Agregados

## Descripcion

La descripción del depósito no coincide con la descripción en base de datos.

[adjunto]
[adjunto]
Dato extra:
Está tomando la descripción del depósito del nombre del proveedor.

```
public function providerOrder(array $filters, array $pagination): array
    {
        $get = "SELECT
                    fp_proveedores.cnompro as warehouseDescription <------- *
    }
```
