# Sensor de Temperatura y Humedad — ESP32 + DHT11

Proyecto con el **Kit HEMMEL NodeMCU ESP-32S**: medir temperatura y humedad
con un sensor DHT11 y enviar los datos por WiFi a un servidor.

## Esquema de conexión

![[IoT/assets/esquema_dht11_esp32.png]]

| DHT11 | Cable | ESP32 |
|---|---|---|
| **+ / VCC** | 🔴 rojo | **3V3** |
| **OUT / DATA** | 🟡 amarillo | **GPIO4** (D4) |
| **− / GND** | ⚫ negro | **GND** |

> ⚠️ Alimentar el DHT11 con **3V3**, no con 5V (VIN): el pin de datos va directo
> a un GPIO del ESP32, que trabaja a 3.3V.

Si usás el **DHT11 suelto de 4 patas** (no el módulo azul), agregá una resistencia
de **10 kΩ** entre VCC y DATA. El módulo ya la trae incorporada.

## Componentes del kit

- Placa NodeMCU ESP-32S (38 pines) — cerebro + WiFi
- Sensor de Humedad y Temperatura (DHT11)
- Protoboard 830 puntos
- Jumpers macho-macho
- Cable USB-A a USB-C

## Montaje en el protoboard

1. Montar la **ESP32 a caballo del canal central** (cada fila de pines queda aislada).
2. Llevar **3V3 → riel +** y **GND → riel −** con dos jumpers.
3. Conectar el DHT11: **+** al riel rojo, **−** al riel negro, **OUT** a un jumper que va a **GPIO4**.

## Software (Arduino IDE)

1. Instalar el soporte para ESP32 (URL del gestor de placas):
   `https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json`
2. Placa: **ESP32 Dev Module**.
3. Librerías: **DHT sensor library** (Adafruit) + **Adafruit Unified Sensor**.

### Firmware

```cpp
#include <WiFi.h>
#include <HTTPClient.h>
#include <DHT.h>

#define DHTPIN  4
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

const char* ssid     = "TU_WIFI";
const char* password = "TU_CLAVE";
const char* servidor = "http://192.168.0.100:3000/datos"; // tu server

void setup() {
  Serial.begin(115200);
  dht.begin();
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) { delay(500); Serial.print("."); }
  Serial.println("\nWiFi conectado: " + WiFi.localIP().toString());
}

void loop() {
  float temp = dht.readTemperature();
  float hum  = dht.readHumidity();

  if (isnan(temp) || isnan(hum)) {
    Serial.println("Error leyendo el DHT11");
  } else if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(servidor);
    http.addHeader("Content-Type", "application/json");
    String json = "{\"temperatura\":" + String(temp,1) +
                  ",\"humedad\":" + String(hum,1) + "}";
    int code = http.POST(json);
    Serial.printf("Enviado: %s -> HTTP %d\n", json.c_str(), code);
    http.end();
  }
  delay(30000); // cada 30 segundos
}
```

## Servidor de prueba (Node.js)

```js
// server.js  ->  node server.js
const express = require('express');
const app = express();
app.use(express.json());
app.post('/datos', (req, res) => {
  console.log(new Date().toISOString(), req.body);
  res.sendStatus(200);
});
app.listen(3000, () => console.log('Escuchando en :3000'));
```

Poner la **IP de la PC** (la que corre el server) en la constante `servidor` del
firmware. Para algo más vistoso o accesible desde internet: **ThingSpeak**,
**MQTT + Home Assistant** o **InfluxDB + Grafana**.

## Próximos pasos

- [ ] Probar lectura por monitor serie antes de sumar WiFi.
- [ ] Definir destino final de los datos (PC local / nube / Home Assistant).
- [ ] Caja o soporte para el sensor.
