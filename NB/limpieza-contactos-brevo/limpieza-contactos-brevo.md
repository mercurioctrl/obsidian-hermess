# Limpieza de Contactos Brevo

Herramienta local en Python para validar, clasificar y limpiar la base de contactos
de **New Bytes** exportada de Brevo (~231.000 emails), sin servicios externos pagos.
Objetivo: depurar la lista para minimizar rebotes/quejas y evitar que Brevo suspenda
la reputación de envío.

**Stack:** Python 3.12 · pandas · email-validator · dnspython · tqdm · disposable-email-domains

**Ubicación del código:** `/home/hermess/Descargas/brevo/`

## Resultado (base de 231.227 contactos)

- **226.113 válidos** → mantener/reimportar
- **5.114 a bloquear** → importar a Brevo para bloquear/eliminar

## Notas del proyecto

- [[arquitectura|Arquitectura]] — pipeline, decisión de no-corregir, clasificación por motivo
- [[stack|Stack]] — tecnologías y dependencias
- [[changelog|Changelog]] — historial de trabajo
- [[contexto|Contexto]] — reglas de negocio y decisiones del usuario
- [[memoria|Memoria]] — contexto acumulado de sesiones con Claude

---
*Última sincronización: 2026-06-17*
