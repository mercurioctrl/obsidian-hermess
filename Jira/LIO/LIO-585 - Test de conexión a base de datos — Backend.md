---
jira_key: "LIO-585"
aliases: ["LIO-585"]
summary: "Test de conexión a base de datos — Backend"
status: "En curso"
type: "Tarea"
priority: "Medium"
assignee: "Guillermo Avila"
reporter: "Catriel Mercurio"
created: "2026-03-27 10:16"
updated: "2026-03-31 10:33"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-585"
---

# LIO-585: Test de conexión a base de datos — Backend

| Campo | Valor |
|-------|-------|
| Estado | En curso (En curso) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Guillermo Avila |
| Reportado por | Catriel Mercurio |
| Creado | 2026-03-27 10:16 |
| Actualizado | 2026-03-31 10:33 |
| Etiquetas | ninguna |
| Jira | [LIO-585](https://bluinc.atlassian.net/browse/LIO-585) |

## Relaciones

- **Padre:** [[LIO-584 - Testing|LIO-584]] Testing

## Descripcion

Como equipo de desarrollo, quiero tener un test que verifique que la conexión a SQL Server funciona correctamente desde el entorno de tests, para saber que el resto de los tests unitarios tiene una base válida sobre la que trabajar.

> **Este es el primer test que hay que correr.** Si falla, no tiene sentido ejecutar ningún otro. Un error aquí significa un problema de configuración del entorno (credenciales, red, contenedor), no un bug en el código.


---

## Contexto

El proyecto usa SQL Server remoto (`DB_CONNECTION=sqlsrv`). La conexión **no es local ni usa SQLite** — apunta a un servidor real. El entorno de testing hereda la misma configuración de `DB_*` del `.env`.

A diferencia de los otros tests unitarios (que mockean la DB con `DB::shouldReceive`), este test **sí toca la base de datos real** de forma intencional. Su único propósito es confirmar que la conexión existe y que se puede ejecutar una query mínima.

---

## Cambios requeridos

### 1. Test — `DatabaseConnectionTest.php`

**Archivo:** `tests/Feature/DatabaseConnectionTest.php` *(archivo nuevo)*

```
<?php
​
namespace Tests\Feature;
​
use Tests\TestCase;
use Illuminate\Support\Facades\DB;
​
class DatabaseConnectionTest extends TestCase
{
    /** @test */
    public function can_connect_to_the_database(): void
    {
        // Intenta obtener la conexión PDO activa.
        // Lanza excepción si no puede conectar.
        $pdo = DB::connection()->getPdo();
​
        $this->assertNotNull($pdo);
    }
​
    /** @test */
    public function can_execute_a_simple_query(): void
    {
        // SELECT 1 funciona en SQL Server y no depende de ninguna tabla del negocio.
        $result = DB::select('SELECT 1 AS value');
​
        $this->assertNotEmpty($result);
        $this->assertSame(1, (int) $result[0]->value);
    }
​
    /** @test */
    public function connected_to_the_correct_driver(): void
    {
        $driver = DB::connection()->getDriverName();
​
        $this->assertSame('sqlsrv', $driver);
    }
}
```

---

## Comando para correr el test

```
docker exec sitio-api-rest-4.1-laravel php /var/www/app/vendor/bin/phpunit --filter DatabaseConnectionTest
```

---

## Qué significa cada resultado

| Resultado | Causa probable |
| --- | --- |
| ✅ Los 3 tests pasan | Conexión OK. Se puede continuar con los tests unitarios. |
| ❌ `can_connect_to_the_database` falla | Credenciales incorrectas, servidor inaccesible, o driver `sqlsrv` no instalado en el contenedor. |
| ❌ `can_execute_a_simple_query` falla | La conexión abre pero no puede ejecutar queries. Puede ser un problema de permisos del usuario de DB. |
| ❌ `connected_to_the_correct_driver` falla | El `.env` de testing no está apuntando a `sqlsrv`. Verificar `DB_CONNECTION` en `.env` y en `phpunit.xml`. |

---

## Qué hacer si falla

- Verificar que el contenedor está corriendo: `docker ps | grep sitio-api-rest`


- Verificar variables de entorno dentro del contenedor:

```
docker exec sitio-api-rest-4.1-laravel php /var/www/app/artisan tinker
>>> DB::connection()->getPdo();
```


- Verificar que el driver `sqlsrv` está instalado:

```
docker exec sitio-api-rest-4.1-laravel php -m | grep sqlsrv
```


- Revisar `phpunit.xml` — si tiene algún `<env name="DB_*">` que sobreescriba las credenciales reales.



---

## Criterios de aceptación

- `can_connect_to_the_database`: devuelve una instancia PDO no nula


- `can_execute_a_simple_query`: `SELECT 1` devuelve `value=1`


- `connected_to_the_correct_driver`: el driver activo es `sqlsrv`


- El test corre desde dentro del contenedor Docker


- Si alguno de los 3 falla, se detiene el trabajo de tests hasta resolver el problema de entorno



---

## Notas técnicas

- Este es el único test del proyecto que **no mockea la DB** de forma intencional.


- No escribe ni modifica datos — solo lee con `SELECT 1`.


- Si en el futuro se quiere un entorno de CI sin acceso a la DB real, este test se puede marcar con `@group integration` y excluirlo del pipeline con `--exclude-group integration`.


- El `phpunit.xml` actual no sobreescribe `DB_*`, pero conviene confirmarlo antes de correr.
