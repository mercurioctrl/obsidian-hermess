---
jira_key: "LIO-354"
aliases: ["LIO-354"]
summary: "API - Oportunidad de mejora - Registro de usuarios -> Acortar nombre de usuario"
status: "Finalizada"
type: "Tarea"
priority: "Lowest"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2025-05-15 17:13"
updated: "2025-06-02 19:25"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-354"
---

# LIO-354: API - Oportunidad de mejora - Registro de usuarios -> Acortar nombre de usuario

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Lowest |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2025-05-15 17:13 |
| Actualizado | 2025-06-02 19:25 |
| Etiquetas | ninguna |
| Jira | [LIO-354](https://bluinc.atlassian.net/browse/LIO-354) |

## Relaciones

- **relates to:** [[LIO-34]] API - Feat - Crear formularios de registro especifico para empresas e individuos 

## Descripcion

Al intentar registrar un usuario en el sitio, se presenta un error de base de datos. Por ello, surge la oportunidad de mejora para que, en caso de que el nombre exceda la longitud máxima permitida, este se recorte y se almacene completa en la tabla de vendedores.


Te dejo aquí los datos de la prueba:

```
CUIT: 30707064494
Razón Social: 'ALVAREZ ARTURO HIPOLITO OSCAR Y COCCO FERNANDO GABRIEL SOCIEDAD DE HECHO'
[LO].[dbo].[usuarios]
[LO].[dbo].[vendedores] 
```

```
curl "https://omega-api4.libreopcion.com.ar/v4/auth/register" -X POST -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:138.0) Gecko/20100101 Firefox/138.0" -H "Accept: application/json, text/plain, */*" -H "Accept-Language: es-MX" -H "Accept-Encoding: gzip, deflate, br, zstd" -H "Content-Type: application/json" -H "Origin: https://registrate.libreopcion.com" -H "Connection: keep-alive" -H "Referer: https://registrate.libreopcion.com/" -H "Sec-Fetch-Dest: empty" -H "Sec-Fetch-Mode: cors" -H "Sec-Fetch-Site: cross-site" -H "Priority: u=0" --data-raw "{""document"":""30707064494"",""fullName"":""ALVAREZ ARTURO HIPOLITO OSCAR Y COCCO FERNANDO GABRIEL SOCIEDAD DE HECHO"",""email"":""abcde^@gmail.com"",""password"":""abcde"",""businessName"":""ALVAREZ ARTURO HIPOLITO OSCAR Y COCCO FERNANDO GABRIEL SOCIEDAD DE HECHO""}"
```

[adjunto]
