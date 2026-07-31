# 06 — Sticky client 5GHz + incidente DFS (2026-07-30)

## Problema inicial

La notebook **"Mac" de Ale** quedaba **pegada al AP Galeria** (de otra planta) en vez de asociarse al AP más cercano. Aparecía con **dos MAC aleatorias** (macOS randomiza MAC e IP):

| Cliente | IP | AP | Banda | Señal | Estado |
|---|---|---|---|---|---|
| `9e:d2:49:38:40:68` | 10.10.10.98 | AP Galeria | 5GHz (ch 161) | **-85 dBm** | 9 roams, pésima |
| `b6:8c:85:6d:31:6a` | 10.10.10.91 | AP Galeria | 5GHz (ch 161) | **-81 dBm** | mala |

## Causa raíz del sticky client

El **Minimum RSSI** (mecanismo que desasocia al cliente con señal débil para forzarlo a reconectar al AP más cercano) estaba activado **solo en 2.4GHz** y **desactivado en 5GHz** en los 3 APs. Como 5GHz atenúa más entre plantas, el cliente se quedaba pegado a un AP lejano a -85 dBm y nada lo obligaba a soltarse.

## ⚠️ Qué salió mal (y por qué NO se debe hacer así)

**Intento fallido:** se activó Min RSSI -75 dBm en 5GHz en los 3 APs. Consecuencias:

1. **`nexus` es solo-5GHz.** Con Min RSSI en 5GHz, un cliente que no cumple el umbral es rechazado, y como `nexus` no tiene 2.4GHz, **se queda sin red** (no hay banda donde caer). → Ale no podía conectar iPhone ni Mac.
2. **El cambio de `radio_table` disparó reprovisionamiento de los APs**, y el VAP de `nexus` en 5GHz **no levantó en Vestidor ni Oficina** (quedó emitiendo solo en Galeria). → El SSID `nexus` "desapareció" para todos; solo se veía `nexus-lot` (2.4GHz).

**Lección:** nunca activar Min RSSI en una banda cuando el SSID es exclusivo de esa banda. Y todo cambio de `radio_table` reprovisiona el AP (corta clientes ~1 min).

## Resolución aplicada

1. **Revertido el Min RSSI de 5GHz** → OFF en los 3 APs (estado original).
2. **Force-provision de Oficina y Vestidor** → reconstruyó el VAP de `nexus` en 5GHz (volvió a emitirse en los 3 APs).
3. **Causa del "no aparece al lado de Oficina": canal DFS.** Oficina tenía autoselección de canal y había caído en **ch104 (DFS)**. En canales DFS el AP hace un chequeo de radar (o se calla si detecta uno) y **no emite beacon** aunque el controlador diga "RUN".
   - **Fijado el 5GHz de Oficina a canal 149 (no-DFS)** y desactivada la optimización automática de canal (`channel_optimization_enabled=false`), para que no vuelva a saltar a un DFS.

## Estado final (verificado)

| AP | 2.4GHz | 5GHz canal | tipo | `nexus` 5G |
|---|---|---|---|---|
| Vestidor | ch6 RUN | **40** | no-DFS | ✅ |
| Galeria | ch11 RUN | **161** | no-DFS | ✅ |
| Oficina | ch1 RUN | **149** (fijado) | no-DFS | ✅ (5 clientes) |

- Min RSSI: **2.4GHz ON (-75), 5GHz OFF** en los 3 (estado original restaurado).
- Canales 5GHz 40 / 149 / 161: no se pisan entre sí.

## Pendientes / próximos pasos

- **El sticky client sigue sin resolverse** (se revirtió el Min RSSI de 5GHz). La solución correcta es:
  1. Pasar **`nexus` a doble banda** (`wlan_band` de `5g` → `both`) para que haya 2.4GHz donde caer.
  2. **Recién entonces** activar Min RSSI en 5GHz (con band-steering para preferir 5GHz cerca del AP).
- Alternativa/complemento: bajar la **potencia TX de 5GHz de Galeria** (está en 22 dBm, la más alta) para que no "grite" a otras plantas.
- **Vestidor 5GHz** tiene TX bajo (14 dBm) y 0 clientes — evaluar subir potencia para mejorar cobertura de esa zona.

## Notas

- **macOS/iOS usan MAC aleatoria** → el mismo equipo aparece con varias MAC/IP. Buscarlo por **nombre "Mac"** o por IP, no por MAC fija.
- Todo cambio de `radio_table` vía API (`PUT /rest/device/{_id}`) reprovisiona el AP. Verificar siempre después que los VAPs volvieron a levantar.

## Ver también

- [[01-cambios-2025-05]] — activación original de Min RSSI (solo 2.4GHz, mayo 2025)
- [[Red]] — índice de la red
