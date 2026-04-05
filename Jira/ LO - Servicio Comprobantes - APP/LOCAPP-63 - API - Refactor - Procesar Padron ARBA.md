---
jira_key: "LOCAPP-63"
aliases: ["LOCAPP-63"]
summary: "API - Refactor - Procesar Padron ARBA"
status: "Finalizada"
type: "Subtarea"
priority: "Lowest"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-04-21 14:01"
updated: "2025-05-01 18:54"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LOCAPP-63"
---

# LOCAPP-63: API - Refactor - Procesar Padron ARBA

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Lowest |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-04-21 14:01 |
| Actualizado | 2025-05-01 18:54 |
| Etiquetas | ninguna |
| Jira | [LOCAPP-63](https://bluinc.atlassian.net/browse/LOCAPP-63) |

## Relaciones

- **Padre:** [[LOCAPP-62 - Descarga y procesamiento de padrones|LOCAPP-62]] Descarga y procesamiento de padrones
- **relates to:** [[LOCAPP-65 - API - Procesar Padron ARBA - Propuesta de mejora en la autenticación|LOCAPP-65]] API - Procesar Padron ARBA - Propuesta de mejora en la autenticación

## Descripcion

Crearemos un recurso que sirve para procesar los archivos que nos entrega ARBA para saber que percepción debemos cobrarle a cada uno de nuestros clientes y guardarlo en nuestra tabla de clientes para tenerlo mas a la mano.

Estos archivos se procesan una sola vez cuando arranca el mes, ya que suelen ser costosos de procesar y se guardan en la base de datos para cada cliente de modo tal que podamos hacer cálculos y utilizar la alícuota de una mejor manera.

```
POST {{API_URL}}/v2/padron/process/arba
```

### Funcionalidad Esperada

- **Lectura de archivo:**

- Leer línea por línea el archivo `.txt` con registros `P;...` (separados por `;`).


- Extraer: CUIT, fecha vigencia desde, fecha vigencia hasta, alícuota de percepción.




- **Condiciones para considerar un registro válido:**

- Tipo de línea: `P`


- No debe estar marcado como excluido (`N`) ni exento (`N`)


- Se aceptan alícuotas `> 0` 


- Solo sirve si existe el CUIT en nuestra base de datos (Buscar solo aquellos con CUIT para hacer mas rápido) `NewBytes_DBF.dbo.clientes.cdnicif`




- **Comparación de fechas:**

- Si el cliente **no tiene percepción vigente** (`NewBytes_DBF.dbo.clientes`.`percepcion_vencimiento_arba IS NULL`) o **la nueva fecha es más reciente**




- **Actualización de base:**

- Si todo esto se cumple guardamos en `NewBytes_DBF.dbo.clientes.percepcion_arba`





Esto si queres andalo mirando, pero es para charlar antes y no es prioritario
