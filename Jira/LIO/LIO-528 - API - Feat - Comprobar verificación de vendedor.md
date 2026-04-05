---
jira_key: "LIO-528"
aliases: ["LIO-528"]
summary: "API - Feat - Comprobar verificación de vendedor"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Franco Callipo"
reporter: "Catriel Mercurio"
created: "2026-02-04 08:32"
updated: "2026-02-20 10:58"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-528"
---

# LIO-528: API - Feat - Comprobar verificación de vendedor

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Franco Callipo |
| Reportado por | Catriel Mercurio |
| Creado | 2026-02-04 08:32 |
| Actualizado | 2026-02-20 10:58 |
| Etiquetas | ninguna |
| Jira | [LIO-528](https://bluinc.atlassian.net/browse/LIO-528) |

## Relaciones

- **Padre:** [[LIO-526]] Verificar Vendedores
- **has action item:** [[LIO-530]] APP - Feat - Pantalla de verificacion del Vendedor

## Descripcion

## Endpoint

| Verb | Route |
| --- | --- |
| GET | `/vendor-verification` |

---

## Propósito

Permite al frontend consultar si el vendedor completó la verificación y recuperar los datos enviados previamente.

Se utiliza para mostrar el estado actual en la pantalla de verificación.

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
| Authorization | Bearer JWT |

No tiene body.

---

### Ejemplo curl

```
curl -X GET https://api.ejemplo.com/api/v4/vendor-verification \
  -H "Authorization: Bearer <jwt_token>"
```

---

## Responses

---

### 200 — Vendor verificado (registro existente)

```
{
  "verified": true,
  "strong_verification": false,
  "real_name": "Juan Carlos Pérez",
  "real_address": "Calle Corrientes 1234, Piso 3, Depto 5A",
  "real_phone": "+54 11 1234 5678",
  "dni_front": "a1b2c3d4e5f6",
  "dni_back": "g7h8i9j0k1l2",
  "created_at": "2026-02-04T12:00:00"
}
```

---

### Campos de respuesta

| Field | Type | Description |
| --- | --- | --- |
| verified | boolean | Siempre `true` si existe registro |
| strong_verification | boolean | Si es `true`, el vendedor debe reenviar datos |
| real_name | string | Nombre real enviado |
| real_address | string | Dirección real |
| real_phone | string | Teléfono real |
| dni_front | string | Filename imagen frontal DNI |
| dni_back | string | Filename imagen trasera DNI |
| created_at | string | Fecha de verificación |

---

### 200 — Vendor NO verificado (sin registro)

```
{
  "verified": false
}
```

El frontend debe interpretar esto como: mostrar pantalla de verificación.

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

Flujo:

- Obtener usuario desde JWT


- Buscar registro en `vendor_verification` por `usuarioID`


- Si existe → devolver DTO con datos


- Si no existe → devolver `{ verified: false }`



---

## Tabla afectada (read only)

### LO.dbo.vendor_verification

```
SELECT *
FROM [LO].[dbo].[vendor_verification]
WHERE usuarioID = :usuarioID

```

---

## Archivos a crear

| File | Responsabilidad |
| --- | --- |
| app/Http/Controllers/VendorVerification/VendorVerificationStatusController.php | Controller invokable. Devuelve DTO o `{ verified:false }` |
| app/Dto/VendorVerification/VendorVerificationDto.php | Mapea la fila de DB a response |

---

## Archivos reutilizados (creados por POST)

| File |
| --- |
| app/Service/VendorVerification/VendorVerificationService.php |
| app/Repository/VendorVerification/VendorVerificationRepository.php |

---

## Archivos a modificar

| File | Cambio |
| --- | --- |
| routes/api.php | Agregar ruta GET /vendor-verification |

---

## Nota sobre strong_verification

Cuando un administrador establece `strong_verification = 1`:

- Este endpoint devuelve `"strong_verification": true`


- El frontend debe mostrar aviso de re-verificación obligatoria


- El vendedor puede volver a llamar a `POST /vendor-verification` (permitido UPDATE)
