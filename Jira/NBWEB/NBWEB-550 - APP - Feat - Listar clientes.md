---
jira_key: "NBWEB-550"
aliases: ["NBWEB-550"]
summary: "APP - Feat - Listar clientes"
status: "Code Review"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2023-05-29 07:31"
updated: "2023-07-27 12:25"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-550"
---

# NBWEB-550: APP - Feat - Listar clientes

| Campo | Valor |
|-------|-------|
| Estado | Code Review (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2023-05-29 07:31 |
| Actualizado | 2023-07-27 12:25 |
| Etiquetas | ninguna |
| Jira | [NBWEB-550](https://bluinc.atlassian.net/browse/NBWEB-550) |

## Relaciones

- **Padre:** [[NBWEB-548 - CMS - Clientes|NBWEB-548]] CMS - Clientes
- **is blocked by:** [[NBWEB-556 - API - Repositorio empresas|NBWEB-556]] API - Repositorio empresas

## Descripcion

Agregaremos una sección extra en el CMS dedicada específicamente a los clientes (/`customers`)

En ella mostraremos el listado obtenido en [https://lioteam.atlassian.net/browse/NBWEB-549](https://lioteam.atlassian.net/browse/NBWEB-549)

```
  "id": 77160,
    "clientName": "ECHANIZ HERMANOS SOCIEDAD ANONIMA",
    "clientComercialName": "Echaniz hnos",
    "discount": 1.0,
    "priceList": 1.0,
    "defaultCurrency": 1,
    "ccoddiv": "DOL",
    "brokerage": 0,
    "userBlack": null,
    "userBlackpercentage": 5000000.0,
    "profile": 1,
    "company": 4,
    "sellerId": 41,
    "lastNameSeller": "Sheridaim",
    "sellerName": "Natalia"
```

- Id 


- ClienteName → Es el nombre del cliente real, dado de alta en afip


- ClientComercialName → Es el nombre de fantasía del cliente


- defaultCurrency → Es la divisa por default que utiliza la cuenta y es un selector Dolares (1) / Pesos (/)


- brokerage → Indica si es una intermediacion (importacion en nombre del cliente), debe ser un conmutador, según sea 1 o 0 

[adjunto]

- UserBlack → Indica si puede usar descuentos Black, es un conmutador


- UserBlackPercentage - > Es un numero porcentual entre cero y 100


- Profile → Es el tipo de perfil que tiene la cuenta del cliente debe mostrar un selector con las opciones: Perfil 1 (1),Perfil 2 (2),Perfil 3 (3),Perfil 4 (4),Perfil 5 (5),Perfil 6 (6), MarketPlace (7), Al costo (8). Lo que esta en paracentesis es el entero que se envía, el texto el a descripcion de la opcion.


- Comprany → Es el selector de la empresa que le vende, es un selector , nuevamente el entero que se envia entre parentesis y el texto del selector con el que viene marcado en recurso y el resto de las opciones



```
 (4)NB DISTRIBUIDORA MAYORISTA SRL
    (2)OXXEN SRL
    (3)NBGLOBAL
    (5)DIGITO BINARIO SRL
    (7)SUC 10
    (8)MUGELLO SRL
    (6)CONSORCIO DE COOPERACION RED DE TECNOLOGIA
```

- sellerId, lastNameSeller, sellerName → Es el id del vendedor, nombre y apellido en el siguiente formato : (sellerId) - sellerName lastNameSeller



El resto de los parametros por ahora no se muestra, pero los usaremos para operar mas adelante.
