---
jira_key: "NBWEB-470"
summary: "Refactor - Procesar carrito - Producteca"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-08-22 15:19"
updated: "2022-08-23 14:33"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-470"
---

# NBWEB-470: Refactor - Procesar carrito - Producteca

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-08-22 15:19 |
| Actualizado | 2022-08-23 14:33 |
| Etiquetas | ninguna |
| Jira | [NBWEB-470](https://bluinc.atlassian.net/browse/NBWEB-470) |

## Descripción

```
POST https://api.nb.com.ar/v1/carrito/process
```

A la request que ya existe

```

--form 'codigoPostalFavorito="1438"' \
--form 'mediodeEnvioId="4065"' \
--form 'medioDePagoId="3"' \
--form 'idDirCli="11011"'
```

Se agrega un parámetro opcional

```
[
  {
  "salePrice": 122.34,
  "id": 108613
  },
  {
  "salePrice": 3122.34,
  "id": 108345
  }
]
```

En caso de estar, se guarda en una columna nueva en `NewBytes_DBF.dbo.pedclil` llamada `salePrice` que puede ser null
