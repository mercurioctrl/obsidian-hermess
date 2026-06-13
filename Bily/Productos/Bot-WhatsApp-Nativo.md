# Producto: Bot Copiloto Nativo para WhatsApp

## Contexto
Idea registrada a partir de notas de voz y mensajes de Catriel el 17 de Mayo de 2026.
Nombre clave del proyecto en desarrollo: **[[Bily/Productos/Billy-Bot|Billy Bot]]**

## Descripción General
Un bot conversacional diseñado para operar de manera nativa y directa desde WhatsApp, funcionando como un **orquestador multi-agente** con memoria persistente y capacidad de comunicación autónoma con terceros. El sistema está pensado como una plataforma multi-instancia (cada agente con su propio número).

## Filosofía de Producto y Experiencia de Usuario (UX)
- **Onboarding ("Minteo" del Bot):** Ver detalles en [[Bily/Productos/Bot-WhatsApp-Minteeo-y-Suenio|Minteo y Sueño]]. Un proceso de configuración inicial interactivo, empático (sin ser empalagoso) y extremadamente pulido.
- **Perfiles de Asistencia (Arquetipos):** El sistema ofrece perfiles o roles predefinidos (ej: Emprendedor, CEO, Creativo, Operativo). 
- **Gestor de Objetivos y To-Do Empresarial:** En perfiles orientados a negocio, el bot ayuda a descomponer problemas grandes.
- **Interés Genuino como Feature de Marketing:** El bot está diseñado para mostrar curiosidad sana por la persona.
- **Simplicidad Nivel Apple:** Fricción cero. 
- **Formateo Nativo (MD a WhatsApp):** Adaptador de formato.
- **Elevator Pitch:** Ver borrador en [[Bily/Productos/Bot-WhatsApp-Elevator-Pitch|Elevator Pitch]].

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
Toda la arquitectura, microservicios detallados (incluyendo visión y OCR) se definieron en: **[[Bily/Productos/Billy-Bot|Arquitectura de Microservicios (Billy Bot)]]**.

- **Cliente de WhatsApp:** `whatsapp-web.js` con `puppeteer`.
- **Procesamiento AI Híbrido (Tiered LLM Architecture):** Modelo pago para orquestación + microservicios locales para multimedia y tareas pesadas.
- **Contenerización (Docker):** Arquitectura desacoplada.

## Ver también
- [[Bily/Bily|Inicio de Bily]]
