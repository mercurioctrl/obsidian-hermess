---
jira_key: "LIO-527"
aliases: ["LIO-527"]
summary: "API - Feat - Guardar informacion de verificación de vendedores "
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Franco Callipo"
reporter: "Catriel Mercurio"
created: "2026-02-04 08:25"
updated: "2026-02-20 10:58"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-527"
---

# LIO-527: API - Feat - Guardar informacion de verificación de vendedores 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Franco Callipo |
| Reportado por | Catriel Mercurio |
| Creado | 2026-02-04 08:25 |
| Actualizado | 2026-02-20 10:58 |
| Etiquetas | ninguna |
| Jira | [LIO-527](https://bluinc.atlassian.net/browse/LIO-527) |

## Relaciones

- **Padre:** [[LIO-526 - Verificar Vendedores|LIO-526]] Verificar Vendedores
- **has action item:** [[LIO-530 - APP - Feat - Pantalla de verificacion del Vendedor|LIO-530]] APP - Feat - Pantalla de verificacion del Vendedor

## Descripcion

## Endpoint

| Verb | Route |
| --- | --- |
| POST | `/vendor-verification` |

---

## Propósito

El vendedor envía sus datos reales junto con las referencias de imágenes del DNI previamente subidas mediante `POST /uploadImage`.

El backend:

- Guarda la información


- Marca al vendedor como verificado inmediatamente



---

## Autenticación

Requiere JWT Bearer Token.

Obtención del usuario desde token:

```
$accessToken = TokenManager::getTokenFromRequest();
$user = TokenManager::getUserFromToken($accessToken);
```

---

## Request

### Headers

| Header | Value |
| --- | --- |
| Content-Type | application/json |
| Authorization | Bearer JWT |

---

### Body (JSON)

```
{
  "real_name": "Juan Carlos Pérez",
  "real_address": "Calle Corrientes 1234, Piso 3, Depto 5A",
  "real_phone": "+54 11 1234 5678",
  "dni_front": "08a36d6a8b5ef1941c90bd2ee2dc9e21.jpg",<-- esto lo manda el front basandose en la imagen subida
  "dni_back": "87a3c051705a5dbff1752bc6ff969e35.jpeg" <-- esto lo manda el front basandose en la imagen subida
}

```

---

### Campos

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| real_name | string | Yes | Nombre completo real del vendedor |
| real_address | string | Yes | Dirección real completa |
| real_phone | string | Yes | Teléfono real |
| dni_front | string | Yes | Filename devuelto por `POST /uploadImage` (frente DNI) |
| dni_back | string | Yes | Filename devuelto por `POST /uploadImage` (dorso DNI) |

---

### Validaciones (Laravel)

```
[
  'real_name'    => 'required|string|max:255',
  'real_address' => 'required|string|max:500',
  'real_phone'   => 'required|string|max:50',
  'dni_front'    => 'required|string',
  'dni_back'     => 'required|string',
]

```

---

## Responses

### 200 — Verificación completada

```
{
  "success": true,
  "msg": "Verificación completada correctamente"
}
```

---

### 400 — Vendedor ya verificado

```
{
  "errors": {
    "status": 400,
    "title": "El vendedor ya fue verificado"
  }
}
```

---

### 422 — Validation error

```
{
  "errors": {
    "status": 422,
    "title": "El campo real_name es obligatorio."
  }
}
```

---

### 401 — Token inválido o ausente

```
{
  "errors": {
    "status": 401,
    "title": "El token no es válido."
  }
}
```

---

## Lógica de negocio (Service)

Flujo completo:

- Obtener usuario desde JWT


- Buscar registro existente en `vendor_verification` por `usuarioID`


- Si existe y `strong_verification = 0` → error: vendedor ya verificado


- Si existe y `strong_verification = 1` → actualizar datos y resetear flag


- Si no existe → crear registro nuevo verificado


- Responder `{ success: true }`



---

### Significado del campo strong_verification

Permite que un administrador reabra el proceso de verificación para que el vendedor vuelva a enviar datos.

---

## Tabla afectada (crearla)

### LO.dbo.vendor_verification

| Column | Type | Valor en INSERT |
| --- | --- | --- |
| usuarioID | INT | User ID desde JWT |
| real_name | NVARCHAR(255) | Payload |
| real_address | NVARCHAR(500) | Payload |
| real_phone | NVARCHAR(50) | Payload |
| dni_front | NVARCHAR(500) | Filename |
| dni_back | NVARCHAR(500) | Filename |
| verified | BIT | 1 (auto aprobado) |
| strong_verification | BIT | 0 |
| created_at | DATETIME | GETDATE() |
| updated_at | DATETIME | NULL / GETDATE() en update |

---

## Archivos a crear

| File | Responsabilidad |
| --- | --- |
| app/Http/Controllers/VendorVerification/VendorVerificationSubmitController.php | Controller invokable. Valida request y delega al service |
| app/Service/VendorVerification/VendorVerificationService.php | Lógica de negocio (JWT + insert/update) |
| app/Repository/VendorVerification/VendorVerificationRepository.php | Queries SQL (`getByUserId`, `create`, `update`) |

---

## Archivos a modificar

| File | Cambio |
| --- | --- |
| routes/api.php | Agregar ruta POST /vendor-verification |

---

## Ejemplo completo (curl)

### 1) Subir imágenes

```
FRONT=$(curl -sX POST https://api.ejemplo.com/api/v4/uploadImage \
  -F "file=@dni_front.jpg" | jq -r '.response.filename')

BACK=$(curl -sX POST https://api.ejemplo.com/api/v4/uploadImage \
  -F "file=@dni_back.jpg" | jq -r '.response.filename')

```

---

### 2) Enviar verificación

```
curl -X POST https://api.ejemplo.com/api/v4/vendor-verification \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <jwt_token>" \
  -d "{
    \"real_name\": \"Juan Carlos Pérez\",
    \"real_address\": \"Calle Corrientes 1234, Piso 3, Depto 5A\",
    \"real_phone\": \"+54 11 1234 5678\",
    \"dni_front\": \"$FRONT\",
    \"dni_back\": \"$BACK\"
  }"
```
