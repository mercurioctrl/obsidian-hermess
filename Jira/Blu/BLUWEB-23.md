---
jira_key: "BLUWEB-23"
summary: "API - Feat - Crear tabla roles con migración inicial"
status: "LISTO"
type: "Subtarea"
priority: "High"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-05-13 17:42"
updated: "2025-05-16 17:11"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/BLUWEB-23"
---

# BLUWEB-23: API - Feat - Crear tabla roles con migración inicial

| Campo | Valor |
|-------|-------|
| Estado | LISTO (Listo) |
| Tipo | Subtarea |
| Prioridad | High |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-05-13 17:42 |
| Actualizado | 2025-05-16 17:11 |
| Etiquetas | ninguna |
| Jira | [BLUWEB-23](https://bluinc.atlassian.net/browse/BLUWEB-23) |

## Descripción

Crear la migración de la tabla `roles`, que almacenará los tipos de roles del sistema, permitiendo una relación externa con los usuarios y dejando de depender de strings hardcodeados.


**Estructura esperada de la tabla** `roles`

Campo

Tipo

Requerido

Comentario

id

bigIncrements

✅

PK autoincremental

code

string

✅ unique

`admin`, `staff`, `client`

name

string

✅

Nombre legible del rol

created_at

timestamp

✅

Laravel default

updated_at

timestamp

✅

Laravel default

**Código de la migración sugerida**

```
Schema::create('roles', function (Blueprint $table) {
    $table->id();
    $table->string('code')->unique(); // Ej: admin, staff, client
    $table->string('name');           // Ej: Administrador, Colaborador, Cliente
    $table->timestamps();
});

```

### Criterios de aceptación

- La migración se encuentra en `database/migrations` y corre correctamente


- La tabla `roles` se crea con los campos `id`, `code`, `name`, `timestamps`


- El campo `code` está indexado y es único


- Se podrá relacionar luego con la tabla `users` (por `role_id`)


- El sistema usará esta tabla para poblar selectores de roles o validaciones



### Sugerencia: Seeder inicial para roles

Podés agregar esta semilla en otra historia o combinarla:

```
DB::table('roles')->insert([
    ['code' => 'admin', 'name' => 'Administrador'],
    ['code' => 'staff', 'name' => 'Colaborador'],
    ['code' => 'client', 'name' => 'Cliente'],
]);
```
