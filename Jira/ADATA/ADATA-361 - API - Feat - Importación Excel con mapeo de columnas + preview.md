---
jira_key: "ADATA-361"
aliases: ["ADATA-361"]
summary: "API - Feat - Importación Excel con mapeo de columnas + preview"
status: "Listo"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2026-02-19 11:19"
updated: "2026-02-23 12:40"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/ADATA-361"
---

# ADATA-361: API - Feat - Importación Excel con mapeo de columnas + preview

| Campo | Valor |
|-------|-------|
| Estado | Listo (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2026-02-19 11:19 |
| Actualizado | 2026-02-23 12:40 |
| Etiquetas | ninguna |
| Jira | [ADATA-361](https://bluinc.atlassian.net/browse/ADATA-361) |

## Relaciones

- **Padre:** [[ADATA-356]] XPG - Landing Fidelización (Puntos + Aceleradores + Ranking + Carga Compras)

## Descripcion

Permitir subir `.xlsx` para cargar compras masivamente.
Flujo:

- Subir archivo


- Preview de filas


- UI manda mapping (columna→campo)


- API valida y carga filas válidas


- Respuesta con resumen: insertadas / rechazadas + motivos



Campos a mapear

- sku (opcional)


- nombreProducto (requerido)


- cantidad (requerido)


- precio (opcional)


- montoTotal (requerido si precio no viene)


- facturaCompra (opcional)


- fechaCompra (opcional)


- cuit (requerido si el archivo mezcla clientes; si no, se selecciona clientId al importar)



Endpoint sugerido

- `POST /purchases/import`



### Acceptance Criteria

| AC | Criterio |
| --- | --- |
| AC1 | Import soporta preview + mapping antes de insertar. |
| AC2 | Filas inválidas se rechazan con motivo por fila. |
| AC3 | Si el archivo trae CUIT por fila, se resuelve clientId por CUIT y se valida pertenencia al user. |
| AC4 | Se devuelve resumen final (ok/rechazadas/warnings). |
