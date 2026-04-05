---
jira_key: "LIO-526"
aliases: ["LIO-526"]
summary: "Verificar Vendedores"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2026-02-04 08:17"
updated: "2026-03-11 09:20"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-526"
---

# LIO-526: Verificar Vendedores

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2026-02-04 08:17 |
| Actualizado | 2026-03-11 09:20 |
| Etiquetas | ninguna |
| Jira | [LIO-526](https://bluinc.atlassian.net/browse/LIO-526) |

## Relaciones

- **Padre:** [[LIO-5 - Seguridad y Confianza|LIO-5]] Seguridad y Confianza
- **Subtarea:** [[LIO-527 - API - Feat - Guardar informacion de verificación de vendedores|LIO-527]] API - Feat - Guardar informacion de verificación de vendedores 
- **Subtarea:** [[LIO-528 - API - Feat - Comprobar verificación de vendedor|LIO-528]] API - Feat - Comprobar verificación de vendedor
- **Subtarea:** [[LIO-529 - API - Refactor - Agregar parámetros de verificación al objeto user|LIO-529]] API - Refactor - Agregar parámetros de verificación al objeto user
- **Subtarea:** [[LIO-530 - APP - Feat - Pantalla de verificacion del Vendedor|LIO-530]] APP - Feat - Pantalla de verificacion del Vendedor
- **Subtarea:** [[LIO-578 - APIAPP - Feat - Validar numero de telefono|LIO-578]] API/APP - Feat - Validar numero de telefono
- **Subtarea:** [[LIO-587 - APIAPP - Review - Validar numero de telefono - Proceso de verificar vendedor|LIO-587]] API/APP - Review - Validar numero de telefono - Proceso de verificar vendedor indeterminado y propuesta de mejora

## Descripcion

## **Deadline: 11 de febrero de 2026**

## Descripción

Implementar un flujo de verificación obligatorio para vendedores posterior al login. El sistema solicita datos reales del vendedor (nombre, domicilio, teléfono) y las imágenes del frente y dorso de su DNI. Una vez enviados, el vendedor queda verificado inmediatamente y puede acceder a la home. El sistema también soporta una verificación secundaria fuerte (strong_verification) que permite a un admin reabrir la verificación en el futuro si es necesario.

---

## Dependencias

- El endpoint `POST /uploadImage` ya existe y no requiere modificaciones.


- La tabla `vendor_verification` debe estar creada antes de deployar los endpoints nuevos.


- El frontend necesita que el backend esté deployado para testear el flujo end-to-end.



---

## Entrega

| Story | Área | Estado |
| --- | --- | --- |
| Story 1 — Tabla y setup | Backend | Pendiente |
| Story 2 — POST /vendor-verification | Backend | Pendiente |
| Story 3 — GET /vendor-verification | Backend | Pendiente |
| Story 4 — Pantalla de verificación | Frontend | Pendiente |
