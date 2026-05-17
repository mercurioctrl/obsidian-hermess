# Producto: Bot Copiloto Nativo para WhatsApp

## Contexto
Idea registrada a partir de notas de voz y mensajes de Catriel el 17 de Mayo de 2026.

## Descripción General
Un bot conversacional diseñado para operar de manera nativa y directa desde WhatsApp, funcionando como un **orquestador multi-agente** con memoria persistente y capacidad de comunicación autónoma con terceros. El sistema está pensado como una plataforma multi-instancia (cada agente con su propio número).

## Características Clave (Requerimientos)
1. **Cerebro / Base de Conocimiento Permanente:** Sistema de memoria a largo plazo absoluto (no olvida nada).
2. **Arquitectura Multi-Agente:** Un agente principal ("Orquestador") en el hilo general que deriva tareas a sub-agentes especializados.
3. **Comunicación Autónoma con Terceros (Killer Feature):** Capacidad de iniciar y mantener conversaciones con otras personas o negocios por WhatsApp. (Ej: Pedir cotizaciones a múltiples proveedores, dialogar con ellos y consolidar la información).
4. **Lectura de Contexto Completo:** Acceso, lectura y análisis de todo el historial de los chats.
5. **Tareas Programadas (Cronjobs):** Soporte para procesos en background, seguimientos (follow-ups) y automatizaciones diferidas.
6. **Multi-Instancia:** Escalabilidad horizontal. El sistema debe poder levantar múltiples agentes fácilmente, cada uno asociado a un número de WhatsApp distinto.

## Stack Tecnológico y Arquitectura Propuesta
- **Cliente de WhatsApp:** `whatsapp-web.js` con `puppeteer`. Se descarta la API oficial de Meta para evitar restricciones de plantillas y permitir conversaciones orgánicas (outbound).
- **Contenerización (Docker):** Debido al requerimiento de levantar múltiples agentes fácilmente y al consumo de Puppeteer, la arquitectura debe estar fuertemente desacoplada usando contenedores.

### Esquema de Arquitectura Base
1. **Capa de Comunicación (Workers de WhatsApp):** 
   - Múltiples contenedores independientes (uno por cada número de teléfono).
   - Su única responsabilidad es correr `whatsapp-web.js`, escanear el QR, mantener la sesión, recibir mensajes entrantes (y mandarlos al orquestador vía Webhook/Cola de mensajes) y enviar los mensajes salientes.
2. **Capa de Orquestación (Core Multi-Agente):** 
   - El "Cerebro Central". Recibe los eventos de todos los workers.
   - Enruta el mensaje al Agente Principal del número correspondiente.
   - Gestiona el despachador de Sub-agentes y los Cronjobs de seguimiento.
3. **Capa de Memoria (Bases de Datos):**
   - **Vectorial (ej. Qdrant / Pinecone):** Para la memoria semántica, RAG y búsqueda de historial.
   - **Transaccional/Relacional (ej. PostgreSQL):** Para estados de conversación, colas de tareas cron y configuraciones de cada número/agente.
