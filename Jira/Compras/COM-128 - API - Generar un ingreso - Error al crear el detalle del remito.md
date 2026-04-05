---
jira_key: "COM-128"
aliases: ["COM-128"]
summary: "API - Generar un ingreso - Error al crear el detalle del remito"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Catriel Mercurio"
reporter: "Guillermo Avila"
created: "2024-07-23 00:48"
updated: "2024-08-08 03:29"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-128"
---

# COM-128: API - Generar un ingreso - Error al crear el detalle del remito

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Catriel Mercurio |
| Reportado por | Guillermo Avila |
| Creado | 2024-07-23 00:48 |
| Actualizado | 2024-08-08 03:29 |
| Etiquetas | ninguna |
| Jira | [COM-128](https://bluinc.atlassian.net/browse/COM-128) |

## Relaciones

- **Padre:** [[COM-8 - Ordenes de compra|COM-8]] Ordenes de compra
- **blocks:** [[COM-110 - API - Generar un ingreso|COM-110]] API - Generar un ingreso

## Descripcion

Al intentar crear la orden de ingreso, me aparece el siguiente error de SQL, esto puede ser al momento de intentar insertar el detalle del remito.

```
{{API_URL}}/v1/makeProviderOrderInbound
```

[adjunto]
```
{
    "errors": {
        "status": 500,
        "title": "SQLSTATE[07002]: [Microsoft][ODBC Driver 17 for SQL Server]COUNT field incorrect or syntax error (SQL: INSERT INTO newbytes_dbf.dbo.albprol (\n                                      nnumalb,\n                                      cref,\n                                      cdetalle,\n                                      nprediv,\n                                      ncanent,\n                                      nservicio,\n                                      ndto,\n                                      cserie,\n                                      nivaserv,\n                                      nlinea,\n                                      ntipocomp,\n                                      nmontoimp,\n                                      ntipoimp,\n                                      id_articulo)\n                        VALUES (:nnumalb,\n                                :cref,\n                                :cdetalle,\n                                :nprediv,\n                                :ncanent,\n                                :nservicio,\n                                :ndto,\n                                :cserie,\n                                :nivaserv,\n                                (SELECT IIF(MAX(nlinea) IS NULL, 1, MAX(nlinea) + 1) FROM newbytes_dbf.dbo.albprol WHERE nnumalb = :nnumalb),\n                                :ntipocomp,\n                                :nmontoimp,\n                                :ntipoimp,\n                                :ID_Articulo))",
        "file": "/var/www/app/vendor/laravel/framework/src/Illuminate/Database/Connection.php",
        "line": 760
    }
}
```
