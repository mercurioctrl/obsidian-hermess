---
jira_key: "PED-206"
aliases: ["PED-206"]
summary: "API - Feat - Listar solicitudes de cliente -> Filtro full"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-11-01 09:50"
updated: "2023-11-01 13:18"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-206"
---

# PED-206: API - Feat - Listar solicitudes de cliente -> Filtro full

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-11-01 09:50 |
| Actualizado | 2023-11-01 13:18 |
| Etiquetas | ninguna |
| Jira | [PED-206](https://bluinc.atlassian.net/browse/PED-206) |

## Relaciones

- **Padre:** [[PED-201]] Solicitudes de Alta

## Descripcion

Agregaremos algunos datos extra, que nos sirven para precargar la suscripcion del cliente



```
GET {API_URL}/v1/clientRequest?full=true
```

```
[
        {
            "id": 49962,
            "requestId": 49962,
            "date": null,
            "username": "JuanCruzNuevo",
            "userEmail": "juancruz_nuevo14@hotmail.com",
            "emailConfirmed": 1,
            "socialReason": "Juan cruz nuevo",
            "fantasyName": "Jn computaci\u00f3n",
            "dni": "36051919",
            "name": "Juan cruz",
            "cuit": "36051919",
            "fixedPhone": "2396511283",
            "cellPhone": "",
            "secondaryEmail": null,
            "companyWebsite": null,
            "howYouKnowUs": "Buscador",
            "requestDate": "12/12/2019 12:12"
            <--- Cuando full=true  agregamos estos parametros ---->
            provinceId:
            taxType:
            address:
            zipCode:
            whaPhone:
        },
        {
            "id": 49961,
            "requestId": 49961,
            "date": null,
            "username": "agustiin12",
            "userEmail": "agustinmilito12@gmail.com",
            "emailConfirmed": 1,
            "socialReason": "Emprendimiento",
            "fantasyName": "Milix",
            "dni": "45307540",
            "name": "Agustin",
            "cuit": "45307540",
            "fixedPhone": "01159639233",
            "cellPhone": "",
            "secondaryEmail": null,
            "companyWebsite": null,
            "howYouKnowUs": "internet",
            "requestDate": "12/12/2019 12:12"
            <--- Cuando full=true  agregamos estos parametros ---->
            provinceId:
            taxType:
            address:
            zipCode:
            whaPhone:
        }
    ]
```

### Repositorio

```
SELECT
id,
UserName,
UserEmail,
correoConfirmado,
REPLACE(nombre, 'ñ', 'ñ')  as nombre,
CONVERT(VARCHAR, fecha, 20) as fecha,
RSocial,
NFantasia,
dni,
cuit,
telFi,
telCel,
email2,
wwwEmpresa,
comoNos
FROM [NB_WEB].dbo.usuarios_nb
RIGHT JOIN [NB_WEB].dbo.info_usuarios
ON usuarios_nb.UserId = info_usuarios.UserLogId
WHERE activa = 0 and eliminado =0
ORDER BY UserId DESC
```
