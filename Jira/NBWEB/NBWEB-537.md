---
jira_key: "NBWEB-537"
summary: "APP - Feat - Grilla de personal"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-04-26 16:14"
updated: "2023-05-08 07:22"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-537"
---

# NBWEB-537: APP - Feat - Grilla de personal

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-04-26 16:14 |
| Actualizado | 2023-05-08 07:22 |
| Etiquetas | ninguna |
| Jira | [NBWEB-537](https://bluinc.atlassian.net/browse/NBWEB-537) |

## Descripción

Basándose en el recurso [link](https://lioteam.atlassian.net/browse/NBWEB-530) 



Vamos a agregar una seccion “personal” y maquetar en ella una tabla para alojar parámetros editables y permisos del personal general de la empresa.

En esta tabla cada registro seria un individuo dentro del personal y cada columna un parámetro o permiso.

Se debe construir el siguiente recurso

```
GET {API_URL}/v1/cms/staff
```

Recibe

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

**id**

**Descripcion**

**parametro a**

**hijos**

**permiso**

**permiso**

123123

Bart Simpson

Padre

3

{checkbox}

{checkbox}

232332

Homero Simpson

Hijo

0

{checkbox}

{checkbox}

Los campos de la grilla, pueden editarse como lo hacen otras secciones con 

```
PATCH {API_URL}/v1/cms/staff
```

[link](https://lioteam.atlassian.net/browse/NBWEB-531)
