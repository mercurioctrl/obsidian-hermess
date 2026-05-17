# Producto: Bot Copiloto Nativo para WhatsApp

## Contexto
Idea registrada a partir de notas de voz y mensajes de Catriel el 17 de Mayo de 2026.

## Descripción General
Un bot conversacional diseñado para operar de manera nativa y directa desde WhatsApp, funcionando como un **orquestador multi-agente** con memoria persistente y capacidad de comunicación autónoma con terceros. El sistema está pensado como una plataforma multi-instancia (cada agente con su propio número).

## Filosofía de Producto y Experiencia de Usuario (UX)
- **Onboarding ("Minteo" del Bot):** Un proceso de configuración inicial interactivo, empático (sin ser empalagoso) y extremadamente pulido. El usuario "crea" o "mintea" su propio bot conversando con él para definir su personalidad y el tipo de tareas principales que le va a delegar.
- **Perfiles de Asistencia (Arquetipos):** El sistema ofrece perfiles o roles predefinidos (ej: Emprendedor, CEO, Creativo, Operativo). Dependiendo del perfil elegido durante el minteo, el bot adopta una postura proactiva específica. Por ejemplo, un perfil "Emprendedor" o "CEO" le preguntará activamente al usuario por sus objetivos de negocio, KPIs y hará un seguimiento de metas.
- **Gestor de Objetivos y To-Do Empresarial:** En perfiles orientados a negocio, el bot ayuda a descomponer problemas grandes en partes manejables, genera y mantiene una lista de tareas y la organiza siguiendo principios clásicos de administración.
- **Interés Genuino como Feature de Marketing:** El bot está diseñado para mostrar curiosidad sana por la persona (preguntar por su entorno, relaciones, intereses y objetivos) de forma natural y no invasiva. Esta proactividad y sensación de “atención personalizada” funciona como gancho psicológico para aumentar la retención y el engagement en los primeros días de uso.
- **Simplicidad Nivel Apple:** Fricción cero. Diseño directo donde "las cosas son lo que son" y no hay jerga técnica.
- **Formateo Nativo (MD a WhatsApp):** Adaptador de formato que traduce Markdown a estilo WhatsApp para una lectura agradable en móvil.

## Características Clave (Requerimientos)
1. **Cerebro / Base de Conocimiento Permanente:** Sistema de memoria a largo plazo absoluto (no olvida nada).
2. **Arquitectura Multi-Agente (Enrutamiento Inteligente):** 
   - *Agente Orquestador (High-IQ):* Modelo pago de alta capacidad.
   - *Sub-agentes y Tools locales:* Tareas pesadas delegadas a modelos locales.
3. **Comunicación Autónoma con Terceros (Killer Feature):** Conversar con personas/negocios por WhatsApp.
4. **Lectura de Contexto Completo:** Acceso y análisis del historial completo.
5. **Procesamiento de Multimedia Nativo (Zero-Token Cost):** Audios e imágenes via APIs locales.
6. **Tareas Programadas (Cronjobs) y Proactividad:** Seguimientos y automatizaciones.
7. **Multi-Instancia:** Escalabilidad horizontal por número.
8. **Traductor de Formato a WhatsApp:** MD -> formato WhatsApp.

## Stack Tecnológico y Arquitectura Propuesta
- **Cliente de WhatsApp:** `whatsapp-web.js` con `puppeteer`.
- **Procesamiento AI Híbrido (Tiered LLM Architecture):** Modelo pago para orquestación + microservicios locales para multimedia y tareas pesadas.
- **Contenerización (Docker):** Arquitectura desacoplada.

### Esquema de Arquitectura Base
1. **Capa de Comunicación (Workers de WhatsApp).**
2. **Capa de Orquestación (Core Inteligente).**
3. **Capa de Tools & Ingesta (APIs Locales).**
4. **Capa de Memoria (Bases de Datos).**
