# 06 — Sticky client 5GHz: Min RSSI en la banda de 5GHz (2026-07-30)

## Problema

La notebook **"Mac" de Ale** quedaba **pegada al [[Red#Dispositivos|AP Galeria]]** (de otra planta) en vez de asociarse al AP más cercano. Aparecía con **dos MAC aleatorias** (macOS randomiza MAC e IP):

| Cliente | IP | AP | Banda | Señal | Estado |
|---|---|---|---|---|---|
| `9e:d2:49:38:40:68` | 10.10.10.98 | AP Galeria | 5GHz (ch 161) | **-85 dBm** | 9 roams, pésima |
| `b6:8c:85:6d:31:6a` | 10.10.10.91 | AP Galeria | 5GHz (ch 161) | **-81 dBm** | mala |

## Causa raíz

El **Minimum RSSI** (mecanismo que desasocia al cliente con señal débil para forzarlo a reconectar al AP más cercano) estaba activado **solo en 2.4GHz**, pero **desactivado en 5GHz** en los 3 APs:

```
                2.4GHz (ng)        5GHz (na)
AP Vestidor     ON  @ -75      →   OFF   ✗
AP Galeria      ON  @ -75      →   OFF   ✗
AP Oficina      ON  @ -75      →   OFF   ✗
```

Como 5GHz atenúa más entre plantas, el cliente se quedaba pegado a un AP lejano a -85 dBm y nada lo obligaba a soltarse. En 2.4GHz esto no ocurría porque a -75 dBm lo pateaba.

Antecedente relacionado: en mayo 2025 se activó Min RSSI **solo en 2.4GHz** ([[01-cambios-2025-05#Cambios aplicados]]).

## Cambio aplicado

**Minimum RSSI = -75 dBm activado en la radio 5GHz (`na`) de los 3 APs** (Vestidor, Galeria, Oficina), igual que ya estaba en 2.4GHz. Vía API del controlador (`PUT /api/s/default/rest/device/{_id}` modificando `radio_table[na].min_rssi_enabled=true`, `min_rssi=-75`).

## Resultado

El "Mac" se soltó **solo** de Galeria durante la reconfiguración y reconectó al **AP Oficina** (el más cercano):

| | Antes | Después |
|---|---|---|
| AP | Galeria (otra planta) | **Oficina** ✅ |
| Banda | 5GHz ch 161 | 2.4GHz |
| Señal | -85 / -81 dBm | **-40 dBm** ✅ |
| MAC/IP | .91 / .98 | `02:d3:ea:97:8c:24` / 10.10.10.237 |

No hizo falta kick manual: cayó y reconectó por sí mismo al bajar del umbral.

## Notas para futuro

- **macOS usa MAC aleatoria** → el mismo equipo aparece con varias MAC/IP. Buscarlo por **nombre "Mac"** o por IP, no por MAC fija.
- El cambio de Min RSSI en 5GHz afecta a **todos** los clientes de 5GHz (es lo deseado: cortar clientes lejanos).
- **Siguiente escalón** si algún cliente vuelve a quedar pegado a Galeria: bajar la **potencia TX de la radio 5GHz de Galeria** (estaba en **22 dBm**, la más alta de los 3 APs; Oficina 21, Vestidor 14).

## Ver también

- [[01-cambios-2025-05]] — activación original de Min RSSI (solo 2.4GHz, mayo 2025)
- [[Red]] — índice de la red
