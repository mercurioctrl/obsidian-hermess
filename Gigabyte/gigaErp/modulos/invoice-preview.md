# Módulo: Invoice Preview (estilo Blu)

Preview HTML de la invoice con descarga PDF cliente-side, compartible por link con
token. Identidad visual replica el presupuesto de `erp.blustudioinc.com` — ver
[[memoria#Referencia Blu ERP]].

## Endpoint

```
GET /api/ventas/{venta}/preview
```

**Público** (fuera del grupo `auth:sanctum`). El controller hace la auth a mano:

```php
public function preview(Request $request, Venta $venta) {
    $token = $request->bearerToken() ?? $request->query('token');
    if (!$token) abort(401);
    $access = \Laravel\Sanctum\PersonalAccessToken::findToken($token);
    if (!$access || !$access->tokenable) abort(401);
    ...
}
```

Esto permite **dos modos de uso:**
- Header `Authorization: Bearer {token}` — desde la SPA con `fetch`
- Query `?token={token}` — para abrir en nueva tab o compartir el link

## Frontend

### Desde el listado de órdenes (`pages/ordenes-venta/index.vue`)

La columna **Invoice** muestra el `VTA-XXXX` como link verde con ícono `external-link`.
Click → `window.open(url, '_blank')`. `@click.stop` para que no dispare el row-click
que navega al detalle.

```ts
function abrirInvoice(ventaId: number) {
  const url = `/api/ventas/${ventaId}/preview?token=${encodeURIComponent(authStore.token)}`
  window.open(url, '_blank')
}
```

### Desde el detalle de la orden (`pages/ordenes-venta/[id].vue`)

Si la orden está `FACTURADA`, en la caja verde "Invoice generada" hay dos botones:
- **Ver invoice** — abre la preview en nueva tab (mismo patrón)
- **Descargar PDF** — usa el endpoint viejo `/api/ventas/{id}/pdf` (DomPDF server-side, fallback)

## Blade template

`backend/resources/views/ventas/invoice-preview.blade.php`

### Estructura visual
- **Header**: logo izq + `Documento / Invoice / N° VTA-XXXX / Fecha / Términos de pago / Status badge` der
- **Divider** 1px
- **Parties**: Emisor (de `configuraciones`) / Cliente
- **Tabla de ítems**: Descripción (con SKU debajo) · Cant. · P. Unit. · Subtotal
- **Totales**: Subtotal · Shipping (si > 0) · **Total** (grand, border-top 2px)
- **Observaciones** (si `venta.notas` existe)
- **Footer**: contacto + logo desvanecido (opacity .12)
- **Botón "Descargar PDF"** (oculto con `@media print`)

### Estilo
- Helvetica Neue, `max-width: 780px`, `padding: 44px 56px` (ajustado para fit A4)
- Paleta minimalista: negro / grises / acentos sutiles
- `@media print` reduce padding y oculta el botón

### Descarga PDF (cliente-side con html2pdf.js)

```js
html2pdf().set({
  margin: 0,
  filename: 'invoice-{VTA-XXXX}.pdf',
  image: { type: 'jpeg', quality: 0.98 },
  html2canvas: { scale: 2, useCORS: true, scrollY: 0, windowHeight: elemento.scrollHeight },
  jsPDF: { unit: 'mm', format: 'a4', orientation: 'portrait' },
  pagebreak: { mode: ['avoid-all', 'css', 'legacy'] },
}).from(elemento).save();
```

CDN: `https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js`

## Gotcha resuelta: logo SVG recortado en el PDF

El SVG `aorus_logo_black.svg` tiene `viewBox="519 657 1819 455"` (no empieza en 0,0).
html2canvas no respeta el offset → en el PDF aparece solo el ala / vacío. **Solución:**
embeber un PNG del logo como data URI base64.

```php
$logoPath = public_path('logos/aorus_logo_black.png');
$logoData = is_file($logoPath)
  ? 'data:image/png;base64,' . base64_encode(file_get_contents($logoPath))
  : '';
```

El PNG vive en `backend/public/logos/aorus_logo_black.png` (commiteado), generado
con playwright/chromium. Ver detalle en [[troubleshooting#Logo recortado]].

## Dockerfile

El backend `Dockerfile` ahora hace `COPY resources/` y `COPY public/logos/` — antes
solo copiaba `app/`, `bootstrap/`, `routes/`, `database/`, así que los blades y
assets solo vivían en runtime vía `docker cp`. **Fix en commit `001f8c8`.**

## Configuración de la empresa

Datos del emisor que aparecen en la preview vienen de `configuraciones` (key/value):

```
empresa_nombre, empresa_direccion, empresa_ciudad_pais,
empresa_telefono, empresa_email, empresa_web,
invoice_payment_terms (default "Net 30")
```

Seteados en migración `0029` con defaults editables desde la UI de Configuración.

## Ver también

- [[ordenes-venta]] — quién genera la invoice
- [[productos]] — origen de los datos de cada ítem
- [[troubleshooting]] — gotcha html2canvas/SVG
- [[memoria]] — referencia visual Blu ERP
