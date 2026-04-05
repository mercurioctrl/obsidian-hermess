---
jira_key: "COM-149"
aliases: ["COM-149"]
summary: "APP - Refactor - Modal y cantidades de una orden"
status: "Finalizada"
type: "Subtarea"
priority: "Highest"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2024-11-26 16:13"
updated: "2024-12-17 10:38"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-149"
---

# COM-149: APP - Refactor - Modal y cantidades de una orden

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Highest |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2024-11-26 16:13 |
| Actualizado | 2024-12-17 10:38 |
| Etiquetas | ninguna |
| Jira | [COM-149](https://bluinc.atlassian.net/browse/COM-149) |

## Relaciones

- **Padre:** [[COM-38 - Ver orden de compra|COM-38]] Ver orden de compra
- **action item from:** [[COM-148 - API - Refactor - Cambios en cantidades de los items|COM-148]] API - Refactor - Cambios en cantidades de los items

## Descripcion

**A)** Es la cantidad que estamos ingresando en el momento, un numero entero. Y cada vez que uno lo abre esta en cero, no proviene de ningún atributo sino que es un input para hacer nuevos ingresos. Si valaro maximo es la diferencia entre `amount` y `amountEntered` `(valorMaximoInput = amount - amountEntered)` lo cual permite que nunca puedan ingresarse mas que la cantidad comprada al proveedor.

**B) **Mostraremos dos números separados por una barra para dar cuentas cuantos ingresaron a la izquierda, y cuantos son los que deben ingresar en total.

De tal modo que si ingresaron 5 de 10 unidades que tienen la orden mostraremos: 5/10 siendo la siguiente estructura `amountEntered / amount`

[adjunto]
Seria bueno agregar en ambas columnas una “i” informativa para explicar de que se trata cada parametro.
