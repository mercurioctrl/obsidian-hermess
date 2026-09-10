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

Tres disparadores. **Un mínimo de 24 h es siempre también mínimo de 60 min**, así que cuando varios dan positivo sale **un solo mensaje**, nombrando la ventana más larga.

| Disparador | Condición | Anti-spam |
|---|---|---|
| 📉 **Mínimo de 60 min** | es **estrictamente** el más bajo de la última hora | ninguno — avisa siempre |
| 📉 **Mínimo de 24 h** | rompe el mínimo del día | tiene que ganarle por 0,15% + cooldown 30 min |
| 🎯 **Umbral fijo** | baja de $1.575 | por flanco: re-arma al subir 0,30% |

La ventana de 60 min va sin banda muerta ni cooldown a pedido explícito de Catriel: *"cuando comparado con los últimos 59, es el más bajo, ahí avisame"*. Si termina siendo mucho volumen, los diales son `dead_band_pct` (probar 0.05) y `cooldown_minutes` en `config.json`.

Hay un **warm-up** por ventana (20 min para la de 1 h, 45 para la de 24 h): sin él la primera muestra es trivialmente el mínimo y el monitor se avisaría solo apenas prende.

## El bug que casi queda vivo

`tick()` graba la muestra **antes** de evaluar las alertas. Como la consulta del mínimo no tenía techo temporal, **el mínimo de la ventana incluía el precio que se estaba evaluando** — y "precio menor que el mínimo" nunca puede ser cierto si el precio *es* el mínimo. Resultado: las alertas de mínimo móvil **no habrían disparado jamás**, sólo andaba la de umbral fijo.

Se detectó inyectando un precio absurdo ($1.000) y viendo que no sonaba la alarma. La ventana ahora se calcula con `before=now`, que excluye la muestra actual.

Lección para el próximo test: **llamar a `check_alerts()` directo no reproduce producción**, porque se saltea el `record()` previo. Hay que grabar la muestra primero, como hace `tick()`.

## Ajustes

Todo se toca en `config.json` y después `systemctl --user restart usdt-mon`. Lo que más se va a mover:

- `threshold` — el precio fijo que dispara la alerta (hoy 1575).
- `windows` — la lista de ventanas de mínimo móvil (hoy 60 min y 24 h). Se pueden agregar más (ej. 168 para 7 días).
- `trans_amount` — el monto que querés operar (hoy 145.001). **Importa**: hay anuncios más baratos cuyos límites no aceptan tu monto, y el monitor los descarta a propósito.
- `cooldown_minutes` / `dead_band_pct` dentro de cada ventana — si te parece que avisa mucho, subilos.

Para ver el estado sin esperar: `python3 ~/usdt-mon/monitor.py --status`

## Cuidados

Son ~2.880 requests por día contra Binance. Hay backoff exponencial ante fallos (hasta 10 min) y un jitter de 0-4 s en el poll para no ser un robot perfectamente periódico. Si el monitor queda 10 minutos sin datos avisa por WhatsApp, y avisa también cuando se recupera.

Relacionado: [[Monitoreo_WAN]] · [[MEMORIA]]
