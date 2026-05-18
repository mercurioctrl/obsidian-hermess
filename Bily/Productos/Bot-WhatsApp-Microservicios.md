# Producto Bot WhatsApp – Microservicios definidos

## Microservicios actuales

1. **Worker de WhatsApp (whatsapp-worker)**
   - Mantiene sesiones de WhatsApp Web (whatsapp-web.js + Puppeteer).
   - Envía y recibe mensajes, maneja archivos multimedia.
   - Comunica los eventos al Orquestador vía API/cola.

2. **Orquestador / Core Multi-Agente (orchestrator-core)**
   - Usa un LLM pago (alta capacidad) para:
     - Entender al usuario.
     - Planear y decidir qué tools/microservicios usar.
     - Coordinar sub-agentes especializados.
   - Habla con el usuario (WhatsApp) y con la app web.

3. **Memoria y Datos (memory-service)**
   - Capa que abstrae la memoria:
     - Base vectorial (historial, notas, contexto).
     - Base relacional (kanbans, to-dos, facturas, estados).
   - Expone APIs tipo `/kanban`, `/personas`, `/hogar`, etc.
   - Encapsula el acceso a la bóveda Markdown (Obsidian) y a la DB.

4. **Tools Locales / Multimedia (tools-service)**
   - Agrupa herramientas de bajo nivel que se usan vía API:
     - Audios → transcripción local (Whisper / whisper.cpp).
     - Imágenes básicas → OCR simple o extracción de texto liviana.
   - Pensado para reducir costo de tokens delegando trabajo pesado al servidor.

5. **Navegador Automatizado (browser-service)**
   - Único punto de control de navegadores (Puppeteer/Playwright).
   - Mantiene perfiles/sesiones persistentes (login de WhatsApp y otros sitios).
   - Puede configurar proxies, user-agents, viewport, etc.
   - Endpoints ejemplo:
     - `/browser/open` · `/browser/click` · `/browser/fill` · `/browser/screenshot`
     - `/browser/fetch-and-extract` → carga una URL, extrae HTML y lo convierte a Markdown/Texto destilado.

6. **Visión / Facturas (vision-service)**
   - Microservicio en **Python** para manejo avanzado de imágenes.
   - Objetivo: leer y entender fotos de facturas, tickets, remitos, presupuestos, etc.
   - Endpoints previstos:
     - `POST /vision/ocr` → texto crudo de la imagen.
     - `POST /vision/factura` → JSON estructurado con proveedor, fechas, monto, ítems.

7. **Task Runner de Automatización Web (task-runner-service)**
   - Microservicio en **Python** que orquesta "bots chiquitos" para tareas web complejas:
     - Pedir turnos con credenciales del usuario.
     - Chequear disponibilidad / estados en sitios con login.
     - Scraping resistente con rotación de proxies.
   - No maneja el navegador directo: habla con `browser-service` para los pasos concretos.
   - Usa un vault seguro para credenciales (el LLM nunca ve user/pass).
   - Endpoints ejemplo:
     - `POST /tasks/web` → recibe un `spec` de alto nivel (objetivo, url_base, credenciales_ref, restricciones).
     - `GET /tasks/{id}/status` → para tareas largas.

_Nota: todos estos microservicios cuelgan del mismo ecosistema y el Orquestador decide cuándo usar cada uno. El navegador (browser-service) es único y compartido: task-runner, vision-service y el resto lo usan como motor, no lo duplican._
