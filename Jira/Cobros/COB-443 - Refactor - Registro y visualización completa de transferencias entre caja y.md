---
jira_key: "COB-443"
aliases: ["COB-443"]
summary: "Refactor - Registro y visualización completa de transferencias entre caja y cuenta"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Guillermo Avila"
reporter: "Catriel Mercurio"
created: "2023-06-30 09:07"
updated: "2024-04-16 12:19"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-443"
---

# COB-443: Refactor - Registro y visualización completa de transferencias entre caja y cuenta

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Guillermo Avila |
| Reportado por | Catriel Mercurio |
| Creado | 2023-06-30 09:07 |
| Actualizado | 2024-04-16 12:19 |
| Etiquetas | ninguna |
| Jira | [COB-443](https://bluinc.atlassian.net/browse/COB-443) |

## Relaciones

- **Padre:** [[COB-15]] Cajas

## Descripcion

Al realizar una transferencia entre caja y cuenta

[adjunto]
Utilizando el recurso 

```
POST {API_URL}/v1/bankTransfers
```

Se guarda el resultado de la siguiente manera en la vista de caja (en la caja)

[adjunto]
Y de la siguiente manera en la sección de banco 

[adjunto]
**Lo que se busca es dar cuenta, tanto en la seccion de caja como en la seccion de banco, quien es el emisor y el receptor de la misma.**

Como se puede ver, se aprecia en uno u otro que el agente fue seba, pero no se aprecia bien cual es la caja y banco de origen destino.

La idea es agregar la informacion faltante (caja o banco) en los recursos

```
GET {API_URL}/v1/box/
```

Y 

```
GET {API_URL}/v1/currentBankAccount
```

para poder visualizar completa la informacion ya sea que la transferencia es de

 banco a caja

o de caja a banco

En caso de agregarse nuevos parametros a los objetos, los mismos seran en ingles y deben dejarse anotados en esta historia para saber como es el objeto final

En caso de que para obtener el dato, sea necesario cruzar muchas tablas y esto demore los listados, lo mejor es gurdar el dato (origen/destino) en una tabla que ya estemos utilizando en lugar de ir a buscarlo.
