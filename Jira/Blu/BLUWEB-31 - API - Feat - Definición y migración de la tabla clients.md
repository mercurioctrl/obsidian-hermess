---
jira_key: "BLUWEB-31"
aliases: ["BLUWEB-31"]
summary: "API - Feat - Definición y migración de la tabla clients"
status: "LISTO"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-05-19 08:18"
updated: "2025-05-19 15:36"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/BLUWEB-31"
---

# BLUWEB-31: API - Feat - Definición y migración de la tabla clients

| Campo | Valor |
|-------|-------|
| Estado | LISTO (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-05-19 08:18 |
| Actualizado | 2025-05-19 15:36 |
| Etiquetas | ninguna |
| Jira | [BLUWEB-31](https://bluinc.atlassian.net/browse/BLUWEB-31) |

## Relaciones

- **Padre:** [[BLUWEB-11 - Sistema de clientes del BackOffice|BLUWEB-11]] Sistema de clientes del BackOffice

## Descripcion

Siguiendo la lógica aplicada en [link](https://bluinc.atlassian.net/browse/BLUWEB-9)  crearemos la tabla `clients` 

```
Schema::create('clients', function (Blueprint $table) {
    $table->id();
    $table->string('first_name');
    $table->string('last_name');
    $table->string('companyName');
    $table->string('last_name');
    $table->string('email')->unique();
    $table->string('phone')->nullable();
    $table->string('whatsapp')->nullable();
    $table->string('cbu')->nullable();
    $table->string('alias')->nullable();
    $table->enum('status', ['active', 'inactive'])->default('active');
    $table->timestamps();
});
```

Estructura de la tabla

```
{
  "id": 1,
  "first_name": "Ana",
  "last_name": "Martínez",
  "companyName": "Cafe Martinez"
  "email": "ana@example.com",
  "phone": "1133445566",
  "whatsapp": "1133445566",
  "cbu": "2850590940090412345000",
  "alias": "ana.banco.cuenta",
  "status": "active"
}

```
