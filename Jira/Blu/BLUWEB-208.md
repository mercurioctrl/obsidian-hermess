---
jira_key: "BLUWEB-208"
summary: "API - Feat - Recurso de suscripción a newsletter para landings de clientes (partner newsletter subscriptions)"
status: "LISTO"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-11-14 08:38"
updated: "2025-12-10 14:01"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/BLUWEB-208"
---

# BLUWEB-208: API - Feat - Recurso de suscripción a newsletter para landings de clientes (partner newsletter subscriptions)

| Campo | Valor |
|-------|-------|
| Estado | LISTO (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-11-14 08:38 |
| Actualizado | 2025-12-10 14:01 |
| Etiquetas | ninguna |
| Jira | [BLUWEB-208](https://bluinc.atlassian.net/browse/BLUWEB-208) |

## Descripción

Se aceptan cambios o mejoras a la idea origina y de llevarse adelante debe ser alterada la informacion de la historia con la solución tal cual fue realizada

Vamos a crear un recurso en la API que permita a las landings de los clientes registrar suscripciones a newsletter directamente en nuestra base de datos. El objetivo es:

- Guardar suscriptos asociados al cliente y al sitio/landing.


- Evitar duplicados por cliente + email.


- Dejar preparado el modelo para eventualmente enviar emails de bienvenida o doble opt-in.



Las landings consumirán este recurso desde el front, usando una **apiKey** por cliente.

---

### Alcance funcional

- **Tabla de suscriptores de newsletter**

- Tabla: `newsletter_subscriptions` (nombre a definir)


- Campos mínimos:

- `id` (PK)


- `clientId`


- `siteOrigin` (dominio / landing de origen)


- `email`


- `name` (opcional)


- `subscriptionSource` (ej.: `landing`, `popup`, `footer`, opcional)


- `createdAt`


- `confirmedAt` (nullable, para doble opt-in futuro)


- `isActive` (bool, por si se desuscribe)


- `confirmationToken` (nullable, para doble opt-in futuro)




- Debe existir una restricción de unicidad al menos para:

- (`clientId`, `email`) o (`clientId`, `siteOrigin`, `email`) según la granularidad que se quiera.






- **Autenticación / seguridad**

- Mismo esquema que el de contacto:

- apiKey por cliente en header `X-Client-ApiKey`.




- Mapeo `apiKey` → `clientId`.


- Validación opcional del dominio de origen (`Origin` / `siteOrigin`).





---

### Endpoint


```
POST {API_URL}/partner/newsletter/subscriptions
```

**Headers esperados**

```
X-Client-ApiKey: {apiKeyDelCliente}
Content-Type: application/json

```

**Body (ejemplo)**

```
{
  "siteOrigin": "https://landing-cliente.com",
  "email": "suscriptor@example.com",
  "name": "María López",
  "subscriptionSource": "popup-home"
}

```

**Comportamiento**

- Valida la `apiKey`:

- Si no es válida → 401.




- Valida el `email` (formato básico, que no esté vacío).


- Mapea `apiKey` → `clientId`.


- Opcional: valida que `siteOrigin` sea uno de los sitios configurados para ese cliente.


- Verifica si ya existe una suscripción activa para ese `clientId` (y opcionalmente `siteOrigin`) + `email`:

- Si ya existe → operación **idempotente**: no crea otro registro, devuelve estado `already_subscribed`.


- Si no existe → crea un nuevo registro en `newsletter_subscriptions` con `isActive = 1` y `createdAt` con fecha/hora actual.




- (Opcional/futuro) Dejar preparado un campo `confirmationToken` para implementar doble opt-in más adelante.


- Devuelve una respuesta JSON sencilla.



**Respuesta de alta exitosa (ejemplo)**

```
{
  "success": true,
  "status": "subscribed",
  "message": "El email fue suscripto correctamente.",
  "email": "suscriptor@example.com"
}

```

**Respuesta cuando ya estaba suscripto**

```
{
  "success": true,
  "status": "already_subscribed",
  "message": "El email ya se encuentra suscripto.",
  "email": "suscriptor@example.com"
}

```

**Respuesta de error de validación**

```
{
  "success": false,
  "status": "validation_error",
  "message": "El email no tiene un formato válido."
}

```

---

### Criterios de aceptación

- Si la `X-Client-ApiKey` es inválida, el endpoint devuelve **401** con un JSON indicando error de autenticación y no inserta nada en la base.


- Cuando el `email` es válido y no existe todavía para ese `clientId` (y opcional `siteOrigin`), el endpoint crea un registro en `newsletter_subscriptions` con `isActive = 1` y `createdAt` completado.


- Si el `email` ya existe para ese `clientId`, el endpoint responde con `status = "already_subscribed"` sin crear un nuevo registro (operación idempotente).


- Si el `email` está vacío o tiene un formato inválido, el endpoint devuelve **422** con `status = "validation_error"` y detalle del problema.


- El endpoint puede ser consumido desde una landing estática sin backend, usando CORS y apiKey, manteniendo el modelo seguro a nivel de cliente (no se pueden registrar suscriptores para otro cliente con una apiKey distinta).
