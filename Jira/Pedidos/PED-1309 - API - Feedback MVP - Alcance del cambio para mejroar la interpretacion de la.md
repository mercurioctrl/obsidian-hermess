---
jira_key: "PED-1309"
aliases: ["PED-1309"]
summary: "API - Feedback MVP - Alcance del cambio para mejroar la interpretacion de la relacion costo - beneficio en el armado de kits"
status: "Finalizada"
type: "Tarea"
priority: "High"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2026-02-12 06:45"
updated: "2026-02-24 10:34"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1309"
---

# PED-1309: API - Feedback MVP - Alcance del cambio para mejroar la interpretacion de la relacion costo - beneficio en el armado de kits

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | High |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2026-02-12 06:45 |
| Actualizado | 2026-02-24 10:34 |
| Etiquetas | ninguna |
| Jira | [PED-1309](https://bluinc.atlassian.net/browse/PED-1309) |

## Relaciones

- **Padre:** [[PED-1170 - Kits|PED-1170]] Kits
- **has action item:** [[INV-341 - APP - Refactor - Cambios en la creacionedición de kits|INV-341]] APP - Refactor - Cambios en la creacion/edición de kits

## Descripcion

Eze, te dejo lo que investigue y lo que los PMs dejaron por escrito la necesidad puntual de personalizar costo

Esquema de costeo en BUNDLES
Para el armado de un combo, ya sea de dos productos o más de una marca o dos productos o más de distintas marcas, requerimos que se pueda desglosar el combo en sus items unitarios, con sus costos unitarios y sus utilidades unitarias.
De esta forma podríamos: 

- Marcar cada uno su utilidad sin perjudicar la rentabilidad del producto


- Mejorar el costo unitario de un producto que tenga fondos habilitados por X marca para el bundle. (Sin tener que modificar el costo del item unico para que el bundle tenga sentido y no sea lo mismo que comprarlo aparte)



Segun entiendo hay al menods 2 partes, primero guardar los datos nuevos

1 - **Guardar la nueva informacion para cada item en** `NewBytes_DBF.dbo.articulo_kits` **es decir que debemos agregar a la tabla y a los recursos que la complenta lo siguiente:**

### Costo sustituto del bundle

- `bundleCostSubstitute`



### Utilidades Mayorista

- `bundleUtilityMAY1`


- `bundleUtilityMAY2`



### Utilidades Minorista

- `bundleUtilityPL`


- `bundleUtilityPL1`



### Uilidades LibreOpción (LO)

- `bundleUtilityLO1`


- `bundleUtilityLO2`



### Utilidad Marketing Funds

- `bundleUtilityMK1`



2 - Al sincronizar el stock con el syncUp que sincronizamos el stock, también debería sincronizarse el costo del bundle siendo este la suma de los `bundleCostSubstitute` de las partes. Además buscaremos la forma de obtener el precio para cada caso (npvp1, nvp5, nplo) basandonos en la suma de sus parte y su utilidad, para lograr que el precio puesto al kit para cada lista de precio, sea dinamico como es el stock, pero ajustado a la suma de los costos mas utilidad de las partes.

3 - En la API de pedidos al realizar la insercion en `[NewBytes_DBF].[dbo].[pedclil]` podemos aprovechar la feature realizada para LASET que nos permite personlizar el costo para cada venta usando `[NewBytes_DBF].[dbo].[pedclil].costForSale` para guardar cada  `bundleCostSubstitute` y el precio lo marcaremos usando el esquema

A,B,C = bundleCostSubstitute + bundleCostSubstitute *(`bundleUtilityPL` + `bundleUtilityPLI`) / 100

D = bundleCostSubstitute + bundleCostSubstitute *(`bundleUtilityMAY1` + `bundleUtilityMAY1`) / 100

4 - Hay una posible cuarta parte, que es en la liquidacion, pero creo que si esto queda bien, ni habria que tocarlo (probemos primero con esto nada mas). 

---

## Fase 2 - Listas de precios automáticas 

## Objetivo

Incorporar utilidades específicas para **items que forman parte de un kit/bundle**, asociadas al `itemId` del kit, utilizando la tabla:

```
[NEW_BYTES].[dbo].[ST_GANANCIA_ESTIPULADA_ARTICULOS]
```

El objetivo es que el **proceso automático de cálculo de listas** pueda reutilizar esta información **sin cambios**, resolviendo las utilidades de forma dinámica según el artículo (kit).

---

## Comportamiento esperado

Para el item del kit (NO PARA SUS COMPONENTES):

- Si **no existe** un registro en `ST_GANANCIA_ESTIPULADA_ARTICULOS`
→ se debe **crear** la fila correspondiente.


- Si **ya existe** el registro
→ se deben **actualizar** únicamente las columnas de utilidad involucradas.



Este comportamiento debe ser **idempotente** (ejecutable múltiples veces sin efectos colaterales).

---

## Mapeo de campos

Los valores recibidos desde el bundle se persistirán utilizando el siguiente mapeo, de forma que el motor de precios actual pueda consumirlos sin modificaciones:

| Campo lógico (bundle) | Columna destino |
| --- | --- |
| `idKit` | `ID_ARTICULO` |
| `bundleUtilityPL` +`bundleUtilityPL1` | `PORC_GANAN_ESTIP` (eso es segun el caculo de google doc [link](https://docs.google.com/spreadsheets/d/1ntdPbs-wnLG6oqs20DmmByzE7ND8Twuq2P7-EBv30-c/edit?usp=sharing), osea: utilidad=ganancia/costo ) |
| `bundleUtilityMAY1` + `bundleUtilityMAY2` | `PORC_GANAN_ESTIP3` (eso es segun el caculo de google doc [link](https://docs.google.com/spreadsheets/d/1ntdPbs-wnLG6oqs20DmmByzE7ND8Twuq2P7-EBv30-c/edit?usp=sharing) , osea: utilidad=ganancia/costo) |
| `bundleUtilityLO` + `bundleUtilityLO1` | `PORC_GANAN_ESTIPLO` (eso es segun el caculo de google doc [link](https://docs.google.com/spreadsheets/d/1ntdPbs-wnLG6oqs20DmmByzE7ND8Twuq2P7-EBv30-c/edit?usp=sharing), osea: utilidad=ganancia/costo ) |

`PORC_GANAN_ESTIP2 = 0`

`PORC_GANAN_ESTIP4 = 0`

`PORC_GANAN_ESTIPLO = 0`

Usaremos el resultado del calculo deutilidad para una sola columna del par y la otra queda en cero, en una sola columna. Decime si no entendes esta parte que es la mas confusa

---

## Resultado esperado

- Las utilidades del kit quedan almacenadas como si fueran un artículo estándar.


- El cálculo automático de listas utiliza estas utilidades **sin lógica especial para bundles**.


- Se mantiene compatibilidad total con el esquema actual de pricing.
