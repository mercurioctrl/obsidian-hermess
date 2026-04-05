---
jira_key: "PED-1204"
aliases: ["PED-1204"]
summary: "API - Feat - Leer parametros de usuario de libre opcion para un cliente de NB (Capa 1)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Franco Callipo"
reporter: "Catriel Mercurio"
created: "2025-12-26 09:39"
updated: "2026-01-14 10:21"
labels: ["esperandoDependencia"]
jira_url: "https://bluinc.atlassian.net/browse/PED-1204"
---

# PED-1204: API - Feat - Leer parametros de usuario de libre opcion para un cliente de NB (Capa 1)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Franco Callipo |
| Reportado por | Catriel Mercurio |
| Creado | 2025-12-26 09:39 |
| Actualizado | 2026-01-14 10:21 |
| Etiquetas | esperandoDependencia |
| Jira | [PED-1204](https://bluinc.atlassian.net/browse/PED-1204) |

## Relaciones

- **Padre:** [[PED-600]] Edicion/Alta de cliente
- **has action item:** [[PED-1202]] API - Feat - Editar parametros de usuario de libre opcion para un cliente de NB (Capa 1)
- **action item from:** [[PED-1202]] API - Feat - Editar parametros de usuario de libre opcion para un cliente de NB (Capa 1)
- **is cloned by:** [[PED-1247]] API - Refactor - Leer parámetros de usuario de libre opción para un cliente de NB (Capa 1) -> Agregar seguridad y estructura de respuesta

## Descripcion

Al igual que existe un recurso para **editar usuarios de Libre Opción**, se requiere exponer un recurso de **lectura** que permita **obtener la información básica del usuario de LO** asociado a un cliente determinado.

Este recurso será utilizado por capas superiores (backoffice / paneles administrativos) para **consultar el estado y los datos principales del usuario**, sin necesidad de acceder directamente a la base de datos.

---

### Nuevo recurso a implementar (Libre Opción)

```
GET /v1/loUser/{clientLo}
```

---

### Comportamiento esperado

- El recurso debe **obtener los datos del usuario de Libre Opción** desde la tabla `LO.dbo.usuarios`.


- El parámetro `{clientLo}` se utiliza para vincular con `LO.dbo.usuarios.id`.


- El endpoint es **solo lectura** y no debe producir efectos colaterales.



---

### Respuesta esperada

**Ejemplo de response:**

```
{
  "name": "Hernan Jose",
  "disabled": true,
  "mail": "dfsdfsdf@fsdf.com"
}
```

---

### Mapeo de campos

| Campo response | Columna en DB |
| --- | --- |
| name | LO.dbo.usuarios.nombre |
| mail | LO.dbo.usuarios.correo |
| disabled | LO.dbo.usuarios.activo |

> ⚠️ El campo `password` **no debe exponerse** bajo ningún concepto.


---

### Casos a contemplar

- Si el `{clientLo}` no existe, el recurso debe responder con un **error controlado** (ej. `404 Not Found`).


- Si el usuario existe pero se encuentra deshabilitado, el recurso debe devolver igualmente la información, reflejando `disabled = true`.


- El recurso no debe devolver campos adicionales no especificados en el contrato.
