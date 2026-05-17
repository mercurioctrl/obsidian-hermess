# Producto: Bot Copiloto Nativo para WhatsApp

## Contexto
Idea registrada a partir de notas de voz y mensajes de Catriel el 17 de Mayo de 2026.

## Descripción General
Un bot conversacional diseñado para operar de manera nativa y directa desde WhatsApp, funcionando como un **orquestador multi-agente** con memoria persistente y capacidad de comunicación autónoma con terceros. El sistema está pensado como una plataforma multi-instancia (cada agente con su propio número).

## Características Clave (Requerimientos)
1. **Cerebro / Base de Conocimiento Permanente:** Sistema de memoria a largo plazo absoluto (no olvida nada).
2. **Arquitectura Multi-Agente (Enrutamiento Inteligente):** 
   - *Agente Orquestador (High-IQ):* Utiliza un modelo pago de alta capacidad (con excelente soporte para tool-calling y toma de decisiones) para manejar el hilo general y derivar tareas.
   - *Sub-agentes y Tools locales:* Las tareas pesadas, de gran volumen de texto o repetitivas se delegan a modelos locales.
3. **Comunicación Autónoma con Terceros (Killer Feature):** Capacidad de iniciar y mantener conversaciones con otras personas o negocios por WhatsApp. (Ej: Pedir cotizaciones a múltiples proveedores, dialogar con ellos y consolidar la información).
4. **Lectura de Contexto Completo:** Acceso, lectura y análisis de todo el historial de los chats.
5. **Procesamiento de Multimedia Nativo (Zero-Token Cost):** Las herramientas para interpretar audios y leer imágenes se procesan estrictamente mediante APIs locales para evitar costos.
6. **Tareas Programadas (Cronjobs):** Soporte para procesos en background, seguimientos (follow-ups) y automatizaciones diferidas.
7. **Multi-Instancia:** Escalabilidad horizontal. El sistema debe poder levantar múltiples agentes fácilmente, cada uno asociado a un número de WhatsApp distinto.

## Stack Tecnológico y Arquitectura Propuesta
- **Cliente de WhatsApp:** `whatsapp-web.js` con `puppeteer`. Se descarta la API oficial de Meta para evitar restricciones de plantillas y permitir conversaciones orgánicas (outbound).
- **Procesamiento AI Híbrido (Tiered LLM Architecture):**
  - *Decisiones / Orquestación:* Modelo pago con alta capacidad de razonamiento (ej. GPT-4o, Claude 3.5 Sonnet, Gemini Pro).
  - *Procesamiento Pesado / Multimedia:* Microservicios locales (APIs on-premise).
    - *Audios:* `whisper.cpp`.
    - *Imágenes:* Ollama (modelos de visión como LLaVA/Moondream) o Tesseract.
    - *Clasificación/Extracción básica:* Ollama (Llama 3, Phi-3).
- **Contenerización (Docker):** Debido al requerimiento de levantar múltiples agentes fácilmente y al consumo de Puppeteer, la arquitectura debe estar fuertemente desacoplada usando contenedores.

### Esquema de Arquitectura Base
1. **Capa de Comunicación (Workers de WhatsApp):** Múltiples contenedores independientes corriendo `whatsapp-web.js`.
2. **Capa de Orquestación (Core Inteligente):** Motor impulsado por un LLM pago que toma decisiones, enruta y usa herramientas.
3. **Capa de Tools & Ingesta (APIs Locales):** Microservicios de inferencia local. Reciben audios, imágenes o textos largos desde el Orquestador o los workers, los procesan gratis y devuelven el resultado limpio.
4. **Capa de Memoria (Bases de Datos):** Base Vectorial (para RAG/historial) y Base Relacional (para estados y cronjobs).
