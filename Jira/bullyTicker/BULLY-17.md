---
jira_key: "BULLY-17"
summary: "API - Feat - Trazar medias moviles (SMA)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-06-26 09:21"
updated: "2023-07-10 10:14"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/BULLY-17"
---

# BULLY-17: API - Feat - Trazar medias moviles (SMA)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-06-26 09:21 |
| Actualizado | 2023-07-10 10:14 |
| Etiquetas | ninguna |
| Jira | [BULLY-17](https://bluinc.atlassian.net/browse/BULLY-17) |

## Descripción

Según lo estuvimos conversando el calculo de una Media Móvil Simple (SMA) en un gráfico de un activo implica promediar los precios de cierre de dicho activo durante un período de tiempo determinado. 

**¿como se calcula la SMA entonces si fuera para un periodo de 10 dias?**

-  Por ejemplo, si queres calcular la SMA de los últimos 10 días, necesitarás juntar los precios de cierre de esos 10 días.


- Se suman los precios de todos esos días obtenidos antes.


- Se divide la suma total de los precios de cierre entre el número de días en el período. En nuestro ejemplo, dividis la suma por 10.


- El resultado obtenido en el paso anterior será la SMA de 10 días para el activo en cuestión.





**Ejemplo Practico de dos ciclos:**

Supongamos que deseamos calcular la curva SMA de 10 días para un activo utilizando los siguientes precios de cierre:

- Día 1: $10.00 


- Día 2: $11.00 


- Día 3: $12.00 


- Día 4: $11.50 


- Día 5: $10.50 


- Día 6: $11.50 


- Día 7: $12.50 


- Día 8: $13.00 


- Día 9: $12.50 


- Día 10: $11.50



- Se calcula la SMA para el primer punto de la curva (día 10 en este caso):  Se suman los precios de cierre de los últimos 10 días: $10.00 + $11.00 + $12.00 + $11.50 + $10.50 + $11.50 + $12.50 + $13.00 + $12.50 + $11.50 = $126.50 Se divide la suma total por el número de días en el período: $126.50 / 10 = $12.65 

La SMA para el día 10 es $12.65.



- Se calcula la SMA para el segundo punto de la curva (día 9 en este caso): Se elimina el precio de cierre más antiguo ($10.00) y se agrega el precio de cierre más reciente ($12.50). 
se suman los precios de cierre de los últimos 10 días: $11.00 + $12.00 + $11.50 + $10.50 + $11.50 + $12.50 + $13.00 + $12.50 + $11.50 + $12.50 = $120.00 
se divide la suma total por el número de días en el período: $120.00 / 10 = $12.00 

La SMA para el día 9 es $12.00.


- Se repite el paso 2 para cada día restante, eliminando el precio de cierre más antiguo y agregando el precio de cierre más reciente.





Una vez que hayas calculado todos los puntos de la curva SMA, podes dibujarlos en un gráfico con ejes de tiempo y precio. En el eje horizontal (tiempo), se colocan los días correspondientes, y en el eje vertical (precio), se colocan los valores de la SMA calculados para cada día. Conecta los puntos de la curva para obtener la representación visual de la SMA en el gráfico.

Este ejemplo es solo para 10 días, pero puedes aplicar el mismo proceso para cualquier otro período que desees analizar, por eso debe ser una funcion.



# [historia en desarrollo]
