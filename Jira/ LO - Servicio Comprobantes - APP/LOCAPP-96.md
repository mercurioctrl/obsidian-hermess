---
jira_key: "LOCAPP-96"
summary: "APP - Feat - Mostrar Qr de un certificado y descargarlo cuando se recibe el parámetro de descarga"
status: "Finalizada"
type: "Tarea"
priority: "High"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-12-02 08:51"
updated: "2025-12-04 15:07"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LOCAPP-96"
---

# LOCAPP-96: APP - Feat - Mostrar Qr de un certificado y descargarlo cuando se recibe el parámetro de descarga

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | High |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-12-02 08:51 |
| Actualizado | 2025-12-04 15:07 |
| Etiquetas | ninguna |
| Jira | [LOCAPP-96](https://bluinc.atlassian.net/browse/LOCAPP-96) |

## Descripción

Así como realizamos en [link](https://bluinc.atlassian.net/browse/LOCAPP-94) dejaremos el recurso disponible para que al ejecutar

```
https://comprobantes.lio.red/voucher/certificate/{certificadoID}/qr
```

Utilicemos `certificadoID` para obtener los datos del qr

```
https://comprobantes.lio.red/voucher/certificate/{certificadoID}
```

Pero tambien para obtener el certificado y mostrarlo
