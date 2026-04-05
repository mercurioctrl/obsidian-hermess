---
jira_key: "LAW-43"
aliases: ["LAW-43"]
summary: "Onboarding producción"
status: "En curso"
type: "Epic"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2026-02-23 06:47"
updated: "2026-02-26 09:22"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LAW-43"
---

# LAW-43: Onboarding producción

| Campo | Valor |
|-------|-------|
| Estado | En curso (En curso) |
| Tipo | Epic |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2026-02-23 06:47 |
| Actualizado | 2026-02-26 09:22 |
| Etiquetas | ninguna |
| Jira | [LAW-43](https://bluinc.atlassian.net/browse/LAW-43) |

## Relaciones

*Sin relaciones*

## Descripcion

Leelo tranquila a ver que te parece, la idea es marcar hoy ya los días por calendario ordenados de esta manera, la idea es que puedan llevar adelante todo el procesos ustedes con Eze, durante 5 días mas o menos y que yo solo intervenga frente a algún problema concreto si es necesario o para dirimir alguna cuestión. 

## Cómo lo encararía yo 

La idea no es “probar pantallas sueltas”, sino **probar el circuito real de trabajo** del cliente, por partes, con orden.

Como hay que validar refactorizaciones, lo mejor es armar una semana de pruebas con:

- **reunión corta por día**


- **un tema claro por día**


- **anotación prolija de todo lo que falle / haya que ajustar**


- **cierre con prioridades**



Así no se mezcla todo, no se pierde info y no terminas con 40 cosas anotadas en slack, o en un archivo suelto. Para eso vamos a usar Historias por reunion, y subtareas dentro de ellas, en este mismo EPIC.

---

## Metodología de trabajo (simple y prolija)

### 1) Reuniones cortas, con foco

Cada reunión tiene que tener un objetivo concreto.
Ejemplo: “hoy probamos pedidos”, “hoy probamos cobranzas”, etc.

No mezclar mil temas porque se desordena y después no sabés qué falta, o hay mucho “ida y vuelta” sin saber que hacer.

---

### 2) Estructura fija para cada reunión (siempre igual)

Yo haría esto:

### **A. Inicio (5 min aprox)**

- Qué vamos a probar hoy


- Qué quedó pendiente del día anterior


- Si hubo algún fix que entró para volver a probar



### **B. Prueba guiada (30 min aprox)**

- Vos guiás el flujo principal


- El cliente prueba casos reales de su operatoria


- Todo lo que aparezca se anota (sin ponerse a debuggear en vivo)



### **C. Cierre (10-15 min aprox)**

- Clasifican lo encontrado


- Definen qué es bug, qué es mejora, qué es duda funcional


- Priorizan


- Se deja claro qué se prueba mañana



---

## Cómo tomar nota (clave)

No anotar todo como “error”. Separarlo así:

### Tipos de hallazgos

- **Bug** → algo no funciona


- **Regresión** → antes andaba y se rompió


- **Mejora** → funciona pero hay que ajustarlo


- **Duda funcional** → hay que definir criterio con el cliente


- **Cambio de alcance** → el cliente pide algo nuevo (esto hay que marcarlo bien y seguro lo pateamos a una instancia posterior)



### Prioridad

- **Alta** → bloquea operación


- **Media** → se puede seguir, pero molesta o confunde


- **Baja** → detalle / cosmético / mejora menor



---

## Regla importante (para evitar quilombo)

Cada hallazgo tiene que quedar con:

- dónde pasó (módulo/pantalla)


- qué hizo el cliente


- qué esperaba


- qué pasó realmente


- evidencia (captura, video, pedido, algo que no sea todo el texto que puede ser ambiguo o poco descriptivo días despues.)



Si no, después nadie se acuerda y se pierde tiempo.

---

## Orden para probar durante la semana

Yo lo ordenaría así, porque tiene lógica operativa y evita contaminar pruebas:

### **DÍA 1 – Base / Datos**

Primero asegurarse de que lo base esté bien:

- productos


- stock


- categorías


- marcas


- depósitos


- lo mínimo de compras si impacta stock



---

### **DÍA 2 – Pedidos (core del negocio)**

Acá probás el circuito principal:

- crear pedido


- agregar productos


- validar stock


- cambiar estados


- liquidar



Y al menos:

- 1 caso normal (happy path)


- 1 caso con excepción (edición, cancelación, algo fuera de lo ideal)



---

### **DÍA 3 – Cobranzas**

Con pedidos ya probados, ves si lo cobrado está bien:

- que aparezca lo que se liquidó


- gestión de cobro


- estados


- medios de pago relevantes



Acá es clave validar que lo que sale de pedidos entra bien en cobranzas según el criterio de naty.

---

### **DÍA 4 – Expedición / Logística**

Probás toda la parte de despacho:

- preparación


- envío


- tracking


- estados logísticos


- impacto en stock (si aplica en el flujo visible)



La idea es validar la continuidad desde pedido hacia entrega.

---

### **DÍA 5 – Postventa + re-test de pendientes (esto es lo menos importante al menos al principio)**

Último día:

- probás postventa (garantías, devoluciones, etc.)


- y dejás una parte del día para **retestear fixes** de lo que fue saliendo en la semana



Esto es clave, porque si no todo queda “pendiente” y nunca se cierra nada.

---

## Criterio de trabajo para que no se vaya de tema

Te diría estas reglas, simples pero efectivas:

- **Un tema por reunión**


- **No resolver en vivo**


- **Todo se anota con evidencia**


- **Todo se clasifica (bug / mejora / duda / alcance)**


- **Todos los días se cierra con prioridades**


- **Viernes se usa también para re-test, no solo para probar algo nuevo**



---

## Cómo se lo diría a las chicas (mas o menos)

“Vamos a avanzar esta semana con una validación ordenada por áreas.
Cada día vamos a revisar un bloque puntual del sistema, probar flujos reales de trabajo y registrar cualquier ajuste o falla detectada.
La idea es separar bien lo que es bug, mejora o definición funcional, para priorizar y corregir rápido.
El viernes cerramos con postventa y una ronda de re-test de los puntos críticos que hayan surgido.”

---

Si somos ordenados con el mecanismo hasta se puede generar un documento automático para cada uno de los 5 días
