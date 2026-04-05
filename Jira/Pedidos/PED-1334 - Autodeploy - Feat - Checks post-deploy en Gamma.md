---
jira_key: "PED-1334"
aliases: ["PED-1334"]
summary: "Autodeploy - Feat - Checks post-deploy en Gamma"
status: "Ready for QA"
type: "Subtarea"
priority: "Medium"
assignee: "Guillermo Avila"
reporter: "Guillermo Avila"
created: "2026-03-17 18:18"
updated: "2026-03-30 17:45"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1334"
---

# PED-1334: Autodeploy - Feat - Checks post-deploy en Gamma

| Campo | Valor |
|-------|-------|
| Estado | Ready for QA (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Guillermo Avila |
| Reportado por | Guillermo Avila |
| Creado | 2026-03-17 18:18 |
| Actualizado | 2026-03-30 17:45 |
| Etiquetas | ninguna |
| Jira | [PED-1334](https://bluinc.atlassian.net/browse/PED-1334) |

## Relaciones

- **Padre:** [[PED-1330]] GitHub Actions

## Descripcion

Crear un workflow independiente para ejecutar checks automáticos básicos sobre Gamma después de un deploy exitoso, con el fin de validar rápidamente algunos endpoints sigan funcionando.



### Criterios de aceptación

- Se crea un workflow nuevo para checks post-deploy en Gamma.


- El workflow se ejecuta automáticamente al finalizar exitosamente el deploy de Gamma.


- El workflow puede ejecutarse manualmente desde GitHub Actions.


- El workflow valida el endpoint `https://gamma.pedidos.saftel.com/api/version`.


- El workflow realiza login sobre `https://gamma.pedidos.saftel.com/v1/auth/login` usando secrets del repositorio.


- El workflow valida el endpoint `https://gamma.pedidos.saftel.com/v1/orders` usando el token obtenido en el login.


- Cada validación deja evidencia en los logs del workflow.


- Si alguna validación falla, el workflow se marca como failed.


- El workflow de deploy actual se mantiene separado de los checks.


- Se elimina el smoke test actual del workflow de deploy para evitar duplicidad.



### Secrets requeridos

- `GAMMA_QA_USER`


- `GAMMA_QA_PASSWORD`


- `GAMMA_QA_IP`
