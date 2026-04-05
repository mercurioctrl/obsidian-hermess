---
jira_key: "NBE-212"
aliases: ["NBE-212"]
summary: "API - Refactor - Reducir campos olbigatorioso en registro dado un parametro para tal fin en las variables globales (.env)"
status: "Listo"
type: "Tarea"
priority: "High"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-12-09 07:55"
updated: "2025-12-09 15:15"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBE-212"
---

# NBE-212: API - Refactor - Reducir campos olbigatorioso en registro dado un parametro para tal fin en las variables globales (.env)

| Campo | Valor |
|-------|-------|
| Estado | Listo (Listo) |
| Tipo | Tarea |
| Prioridad | High |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-12-09 07:55 |
| Actualizado | 2025-12-09 15:15 |
| Etiquetas | ninguna |
| Jira | [NBE-212](https://bluinc.atlassian.net/browse/NBE-212) |

## Relaciones

- **Padre:** [[NBE-211]] Mejoras de usabilidad para captar clientes
- **relates to:** [[NBE-213]] APP - Refactor - Minificar a un solo paso reducido al formulario de registro

## Descripcion

Recordar que NBE es la misma API que NB configurada distinta

Refactorizar el endpoint 

```
PUT /v1/registrationRequest
```

 para soportar un modo de **registro mínimo** controlado por un flag en `.env` (ej: `REGISTRATION_MINIMAL_ENABLED`).

Cuando el flag esté **activo**, sólo serán obligatorios:

- `email`


- `username`


- `password`



El resto de los campos dejarán de ser requeridos:

- Si vienen en el request, se persisten normalmente.


- Si no vienen:

- Se completan con **valores genéricos por defecto** los campos que sean **NOT NULL** en la base (ej: provincia/localidad = CABA) o se usaran estrategias lógicas, por ejemplo: Para el campo `showName`, lo copiaremos de `userName`, que si lo tenemos y es casi lo mismo.


- Se guardan en **NULL** los campos que lo permitan.





Cuando el flag esté **inactivo**, se mantiene el comportamiento actual del registro (validaciones completas).

---

### Criterios de aceptación

- Con flag OFF → el endpoint funciona igual que hoy.


- Con flag ON → permite alta sólo con `email`, `username`, `password`.


- Sin alguno de esos tres campos → error de validación.


- La inserción nunca debe fallar por restricciones NOT NULL.


- Requests completos siguen funcionando sin cambios en ambos modos.
