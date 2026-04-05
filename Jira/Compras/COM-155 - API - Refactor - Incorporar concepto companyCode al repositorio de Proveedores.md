---
jira_key: "COM-155"
aliases: ["COM-155"]
summary: "API - Refactor - Incorporar concepto companyCode al repositorio de Proveedores"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-12-09 08:12"
updated: "2024-12-22 23:09"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-155"
---

# COM-155: API - Refactor - Incorporar concepto companyCode al repositorio de Proveedores

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-12-09 08:12 |
| Actualizado | 2024-12-22 23:09 |
| Etiquetas | ninguna |
| Jira | [COM-155](https://bluinc.atlassian.net/browse/COM-155) |

## Relaciones

- **Padre:** [[COM-6]] Listar proveedores
- **has action item:** [[COM-159]] APP - Refactor - Agregar filtro empresa global

## Descripcion

Al igual que lo realizado en ventas, incorporaremos el concepto `companyCode` a la parte de compras

Para esto lo agregaremos en la tabla `[NewBytes_DBF].[dbo].[FP_Proveedores].companyCode`

Y de esta forma lo filtraremos en el recurso

```
GET {API_URL}/v1/providers?companyCode={companyCode}
```

A su vez, tambien lo agregaremos en el objeto de respuesta del recurso

```
{
    "response": [
        {
            "id": 16141,
            "providerCode": "002077",
            "name": "TECI S A C",
            "businessName": "TECI S A C",
            "address": "HUMBERTO 1 2352\/58",
            "countryId": 7,
            "prefixFlag": "AR",
            "countryDescription": "Argentina",
            "countryFlagId": 1,
            "provinceId": 2,
            "locateId": 20892,
            "ccoddiv": "DOL",
            "locateDescription": "BUENOS AIRES",
            "companyCode": 4 <<-- SE AGREGA
        },
```

Para evitar concurrencias indeseadas dado que somos tres tirando codigo a este repo, se aconseja trabajar una rama aparte por feature a partir de development
