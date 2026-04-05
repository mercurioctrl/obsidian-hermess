---
jira_key: "BLUWEB-22"
aliases: ["BLUWEB-22"]
summary: "API - Feat - Crear tabla users con migración inicial"
status: "LISTO"
type: "Subtarea"
priority: "High"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-05-13 10:36"
updated: "2025-05-16 17:10"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/BLUWEB-22"
---

# BLUWEB-22: API - Feat - Crear tabla users con migración inicial

| Campo | Valor |
|-------|-------|
| Estado | LISTO (Listo) |
| Tipo | Subtarea |
| Prioridad | High |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-05-13 10:36 |
| Actualizado | 2025-05-16 17:10 |
| Etiquetas | ninguna |
| Jira | [BLUWEB-22](https://bluinc.atlassian.net/browse/BLUWEB-22) |

## Relaciones

- **Padre:** [[BLUWEB-9 - Autenticación y Administracion de usuarios|BLUWEB-9]] Autenticación y Administracion de usuarios 

## Descripcion

Crear la migración que define la estructura de la tabla `users`, incluyendo todos los campos necesarios para login, datos personales, contacto y cuenta bancaria.

### Estructura esperada de la tabla

| Campo | Tipo | Requerido | Comentario |
| --- | --- | --- | --- |
| id | bigIncrements | ✅ | PK autoincremental |
| first_name | string | ✅ | Nombre |
| last_name | string | ✅ | Apellido |
| email | string | ✅ unique | Login |
| password | string | ✅ | Hash bcrypt |
| role | string | ✅ | `admin`, `staff`, `client` |
| job_title | string | ❌ | Rol laboral descriptivo |
| phone | string | ❌ | Teléfono |
| whatsapp | string | ❌ | WhatsApp |
| cbu | string | ❌ | Clave Bancaria Uniforme |
| alias | string | ❌ | Alias CBU |
| status | string | ✅ | `active` o `inactive` |
| created_at | timestamp | ✅ | Laravel default |
| updated_at | timestamp | ✅ | Laravel default |

**Código de la migración sugerida**

```
Schema::create('users', function (Blueprint $table) {
    $table->id();
    $table->string('first_name');
    $table->string('last_name');
    $table->string('email')->unique();
    $table->string('password');
    $table->string('role'); // admin, staff, client
    $table->string('job_title')->nullable();
    $table->string('phone')->nullable();
    $table->string('whatsapp')->nullable();
    $table->string('cbu')->nullable();
    $table->string('alias')->nullable();
    $table->enum('status', ['active', 'inactive'])->default('active');
    $table->timestamps();
});
```

### Criterios de aceptación

- La migración se encuentra en `database/migrations` y corre correctamente


- Se puede ejecutar con `php artisan migrate`


- La tabla `users` se crea con todos los campos definidos


- Soporta operaciones CRUD completas desde Eloquent
