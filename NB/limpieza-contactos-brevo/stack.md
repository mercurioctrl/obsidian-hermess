# Stack

- **Python 3.12** en venv (`.venv/`), sistema con PEP 668 (externally-managed),
  por eso se usa venv obligatorio.
- **pandas** — carga/manipulación del CSV (231k filas en memoria, sin problema).
- **email-validator** — validación sintáctica (`check_deliverability=False`; el DNS
  se hace aparte).
- **dnspython** — consultas MX/A con resolvers públicos y timeout 5s/8s.
- **tqdm** — barra de progreso de la verificación DNS.
- **disposable-email-domains** — lista pública de ~6.945 dominios temporales.

## Instalación

```bash
python3 -m venv .venv
.venv/bin/pip install pandas email-validator dnspython tqdm disposable-email-domains
```

## Performance

- ~17.000 dominios únicos verificados por DNS con caché → ~2-3 min con 80 hilos.
- Caché por dominio: cada dominio se consulta una sola vez.

## Ver también
- [[arquitectura]] · [[limpieza-contactos-brevo]]
