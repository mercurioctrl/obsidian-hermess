---
jira_key: "PEGA-187"
summary: "API - O. Mejora - Siempre que devuelvo el nombre de un producto para formular un enlace, debo retirar los caracteres incompatibles"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-05-20 14:31"
updated: "2025-06-04 11:03"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-187"
---

# PEGA-187: API - O. Mejora - Siempre que devuelvo el nombre de un producto para formular un enlace, debo retirar los caracteres incompatibles

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-05-20 14:31 |
| Actualizado | 2025-06-04 11:03 |
| Etiquetas | ninguna |
| Jira | [PEGA-187](https://bluinc.atlassian.net/browse/PEGA-187) |

## Descripción

Varios veces vienen por parte de los resellers productos que tienen en su descripcion caracteres incompatiles con url, lo que produce un fallo al enlazarlos directamente.

Ejemplo:

[https://preciosgamer.com/disco_solido_ssd_m.2_team_1tb_mp33_pro_3400mb/s_nvme_pci-e_gen3_x4_-_128715](https://preciosgamer.com/disco_solido_ssd_m.2_team_1tb_mp33_pro_3400mb/s_nvme_pci-e_gen3_x4_-_128715)

Se puede sanitizar usando slug o similares en laravel
