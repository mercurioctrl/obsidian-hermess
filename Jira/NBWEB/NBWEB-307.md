---
jira_key: "NBWEB-307"
summary: "Modificar Tabla mediosEnvio "
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Catriel Mercurio"
reporter: "Emanuel Jesus Ferreyra"
created: "2022-06-28 10:53"
updated: "2022-06-28 14:57"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-307"
---

# NBWEB-307: Modificar Tabla mediosEnvio 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Catriel Mercurio |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2022-06-28 10:53 |
| Actualizado | 2022-06-28 14:57 |
| Etiquetas | ninguna |
| Jira | [NBWEB-307](https://bluinc.atlassian.net/browse/NBWEB-307) |

## Descripción

Query para crear columna minFee que contendra la tarifa minima de un trasportista.

```
ALTER TABLE [LO].[dbo].[mediosEnvio]
ADD minFee int NULL;
```

Query para asignar tarifa minima a **Trasporte Camioneta**. $**2500**

```
UPDATE [LO].[dbo].[mediosEnvio]
SET minFee = 2500
WHERE id = 3031;
```

Query para actualizar tarifa minima de **MiniFlete $800**

```
update [LO].[dbo].[mediosEnvio]
SET minFee = 800
where id = 4056;
```

Query para actualizar tarifa minima de **Moto $300**

```
update [LO].[dbo].[mediosEnvio]
SET minFee = 300
where id = 3030;
```
