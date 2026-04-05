---
jira_key: "NBWEB-669"
aliases: ["NBWEB-669"]
summary: "API - Feat - Dataset para limites de exclusion"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Guillermo Avila"
reporter: "Catriel Mercurio"
created: "2024-03-25 10:48"
updated: "2024-04-01 12:30"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-669"
---

# NBWEB-669: API - Feat - Dataset para limites de exclusion

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Guillermo Avila |
| Reportado por | Catriel Mercurio |
| Creado | 2024-03-25 10:48 |
| Actualizado | 2024-04-01 12:30 |
| Etiquetas | ninguna |
| Jira | [NBWEB-669](https://bluinc.atlassian.net/browse/NBWEB-669) |

## Relaciones

- **Padre:** [[NBWEB-668]] Envíos bonificados
- **blocks:** [[NBWEB-670]] MS - Feat - Cotizar con la bonificacion desde ms-envios directamente
- **blocks:** [[NBWEB-671]] APP - Feat- Mostrar los que tienen precios en cero, como GRATIS y mensaje con condiciones

## Descripcion

Se debe en primero lugar ubicar todos los cogidos postales de capital y de el primer cordón del conurbano.

**Definicion Primer cordón**

Avellaneda, Lanús, Lomas de Zamora, La Matanza (parte este), Morón, Tres de Febrero, San Martín, Vicente López, San Isidro.

Es posible que cada una de estos partidos o municipios tengas mas de un código postal.

Crearemos entonces una tabla llamada `[NB_WEB].[dbo].bonusShippingZipCode`

Con las columnas 

- id (autonumerica)


- zipCode (entero)


- placeId
