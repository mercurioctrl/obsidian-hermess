---
jira_key: "NBWEB-142"
aliases: ["NBWEB-142"]
summary: "API - Traer direcciones de envío"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-04-26 10:43"
updated: "2022-06-26 21:33"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-142"
---

# NBWEB-142: API - Traer direcciones de envío

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-04-26 10:43 |
| Actualizado | 2022-06-26 21:33 |
| Etiquetas | ninguna |
| Jira | [NBWEB-142](https://bluinc.atlassian.net/browse/NBWEB-142) |

## Relaciones

- **Padre:** [[NBWEB-11 - API - Implementar Cotizadores de envio|NBWEB-11]] API - Implementar Cotizadores de envio
- **blocks:** [[NBWEB-145 - APP - Carrito - Maquetar y conectar Direcciones de envio|NBWEB-145]] APP -  Carrito - Maquetar y conectar Direcciones de envio 

## Descripcion

Se debe traer las direcciones que figuran en `[NB_WEB].[dbo].[dircli]`, siendo la que es favorita, la que se encuentra cargada en `[NewBytes_DBF].[dbo].[dircli]` para ese cliente

```
GET {{API_URL}}/v1/miCuenta/deliveryAddresses
```

Retorna:

```json
[
    {
        "direccion": "alguna de prueba 124",
        "telefono": "1530510267",
        "localidad": "CIUDAD DE BUENOS AIRES        ",
        "provincia": "BUENOS AIRES ( BS. AS )       ",
        "codigoPostal": "1407",
        "IdDirCli": "18063",
        "predeterminado": null
    },
    {
        "direccion": "Direccion de prueba 234",
        "telefono": "1540329485",
        "localidad": "AGUA PINTADA                  ",
        "provincia": "CORDOBA                       ",
        "codigoPostal": "5000",
        "IdDirCli": "19140",
        "predeterminado": null
    },
    {
        "direccion": "Direccion de pruba",
        "telefono": "423434",
        "localidad": "MAR DEL PLATA                 ",
        "provincia": "BUENOS AIRES ( BS. AS )       ",
        "codigoPostal": "4324",
        "IdDirCli": "19149",
        "predeterminado": "29626"
    }
]
```



Query de Referencia para obtener la información necesaria de provincias y localidades



```
        LEFT JOIN NewBytes_DBF.dbo.FP_Ciudades ON FP_Ciudades.CCODPOBL = dircli.ccodpobl
        LEFT JOIN NewBytes_DBF.dbo.FP_Provincias ON FP_Provincias.Id_Provincia = FP_Ciudades.Id_Provincia
```
