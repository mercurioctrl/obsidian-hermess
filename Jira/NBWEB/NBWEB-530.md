---
jira_key: "NBWEB-530"
summary: "API - Listar parametros del personal"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Guillermo Avila"
reporter: "Catriel Mercurio"
created: "2023-04-12 10:28"
updated: "2023-05-08 07:24"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-530"
---

# NBWEB-530: API - Listar parametros del personal

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Guillermo Avila |
| Reportado por | Catriel Mercurio |
| Creado | 2023-04-12 10:28 |
| Actualizado | 2023-05-08 07:24 |
| Etiquetas | ninguna |
| Jira | [NBWEB-530](https://bluinc.atlassian.net/browse/NBWEB-530) |

## Descripción

El codigo se encuentra en [link](https://github.com/New-Bytes/sitio-api-rest-v3/) 

Usando el repositorio

```
SELECT  [id]
      ,[proveedores]
      ,[clientes]
      ,[proveedores_pedidos]
      ,[proveedores_remitos]
      ,[proveedores_lista]
      ,[gerencia]
      ,[modoDios]
      ,[administracion]
      ,[clientes_solicitudes]
      ,[clientes_clientes]
      ,[clientes_pedidos]
      ,[clientes_remitos]
      ,[clientes_facturas]
      ,[proveedores_facturas]
      ,[sincronizar]
      ,[ultimos50]
      ,[gestion_preguntas]
      ,[gestion_agentes]
      ,[inventario_informe]
      ,[proveedores_stock_mod]
      ,[modoPro]
      ,[proveedores_ordenProduccion]
      ,[lockRem]
      ,[cobrarRemito]
      ,[gestion_miscelanea]
      ,[inventario]
      ,[desliquidar]
      ,[controldeprecio]
      ,[percepciones]
      ,[grilla_lo]
      ,[contarstock]
      ,[regularizacion]
      ,[resumencc]
      ,[modificar_precio_envio]
      ,[nc_rma_precio_manual]
      ,[ver_stock_lo]
      ,[ver_stock_d0]
      ,[ocultar_lo]
      ,[pm]
      ,[cambiar_perfil]
      ,[ver_comisiones_de_todos]
      ,[cobro]
      ,[postventa_solucion]
      ,[postventa]
      ,[postventa_creditos]
      ,[postventa_admin]
      ,[cobro_admin]
      ,[expedicion_admin]
      ,[expedicion]
      ,[edit_credit]
      , B.[visible_pedidos]
      , B.comiosiona
      , B.dtoGral
      , B.dtoMax
      , B.xRemitoVto
      , B.cnbrage
      , B.capeage
  FROM [NB_WEB].[dbo].[permisos_agente] A
  LEFT JOIN NewBytes_DBF.DBO.agentes B ON A.agente_fp = B.ID_VENDEDOR 

```

Se debe construir el siguiente recurso

```
GET {API_URL}/v1/cms/staff
```

De modo tal que devuelva el siguiente Array de ejemplo para todos los registros

```
[
  {
    "id": 1,
    "show": 1,
    "commissions": 1,
    "dtoGral": -200.0,
    "dtoMax": 4500.0,
    "daysMaximumOrders": 7,
    "firstName": "Andrea",
    "lastName": "Altamiranda",
    "proveedores": 1,
    "clientes": 1,
    "proveedores_pedidos": 1,
    "proveedores_remitos": 1,
    "proveedores_lista": 1,
    "gerencia": 0,
    "modoDios": 0,
    "administracion": 1,
    "clientes_solicitudes": 1,
    "clientes_clientes": 1,
    "clientes_pedidos": 1,
    "clientes_remitos": 1,
    "clientes_facturas": 1,
    "proveedores_facturas": 1,
    "sincronizar": 1,
    "ultimos50": 1,
    "gestion_preguntas": 1,
    "gestion_agentes": 1,
    "inventario_informe": 1,
    "proveedores_stock_mod": 1,
    "modoPro": 1,
    "proveedores_ordenProduccion": 1,
    "lockRem": 0,
    "cobrarRemito": 0,
    "gestion_miscelanea": 1,
    "inventario": 0,
    "desliquidar": 41,
    "controldeprecio": 0,
    "percepciones": null,
    "grilla_lo": 0,
    "contarstock": 0,
    "regularizacion": 0,
    "resumencc": 0,
    "modificar_precio_envio": 0,
    "nc_rma_precio_manual": 0,
    "ver_stock_lo": 0,
    "ver_stock_d0": 0,
    "ocultar_lo": 0,
    "pm": 0,
    "cambiar_perfil": 1,
    "ver_comisiones_de_todos": 1,
    "cobro": 0,
    "postventa_solucion": 0,
    "postventa": 0,
    "postventa_creditos": 0,
    "postventa_admin": 0,
    "cobro_admin": 0,
    "expedicion_admin": 0,
    "expedicion": 0,
    "edit_credit": 0
  },
  {
    "id": 2,
    "show": null,
    "commissions": null,
    "dtoGral": null,
    "dtoMax": null,
    "daysMaximumOrders": null,
    "firstName": null,
    "lastName": null,
    "proveedores": 0,
    "clientes": 1,
    "proveedores_pedidos": 0,
    "proveedores_remitos": 0,
    "proveedores_lista": 0,
    "gerencia": 0,
    "modoDios": 0,
    "administracion": 0,
    "clientes_solicitudes": 1,
    "clientes_clientes": 1,
    "clientes_pedidos": 1,
    "clientes_remitos": 1,
    "clientes_facturas": 0,
    "proveedores_facturas": 0,
    "sincronizar": 0,
    "ultimos50": 0,
    "gestion_preguntas": 1,
    "gestion_agentes": 0,
    "inventario_informe": 0,
    "proveedores_stock_mod": 0,
    "modoPro": null,
    "proveedores_ordenProduccion": null,
    "lockRem": 0,
    "cobrarRemito": 0,
    "gestion_miscelanea": null,
    "inventario": 0,
    "desliquidar": 0,
    "controldeprecio": 0,
    "percepciones": null,
    "grilla_lo": 0,
    "contarstock": 0,
    "regularizacion": 0,
    "resumencc": 0,
    "modificar_precio_envio": 0,
    "nc_rma_precio_manual": 0,
    "ver_stock_lo": 0,
    "ver_stock_d0": 0,
    "ocultar_lo": 0,
    "pm": 0,
    "cambiar_perfil": 0,
    "ver_comisiones_de_todos": 0,
    "cobro": 0,
    "postventa_solucion": 0,
    "postventa": 0,
    "postventa_creditos": 0,
    "postventa_admin": 0,
    "cobro_admin": 0,
    "expedicion_admin": 0,
    "expedicion": 0,
    "edit_credit": 0
  }
  ]
```
