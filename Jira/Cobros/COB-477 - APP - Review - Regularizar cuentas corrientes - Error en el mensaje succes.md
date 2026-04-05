---
jira_key: "COB-477"
aliases: ["COB-477"]
summary: "APP - Review - Regularizar cuentas corrientes -> Error en el mensaje \"succes\""
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2023-10-31 13:13"
updated: "2023-10-31 16:43"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-477"
---

# COB-477: APP - Review - Regularizar cuentas corrientes -> Error en el mensaje "succes"

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2023-10-31 13:13 |
| Actualizado | 2023-10-31 16:43 |
| Etiquetas | ninguna |
| Jira | [COB-477](https://bluinc.atlassian.net/browse/COB-477) |

## Relaciones

- **Padre:** [[COB-453]] Feat - Regularizar cuenta para administradores

## Descripcion

Al ejecutar el recurso para regularizar, 

[adjunto]
Cuando se hace correctamente devuelve un 200 y el mensaje 

```
{

    "status": "success",

    "message": "La cuenta del cliente fue ajustada correctamante"

}
```

Pero la notifiacion se muestra una cruz roja de error, con el texto vacio
