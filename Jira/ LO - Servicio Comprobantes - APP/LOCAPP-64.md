---
jira_key: "LOCAPP-64"
summary: "API - Refactor - Agregar Percepcion ARBA al realizar un comprobante"
status: "Finalizada"
type: "Subtarea"
priority: "High"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-04-28 08:18"
updated: "2025-05-12 14:33"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LOCAPP-64"
---

# LOCAPP-64: API - Refactor - Agregar Percepcion ARBA al realizar un comprobante

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | High |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-04-28 08:18 |
| Actualizado | 2025-05-12 14:33 |
| Etiquetas | ninguna |
| Jira | [LOCAPP-64](https://bluinc.atlassian.net/browse/LOCAPP-64) |

## Descripción

Dado que hemos agregado un nuevo tipo de percepción, es necesario tambien enviarla al webservice de AFIP y almacenarla para mostrar en nuestro comprobante impreso.

Para esto debemos tener en cuenta que en el **web service de AFIP**, especialmente al emitir facturas electrónicas a través del **WSFE (Web Services de Facturación Electrónica)**, las **percepciones de Ingresos Brutos** **no tienen un campo específico por jurisdicción**, por lo tanto, se envían como **ítems adicionales en el detalle** de la factura, **dentro del campo de “tributos”**, diferenciados por código y descripción.

### Cómo se informan en el WSFE

Usando los datos que creamos previamente en `[NEW_BYTES].[dbo].[MS_REMITO_PERCEPCIONES]` construiremos nuestro objeto de `Tributos`

El nodo `Tributos` permite incluir percepciones de IIBB (entre otros conceptos). Pero **AFIP no distingue jurisdicciones**, así que si tenés percepciones de CABA y PBA, **tenés que enviar dos entradas separadas** en ese nodo, con:

- **Distintas descripciones**


- **El mismo código tributario (**`05`** para Ingresos Brutos)**



```
<Tributos>
  <Tributo>
    <Id>5</Id> <!-- Código 5 = IIBB -->
    <Desc>Percepción IIBB CABA</Desc>
    <BaseImp>100000.00</BaseImp>
    <Alic>3.00</Alic>
    <Importe>3000.00</Importe>
  </Tributo>
  <Tributo>
    <Id>5</Id> <!-- Mismo código para PBA -->
    <Desc>Percepción IIBB PBA</Desc>
    <BaseImp>100000.00</BaseImp>
    <Alic>2.50</Alic>
    <Importe>2500.00</Importe>
  </Tributo>
</Tributos>

```

### Recomendaciones:

- El `Id = 5` identifica la percepción de Ingresos Brutos.


- La **descripción (**`Desc`**) es libre**, podes usarla para diferenciar las jurisdicciones.


- Aunque AFIP no valida jurisdicciones en ese campo, es importante que la percepción esté discriminada correctamente para que tu cliente la pueda imputar bien en su declaración SIFERE.



**¿Entonces donde lo almacenamos?**

Esto evalualo vos y decime cual es tu preferencia según tu criterio para mantener la coherencia de como funciona la informacion de comproabantes

- Agregar 2 nuevas Columnas para (si pude crear exitosamente el comprobante), almacenarlo en la cabecera


```
      ,[IIBBRETENCION_CLI] <-- Estas ya las tenemos y se usan para CABA
      ,[ImportePercepCLi] < -- Estas ya las tenemos y se usan para CABA
      ,[IIBBRETENCION_ARBA_CLI] <-- Estas ya las tenemos y se usan para CABA
      ,[ImportePercepCLi_ARBA_] < -- Estas ya las tenemos y se usan para CABA
```




- Dejar las 2 columnas que ya tenemos para guardar las percepciones sumadas, y en el desglose para mostrarlo diferenciado en el comprobante impreso usar lo que guardamos en `[NEW_BYTES].[dbo].[MS_REMITO_PERCEPCIONES]`
