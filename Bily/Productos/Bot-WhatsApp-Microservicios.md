# Producto Bot WhatsApp – Microservicios definidos

## Microservicios actuales

1. **Worker de WhatsApp (whatsapp-worker)**
   - Responsable de mantener sesiones de WhatsApp Web (whatsapp-web.js + Puppeteer).
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
   - Expone un navegador controlado por Puppeteer/Playwright.
   - Mantiene perfiles/sesiones persistentes (por ejemplo, el login de WhatsApp u otros sitios).
   - Ofrece endpoints como:
     - `/browser/fetch-and-extract` → carga una URL, extrae HTML y lo convierte a Markdown/Texto destilado.
   - Sirve como base para cosas como:
     - Chequear cobertura de fibra.
     - Rellenar formularios web.

6. **Visión / Facturas (vision-service)**
   - Nuevo microservicio en **Python** para manejo avanzado de imágenes.
   - Objetivo: leer y entender fotos de facturas, tickets, remitos, presupuestos, etc.
   - Endpoints previstos:
     - `POST /vision/ocr` → devuelve texto crudo de la imagen.
     - `POST /vision/factura` → devuelve JSON estructurado con:
       - Proveedor.
       - Fecha de emisión y vencimiento.
       - Monto total.
       - Ítems / conceptos relevantes.
   - Internamente puede combinar OCR clásico (Tesseract) con un modelo de visión tipo LLaVA/Moondream (Ollama) para interpretar bien estructuras complejas.

_Nota: todos estos microservicios cuelgan de un mismo ecosistema y el Orquestador es quien decide cuándo usar cada uno._
