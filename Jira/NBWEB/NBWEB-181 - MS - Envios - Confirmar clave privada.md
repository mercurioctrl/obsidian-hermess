---
jira_key: "NBWEB-181"
aliases: ["NBWEB-181"]
summary: "MS - Envios -  Confirmar clave privada"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-05-13 08:53"
updated: "2022-11-09 11:31"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-181"
---

# NBWEB-181: MS - Envios -  Confirmar clave privada

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-05-13 08:53 |
| Actualizado | 2022-11-09 11:31 |
| Etiquetas | ninguna |
| Jira | [NBWEB-181](https://bluinc.atlassian.net/browse/NBWEB-181) |

## Relaciones

- **Padre:** [[NBWEB-76]] API - Implementar MS envios

## Descripcion

```
PUT {{API_URL}}/v1/shipping/{idEnvio or Clave Publica}
```

Request

```
{
privateKey : 'Clave Privada'
}
```

En el caso de coincidir con la palabra clave se marca en la tabla de envíos la **fecha y hora de entrega **y el tiempo total transcurrido.
