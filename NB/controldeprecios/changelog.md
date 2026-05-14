# Changelog — Control de Precios

## 2026-05-13

- feat: Agregado permiso `unlockedLoPriceModify` en `[NB_WEB].dbo.permisos_agente`
  - `procesar/cambiarUtilidad.php`: bloquea modificación de LO2 si el agente no tiene el permiso (devuelve JSON error al JS)
  - `procesar/cambiarTodo.php`: saltea el bloque LO2 masivo si el agente no tiene el permiso
  - LO1 no fue restringido (decisión del usuario)
- fix: `acces/functions.php` — ya existía `unlockedLoPrice` para ocultar columnas LO2/LOP/LIBRE_OPCION a nivel visual (`columnas.php`)

Archivos modificados: `procesar/cambiarUtilidad.php`, `procesar/cambiarTodo.php`

---

## Ver también
- [[NB/controldeprecios/controldeprecios|Control de Precios]]
- [[NB/controldeprecios/contexto|Contexto]]
