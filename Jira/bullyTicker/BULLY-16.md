---
jira_key: "BULLY-16"
summary: "API - Feat - Objeto user (Login ETNA)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-06-22 14:18"
updated: "2023-07-10 10:14"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/BULLY-16"
---

# BULLY-16: API - Feat - Objeto user (Login ETNA)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-06-22 14:18 |
| Actualizado | 2023-07-10 10:14 |
| Etiquetas | ninguna |
| Jira | [BULLY-16](https://bluinc.atlassian.net/browse/BULLY-16) |

## Descripción

Al hacer login en nuestra aplicación usando las variables de entorno en `.env`, tambien haremos login en la api de ETNA, segun la documentacion [link](https://help.etnatrader.com/web-api/trading-api/authentication/requesting-tokens) 

El login con ETNA debe ser persistente, pensando en que consultar el gráfico es algo que uno hace en iteracion constante y no se debe re loguear a menos que sea necesario

Utilizando el ejemplo en [link](https://help.etnatrader.com/web-api/trading-api/code-samples/get-user-information)  para obtener la informacion de usuario en nuestro propio metodo `getUsersInfo` y almacenar la informacion de usuario en nuestro propio JWT

```
{
    "UserId": 644, //this is the ID from the path
    "FirstName": "Robert",
    "MiddleName": "",
    "LastName": "Zakiev",
    "Login": "robert.zak",
    "Email": "someEmail@etnatrader.com",
    "AddedDate": "2019-01-14T12:27:37.6205663Z",
    "Salutation": "NoSalutation",
    "Suffix": "NoSuffix"
}
```

Adicionalmente agregaremos el recurso 

```
GET {API_URL}/v1/user
```

Para poder consultar la informacion del usuario (y la que obtuvimos arriba) en un objeto como lo hacemos siempre
