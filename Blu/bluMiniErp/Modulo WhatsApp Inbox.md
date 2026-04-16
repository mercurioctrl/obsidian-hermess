# Modulo WhatsApp Inbox

Integración con un servicio externo tipo cola para enviar mensajes de WhatsApp desde el ERP. Sumada el 2026-04-15 para permitir compartir adjuntos de proyecto con los contactos del cliente.

Ver tambien: [[Backend - API#WhatsApp Inbox - envio de adjuntos]], [[Base de Datos#cliente_telefonos]], [[memoria#WhatsApp Inbox API y compartir adjuntos]].

---

## Servicio externo (Inbox API) — referencia completa

API pública autenticada por token pensada para que sistemas externos (ERP, panel propio, automatizaciones) encolen mensajes de WhatsApp contra un bot con cliente de WhatsApp Web activo. Los mensajes entran a una cola persistente (`cola_envios` en SQLite) y un worker los va enviando **cada 10s**, con reintentos automáticos hasta **5 veces** antes de marcarlos como fallidos.

> ⚠️ No es la API oficial de WhatsApp Business. Corre detrás de ngrok en la máquina del usuario.

### Endpoint

```
POST <inbox_api_url>/inbox/send
Content-Type: application/json
```

La URL base vive en `configuracion.inbox_api_url` (ej. `https://jen-clement-luz.ngrok-free.dev`). En el ERP, se configura desde Configuración → "Integración WhatsApp (Inbox API)".

### Body JSON

| Campo         | Tipo   | Obligatorio  | Descripción |
|---------------|--------|--------------|-------------|
| `token`       | string | sí           | Debe coincidir con `INBOX_API_TOKEN` del `.env` del bot. Viaja en el **body**, no en headers ni en la URL. |
| `telefono`    | string | sí           | Número del destinatario. Acepta formato nacional/internacional (`5491122334455`) o el chatId completo (`5491122334455@c.us`, `...@lid`). Se normaliza automáticamente. |
| `mensaje`     | string | sí*          | Texto del mensaje. Si se envía media, actúa como **caption**. Obligatorio si no hay media. |
| `mediaUrl`    | string | no           | URL pública `http(s)://` de una imagen o archivo. El bot la descarga y la envía. **No se acepta `localhost` ni IPs privadas.** |
| `mediaBase64` | string | no           | Contenido del archivo en base64 (alternativa a `mediaUrl`). Requiere `mimetype`. |
| `mimetype`    | string | condicional  | MIME type del archivo. **Obligatorio** con `mediaBase64`; opcional con `mediaUrl`. |
| `filename`    | string | no           | Nombre del archivo que verá el cliente. Si se omite, se infiere del `Content-Disposition` o del path. |

### Respuestas

| Status | Body                             | Significado                           |
|--------|----------------------------------|---------------------------------------|
| 200    | `{ "success": true, "id": N }`   | Encolado correctamente (`id` = fila en `cola_envios`). |
| 400    | `{ error: "..." }`               | Campos inválidos / faltantes (ej. `mediaBase64` sin `mimetype`). |
| 401    | `{ error: "..." }`               | Token inválido. |
| 500    | `{ error: "..." }`               | Error interno. |

> `success: true` significa **encolado**, no entregado. No hay confirmación de delivery — solo acknowledge de que se guardó en la cola SQLite.

### Comportamiento

- **Texto:** el worker formatea los enlaces (asegura `https://`, separa URLs del texto adyacente) para que WhatsApp los detecte como clickables. Si detecta URLs locales/privadas (`localhost`, `192.168.x.x`, etc.) deja un warning en el log.
- **Media:** se envía como adjunto nativo de WhatsApp, con `mensaje` como caption.
- **Cola + reintentos:** si WhatsApp está caído o la descarga de `mediaUrl` falla, reintenta hasta 5 veces antes de marcar fallido.
- **Latencia:** puede tardar hasta 10s en enviarse (worker interval).
- **Logging:** todo se guarda en SQLite del bot y aparece en el Chat Viewer e Inbox del panel del bot.

### Ejemplos

**Texto con enlace:**
```bash
curl -X POST https://tu-ngrok.../inbox/send \
  -H "Content-Type: application/json" \
  -d '{
    "token": "TU_TOKEN",
    "telefono": "5491122334455",
    "mensaje": "Hola Catriel, tu presupuesto: www.blu.inc/presupuestos/abc123"
  }'
```

**Imagen desde URL:**
```bash
curl -X POST https://tu-ngrok.../inbox/send \
  -H "Content-Type: application/json" \
  -d '{
    "token": "TU_TOKEN",
    "telefono": "5491122334455",
    "mensaje": "Te paso el logo actualizado",
    "mediaUrl": "https://blu.inc/assets/logoblu.png",
    "filename": "logoblu.png"
  }'
```

**PDF en base64:**
```bash
curl -X POST https://tu-ngrok.../inbox/send \
  -H "Content-Type: application/json" \
  -d '{
    "token": "TU_TOKEN",
    "telefono": "5491122334455",
    "mensaje": "Adjunto la factura",
    "mediaBase64": "JVBERi0x...",
    "mimetype": "application/pdf",
    "filename": "factura.pdf"
  }'
```

### Errores comunes

- ❌ `mediaUrl: "http://localhost/..."` → el bot lo rechaza; el cliente no puede abrir `localhost`. Publicá el archivo en Internet o usá `mediaBase64`.
- ❌ Meter el link del archivo dentro del `mensaje` cuando lo que querés es mandar el archivo. Usá `mediaUrl` y dejá en `mensaje` solo el texto acompañante (va de caption).
- ❌ `mediaBase64` sin `mimetype` → 400.
- ❌ Token en header `Authorization` → 401. El token va dentro del body JSON.

### Uso actual desde el ERP

Hoy el ERP solo usa la variante **texto con enlace** para compartir adjuntos de proyecto (ver sección "Compartir adjuntos por WhatsApp" más abajo). El archivo no se envía como media — se manda el link público a `/api/archivos/publico/{token}` dentro del texto. Esto evita tener que subir el archivo al bot y funciona incluso con archivos grandes.

Para enviar archivos directamente como adjunto nativo de WhatsApp habría que migrar al modo `mediaUrl` (requiere URL pública) o `mediaBase64` (requiere leer el archivo y codificarlo server-side). Ninguno implementado todavía.

---

## Configuración en el ERP

**Tabla:** `configuracion` singleton (migración 0055)

| Columna | Tipo | Notas |
|---------|------|-------|
| `inbox_api_url` | varchar(500) | nullable. URL completa del endpoint |
| `inbox_api_token` | varchar(500) | nullable. Token de autenticacion — nunca se devuelve al frontend |

**`ConfiguracionController::show`** desarma `inbox_api_token` del payload JSON y expone solo el flag `inbox_tiene_token: bool`. Mismo patrón que `mercury_tiene_key`, `mp_tiene_token`, `stripe_tiene_token`.

**`update`** acepta `inbox_api_url` (con validación `url`) e `inbox_api_token`. Si el token viene vacío (`''`), se **elimina del payload** (`unset`) en lugar de persistirse — permite editar la URL sin tener que reingresar el token. Igual al patrón de Mercury/MP/Stripe.

**UI:** card "Integración WhatsApp (Inbox API)" en `pages/configuracion/index.vue`, entre Mercury y Jira. Acento verde `#25D366`. El input de token es `type="password"` con placeholder "Dejá vacío para mantener el token actual". Indicador "Token configurado" (punto verde) cuando `configData.inbox_tiene_token === true`.

Ver [[Medios de Pago]] para el patrón general de integraciones con credenciales en `configuracion`.

---

## Compartir adjuntos por WhatsApp

El caso de uso principal: un proyecto tiene uno o más adjuntos (enlaces o archivos subidos) en el card "Enlaces y Archivos", y el usuario quiere mandárselos al cliente por WhatsApp.

### Flow completo

```
[Proyecto con adjunto]
     |
     | botón WhatsApp en hover (verde, lucide:message-circle)
     | visible solo si cliente.telefonos tiene alguno con tipo=WHATSAPP
     v
[Modal "Enviar por WhatsApp"]
     |
     | - Lista los contactos WHATSAPP del cliente con checkboxes (todos pre-seleccionados)
     | - Muestra titulo del adjunto arriba como preview
     v
[POST /api/proyectos/{id}/adjuntos/{adjunto}/enviar-whatsapp]
     |
     | 1. Valida que telefono_ids pertenecen al cliente del presupuesto del proyecto
     | 2. asegurarPublicToken() -> genera bin2hex(random_bytes(32)) si no existe (64 chars hex)
     | 3. Construye url = url("/api/archivos/publico/{token}")
     | 4. Por cada telefono:
     |    - normaliza numero: preg_replace('/\D+/', '', codigo_area.numero)
     |    - arma mensaje: "Hola {nombre}, te ha enviado el archivo {titulo} - {url}"
     |    - Http::timeout(15)->asJson()->post(inbox_api_url, { token, telefono, mensaje })
     v
[Response: { url, enviados[], fallidos[] }]
     |
     | Frontend: toast con contadores
     v
[El worker de Inbox saca el mensaje de la cola y lo manda por WhatsApp]
```

### Public token para acceso sin auth

**Campo:** `proyecto_adjuntos.public_token` (varchar(80), unique, nullable, migración 0056).

**Método del modelo:** `ProyectoAdjunto::asegurarPublicToken(): string`
```php
public function asegurarPublicToken(): string
{
    if (!$this->public_token) {
        $this->public_token = bin2hex(random_bytes(32));
        $this->save();
    }
    return $this->public_token;
}
```

Genera 64 caracteres hex aleatorios. La seguridad del link compartido se basa **únicamente** en la imposibilidad de adivinar el token — no hay expiración, no hay firma, no hay rate limiting.

**Ruta pública** (fuera del middleware `auth:sanctum`): `GET /api/archivos/publico/{token}` → `ProyectoController::servirArchivoPublico`

```php
public function servirArchivoPublico(string $token)
{
    $adjunto = ProyectoAdjunto::where('public_token', $token)->first();
    if (!$adjunto) abort(404);

    if ($adjunto->tipo === 'ENLACE') {
        return redirect()->away($adjunto->url);
    }

    if (!$adjunto->path || !Storage::disk('public')->exists($adjunto->path)) {
        abort(404);
    }

    $absPath = Storage::disk('public')->path($adjunto->path);
    $fileName = $adjunto->nombre ?: basename($adjunto->path);

    return response()->file($absPath, [
        'Content-Type' => $adjunto->mime_type ?: 'application/octet-stream',
        'Content-Disposition' => 'inline; filename="' . $fileName . '"',
    ]);
}
```

- Si `tipo = ENLACE` → `redirect()->away()` al URL del adjunto
- Si `tipo = ARCHIVO` → `response()->file()` desde `Storage::disk('public')` con `Content-Disposition: inline` (se abre en el browser, no se descarga forzado)
- 404 si el archivo fue borrado del filesystem pero el registro sigue

**Invalidación manual:** `UPDATE proyecto_adjuntos SET public_token = NULL WHERE id = X`. Próximo envío genera un token nuevo.

### Endpoint de envío

**Ruta:** `POST /api/proyectos/{proyecto}/adjuntos/{adjunto}/enviar-whatsapp` (dentro del middleware `auth:sanctum`)

**Body:**
```json
{
  "telefono_ids": [12, 14, 17]
}
```

**Validaciones:**
- `telefono_ids` array required, min 1
- Cada id debe existir en `cliente_telefonos`
- El adjunto debe pertenecer al proyecto (`proyecto_id` match)
- Los teléfonos deben pertenecer al cliente del presupuesto del proyecto (`where('cliente_id', $clienteId)`)
- `Configuracion::first()->inbox_api_url` e `inbox_api_token` tienen que estar cargados, sino 422

**Loop de envío:**
```php
foreach ($telefonos as $tel) {
    $numero = preg_replace('/\D+/', '', $tel->codigo_area . $tel->numero);
    $nombre = $tel->nombre ?: 'Hola';
    $mensaje = "Hola {$nombre}, te ha enviado el archivo {$titulo} - {$url}";

    try {
        $resp = Http::timeout(15)->asJson()->post($config->inbox_api_url, [
            'token' => $config->inbox_api_token,
            'telefono' => $numero,
            'mensaje' => $mensaje,
        ]);
        if ($resp->successful() && ($resp->json('success') ?? false)) {
            $enviados[] = [...];
        } else {
            $fallidos[] = ['error' => $resp->body()];
        }
    } catch (\Throwable $e) {
        $fallidos[] = ['error' => $e->getMessage()];
    }
}
```

- Errores individuales **no rompen el loop** — se registran en `fallidos[]` y se sigue
- Timeout de 15s por request
- El normalizador de número usa regex `\D+` para remover cualquier caracter no-dígito (espacios, guiones, `+`, paréntesis)

**Response:**
```json
{
  "url": "http://localhost:8823/api/archivos/publico/abc123...",
  "enviados": [{ "id": 12, "nombre": "Catriel", "numero": "5491130510267" }],
  "fallidos": [{ "id": 14, "nombre": "Bianca", "error": "timeout" }]
}
```

### Frontend

**Ubicación:** `pages/proyectos/[id].vue`, dentro del card "Enlaces y Archivos" (reusa el mismo patrón visual que el botón X de eliminar).

```vue
<button
  v-if="whatsappContactos.length"
  @click="abrirEnviarWhatsApp(adj)"
  class="p-1 text-[#25D366] opacity-0 group-hover:opacity-100 transition-all"
>
  <Icon name="lucide:message-circle" class="w-3.5 h-3.5" />
</button>
```

**`whatsappContactos` computed:**
```ts
const whatsappContactos = computed<any[]>(() => {
  const tels = proyecto.value?.cliente?.telefonos ?? []
  return tels.filter((t: any) => t.tipo === 'WHATSAPP')
})
```

Requiere que `ProyectoController::show` eager-loadee `presupuesto.cliente.telefonos`. Está agregado en el controller.

**Modal:**
- Pre-carga los ids con `whatsappContactos.value.map(t => t.id)` — **todos seleccionados por defecto**
- Checkboxes estilo Tailwind con `text-[#25D366] focus:ring-[#25D366]`
- Botón Enviar deshabilitado si `!seleccionadosWa.length || enviandoWa`
- Toast final: `success("X enviados")` si `fallidos.length === 0`, mensaje con contadores mixtos si hay falla parcial

---

## Mensaje que recibe el cliente

> Hola Catriel, te ha enviado el archivo presupuesto-abril.pdf - https://miniapp.blustudioinc.com/api/archivos/publico/a1b2c3...

- `nombre` sale de `cliente_telefonos.nombre`. Si está vacío, el mensaje arranca literalmente con "Hola, te ha enviado..." (no se usa el nombre del cliente general porque el teléfono puede ser de una persona distinta del cliente empresa).
- `titulo` sale de `proyecto_adjuntos.nombre` (el que se muestra en la UI). Fallback "Archivo".
- La URL contiene 64 chars hex — tan larga que es imposible adivinarla, pero visible en claro en el mensaje del WhatsApp.

---

## Consideraciones de seguridad

- **Token público en el URL:** cualquiera con el link puede ver/descargar el archivo. Asumir que el mensaje puede ser reenviado. Si el archivo es sensible, el usuario debe borrarlo del proyecto o invalidar el token manualmente (`UPDATE ... SET public_token = NULL`).
- **Sin rate limiting:** la ruta pública no tiene throttling. Si esto se vuelve un problema, agregar middleware `throttle:60,1`.
- **Sin expiración:** los tokens son permanentes hasta que se eliminen a mano. Para v2, agregar `public_token_expires_at` y validar en `servirArchivoPublico`.
- **Inbox API token:** nunca se devuelve al frontend (desarmado del JSON de `show`). Solo se usa server-side para el HTTP POST.

---

## Ver tambien

- [[Backend - API#Proyectos]] — endpoint `enviar-whatsapp` y ruta pública
- [[Backend - Modelos#ProyectoAdjunto]] — método `asegurarPublicToken()`
- [[Base de Datos#cliente_telefonos]] y [[Base de Datos#proyecto_adjuntos]]
- [[memoria#WhatsApp Inbox API y compartir adjuntos]] — contexto de la decisión
- [[changelog#2026-04-15]] — iteración donde se agregó
