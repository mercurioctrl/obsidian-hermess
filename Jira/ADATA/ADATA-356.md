---
jira_key: "ADATA-356"
summary: "XPG - Landing Fidelización (Puntos + Aceleradores + Ranking + Carga Compras)"
status: "Por hacer"
type: "Epic"
priority: "Medium"
assignee: "Sin asignar"
reporter: "Catriel Mercurio"
created: "2026-02-19 11:11"
updated: "2026-02-19 11:52"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/ADATA-356"
---

# ADATA-356: XPG - Landing Fidelización (Puntos + Aceleradores + Ranking + Carga Compras)

| Campo | Valor |
|-------|-------|
| Estado | Por hacer (Por hacer) |
| Tipo | Epic |
| Prioridad | Medium |
| Asignado | Sin asignar |
| Reportado por | Catriel Mercurio |
| Creado | 2026-02-19 11:11 |
| Actualizado | 2026-02-19 11:52 |
| Etiquetas | ninguna |
| Jira | [ADATA-356](https://bluinc.atlassian.net/browse/ADATA-356) |

## Descripción

Construir la landing de fidelización para **XPG** basada en puntos y aceleradores.
El sistema funciona mediante **carga de compras** (manual + Excel) y un motor de **aceleradores** que matchea por **SKU exacto** o por **texto contenido** en el nombre del producto, y multiplica puntos dentro del período de vigencia del acelerador.

#### Objetivo funcional

- Login + autoregistro + recuperación de clave.


- Gestión de **clientes** asociados al usuario (un usuario puede tener varios CUIT).


- Carga de compras:

- Manual


- Importación Excel con **mapeo de columnas** + preview + validación




- Aceleradores:

- Vigentes / Próximos / Expirados


- Match por SKU exacto o por match parcial (contiene)




- Ranking:

- Usuario ve solo: **posición propia + anterior + siguiente** (no ranking completo)


- Admin ve ranking completo




- Panel Admin:

- ranking completo


- (mínimo) inspección de compras y aceleradores





#### Reglas de cálculo (MVP, determinísticas)

- Puntos base por compra: `base = montoTotal`


- Si hay acelerador vigente que matchee: `final = base * multiplicador`


- Vigencia por fecha:

- si existe `fechaCompra` usar esa para validar vigencia


- si no existe `fechaCompra`, usar `fechaCarga`




- Si matchean varios aceleradores: aplicar **solo el de mayor multiplicador** (desempate por `id` o `priority` si lo agregan).



## Observaciones técnicas 



- Normalización para match parcial: `UPPER + trim + colapsar espacios` (ideal remover tildes si aparece)


- Si `fechaCompra` es null, usar `fechaCarga` para vigencia del acelerador


- No exponer ranking completo al usuario (solo snippet)


- Preferible persistir auditoría de puntos por compra para debugging y soporte



---

Este EPIC entrega la **landing de fidelización XPG** basada en **puntos** y **aceleradores**, soportada por un backend que permite **cargar compras**, **aplicar multiplicadores por match** y **construir un ranking** sin exponer el listado completo a los usuarios.

Incluye las siguientes líneas de trabajo:

- **Base de datos y entidades**: creación del modelo para **usuarios**, **clientes (CUIT)**, **compras** y **aceleradores**, con relaciones para que un usuario pueda administrar **múltiples clientes**.


- **Autenticación**: login, autoregistro y recuperación de contraseña para el portal.


- **Aceleradores**: repositorio y administración de aceleradores con vigencia (vigentes, próximos, expirados) y reglas de match por **SKU exacto** o por **texto contenido**.


- **Carga de compras**: alta manual y carga masiva mediante **importación Excel** con **preview y mapeo de columnas**, validación por fila y reporte de resultados.


- **Cálculo de puntos**: motor que calcula puntos por compra aplicando el multiplicador vigente correspondiente y resolviendo colisiones de aceleradores de forma determinística.


- **Ranking**: generación del ranking por suma de puntos, con endpoint para usuario que devuelve solo **posición propia + anterior + siguiente**, y un acceso **admin** para ranking completo.


- **Frontend XPG**: implementación de pantallas según mockups:

- login + recuperación


- registro


- dashboard con puntos, ranking snippet y aceleradores


- carga de compras (manual + Excel)




- **Panel de administración**: UI y endpoints para ver ranking completo, gestionar aceleradores y consultar compras con filtros.



Mokup: [link](https://blu.inc/programaXpg/) 

Repositorio: [git@github.com](mailto:git@github.com):BluIncStudio/programaXpg.git
