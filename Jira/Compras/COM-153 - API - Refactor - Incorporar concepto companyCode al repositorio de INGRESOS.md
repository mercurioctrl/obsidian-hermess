---
jira_key: "COM-153"
aliases: ["COM-153"]
summary: "API - Refactor - Incorporar concepto companyCode al repositorio de INGRESOS"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-12-09 07:55"
updated: "2024-12-20 06:01"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-153"
---

# COM-153: API - Refactor - Incorporar concepto companyCode al repositorio de INGRESOS

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-12-09 07:55 |
| Actualizado | 2024-12-20 06:01 |
| Etiquetas | ninguna |
| Jira | [COM-153](https://bluinc.atlassian.net/browse/COM-153) |

## Relaciones

- **Padre:** [[COM-12]] Listar ingresos (despachos de compra)
- **has action item:** [[COM-159]] APP - Refactor - Agregar filtro empresa global

## Descripcion

Al igual que lo realizado en ventas, incorporaremos el concepto `companyCode` a la parte de compras

Para esto lo agregaremos en la tabla `[NewBytes_DBF].[dbo].[albprot].companyCode`

Y de esta forma lo filtraremos en el recurso 

```
GET {API_URL}/v1/providerOrderInbound?companyCode={companyCode}
```

A su vez, tambien lo agregaremos en el objeto de respuesta del recurso

```
{
    "response": [
        {
            "id": 9525,
            "providerOrder": 11411,
            "providerId": "000039",
            "providerName": "Stylus SA",
            "dispatchName": "",
            "userId": "14",
            "updated": 0,
            "dispatchDate": "2024-12-06 00:00:00.000",
            "numPed": 11411,
            "fullSerialized": true,
            "total": 2659140,
            "totalFinal": 2939634.9,
            "companyCode": 4 <<-- SE AGREGA
        },
```

Para evitar concurrencias indeseadas dado que somos tres tirando codigo a este repo, se aconseja trabajar una rama aparte por feature a partir de development
