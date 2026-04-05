---
jira_key: "LIO-258"
aliases: ["LIO-258"]
summary: "Migrar cambiar pw "
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Ezequiel manzano"
created: "2025-03-11 11:42"
updated: "2025-03-17 00:41"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-258"
---

# LIO-258: Migrar cambiar pw 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Ezequiel manzano |
| Creado | 2025-03-11 11:42 |
| Actualizado | 2025-03-17 00:41 |
| Etiquetas | ninguna |
| Jira | [LIO-258](https://bluinc.atlassian.net/browse/LIO-258) |

## Relaciones

- **relates to:** [[SNB-2855 - Recuperar cuenta no envia correo de recuperacion en API nueva|SNB-2855]] Recuperar cuenta no envia correo de recuperacion en API nueva

## Descripcion

Solicitar cambio de pw

{{API_URL}}/v4/auth/solicitar-cambio-clave?email=ezequielm789@gmail.com

Cambiar pw 



{{API_URL}}/v4/auth/cambiar-clave

Body 

[adjunto]
```
curl --location 'http://localhost:8097/v4/auth/cambiar-clave' \
--form 'token="19dbfb71e647ce868b4db1b50f96833b"' \
--form 'clave="be9343f4e75846909e5478a629bdd2bd"' \
--form 'confirmacion_clave="be9343f4e75846909e5478a629bdd2bd"'
```
