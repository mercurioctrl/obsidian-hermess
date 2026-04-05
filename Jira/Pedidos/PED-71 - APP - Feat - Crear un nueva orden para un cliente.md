---
jira_key: "PED-71"
aliases: ["PED-71"]
summary: "APP - Feat - Crear un nueva orden para un cliente"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-09-14 09:55"
updated: "2023-09-27 10:09"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-71"
---

# PED-71: APP - Feat - Crear un nueva orden para un cliente

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-09-14 09:55 |
| Actualizado | 2023-09-27 10:09 |
| Etiquetas | ninguna |
| Jira | [PED-71](https://bluinc.atlassian.net/browse/PED-71) |

## Relaciones

- **Padre:** [[PED-34]] Generar / Editar ordenes
- **is blocked by:** [[PED-35]] API - Feat - Crear nueva orden para un cliente
- **is blocked by:** [[PED-16]] Listar clientes

## Descripcion

Agregaremos un accionable en el mismo nivel del botón “mostrar” con la leyenda “Nuevo Pedido” que abrirá un modal con el siguiente formulario

- Cliente → Es un input de texto basado en [link](https://lioteam.atlassian.net/browse/PED-16)  que al escribir 3 o mas letras o bien el numero de cliente, me sugiere para elegir aquellos que matchean.


- Sucursal (Por ahora solo muestra:  ‘Sucursal 2', ‘Sucursal 10' y 'Presupuesto’)



Una vez que tengamos la informacion, entonces procesamos con 

```
POST {API_URL}/v1/orders
```

```
[
  {
    clientId: 23452
    branch: '0002'
  }
]
```

Segun [https://lioteam.atlassian.net/browse/PED-16](https://lioteam.atlassian.net/browse/PED-16)
