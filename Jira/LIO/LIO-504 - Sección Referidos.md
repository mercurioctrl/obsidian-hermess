---
jira_key: "LIO-504"
aliases: ["LIO-504"]
summary: "Sección Referidos"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2026-01-12 07:43"
updated: "2026-02-03 17:47"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-504"
---

# LIO-504: Sección Referidos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-12 07:43 |
| Actualizado | 2026-02-03 17:47 |
| Etiquetas | ninguna |
| Jira | [LIO-504](https://bluinc.atlassian.net/browse/LIO-504) |

## Relaciones

- **Padre:** [[LIO-497]] App Mobile Vendedores – Gestión integral del seller en Libre Opción
- **Subtarea:** [[LIO-514]] API LO V4 refactor: Listar todos los tokens de un cliente
- **Subtarea:** [[LIO-515]] API LO V4 refactor se debe mostrar flag de token actual
- **Subtarea:** [[LIO-516]] API LO refactor Asociación de conversion para vincular al token específico
- **Subtarea:** [[LIO-522]] API LO V4 - Review - Listar todos los tokens de un cliente -> Tokens no visibles

## Descripcion

Se debe refactorizar la feature de referidos en la API v4 para soportar la gestión histórica de tokens de referido por usuario. El sistema deberá permitir que un usuario genere múltiples tokens a lo largo del tiempo, conservando el historial completo, sin que esto implique que todos se muestren o gestionen simultáneamente.

A nivel operativo, el usuario trabajará siempre con **el último token generado**, que será el único visible como activo en las interfaces y respuestas estándar de la API. Sin embargo, **todos los tokens previamente creados deberán continuar siendo válidos y funcionales**, pudiendo seguir generando visitas y conversiones mientras no sean explícitamente revocados.

Por ejemplo, si un usuario crea inicialmente un token `viejoReferidoAbc` y luego genera un nuevo token `nuevoReferidoAbc`, el sistema deberá:

- Considerar `nuevoReferidoAbc` como el token actual y visible.


- Mantener `viejoReferidoAbc` operativo para la atribución de visitas y conversiones históricas o futuras.



Para soportar este comportamiento, se deberá refactorizar el manejo de **visitas y conversiones**, de modo que ambas queden correctamente asociadas al token de referido correspondiente, permitiendo trazabilidad y análisis posterior.

Adicionalmente, se evaluará:

- La necesidad de incorporar un recurso específico para **listar los tokens de referido** de un usuario.


- Las distintas casuísticas de uso.


- La viabilidad de incluir una feature para **revocar o cancelar un token**, haciendo que deje de ser funcional para nuevas conversiones.
