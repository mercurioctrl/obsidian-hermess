# Monitor USDT/ARS — Binance P2P

Monitorea el **mejor precio de compra de USDT en pesos** en el P2P de Binance cada 30 segundos y avisa por WhatsApp al grupo **USDT P2P** (`120363431722893957@g.us`). Creado 2026-09-10 a pedido de Catriel.

**Requisito de diseño: cero gasto de IA.** Ningún tick pasa por un LLM. El aviso sale con `openclaw message send`, que es envío directo y no genera turno — el mismo mecanismo que usa [[Monitoreo_WAN]].

## Dónde vive

| Qué | Dónde |
|---|---|
| Código | `~/usdt-mon/monitor.py` |
| Config | `~/usdt-mon/config.json` |
| Historial | `~/usdt-mon/history.db` (SQLite, 90 días) |
| Log | `~/usdt-mon/monitor.log` |
| Servicio | `systemctl --user status usdt-mon` |

Corre por **systemd de usuario**, no por cron: cron no baja de 1 minuto y hacía falta 30 segundos.

## El hallazgo importante

La API `POST /bapi/c2c/v2/friendly/c2c/adv/search` devuelve un **anuncio promocionado en la posición 0, fuera de orden**. Medido el 2026-09-10:

```
data[0] = 1664,89   <- promocionado (classify: "profession")
data[1] = 1590,30   <- el precio real de mercado
```

Un script que lea `data[0]` reporta **4,7% de más**. Hay que ordenar por precio a mano.

Segundo hallazgo: **el endpoint no pide autenticación**. El "Copy as cURL" del navegador arrastra cookies de sesión, `csrftoken`, `device-info` y `aws-waf-token`, pero nada de eso hace falta — alcanza con `content-type: application/json` y un User-Agent de browser.

## Cuándo avisa

Dos alertas independientes, cada una con su cooldown. Si disparan juntas sale un solo mensaje.

1. **Mínimo móvil** — el precio rompe el mínimo de las últimas 24 h. Tiene que ganarle al mínimo previo por al menos 0,15% (banda muerta) o spamearía por centavos. Cooldown 30 min.
2. **Umbral fijo** — cruza hacia abajo los $1.575. Es **por flanco**: dispara una vez y se re-arma recién cuando el precio vuelve a subir 0,30% por encima del umbral.

Hay un **warm-up de 45 minutos** al arrancar: sin él, la primera muestra es trivialmente el mínimo de la ventana y el monitor se avisaría a sí mismo apenas prende.

## Ajustes

Todo se toca en `config.json` y después `systemctl --user restart usdt-mon`. Lo que más se va a mover:

- `threshold` — el precio fijo que dispara la alerta (hoy 1575).
- `window_hours` — la ventana del mínimo móvil (hoy 24).
- `trans_amount` — el monto que querés operar (hoy 145.001). **Importa**: hay anuncios más baratos cuyos límites no aceptan tu monto, y el monitor los descarta a propósito.
- `min_cooldown_minutes` — si te parece que avisa mucho, subilo.

Para ver el estado sin esperar: `python3 ~/usdt-mon/monitor.py --status`

## Cuidados

Son ~2.880 requests por día contra Binance. Hay backoff exponencial ante fallos (hasta 10 min) y un jitter de 0-4 s en el poll para no ser un robot perfectamente periódico. Si el monitor queda 10 minutos sin datos avisa por WhatsApp, y avisa también cuando se recupera.

Relacionado: [[Monitoreo_WAN]] · [[MEMORIA]]
