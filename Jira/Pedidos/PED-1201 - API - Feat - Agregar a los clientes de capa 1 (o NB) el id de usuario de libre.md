---
jira_key: "PED-1201"
aliases: ["PED-1201"]
summary: "API - Feat - Agregar a los clientes de capa 1 (o NB) el id de usuario de libre opción"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Franco Callipo"
reporter: "Catriel Mercurio"
created: "2025-12-26 07:25"
updated: "2026-01-05 14:57"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1201"
---

# PED-1201: API - Feat - Agregar a los clientes de capa 1 (o NB) el id de usuario de libre opción

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Franco Callipo |
| Reportado por | Catriel Mercurio |
| Creado | 2025-12-26 07:25 |
| Actualizado | 2026-01-05 14:57 |
| Etiquetas | ninguna |
| Jira | [PED-1201](https://bluinc.atlassian.net/browse/PED-1201) |

## Relaciones

- **Padre:** [[PED-600 - EdicionAlta de cliente|PED-600]] Edicion/Alta de cliente
- **relates to:** [[PED-1202 - API - Feat - Editar parametros de usuario de libre opcion para un cliente de NB|PED-1202]] API - Feat - Editar parametros de usuario de libre opcion para un cliente de NB (Capa 1)

## Descripcion

#### **Contexto**

El sistema se organiza en **capas lógicas** que representan distintos modelos de negocio.

- **Capa 1 (NB / NewBytes)**: representa la cadena de distribución mayorista y es la base de todos los clientes.


- Capas superiores (por ejemplo **Libre Opción**) se apoyan sobre Capa 1.



Bajo este criterio, **todo cliente de Libre Opción es previamente un cliente de Capa 1**, almacenado en `NewBytes_DBF.dbo.clientes`.

Para poder gestionar correctamente los usuarios de Libre Opción desde la base unificada de clientes, necesitamos **vincular explícitamente ambos mundos**.

#### **Objetivo**

Agregar el **ID de usuario de Libre Opción** (`LO.dbo.usuarios`) al cliente de Capa 1, utilizando la columna existente:

```
NewBytes_DBF.dbo.clientes.clientLo
```

Esto permitirá identificar fácilmente qué clientes de Capa 1 están asociados a un usuario de Libre Opción.

#### **Alcance técnico**

Refactorizar el endpoint:

```
GET {API_URL}/v1/clients
```

Actualmente el recurso devuelve un listado de clientes con múltiples parámetros.
Se debe **incorporar un nuevo campo **`clientLo` en cada elemento de la lista, obtenido directamente de `NewBytes_DBF.dbo.clientes.clientLo`.

#### **Cambio esperado en la respuesta**

**Antes**

```
{
  "ccodcli": 92305,
  "businessName": "Emanuel Jesus",
  "email": "ferreyra-emanuel@outlook.com"
  ... otros parametros ...
  }
```

**Después**

```
{
  "ccodcli": 92305,
  "clientLo": 4344,
  "businessName": "Emanuel Jesus",
  "email": "ferreyra-emanuel@outlook.com"
  ... otros parametros ...
}
```

#### **Reglas**

- El campo `clientLo` debe incluirse **siempre** en la respuesta.


- Si `NewBytes_DBF.dbo.clientes.clientLo` está `NULL` o vacío, el valor devuelto debe ser:



```
"clientLo": null
```

- No se deben modificar otros campos ni el comportamiento actual del endpoint.



#### **Criterios de aceptación**

- El endpoint `/v1/clients` devuelve el nuevo campo `clientLo` para todos los clientes.


- El valor coincide con el almacenado en `NewBytes_DBF.dbo.clientes.clientLo`.


- En ausencia de relación con Libre Opción, el campo se devuelve como `null`.


- No se rompe compatibilidad con consumidores actuales del endpoint.
