# Producto: Bot Copiloto Nativo para WhatsApp

## Contexto
Idea registrada a partir de notas de voz y mensajes de Catriel el 17 de Mayo de 2026.

## Descripción General
Un bot conversacional diseñado para operar de manera nativa y directa desde WhatsApp, funcionando como un **orquestador multi-agente** con memoria persistente y capacidad de comunicación autónoma con terceros. El sistema está pensado como una plataforma multi-instancia (cada agente con su propio número).

## Filosofía de Producto y Experiencia de Usuario (UX)
- **Onboarding ("Minteo" del Bot):** Un proceso de configuración inicial interactivo, empático (sin ser empalagoso) y extremadamente pulido. El usuario "crea" o "mintea" su propio bot conversando con él: respondiendo preguntas simples para definir su personalidad (el "alma" o prompt base) y el tipo de tareas principales que le va a delegar.
- **Simplicidad Nivel Apple:** Fricción cero. Filosofía de diseño directa donde "las cosas son lo que son" y no hay jerga técnica ni nombres rebuscados. El bot y sus interacciones deben ser tan intuitivos que cualquier persona (incluso perfiles totalmente alejados de la tecnología) pueda utilizarlo y entenderlo de forma natural y sin curva de aprendizaje.

## Características Clave (Requerimientos)
1. **Cerebro / Base de Conocimiento Permanente:** Sistema de memoria a largo plazo absoluto (no olvida nada).
2. **Arquitectura Multi-Agente (Enrutamiento Inteligente):** 
   - *Agente Orquestador (High-IQ):* Utiliza un modelo pago de alta capacidad para manejar el hilo general y derivar tareas.
   - *Sub-agentes y Tools locales:* Las tareas pesadas, repetitivas o de volumen se delegan a modelos locales.
3. **Comunicación Autónoma con Terceros (Killer Feature):** Capacidad de iniciar y mantener conversaciones con otras personas o negocios por WhatsApp. (Ej: Pedir cotizaciones a proveedores).
4. **Lectura de Contexto Completo:** Acceso, lectura y análisis de todo el historial de los chats.
5. **Procesamiento de Multimedia Nativo (Zero-Token Cost):** Audios e imágenes se procesan estrictamente mediante APIs locales para evitar costos.
6. **Tareas Programadas (Cronjobs):** Soporte para procesos en background, seguimientos y automatizaciones diferidas.
7. **Multi-Instancia:** Escalabilidad horizontal. Múltiples agentes fácilmente desplegables, cada uno con su número.

## Stack Tecnológico y Arquitectura Propuesta
- **Cliente de WhatsApp:** `whatsapp-web.js` con `puppeteer`. Se descarta la API oficial de Meta para evitar bloqueos y plantillas.
- **Procesamiento AI Híbrido (Tiered LLM Architecture):**
  - *Decisiones / Orquestación:* Modelo pago con alta capacidad de razonamiento.
  - *Procesamiento Pesado / Multimedia:* Microservicios locales (`whisper.cpp`, Ollama con LLaVA/Moondream).
- **Contenerización (Docker):** Arquitectura fuertemente desacoplada.

### Esquema de Arquitectura Base
1. **Capa de Comunicación (Workers de WhatsApp):** Múltiples contenedores independientes corriendo `whatsapp-web.js`.
2. **Capa de Orquestación (Core Inteligente):** Motor LLM pago que toma decisiones, enruta y usa herramientas.
3. **Capa de Tools & Ingesta (APIs Locales):** Microservicios de inferencia local para audios/imágenes.
4. **Capa de Memoria (Bases de Datos):** Base Vectorial (RAG) y Base Relacional (estados y cronjobs).
