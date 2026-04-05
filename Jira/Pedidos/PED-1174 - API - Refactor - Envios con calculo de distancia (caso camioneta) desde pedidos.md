---
jira_key: "PED-1174"
aliases: ["PED-1174"]
summary: "API - Refactor - Envios con calculo de distancia (caso camioneta) desde pedidos"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-12-04 07:57"
updated: "2025-12-22 18:40"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1174"
---

# PED-1174: API - Refactor - Envios con calculo de distancia (caso camioneta) desde pedidos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-12-04 07:57 |
| Actualizado | 2025-12-22 18:40 |
| Etiquetas | ninguna |
| Jira | [PED-1174](https://bluinc.atlassian.net/browse/PED-1174) |

## Relaciones

- **Padre:** [[PED-7]] Repositorios y base del proyecto

## Descripcion

El sistema deberá enviar información completa de la dirección de destino al microservicio de envíos cuando se solicite una cotización para órdenes con destino a las provincias de CABA (id 1) o Buenos Aires (id 2). 

Estos valores se encuentra ne la tabla: `NewBytes_DBF.dbo.FP_Provincias`

### Contexto

Actualmente, el endpoint de cotización de envíos

```
 GET /orders/nb/{branch}-{order}/cp/{cp_destination}
```

solo envía el código postal de destino al microservicio externo de envíos. Sin embargo, para provincias específicas (CABA y Buenos Aires), el microservicio requiere la dirección completa para calcular correctamente las tarifas de envío en camioneta o motocicleta.

### Comportamiento Esperado

El sistema deberá:

- **Validar la provincia de destino** de la orden antes de realizar la consulta al microservicio de envíos


- **Obtener los datos de dirección completa** cuando `provinceId = 1` (CABA) o `provinceId = 2` (Buenos Aires):

- Dirección final (`addressFinal`)


- Localidad final (`localityNameFinal`)


- Provincia final (`provinceNameFinal`)




- **Construir el parámetro **`destinationAddress` en el formato: `"Dirección, Localidad, Provincia"` (separado por comas)


- **Enviar la dirección completa** al microservicio agregando el parámetro opcional al endpoint:

- **Con dirección**: `/order/nb/{branch}-{order}/cp/{cp}/{destinationAddress}`


- **Sin dirección**: `/order/nb/{branch}-{order}/cp/{cp}` → actualmente no se envia nada. seria la logica normal





### Criterios:

- **Solo aplicar para **`provinceId = 1 o 2`: Para el resto de provincias, mantener el comportamiento actual (solo código postal)


- **Validar campos no nulos**: Si alguno de los campos de dirección (`addressFinal`, `localityNameFinal`, `provinceNameFinal`, `provinceId`) es NULL, usar la lógica actual sin enviar `destinationAddress`


- **Formato de dirección**: Los campos deben estar separados por comas y espacios: `"{dirección}, {localidad}, {provincia}"`



### Criterios de Aceptación

- El endpoint `GET /orders/nb/{branch}-{order}/cp/{cp_destination}` obtiene la dirección de envío de la orden


- Se valida que `provinceId` sea 1 (CABA) o 2 (Buenos Aires)


- Para provincias diferentes a 1 o 2, se mantiene el comportamiento actual


- El microservicio de envíos recibe y procesa correctamente la dirección completa
