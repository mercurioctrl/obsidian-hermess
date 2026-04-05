---
jira_key: "LOCAPP-95"
aliases: ["LOCAPP-95"]
summary: "API - Feat - Traer informacion del certificado"
status: "Finalizada"
type: "Tarea"
priority: "High"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-12-02 08:45"
updated: "2025-12-04 11:37"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LOCAPP-95"
---

# LOCAPP-95: API - Feat - Traer informacion del certificado

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | High |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-12-02 08:45 |
| Actualizado | 2025-12-04 11:37 |
| Etiquetas | ninguna |
| Jira | [LOCAPP-95](https://bluinc.atlassian.net/browse/LOCAPP-95) |

## Relaciones

- **Padre:** [[LOCAPP-93]] Certificados
- **has action item:** [[LOCAPP-96]] APP - Feat - Mostrar Qr de un certificado y descargarlo cuando se recibe el parámetro de descarga

## Descripcion

Así como lo hicimos para listar en el CRUD de [link](https://bluinc.atlassian.net/browse/INV-268)  usaremos un recurso en el servicio para que el front pueda mostrar el QR que mapea al certificado

```
GET {API_URL}/electricalCertificate/{id}
```

```
{
"id": 8,
"name": "Certificado General Gabinetes IP54",
"pdf_path": "http://static.nb.com.ar/img/7290717fe486d2c661ecef2d6fc8056a.pdf",
"created_at": "2025-12-02 09:11:05"
}
```
