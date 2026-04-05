---
jira_key: "PED-752"
aliases: ["PED-752"]
summary: "DATA - Agregar grupos a los clientes en tabla cliente de DEV y PROD"
status: "Finalizada"
type: "Subtarea"
priority: "High"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-06-26 09:22"
updated: "2024-06-27 16:37"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-752"
---

# PED-752: DATA - Agregar grupos a los clientes en tabla cliente de DEV y PROD

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | High |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-06-26 09:22 |
| Actualizado | 2024-06-27 16:37 |
| Etiquetas | ninguna |
| Jira | [PED-752](https://bluinc.atlassian.net/browse/PED-752) |

## Relaciones

- **Padre:** [[PED-748]] Incentivo 25 años
- **blocks:** [[NBWEB-756]] API - Feat - Agregar al objeto "user" el grupo al que pertenece el ususariuo
- **is blocked by:** [[PED-757]]  DATA - Agregar grupos de ranking a los clientes - Cliente repetido

## Descripcion

Basándonos en este este esquema [link](https://docs.google.com/spreadsheets/d/1UH6KLY0hBH_WxXXgIs0-lgeYLP2bSM4DagdHzcPuoFg/edit?gid=0#gid=0)  marcaremos los distintos grupos en la tabla `[NewBytes_DBF].[dbo].[clientes]`

**Grupo A**

```
SELECT [ccodcli], [cnomcli], [cnomcom]
FROM [NewBytes_DBF].[dbo].[clientes]
WHERE [cnomcli] IN ('SEGAL GABRIEL ALEJANDRO', 'GRUPO MAXIMUS S.R.L.', 'CIUDAD DE JUEGOS S. R. L.', 'COMPUFAN SRL', 'DAMARFU SA', 'DIAMOND SYSTEM S.A.', 'GRUPOS INTEGRADOS S.A.', 'VENEX S.A.', 'OVERDRIVE S.A', 'GEZATEK S.R.L.', 'GHERTNER MATIAS / SEBASTIAN', 'RETEC CONSORCIO DE COOPERACION EMPRESARIA', 'ARMY TECHNOLOGIES SA', 'DIAZ ADRIANA MARIEL', 'GRUPO MEXX S.R.L', 'MAS TECNOLOGIA S.R.L. / GRUPO MASTEC S.R.L.', 'CHOQUE MAXIMILIANO JOEL', 'JFC HACELA FACIL SRL')
OR [cnomcom] IN ('SEGAL GABRIEL ALEJANDRO', 'GRUPO MAXIMUS S.R.L.', 'CIUDAD DE JUEGOS S. R. L.', 'COMPUFAN SRL', 'DAMARFU SA', 'DIAMOND SYSTEM S.A.', 'GRUPOS INTEGRADOS S.A.', 'VENEX S.A.', 'OVERDRIVE S.A', 'GEZATEK S.R.L.', 'GHERTNER MATIAS / SEBASTIAN', 'RETEC CONSORCIO DE COOPERACION EMPRESARIA', 'ARMY TECHNOLOGIES SA', 'DIAZ ADRIANA MARIEL', 'GRUPO MEXX S.R.L', 'MAS TECNOLOGIA S.R.L. / GRUPO MASTEC S.R.L.', 'CHOQUE MAXIMILIANO JOEL', 'JFC HACELA FACIL SRL');
```

**Grupo B**

```
SELECT [ccodcli], [cnomcli], [cnomcom]
FROM [NewBytes_DBF].[dbo].[clientes]
WHERE [cnomcli] IN ('NOXIESTORE S.A.', 'URANO STREAM S.A.', 'Franquimar S.A.', 'NUNEZ MARIA ALEJANDRA', 'SCHLEGEL PABLO IGNACIO', 'RISTOFF ALBERTO ANTONIO ELIAS', 'Jac Tecnologia SRL', 'SMART COMMERCE S.A.', 'CANONICO MARIO JUAN Y CANONICO NELSON ARIEL', 'MARSRO GAMING S.R.L', 'SCP HARDSTORE SRL', 'CAPISTO HERNAN', 'COMPUGARDEN S.R.L.', 'TOBARES LEANDRO AGUSTIN', 'DE BENEDETTI LARA MARINA', 'GORILA GAMES S.A.S. / OLD GAMES S.A.S.', 'GUTIERREZ - CIPOLAT SOCIEDAD LEY Nº 19550 CAPITULO I SECCION IV', 'GOLDIN DAVID L. Y LOPEZ ALCOBA PABLO A. SH', 'THE KING OF TECHNOLOGY', 'ITERBIO SAS', 'PEREZ NAHUEL')
OR [cnomcom] IN ('NOXIESTORE S.A.', 'URANO STREAM S.A.', 'Franquimar S.A.', 'NUNEZ MARIA ALEJANDRA', 'SCHLEGEL PABLO IGNACIO', 'RISTOFF ALBERTO ANTONIO ELIAS', 'Jac Tecnologia SRL', 'SMART COMMERCE S.A.', 'CANONICO MARIO JUAN Y CANONICO NELSON ARIEL', 'MARSRO GAMING S.R.L', 'SCP HARDSTORE SRL', 'CAPISTO HERNAN', 'COMPUGARDEN S.R.L.', 'TOBARES LEANDRO AGUSTIN', 'DE BENEDETTI LARA MARINA', 'GORILA GAMES S.A.S. / OLD GAMES S.A.S.', 'GUTIERREZ - CIPOLAT SOCIEDAD LEY Nº 19550 CAPITULO I SECCION IV', 'GOLDIN DAVID L. Y LOPEZ ALCOBA PABLO A. SH', 'THE KING OF TECHNOLOGY', 'ITERBIO SAS', 'PEREZ NAHUEL');

```

**Grupo C**

```
Todos los demas
```

Revisar el grupo A y B tienen la cantidad correcta segun la grilla para asegurarnos que no falta ninguno comprador
