---
jira_key: "NBWEB-173"
summary: "MS - Envios - Feature para aplazar fecha de entrega"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-05-10 09:02"
updated: "2022-07-01 17:40"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-173"
---

# NBWEB-173: MS - Envios - Feature para aplazar fecha de entrega

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-05-10 09:02 |
| Actualizado | 2022-07-01 17:40 |
| Etiquetas | ninguna |
| Jira | [NBWEB-173](https://bluinc.atlassian.net/browse/NBWEB-173) |

## Descripción

Se debe poder aplazar los días de entrega para los recursos citados a continuación 

Estaba pensando en hacer algo como los ejemplos de mas abajo, pero escucho mejores soluciones en caso de que se les ocurran



```
{{API_URL}}/pedido/414798/cp/1426/cphost/1407/delay/24
```

```
{{API_URL}}/item/298425/cp/1227/cphost/1429/delay/24
```

```
{{API_URL}}/cart/nb/8004029/cp/1439/delay/24
```

```
{{API_URL}}/bulk/size/15x15x15/weight/3.68/cp/7600/delay/24
```

Los recursos sin el delay, deben funcionar igual que antes. Para todos los tipos de rutas.

Escucho sugerencias o oportunidades de mejora si las tienen
