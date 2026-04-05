---
jira_key: "NBWEB-68"
aliases: ["NBWEB-68"]
summary: "Descargar Carrito en TXT"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-03-30 08:35"
updated: "2022-07-11 09:13"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-68"
---

# NBWEB-68: Descargar Carrito en TXT

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-03-30 08:35 |
| Actualizado | 2022-07-11 09:13 |
| Etiquetas | ninguna |
| Jira | [NBWEB-68](https://bluinc.atlassian.net/browse/NBWEB-68) |

## Relaciones

- **Padre:** [[NBWEB-1 - API - Carrito de compras|NBWEB-1]] API - Carrito de compras

## Descripcion

Utilizando el recurso 

```
{{API_URL}}/v1/carrito/Download/Txt
```

debe descargarse un archivo nomenclado como `id_carrito_por_el_que_cambiar.txt`

con un contenido del siguiente tipo



```
Información del Carrito 10264700

Cliente: LAZAGA EZEQUIEL ROBERTO (027502)
Vendedor: Julian Albarracin
Cotización: 115.75

10 - MONITOR BENQ LED 24 L GW2480 24W BLACK  21,00% | 215,12 | 2.151,19
10 - ACCESORIOS ADATA carry GABINETE P/SSD EX500 RED  21,00% | 10,44 | 104,40
1 - MEMORIA ADATA DIMM XPG GAMMIX 32GB DDR4 3200 CBKD45  10,50% | 141,46 | 141,46

Total: u$s 2.397,04 | $ 277.457,95
Percepcion: 3 (u$s71.91 $8323.74)
Total Final: u$s 2.957,48 | $ 342.328,61

```



*para obtener El nombre del vendedor es posible vincular `[NewBytes_DBF].[dbo].[clientes].ccodage = NewBytes_DBF.DBO.agentes.ccodage`, seleccionando las columnas `agentes.cnbrage, agentes.capeage`
