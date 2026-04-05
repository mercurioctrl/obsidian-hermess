---
jira_key: "PED-827"
aliases: ["PED-827"]
summary: "APP - Refactor - Agregar stock de postventa"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2024-09-19 14:12"
updated: "2024-09-25 11:35"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-827"
---

# PED-827: APP - Refactor - Agregar stock de postventa

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2024-09-19 14:12 |
| Actualizado | 2024-09-25 11:35 |
| Etiquetas | ninguna |
| Jira | [PED-827](https://bluinc.atlassian.net/browse/PED-827) |

## Relaciones

- **Padre:** [[PED-65]] Listado de productos
- **is blocked by:** [[PED-826]] API - Refactor - Agregar al repositorio de productos, aquellos productos que tienen stock en postventa y cuanto stock tiene de manera correspondiente
- **relates to:** [[PED-832]] APP - Refactor - Agregar stock de postventa -> Solo mostrar para roles específicos 
- **relates to:** [[PED-831]] APP - Refactor - Agregar stock de Postventa -> Agregar sucursal

## Descripcion

Ahora que tenemos el parámetro `stockAfterSale` podemos agregarlo en el listado [link](https://lioteam.atlassian.net/browse/PED-826) 

Es importante poder visualizarlo porque es el único stock con el que los usuarios con `user.roleDescription` 'Departamento RMA' o 'Jefe de servicio post venta' son el unico stock con el que pueden interactuar para armar pedidos (suc3)



[adjunto]
Los productos que tienen stock de postventa actualmente son

```
MINI PC GIGABYTE BRIX [[BSRE-1505]] (AMD Ryzen 1505G)
AURICULAR GAMER TRUST FYBER LIGHT DENIM
MOUSE TRUST ONI MICRO WIRELESS BLACK
MOUSE GAMER RAZER VIPER V2 PRO
DISCO SSD ADATA SU650 2.5 480GB
MICROFONO TRUST VELICA STREAMING GXT241
```
