---
jira_key: "LAW-47"
summary: "API -PED - Refactor - Agregar permiso `includeNull` en `permisos_agente`"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2026-03-10 08:45"
updated: "2026-03-13 18:58"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LAW-47"
---

# LAW-47: API -PED - Refactor - Agregar permiso `includeNull` en `permisos_agente`

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2026-03-10 08:45 |
| Actualizado | 2026-03-13 18:58 |
| Etiquetas | ninguna |
| Jira | [LAW-47](https://bluinc.atlassian.net/browse/LAW-47) |

## Descripción

# Backend: Agregar permiso `includeNull` en `permisos_agente`

## Descripción

Agregar el campo `includeNull` a la tabla `NB_WEB.dbo.permisos_agente` para que el usuario tenga (o no) permiso de ver repositorios particulars sin `companyCode` asignado. Este campo debe viajar en el objeto `user` que devuelve 

```
GET /v1/auth/user
```

---

## Paso 1 — Migración en base de datos

Ejecutar en SQL Server:

```
ALTER TABLE [NB_WEB].[dbo].[permisos_agente]
ADD includeNull BIT NOT NULL DEFAULT 0;
```

> Por defecto `0` (sin permiso). Los usuarios que necesiten el permiso deben actualizarse manualmente o desde el panel de administración.


---

## Resultado final

Luego de estos cambios, el objeto devuelto por `GET /v1/auth/user` incluirá:

```
{
  "user": {
    "id": 123,
    "username": "...",
    "companyCode": "NB",
    "includeNull": false,
    ...
  }
}
```

El frontend puede leer `user.includeNull` y pasarlo como parámetro al llamar `/shippingMethods?companyCode=NB&includeNull=true`.
