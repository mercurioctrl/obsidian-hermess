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

## Ver tambien

- [[Stack e Infraestructura]] - Errores de Docker y deploy
- [[Frontend]] - Errores de componentes y stores
- [[Backend - API]] - Errores de rutas y wrappers
- [[Backend - Modelos]] - Errores de relaciones Eloquent
- [[Medios de Pago]] - Errores de integraciones externas
- [[Modulo Permisos]] - Errores de enmascaramiento
