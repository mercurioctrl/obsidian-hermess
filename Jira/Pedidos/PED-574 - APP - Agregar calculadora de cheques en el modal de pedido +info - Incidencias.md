---
jira_key: "PED-574"
aliases: ["PED-574"]
summary: "APP - Agregar calculadora de cheques en el modal de pedido +info - Incidencias varias"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Guillermo Avila"
created: "2024-02-26 23:36"
updated: "2024-03-10 21:52"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-574"
---

# PED-574: APP - Agregar calculadora de cheques en el modal de pedido +info - Incidencias varias

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Guillermo Avila |
| Creado | 2024-02-26 23:36 |
| Actualizado | 2024-03-10 21:52 |
| Etiquetas | ninguna |
| Jira | [PED-574](https://bluinc.atlassian.net/browse/PED-574) |

## Relaciones

- **Padre:** [[PED-3 - Ordenes de compra|PED-3]] Ordenes de compra
- **blocks:** [[PED-570 - APP - Feat - Agregar calculadora de cheques en el modal de pedido +i nfo|PED-570]] APP -  Feat -  Agregar calculadora de cheques en el modal de pedido +i nfo

## Descripcion

No me permite cargar un cheque con un monto igual al del total final del pedido

[adjunto]
Datos extras:

```
Información del pedido: 0002 - 10332511
Cliente: 80591 - Gprueba Ricardo Salinas
Vendedor: Sistema Web
Cotización: $ 800,00

5 - TECLADO GAMER EVGA Z15 SP RGB LINEAR SILVER | 10.5% | $ 73,10 | 365,48 
20 - TECLADO MEC AUREOX UNRIVAILED GAMING GK600 | 10.5% | $ 38,80 | 775,93 
293 - MOUSE PAD GAMING GENIUS 800S | 21% | $ 13,81 | 4.045,05 

Total SIN IVA: u$s 5.186,46 | $ 4.149.167,42
Total Final:      u$s 6.155,77 | $ 4.924.614,41

Pago con cheque 

 Días | Cotización | Interes |                  Total SIN IVA|                  Total Final 
    05 | $     811,60 | $   1,45 | $               4.209.330,34 | $              4.996.021,32 
    10 | $     823,20 | $   2,90 | $               4.269.493,27 | $              5.067.428,22 
    15 | $     834,80 | $   4,35 | $               4.329.656,20 | $              5.138.835,13 
    20 | $     846,40 | $   5,80 | $               4.389.819,13 | $              5.210.242,04 
    25 | $     858,00 | $   7,25 | $               4.449.982,05 | $              5.281.648,95 
    30 | $     869,60 | $   8,70 | $               4.510.144,98 | $              5.353.055,86 
    35 | $     881,20 | $ 10,15 | $               4.570.307,91 | $              5.424.462,77 
    40 | $     892,80 | $ 11,60 | $               4.630.470,84 | $              5.495.869,68 
    45 | $     904,40 | $ 13,05 | $               4.690.633,76 | $              5.567.276,59 
```

---

Actualización 02/03/24
No me permite cargar el cheque ingresando el monto total final

[adjunto]
