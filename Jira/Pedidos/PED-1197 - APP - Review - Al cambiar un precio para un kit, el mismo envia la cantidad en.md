---
jira_key: "PED-1197"
aliases: ["PED-1197"]
summary: "APP - Review - Al cambiar un precio para un kit, el mismo envia la cantidad en cero (cuando es kit, debo repetir la cantidad del kit para que no se cambie por error). Lo mismo sucede al cambiar la cantidad."
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-12-19 15:44"
updated: "2025-12-26 16:22"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1197"
---

# PED-1197: APP - Review - Al cambiar un precio para un kit, el mismo envia la cantidad en cero (cuando es kit, debo repetir la cantidad del kit para que no se cambie por error). Lo mismo sucede al cambiar la cantidad.

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-12-19 15:44 |
| Actualizado | 2025-12-26 16:22 |
| Etiquetas | ninguna |
| Jira | [PED-1197](https://bluinc.atlassian.net/browse/PED-1197) |

## Relaciones

- **Padre:** [[PED-1170 - Kits|PED-1170]] Kits

## Descripcion

### Cómo se reproduce el problema

- Se toma una orden existente que **contiene un kit**.


- Al kit se le asigna una cantidad mayor a 1 (por ejemplo, **10 unidades**).


- Luego, **se modifica el precio del kit**.



---

### Comportamiento observado

- Después de cambiar el precio, la **cantidad del kit pasa a 0**.


- Esto ocurre automáticamente, sin que el usuario cambie explícitamente la cantidad.



---

### Hipótesis (a validar)

- Al modificar el precio, el sistema **reconstruye el payload** del kit.


- En ese nuevo payload:

- El **ID del ítem del kit cambia** (o no coincide con el ID original).


- La cantidad estaba asociada al ID anterior.




- Como el sistema **no logra mapear el nuevo ID con la cantidad existente**, la cantidad queda en **0**.



[adjunto]
