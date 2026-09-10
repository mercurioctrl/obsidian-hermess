# diagnostico

Diagnóstico de por qué la tablet [[fire]] se apagaba y reencendía sola (2026-09-10).

## Síntoma
La tablet, usada como pantalla fija de cámaras, se apagaba o reiniciaba sola. Pasaba **tanto con cargador de pared como con USB**.

## Evidencia (logs vía ADB)
| Señal | Valor | Lectura |
|---|---|---|
| `sys.boot.reason` | `shutdown,battery` | Último apagado **por batería agotada** |
| `ro.boot.bootreason` | `usb` | Reencendió **al detectar corriente USB**, no fue reinicio normal |
| `charge_full` | **3107 mAh** | Capacidad real actual de la batería |
| Capacidad de fábrica (KFMUWI) | ~6300 mAh | Diseño original |
| **Salud estimada** | **~50%** | La batería retiene la mitad de su capacidad |
| Temperatura batería | 29 °C | Normal → **no es sobrecalentamiento** |
| MemAvailable | ~461 MB | Suficiente → **no es falta de RAM** |
| Max charging current (por USB) | 500 mA (2.5W) | El puerto USB de la PC es insuficiente, agravaba el caso |

## Causa raíz
La batería de litio degradada (~50%) desarrolla **resistencia interna alta**. Ante un pico de consumo, el **voltaje se desploma (voltage sag)** aunque el % marque, por ej., 31%. La protección lo interpreta como batería agotada → **apagado forzado** (`shutdown,battery`). Como sigue enchufada, la corriente la **reenciende** (`bootreason: usb`) → ciclo.

Por eso pasaba **también con cargador de pared**: el problema no es cuánta corriente entra, sino que **la celda ya no sostiene el voltaje bajo carga**.

Descartado: no es térmico, no es RAM, no es (solo) el cargador.

## Agravante del caso de uso
Pantalla encendida 24/7 + batería siempre al 100% + calor constante = desgaste acelerado de la celda. Ver [[contexto]].

## Solución de fondo
- **Batería dummy / eliminator** (plaquita DC-DC en lugar de la batería → corriente directa, sin celda). Ideal para kiosco fijo. *No se puede hacer por software: la Fire sin root no expone bypass de power-path.*
- Alternativa: **batería nueva + smart plug** que cargue entre 40–80% en vez de 100% clavado.

Las mitigaciones por software aplicadas están en [[optimizaciones-adb]].

## Ver también
- [[fire]]
- [[optimizaciones-adb]]
- [[contexto]]
