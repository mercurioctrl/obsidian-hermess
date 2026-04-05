---
jira_key: "POS-123"
aliases: ["POS-123"]
summary: "MS - Servicio de emision de comprobantes"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-09-12 17:22"
updated: "2022-10-27 17:38"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-123"
---

# POS-123: MS - Servicio de emision de comprobantes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-09-12 17:22 |
| Actualizado | 2022-10-27 17:38 |
| Etiquetas | ninguna |
| Jira | [POS-123](https://bluinc.atlassian.net/browse/POS-123) |

## Relaciones

- **Padre:** [[POS-24 - Creditos|POS-24]] Creditos
- **Subtarea:** [[POS-124 - MS - Inicializar servicio|POS-124]] MS - Inicializar servicio
- **Subtarea:** [[POS-126 - MS - Feat - Obtener comprobante|POS-126]] MS - Feat - Obtener comprobante
- **Subtarea:** [[POS-127 - MS - Iniciar JWT|POS-127]] MS - Iniciar JWT
- **Subtarea:** [[POS-128 - MS - Feat - Login|POS-128]] MS - Feat - Login
- **Subtarea:** [[POS-129 - MS - Feat - Gestion de credenciales AFIP devprod|POS-129]] MS - Feat - Gestion de credenciales AFIP dev/prod
- **Subtarea:** [[POS-132 - MS - Feat - Emitir comprobante|POS-132]] MS - Feat - Emitir comprobante
- **Subtarea:** [[POS-133 - MS - Feat - Obtener parámetros del cliente para emitir comprobante|POS-133]] MS - Feat - Obtener parámetros del cliente para emitir comprobante
- **Subtarea:** [[POS-134 - MS - Feat - Repositorio de tipos de comprobante que podemos emitir|POS-134]] MS - Feat - Repositorio de tipos de comprobante que podemos emitir
- **Subtarea:** [[POS-135 - API - Feat - Emitir comprobante de un credito de postventa|POS-135]] API - Feat - Emitir comprobante de un credito de postventa
- **Subtarea:** [[POS-145 - API - Feat - Realizar crédito (imputar) en la cuenta corriente del cliente|POS-145]] API - Feat - Realizar crédito (imputar) en la cuenta corriente del cliente
- **Subtarea:** [[POS-262 - MS - Refactor - Obtener parámetros del cliente para emitir comprobante segun|POS-262]] MS - Refactor - Obtener parámetros del cliente para emitir comprobante segun empresa
- **Subtarea:** [[POS-291 - API - Refactor - en logica al realizar nota de credito según sucursal asignada|POS-291]] API - Refactor - en logica al realizar nota de credito según sucursal asignada al pedido

## Descripcion

Se trata de un micro servicio encargado de gestionar tanto en los datos internos como fiscales todos los comprobantes de distintas empresas.

Se trata de una API rest sencilla que gestiona un sistema de clave publica y privada para cada una de las “razones sociales” de la emrpesa para emitir comprobantes fiscales en los servidores de afip.
