# Errores Comunes

Bugs reales ya cometidos en este proyecto. Leer antes de modificar cualquier modulo.

---

## definePageMeta middleware auth rompe la navegacion

**Sintoma:** Click en NavItem no navega. La URL no cambia.

**Causa:** `definePageMeta({ middleware: 'auth' })` busca `~/middleware/auth.ts` que no existe. El middleware se llama `auth.global.ts`.

**Solucion:** No poner nada. El middleware global ya cubre todo. Ver [[Frontend#Middleware]].

---

## withTimestamps en la relacion proyecto_empleado

**Sintoma:** Error SQL al acceder a empleado->proyectos.

**Causa:** La tabla `proyecto_empleado` no tiene timestamps. Ver [[Base de Datos#proyecto_empleado pivot]].

**Solucion:** Solo usar `->withPivot(...)` sin `->withTimestamps()`.

---

## Rebuild de frontend con cache vieja

**Sintoma:** El usuario ve contenido antiguo.

**Solucion:** `docker compose build --no-cache frontend`. Ver [[Stack e Infraestructura#Comandos de deploy]].

---

## Iconos sin prefijo lucide se renderizan como texto

**Sintoma:** El icono aparece como texto literal.

**Solucion:** Siempre usar `name="lucide:search"`. Ver [[Frontend#Iconos]].

---

## Componentes UI con prefijo de directorio

**Sintoma:** "Unknown component" error.

**Causa:** `pathPrefix: false` en nuxt.config.ts. Ver [[Frontend#Configuracion]].

**Solucion:** `<FormField>` no `<UiFormField>`.

---

## Olvidar el wrapper data en endpoints que usan API Resource

**Sintoma:** `modelo.value` queda como `{ data: { id: 1, ... } }`.

**Solucion:** `modelo.value = res?.data ?? res`. Ver [[Backend - API#wrapper data en respuestas]].

---

## cargar completo causa error DOM

**Sintoma:** `Cannot read properties of null (reading 'insertBefore')`.

**Causa:** Llamar `cargar()` con `loading = true` durante interaccion activa.

**Solucion:** Actualizar estado local directamente sin recargar componente.

---

## Agregar ports a servicios que no son Nginx

Solo Nginx debe exponer puerto al host. Ver [[Stack e Infraestructura#Docker - Servicios y puertos]].

---

## Eager load con select omite foreign key

**Sintoma:** Relacion anidada devuelve null.

**Solucion:** Siempre incluir la FK en el select del eager load.

---

## auto_return en MercadoPago sin back_urls

**Causa:** MP requiere `back_urls` con dominio publico. Localhost no sirve.

**Solucion:** No usar `auto_return`. Ver [[Medios de Pago#MercadoPago]].

---

## Cruzar monedas entre gasto y banco/caja

La moneda del gasto DEBE coincidir con la del banco/caja. Ver [[Reglas de Negocio#Monedas y Tipo de Cambio]].

---

## Sumar gastos sin convertir en rentabilidad de proyecto

Iterar gastos y convertir a la moneda del presupuesto usando `tasa_cambio`. Ver [[Reglas de Negocio#Monedas y Tipo de Cambio]].

---

## auth me devuelve wrapper data y fetchMe lo ignora

**Sintoma:** isAdmin es false para todos los usuarios.

**Solucion:** `usuario.value = data?.data ?? data` en fetchMe(). Ver [[Frontend#stores auth]].

---

## MercadoPago account_fund clasificado como egreso

**Sintoma:** Balance calculado negativo por millones.

**Solucion:** `account_fund` siempre es ingreso, independientemente de `collector_id`. Ver [[Medios de Pago#MercadoPago]].

---

## Mercury accountNumber vs UUID

**Sintoma:** API de Mercury da 404.

**Causa:** Usar el `accountNumber` bancario en vez del UUID. Ver [[Medios de Pago#Mercury]].

---

## Mercury endpoint singular vs plural

`/account/{id}` (singular) funciona. `/accounts/{id}` (plural) da 404. Ver [[Medios de Pago#Mercury]].

---

## Please provide a valid cache path tras rebuild del backend

**Causa:** `COPY . .` del Dockerfile pisa `storage/framework/cache/`.

**Solucion:** El `docker-entrypoint.sh` recrea los directorios. Verificar que el container se reinicio. Ver [[Stack e Infraestructura#Entrypoint del backend]].

---

## env no lee variables de entorno del container en PHP-FPM

**Sintoma:** `env('MI_VARIABLE')` devuelve null.

**Solucion:** Siempre usar `config()`, nunca `env()` directo en controllers. Registrar en `config/services.php`. Ver [[Stack e Infraestructura#Variables de entorno]].

---

## TCPDF agrega Powered by TCPDF al pie del PDF

**Solucion:** Crear subclase con `$this->tcpdflink = false`.

---

## Controlador devuelve Eloquent collection directa

**Sintoma:** Enmascaramiento de [[Modulo Permisos]] no aplica.

**Causa:** El controller no usa Resource para serializar. Aplicar enmascaramiento inline.

---

## Campo nuevo en gastos no aparece en vista de proyecto

`ProyectoController::show()` serializa gastos con `->map()` manual. Actualizar en dos lugares: GastoResource y ProyectoController. Ver [[Backend - Modelos#Gasto]].

---

## Rutas especificas despues de apiResource colisionan con id

**Sintoma:** `GET /api/gastos/categorias` retorna error "No query results for model".

**Solucion:** Registrar rutas especificas ANTES del apiResource. Ver [[Backend - API#Gastos]].

---

## Filtrar por campo que luego se enmascara con null

`null != 0` es `true` en PHP. Filtrar con valores reales primero, luego enmascarar. Ver [[Modulo Permisos#Bug critico topDeudores]].

---

## Laravel 11 sin config mail php por default

**Síntoma:** Al intentar enviar un mail con `Mail::to(...)->send(...)`, se obtiene un error tipo "Driver [] is not supported" o "Unable to resolve mailer", incluso con las variables `MAIL_*` correctamente seteadas en el `.env`.

**Causa:** El skeleton de Laravel 11 **no incluye** `config/mail.php` en `config/` por default (solo `app`, `auth`, `cache`, `cors`, `database`, `sanctum`, `services`, `session`). Laravel solo lee los archivos `.php` que existen en `config/` — si `mail.php` no está ahí, `config('mail.default')` devuelve `null` y el Mail facade no puede resolver el transporte aunque las env vars estén perfectas.

**Solución:** Crear `config/mail.php` a mano con la plantilla estándar de Laravel (mailers smtp/log/array/failover + from). Luego `docker cp` al container y `php artisan optimize:clear`. Ver la configuración aplicada en [[Stack e Infraestructura#Mail SMTP]].

**Cómo detectarlo rápido:** `docker exec minisaas-backend php -r "... var_export([config('mail.default'), config('mail.mailers.smtp.host')]);"` — si devuelve `null`, falta el archivo de config.

---

## Log facade sin FQN completo falla en Laravel 11

**Síntoma:** En un `catch` o cualquier otro lugar, llamar `\Log::error(...)` falla con `Class "Log" not found`. El error original que motivaba el catch queda enmascarado porque el propio catch tira una excepción distinta.

**Causa:** Laravel 11 en este repo no tiene registrado el alias global `\Log` (el array `aliases` de `config/app.php` no se provisiona por default en Laravel 11). Con el slash inicial, PHP lo busca en el namespace raíz — y no existe.

**Solución:** Usar siempre el FQN completo del facade: `\Illuminate\Support\Facades\Log::error(...)`. O mejor, agregar `use Illuminate\Support\Facades\Log;` al tope del archivo y llamar `Log::error(...)`.

**Donde se descubrió:** `PresupuestoController::enviarInvoice` — el catch estaba intentando loguear un fallo de `Mail::to(...)` y crasheaba, devolviendo el mensaje `"Class Log not found"` al frontend en lugar del error real de SMTP.

**Cómo detectarlo rápido:** Si una respuesta de error dice `Class "X" not found` donde `X` es un nombre de facade (`Log`, `DB`, `Cache`, `Mail`, etc.), faltan los `use` o hay que usar el FQN con namespace completo.

---

## Browsershot bloqueado por security advisories PKSA

**Síntoma:** `composer update` falla con `Your requirements could not be resolved to an installable set of packages` al intentar instalar `spatie/browsershot ^4.x`. El mensaje lista 6 PKSA (`PKSA-j9hz-k29x-6s58`, etc.) y dice "these were not loaded, because they are affected by security advisories".

**Causa:** Composer 2.8+ bloquea automáticamente la instalación de paquetes con advisories activos. Los advisories de Browsershot son todos de la clase "inyección si se pasa input de usuario directo" — en este repo no aplican porque Browsershot solo recibe HTML generado server-side desde blades internos (no hay user input).

**Solución:** Ignorar los PKSA explícitamente en `composer.json`:

```json
"config": {
    "audit": {
        "abandoned": "ignore",
        "ignore": [
            "PKSA-j9hz-k29x-6s58",
            "PKSA-kq82-8x3t-s3fs",
            "PKSA-8m7x-943y-brpz",
            "PKSA-318x-z311-x7rh",
            "PKSA-y3ty-b1bg-gxtm",
            "PKSA-5jt2-w99c-cs4s"
        ]
    }
}
```

Y en el `composer update` agregar `--no-audit` (en el Dockerfile ya está).

**Importante:** Si alguna vez se expone un endpoint que pasa input de usuario directamente a Browsershot (URLs arbitrarias, HTML desde el frontend, etc.), revisar cada advisory antes de mantenerlo ignorado. Ver [[Stack e Infraestructura#Advisories de Composer (Browsershot PKSA)]].

---

## Mercury IP whitelist en API tokens

**Síntoma:** Cualquier llamada a Mercury API devuelve HTTP 401 con `errorCode: ipNotWhitelisted` y mensaje "This API token can only be used from whitelisted IP addresses. Your current IP address (X.X.X.X) is not whitelisted." — incluso aunque el token sea correcto y la cuenta tenga el plan adecuado.

**Causa:** Mercury permite restringir cada API token a una lista de IPs autorizadas (configurado en el dashboard al crear/editar el token). Cuando está activo, todas las IPs no listadas reciben 401, sin distinguir entre token inválido o token válido pero IP no permitida.

**Solución:**
1. Mercury dashboard → Settings → API Tokens → editar el token activo
2. En "IP whitelist" agregar la IP egress del entorno (la que aparece en el mensaje de error)
3. Guardar y reintentar

**Cuidado en deploy:** la IP egress de **dev local** (Mac/Windows del developer) es distinta de la IP egress del **server de producción**. Hay que agregar las dos al whitelist (o usar tokens diferentes por entorno). Si el server cambia de proveedor o región, también cambia la IP.

**Cómo detectarlo rápido:** El cuerpo del 401 trae el JSON de Mercury con `errorCode: ipNotWhitelisted` y la IP detectada — ese mensaje es el que hay que copiar al whitelist. Si en cambio el error dice "Invalid token", es otro problema.

**Donde aplica:** Todas las llamadas de `MercuryController` y `MercuryInvoiceController`. Ver [[Medios de Pago#Mercury Invoicing API (desde 2026-04-14)]].

---

## Ver tambien

- [[Stack e Infraestructura]] - Errores de Docker y deploy
- [[Frontend]] - Errores de componentes y stores
- [[Backend - API]] - Errores de rutas y wrappers
- [[Backend - Modelos]] - Errores de relaciones Eloquent
- [[Medios de Pago]] - Errores de integraciones externas
- [[Modulo Permisos]] - Errores de enmascaramiento
