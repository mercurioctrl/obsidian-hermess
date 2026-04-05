---
jira_key: "EXP-143"
aliases: ["EXP-143"]
summary: "Feat - Remito fiscal"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Guillermo Avila"
reporter: "Catriel Mercurio"
created: "2023-01-18 08:28"
updated: "2023-03-07 20:23"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-143"
---

# EXP-143: Feat - Remito fiscal

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Guillermo Avila |
| Reportado por | Catriel Mercurio |
| Creado | 2023-01-18 08:28 |
| Actualizado | 2023-03-07 20:23 |
| Etiquetas | ninguna |
| Jira | [EXP-143](https://bluinc.atlassian.net/browse/EXP-143) |

## Relaciones

- **Padre:** [[EXP-1 - Base y Repositorios|EXP-1]] Base y Repositorios
- **Subtarea:** [[EXP-144 - DATASET- Feat - Obtener informacion legal y numeraciones (con punto de corte)|EXP-144]] DATASET- Feat - Obtener informacion legal y numeraciones (con punto de corte)
- **Subtarea:** [[EXP-145 - MS - APP - Feat - Maqueta en el ms de comprobantes el remito fiscal|EXP-145]] MS - APP - Feat - Maqueta en el ms de comprobantes el remito fiscal
- **Subtarea:** [[EXP-146 - MS - API - Feat - Conectar objeto para remito fiscal en comprobantes|EXP-146]] MS - API - Feat - Conectar objeto para remito fiscal en comprobantes
- **Subtarea:** [[EXP-147 - API - Feat - Recurso para remito fiscal|EXP-147]] API - Feat - Recurso para remito fiscal
- **Subtarea:** [[EXP-148 - APP - Feat - Se debe poder descargar de ambos listados de pedidos el remito|EXP-148]] APP - Feat - Se debe poder descargar de ambos listados de pedidos el remito fiscal con preview, imprimir y descarga
- **Subtarea:** [[EXP-183 - APP - Refactor - Dejar espacio en blanco para la firma, y mover direccion con|EXP-183]] APP - Refactor -  Dejar espacio en blanco para la firma, y mover direccion con los datos del cliente y observaciones a la izquierda
- **blocks:** [[SNB-478 - sistema nuevo|SNB-478]] sistema nuevo

## Descripcion

El remito fiscal debe contener como mínimo las siguientes características descritas en el sitio de AFIP

[link](https://servicioscf.afip.gob.ar/publico/abc/ABCpaso2.aspx?id_nivel1=562&id_nivel2=619&id_nivel3=748#:~:text=368685%20%2D%20%C2%BFQu%C3%A9%20datos%20deben%20contener,los%20remitos%20clase%20%22R%22%3F&text=Los%20comprobantes%20deber%C3%A1n%20contener%20en,el%20centro%20del%20espacio%20superior.) 

Fecha de publicación: 25/10/2005

Los comprobantes deberán contener en forma preimpresa:

-Los datos identificatorios del emisor en el extremo superior izquierdo (cuit,nombre de la empresa, direcion, etc).

-La letra "R" y la leyenda "Documento no válido como factura" en forma destacada en el centro del espacio superior.

-Punto de venta, numeración y CUIT en el extremo superior derecho (o Abajo).

-El Código de Autorización de Impresión (CAI) y la fecha de vencimiento en el espacio inferior derecho.



- **Fuente:** Anexo V RG 1415/03
