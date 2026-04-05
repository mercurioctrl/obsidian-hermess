---
jira_key: "LIO-413"
aliases: ["LIO-413"]
summary: "API  - Refactor - Recibir token de referido al hacer login (este caso es para cuando esta guardado en localStorage, porque aun no logueo)"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-08-07 09:29"
updated: "2025-08-31 23:09"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-413"
---

# LIO-413: API  - Refactor - Recibir token de referido al hacer login (este caso es para cuando esta guardado en localStorage, porque aun no logueo)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-08-07 09:29 |
| Actualizado | 2025-08-31 23:09 |
| Etiquetas | ninguna |
| Jira | [LIO-413](https://bluinc.atlassian.net/browse/LIO-413) |

## Relaciones

- **Padre:** [[LIO-408 - Referidos|LIO-408]] Referidos
- **has action item:** [[LIO-438 - APP - Feat - Procesar token de referido cuando el usuario lo lleva en la url|LIO-438]] APP - Feat - Procesar token de referido cuando el usuario lo lleva en la url (con y sin login)

## Descripcion

Dado que existen momentos donde se ingresa a un link de referido y aun no estoy logueado, entonces el token-referido estara alojado en el local storage hasta que se inicie session. Para eso haremos un refactor del recurso de login para recibir el token

```
POST {API_URL}/v4/auth/login
```

```
{
  "username":"user@gmail.com",
  "password":"9995fe63c0f7bcSaaS50S34S21SfS49d",
  "referalToken": "referalToken" <-- Si el front tiene esto en el localStorage, lo envia, sino sera null
}
```

Cuando recibo este token-referidi me fijo si ya figura para este usuario en la tabla `[LO].[dbo].user_referrals` y si no esta lo creo. En caso de estar, actualizo solo la fecha.

## **Tabla:**`[LO].[dbo].user_referrals`

Registra qué referido está vinculado actualmente a un usuario para atribuirle comisiones a quien genero el referido.
Un usuario normalmente tendrá **una sola atribución activa** (según la política de first-click o last-click).

| Campo | Tipo | Descripción |
| --- | --- | --- |
| `id` | BIGINT UNSIGNED (PK) | Identificador único del registro |
| `usuarioID` | BIGINT UNSIGNED (FK users) | Usuario al que se le asigna un referido |
| `referral_id` | BIGINT UNSIGNED (FK referrals) | ID del token de referido asignado |
| `attributed_at` | TIMESTAMP | Fecha en que se atribuyó el referido al usuario |
| `valid_until` | TIMESTAMP NULL | Fecha hasta la que es válida la atribución (ventana de conversión) |
| `created_at` | TIMESTAMP | Fecha de creación del registro |
| `updated_at` | TIMESTAMP | Fecha de última actualización del registro |

---

##  **Índices recomendados**

- **UNIQUE(**`user_id`**)** → Si solo permitís un referido activo por usuario.


- **INDEX(**`referral_id`**)** → Para buscar rápido todas las atribuciones de un referido.


- **INDEX(**`valid_until`**)** → Para filtrar atribuciones vigentes.
