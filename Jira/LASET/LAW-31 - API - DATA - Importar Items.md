---
jira_key: "LAW-31"
aliases: ["LAW-31"]
summary: "API - DATA - Importar Items"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-09-02 09:40"
updated: "2025-09-05 00:49"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LAW-31"
---

# LAW-31: API - DATA - Importar Items

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-09-02 09:40 |
| Actualizado | 2025-09-05 00:49 |
| Etiquetas | ninguna |
| Jira | [LAW-31](https://bluinc.atlassian.net/browse/LAW-31) |

## Relaciones

- **Padre:** [[LAW-30 - Onboarding de la nueva empresa en los sistemas del grupo NB|LAW-30]] Onboarding de la nueva empresa en los sistemas del grupo NB

## Descripcion

Necesitamos cargar en la tabla `articulo` los ítems de **Laset** a partir de una fuente de datos externa (archivo adjunto). La clave funcional es **un ítem por SKU** (agrupado por columna **SKU [G]**). Cada ítem quedará asociado a la **distribuidora Laset** (creada en [[INV-198]]) y a la **empresa 11** (`FP_Empresas`).

Lo que haremos es crear los items para laset en la tabla articulos (Desarrollo)

Para esto agruparemos por el SKU [G] teniendo en cuenta de que un SKU con puede repetirse dentro de la misma empresa, pero si de otras (companyCode, sku)

---

Insertar/actualizar (upsert) registros en `[NewBytes_DBF].[dbo].[articulo]` con el mapeo indicado, garantizando:

- Unicidad por `(ID_PRODUCTO) (companyCode, sku)`


- Idempotencia de la carga (si se vuelve a importar, no duplica)


- Consistencia de `Cref = id_articulo`



---

Para esto cargaremos en base a estos datos la tabla `[NewBytes_DBF].[dbo].[articulo]` tienendo en cuenta al menos las columnas siguientes

- Cref ← igual que id_articulo


- cDetalle ← Es el nombre que se ubica en Nombre Producto [H] 


- nCosteProm ← por ahora tomaremos el valor de Costo Fob [S]


- ID_PRODUCTO ← Es igual a SKU [G]


- id_distribuidora ← Remite a la historia [link](https://bluinc.atlassian.net/browse/INV-198)  donde crearemos una nueva distribuidora Llamada Laset (es tanto una distribuidora como una empresa)


- companyCode ← es la empresa 11 dentro del repositorio `[NewBytes_DBF].[dbo].[FP_Empresas]`




Tal vez se escapo algo, pero mas o menos es asi.. en la daily lo podemos charlar un poco mas extenso y en la reunion con laset, tambien cargaremos marcas y categorías en próximas historias
