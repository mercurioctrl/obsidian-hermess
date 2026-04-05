---
jira_key: "BLUWEB-184"
aliases: ["BLUWEB-184"]
summary: "APP - Refactor - Probar en una nueva rama, fondo nuevo para hero-section "
status: "LISTO"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-09-23 08:42"
updated: "2025-09-26 09:40"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/BLUWEB-184"
---

# BLUWEB-184: APP - Refactor - Probar en una nueva rama, fondo nuevo para hero-section 

| Campo | Valor |
|-------|-------|
| Estado | LISTO (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-09-23 08:42 |
| Actualizado | 2025-09-26 09:40 |
| Etiquetas | ninguna |
| Jira | [BLUWEB-184](https://bluinc.atlassian.net/browse/BLUWEB-184) |

## Relaciones

- **Padre:** [[BLUWEB-141]] Refactor primera iteración
- **action item from:** [[BLUWEB-183]] 3.DSG - Feat - Generar un nuevo background (hero-section) que contenga a la "chica de las gafas" para usar en el sitio
- **has action item:** [[BLUWEB-186]] APP - Refactor - Incluir nuevo fondo con figura para cada caso de uso

## Descripcion

Armar 3 **variantes de la hero section** usando las imágenes que subiste (`BLU_1_40.png`, `BLU_1_30.png`, `BLU_1_20.png`), cada una en una rama diferente del proyecto (o usando *feature flags* si prefieren evitar ramas que pueda pasarse en la url).

Así podrán comparar cómo queda la proporción del espacio ocupado por la chica en relación al fondo y decidir cuál funciona mejor.

### 2. Alternativa con *feature flags*

Si quieren evitar ramas múltiples:

- Se puede parametrizar la hero en el código y cargar dinámicamente la imagen según un *flag* de configuración (por ejemplo en la url).


- Así pueden cambiar entre variantes sin hacer `checkout` de ramas.



### 3. Mantener el fondo original si se usa en otro lado

El **background original sin la chica** no debe ser reemplazado si aparece en otra seccion.
Ese se sigue usando donde ya esté aplicado, como una versión *simple*.

[adjunto]


[adjunto]
[adjunto]
