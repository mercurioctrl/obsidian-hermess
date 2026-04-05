---
jira_key: "NBWEB-595"
summary: "API - Refactor - Logs de visitas sobre un Articulo"
status: "Code Review"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2023-11-21 16:01"
updated: "2023-11-21 16:09"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-595"
---

# NBWEB-595: API - Refactor - Logs de visitas sobre un Articulo

| Campo | Valor |
|-------|-------|
| Estado | Code Review (En curso) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2023-11-21 16:01 |
| Actualizado | 2023-11-21 16:09 |
| Etiquetas | ninguna |
| Jira | [NBWEB-595](https://bluinc.atlassian.net/browse/NBWEB-595) |

## Descripción

Se agrego la siguiente tabla, con la intensiòn de llevar un registro de la cantidad de visitas por articulo.

```
CREATE TABLE NewBytes_DBF.dbo.visitasProducto(
    viewId INT PRIMARY KEY IDENTITY(1,1),
    productId INT,
    categoryId INT,
    brandId INT,
    deviceType VARCHAR(50),
    browserType VARCHAR(50),
    ipAddress VARCHAR(15),
    create_date DATETIME DEFAULT GETDATE()
);
```
