---
jira_key: "COB-382"
aliases: ["COB-382"]
summary: "API - Refactor - Agregar la columna proveedores, cliente y \"agente\" en la grilla de movimientos bancarios"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Guillermo Avila"
reporter: "Catriel Mercurio"
created: "2023-03-23 08:57"
updated: "2023-04-28 08:59"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-382"
---

# COB-382: API - Refactor - Agregar la columna proveedores, cliente y "agente" en la grilla de movimientos bancarios

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Guillermo Avila |
| Reportado por | Catriel Mercurio |
| Creado | 2023-03-23 08:57 |
| Actualizado | 2023-04-28 08:59 |
| Etiquetas | ninguna |
| Jira | [COB-382](https://bluinc.atlassian.net/browse/COB-382) |

## Relaciones

- **Padre:** [[COB-218]] Feat - Movimientos bancarios
- **blocks:** [[COB-392]] APP - Refactor - Agregar columnras "Cliente", "Proveedor" y "Agente" a cada movimiento, en caso de que esten disponibles

## Descripcion

Agregaremos al repositorio [link](https://lioteam.atlassian.net/browse/COB-219)  las columnas

- Cliente


- Proveedor


- Agente (usuario que hizo la operación, este creo que ya esta)





```
{
"dateOperation": "2022-11-02 00:00:00.000",
"amount": 64582.62,
"subTotal": 1709378101.9794693,
"symbolCurrency": "$",
"nameCurrency": "Pesos",
"agent": "CAJA1",
"observation": "0002-00547430",
"balanceTotal": 1709378101.9794686,
"providerId": 45,
"providerDescription": "LOGITECH",
"clientId": 43,
"clientDescription": "Nombre del cliente"
}
```



Esta informacion debería estar guardada en el registro, pero en caso de que no la estemos recolectando, deberemos pedirle a  que en las operaciones donde se hacen cobros bancarios o transferencias bancarias, empiece a registrar tanto el proveedor (cuando se hace un pago a proveedor) como el cliente (Cuando interviene un cliente)

**Tablas utiles**

`[NewBytes_DBF].[dbo].[FP_Proveedores]`

`[NewBytes_DBF].[dbo].[clientes]`

`[BA_BP_MOVIMIENTOS_SALIDAS]` 

 `[BA_BP_MOVIMIENTOS_ENTRADAS]`



La idea final es poder agregar estos parametros como columnas y filtros en el siguiente modal

[adjunto]
