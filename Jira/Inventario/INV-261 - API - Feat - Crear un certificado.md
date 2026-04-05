---
jira_key: "INV-261"
aliases: ["INV-261"]
summary: "API - Feat - Crear un certificado"
status: "Finalizada"
type: "Tarea"
priority: "High"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-12-01 08:01"
updated: "2025-12-02 03:27"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-261"
---

# INV-261: API - Feat - Crear un certificado

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | High |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-12-01 08:01 |
| Actualizado | 2025-12-02 03:27 |
| Etiquetas | ninguna |
| Jira | [INV-261](https://bluinc.atlassian.net/browse/INV-261) |

## Relaciones

- **Padre:** [[INV-260]] Certificados eléctricos por Qr
- **has action item:** [[INV-262]] APP- Feat - Crear un certificado

## Descripcion

## Alta de Certificado Eléctrico

Se deberá crear un nuevo endpoint para registrar certificados eléctricos internos que serán utilizados en la generación de QR de conformidad y marcado de productos.

```
POST {API_URL}/electricalCertificate
```

#### Request (inicial)

```
{
  "name": "Certificado Seguridad Fuentes SFX"
}

```

- `name` (string) → **obligatorio**.
Nombre identificatorio del certificado.



> En esta primera versión no se validan ni reciben otros atributos, aunque la entidad quedará preparada para futuras extensiones.


---

### Persistencia

Se deberá crear una nueva tabla `electricalCertificateFiles` en **SQL Server** para almacenar los certificados.

Campos mínimos:

- `id` → PK autoincremental


- `name` → VARCHAR / NVARCHAR, NOT NULL


- `created_at` → DATETIME


- `updated_at` → DATETIME (nullable)



---

### Resultado esperado

El endpoint deberá:

- Validar la presencia de `name` y que no se repita.


- Crear el registro en base de datos.


- Retornar el certificado creado.



---

### Response ejemplo

```
{
  "id": 1,
  "name": "Certificado Seguridad Baja Tensión",
  "created_at": "2025-12-01 10:34:12"
}

```

---

### Criterios de aceptación

- ✅ El endpoint responde `201 Created` al insertar correctamente.


- ✅ Si falta el `name`, retorna `400 Bad Request` con mensaje de validación.


- ✅ El registro queda persistido en SQL Server.


- ✅ La estructura permite agregar campos adicionales en fases futuras sin romper compatibilidad.
