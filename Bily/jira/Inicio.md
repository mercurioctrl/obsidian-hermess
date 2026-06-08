# Jira — Tickets sincronizados

Notas de tickets Jira autopobladas por el vault sync de la integración Bily↔Jira.
709 tickets de 24 proyectos. Cada nota tiene frontmatter estructurado (`jira_key`, `status`, `assignee`, `sprint`).

Ver arquitectura completa en [[Bily/proyectos/Integracion-Jira/Inicio|Integración Jira]].

## Proyectos

| Proyecto | Tickets |
|---|---|
| ADATA | 119 |
| NBE | 87 |
| LIO | 83 |
| LOMKT | 60 |
| REDESYNEWS | 47 |
| MNB2 | 44 |
| SNB | 41 |
| DNYL | 29 |
| LOCAPP | 27 |
| PED | 26 |
| BLUWEB | 24 |
| LAW | 21 |
| FB | 15 |
| COB | 15 |
| INV | 14 |
| PEGA | 13 |
| NBWEB | 12 |
| MKT | 11 |
| EXP | 8 |
| NAEV | 4 |
| COM | 4 |
| STASK | 2 |
| M1 | 2 |
| POS | 1 |

## Uso

- Linkear desde cualquier nota con `[[Bily/jira/KEY|KEY]]` (ej: `[[Bily/jira/EXP-553|EXP-553]]`)
- Buscar con `vault-search "EXP-553"` o por campos frontmatter
- Actualizar con `sync_all.py` (ver [[Bily/proyectos/Integracion-Jira/Inicio|Integración Jira F4/F6]])

## Ver también

- [[Bily/proyectos/Integracion-Jira/Inicio|Integración Jira]] — arquitectura y roadmap
- [[Bily/proyectos/Integracion-Jira/estado|Estado vivo]] — componentes corriendo
- [[Bily/Inicio|Inicio de Bily]]
