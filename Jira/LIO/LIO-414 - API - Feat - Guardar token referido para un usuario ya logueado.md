---
jira_key: "LIO-414"
aliases: ["LIO-414"]
summary: "API - Feat - Guardar token referido para un usuario ya logueado"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-08-08 08:36"
updated: "2025-09-17 08:46"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-414"
---

# LIO-414: API - Feat - Guardar token referido para un usuario ya logueado

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-08-08 08:36 |
| Actualizado | 2025-09-17 08:46 |
| Etiquetas | ninguna |
| Jira | [LIO-414](https://bluinc.atlassian.net/browse/LIO-414) |

## Relaciones

- **Padre:** [[LIO-408 - Referidos|LIO-408]] Referidos
- **has action item:** [[LIO-438 - APP - Feat - Procesar token de referido cuando el usuario lo lleva en la url|LIO-438]] APP - Feat - Procesar token de referido cuando el usuario lo lleva en la url (con y sin login)
- **has action item:** [[LIO-456 - API - Referrals - Agregar acreditación en billetera al procesar conversión de|LIO-456]] API - Referrals - Agregar acreditación en billetera al procesar conversión de referido

## Descripcion

```
POST {API_URL}/v4/referrals/receive
```

```
{
  "referalToken": "lucas123" <-- Si el front tiene esto en el localStorage, lo envia, sino sera null
}
```

Cuando el usuario ingrese al sitio con un enlace que tiene el atributo `refer`(ejemplo: `libreopcion.com.ar?producto_35434&refer=lucas123`) entonces el front ejecutara nuestro recurso para avisarle a backend que debe almacenarlo si aun no lo tiene

De esta forma podremos registrarlo en caso de que no exista. 

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
