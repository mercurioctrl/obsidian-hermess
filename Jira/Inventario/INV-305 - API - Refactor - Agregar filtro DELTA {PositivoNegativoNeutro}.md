---
jira_key: "INV-305"
aliases: ["INV-305"]
summary: "API - Refactor - Agregar filtro DELTA {Positivo/Negativo/Neutro}"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-12-26 09:47"
updated: "2026-01-09 13:27"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-305"
---

# INV-305: API - Refactor - Agregar filtro DELTA {Positivo/Negativo/Neutro}

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-12-26 09:47 |
| Actualizado | 2026-01-09 13:27 |
| Etiquetas | ninguna |
| Jira | [INV-305](https://bluinc.atlassian.net/browse/INV-305) |

## Relaciones

- **Padre:** [[INV-199]] Control de Stock / Stock en general  / Control de Precios
- **has action item:** [[INV-306]] APP - Refactor - Agregar filtro DELTA {Positivo/Negativo/Neutro}

## Descripcion

Se debe incorporar un nuevo filtro opcional en el recurso de listado de **itemsStocks** que permita acotar los resultados según el signo del **DELTA**.
Este filtro deberá poder combinarse libremente con cualquiera de los filtros existentes.

El objetivo es facilitar la detección de inconsistencias de stock, permitiendo reducir rápidamente el universo de registros a analizar.

#### Nuevo parámetro

```
GET {API_URL}/itemsStocks?delta={positive|negative|neutral}
```

- **positive** → DELTA > 0


- **negative** → DELTA < 0


- **neutral** → DELTA = 0



#### Consideraciones de implementación

- El filtro por `delta` debe aplicarse **únicamente** cuando el parámetro esté presente en la request.


- Si `delta` no es enviado, **no debe agregarse ninguna condición adicional a la query**, evitando así impactos innecesarios en la performance del repositorio.


- El filtro debe ser compatible y combinable con el resto de los parámetros existentes del endpoint.



#### Performance

- En caso de ser necesario, se deberán crear los índices correspondientes para soportar este filtrado de manera eficiente.


- La historia debe incluir la definición de las cláusulas necesarias para poder replicar dichos índices en producción.



Si no esta el filtro presenta no se incluye nada referido a el en el where, y muestra todos los delta normalmente
