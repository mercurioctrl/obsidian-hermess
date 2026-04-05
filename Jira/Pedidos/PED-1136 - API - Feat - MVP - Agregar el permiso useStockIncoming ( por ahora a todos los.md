---
jira_key: "PED-1136"
aliases: ["PED-1136"]
summary: "API - Feat - MVP - Agregar el permiso useStockIncoming ( por ahora a todos los companyCode == 11)"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Marbe Moreno"
created: "2025-10-03 14:27"
updated: "2025-10-24 10:42"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1136"
---

# PED-1136: API - Feat - MVP - Agregar el permiso useStockIncoming ( por ahora a todos los companyCode == 11)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Marbe Moreno |
| Creado | 2025-10-03 14:27 |
| Actualizado | 2025-10-24 10:42 |
| Etiquetas | ninguna |
| Jira | [PED-1136](https://bluinc.atlassian.net/browse/PED-1136) |

## Relaciones

- **Padre:** [[PED-3 - Ordenes de compra|PED-3]] Ordenes de compra
- **has action item:** [[PED-1137 - APP - Feat - MVP - agregar una columna al detalle de la orden sólo si|PED-1137]] APP - Feat - MVP - agregar una columna al detalle de la orden sólo si useStockIncoming   y stockIncoming >0 marcar una etiqueta de en camino

## Descripcion

Exponer un nuevo flag booleano `useStockIncoming` en la respuesta del endpoint de autenticación de usuario. 

```
GET /v1/auth/user
```

```
{
    "user": {
        "id": 7463,
        "codeFP": 19227,
        "username": "Catriel",
        "email": "algo@gmail.com",
        "codeAgent": 12,
        "showName": "catriel2",
        "usuIdentificacion": "Seba",
        "pedidos": true,
        "pm": true,
        "allComissions": true,
        "roleDescription": "Administrador",
        "discountShipping": true,
        "rebill": true,
        "orderOwner": null,
        "ip": "190.189.129.96",
        "whatsappAgent": null,
        "phoneAgent": null,
        "emailAgent": "soporteweb@nb.com.ar",
        "nameAgent": null,
        "roleAgent": "Administrador",
        "companyCode": null,
        "editCostForSale": null,
        "unlimitedReports": null,
        "createManualVoucher": 1,
        "banListPrice": null,
        "useStockIncoming": false <--
    }
}
```

El valor proviene de la tabla `[NB_WEB].[dbo].[permisos_agente]`. Además, setear en base de datos `useStockIncoming = 1` para **todos los agentes cuyo **`companyCode`** sea 11**.

Hoy devuelve los permisos y metadatos del usuario autenticado, pero no informa si puede usar el flujo de “Stock entrante”. Necesitamos un flag explícito para habilitar UI y reglas de negocio dependientes.

---

## Alcance

- **Modelo/Repositorio**

- Leer `useStockIncoming` desde `[NB_WEB].[dbo].[permisos_agente]` asociado al agente actual.




- **Endpoint**

- Enriquecer la respuesta de `GET /v1/auth/user` con el campo booleano `useStockIncoming`.




- **Data Fix**

- Actualizar datos para que **todos los agentes** con `companyCode = 11` queden con `useStockIncoming = 1`.
