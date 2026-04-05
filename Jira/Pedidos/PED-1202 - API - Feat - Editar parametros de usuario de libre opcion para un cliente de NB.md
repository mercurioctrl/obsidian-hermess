---
jira_key: "PED-1202"
aliases: ["PED-1202"]
summary: "API - Feat - Editar parametros de usuario de libre opcion para un cliente de NB (Capa 1)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Franco Callipo"
reporter: "Catriel Mercurio"
created: "2025-12-26 08:03"
updated: "2026-01-06 10:47"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1202"
---

# PED-1202: API - Feat - Editar parametros de usuario de libre opcion para un cliente de NB (Capa 1)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Franco Callipo |
| Reportado por | Catriel Mercurio |
| Creado | 2025-12-26 08:03 |
| Actualizado | 2026-01-06 10:47 |
| Etiquetas | ninguna |
| Jira | [PED-1202](https://bluinc.atlassian.net/browse/PED-1202) |

## Relaciones

- **Padre:** [[PED-600 - EdicionAlta de cliente|PED-600]] Edicion/Alta de cliente
- **relates to:** [[PED-1201 - API - Feat - Agregar a los clientes de capa 1 (o NB) el id de usuario de libre|PED-1201]] API - Feat - Agregar a los clientes de capa 1 (o NB) el id de usuario de libre opción
- **action item from:** [[PED-1204 - API - Feat - Leer parametros de usuario de libre opcion para un cliente de NB|PED-1204]] API - Feat - Leer parametros de usuario de libre opcion para un cliente de NB (Capa 1)
- **has action item:** [[PED-1204 - API - Feat - Leer parametros de usuario de libre opcion para un cliente de NB|PED-1204]] API - Feat - Leer parametros de usuario de libre opcion para un cliente de NB (Capa 1)
- **is cloned by:** [[PED-1233 - API - Refactor - Editar parametros de usuario de libre opcion para un cliente|PED-1233]] API - Refactor - Editar parametros de usuario de libre opcion para un cliente de NB (Capa 1) -> Mejora en el objeto de respuesta

## Descripcion

Al igual que en el caso de los **usuarios de Capa 1** —donde las entidades *usuario* y *cliente* son conceptos distintos—, se requiere exponer un recurso que permita **editar usuarios de forma simple y controlada**.

Actualmente existe un recurso para editar los **usuarios de NewBytes (NB)** asociados a un cliente. Este recurso nos sirve como referencia, ya que la funcionalidad a implementar es conceptualmente equivalente, pero aplicada a los **usuarios de Libre Opción (LO)**.

---

### Recurso existente (referencia)

Este endpoint permite modificar el usuario de NB vinculado a un cliente (disponible en Postman):

```
PATCH /v1/user/{userNB}
```

**Payload de ejemplo (campos editables):**

```
{
  "username": "Hern1",
  "showName": "Hernán Laurant2",
  "disabled": true,
  "mail": "dfsdfsdf@fsdf.com",
  "password": "tejey8ioXn2"
}

```

---

### Nuevo recurso a implementar (Libre Opción)

Se debe crear un recurso equivalente para **editar usuarios de Libre Opción**:

```
PATCH /v1/loUser/{clientLo}

```

**Payload de ejemplo:**

```
{
  "name": "Hernan Jose",
  "disabled": true,
  "mail": "dfsdfsdf@fsdf.com",
  "password": "tejey8ioXn2"
}

```

---

### Comportamiento esperado

- El recurso debe modificar la tabla `LO.dbo.usuarios`.


- El parámetro `{clientLo}` se utiliza para vincular con `LO.dbo.usuarios.id`.



**Mapeo de campos:**

| Payload | Columna en DB |
| --- | --- |
| mail | LO.dbo.usuarios.correo |
| password | LO.dbo.usuarios.password |
| disabled | LO.dbo.usuarios.activo |
| username | LO.dbo.usuarios.username |

> ⚠️ **Importante:**
Solo deben actualizarse los campos que estén presentes en el payload.
Los campos omitidos no deben ser modificados.
