---
jira_key: "PED-31"
aliases: ["PED-31"]
summary: "API - Feat - Crear direccion cliente"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-08-16 08:37"
updated: "2023-08-16 14:39"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-31"
---

# PED-31: API - Feat - Crear direccion cliente

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-08-16 08:37 |
| Actualizado | 2023-08-16 14:39 |
| Etiquetas | ninguna |
| Jira | [PED-31](https://bluinc.atlassian.net/browse/PED-31) |

## Relaciones

- **Padre:** [[PED-16 - Listar clientes|PED-16]] Listar clientes

## Descripcion

```
POST {{API_URL}}/v1/shippingAddress/{clientId}
```

```
  {
        "address": "Messi 2022",
        "localityId": "0001",
        "provinceId":  2,
        "postalCode": "1439",
        "telephone": "1123223222"
  }
```

Retorna

```
{
  succes:true
}
```
