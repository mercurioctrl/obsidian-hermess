---
jira_key: "POS-146"
aliases: ["POS-146"]
summary: "API - Feat - Comprobar finalizacion pendiente / posible"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-09-22 18:03"
updated: "2022-10-18 14:21"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-146"
---

# POS-146: API - Feat - Comprobar finalizacion pendiente / posible

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-09-22 18:03 |
| Actualizado | 2022-10-18 14:21 |
| Etiquetas | ninguna |
| Jira | [POS-146](https://bluinc.atlassian.net/browse/POS-146) |

## Relaciones

- **Padre:** [[POS-21 - Solucion de postventa|POS-21]] Solucion de postventa
- **blocks:** [[POS-147 - API - Feat - Finalizar una postventa|POS-147]] API - Feat - Finalizar una postventa

## Descripcion

Vamos a crear un recurso 

```
GET {API_URL}/v1/isReady/{aftersaleId}/isReady
```

Retorna 

```
{
  isReady:true; //o false
}
```

Se trata un recurso para saber si la postventa se pude finalizar y de este modo mostrar un mensaje, que nos permita realizar la accion con un aviso previo. La logica interna del recurso se reutiliza tambien al momento de confirmar la finalizacion, para verificar que todo este corecto.

Para poder saberlo es necesario primero saber si cada uno de los items que la componen ya se encuentran en su ultimo estado posible () y eso depende de que “solución de postventa” se eligió para cada una.

Imaginemos que pude haber algún caso de este tipo, con mucha diversidad de soluciones.

[adjunto]
Para eso tal vez sea lo mejor definir en un a logica interna (que puede asociarse en la misma tabla de solucionas), cual es el estado inicial de cada “solucion” y de que dependen. Y decir que para que “el todo” `isReady:true;` entonces adentro, todo sea tambien `isReady:true;`.

Para poder decir que toda la postventa devuleva `isReady:true; ` en nuestro recurso, entonces todos los items deberían contestar true a la misma pregunta.

Por defecto, todas las soluciones de postventa menos **No Fallo y Reparado **(siempre isReady:True)** **devuelven `isReady:False` a menos que tengan otra acción realizada que los respalde.

Por el momento tenemos al menos dos lógicas extra, y el resto devuelven todas false.

- **Cambios**: Que para devolver true, necesitan que tenga un pase aceptado relacionado a ese prodcuto y postventa



- **Crédito**: Que para devolver true, necesitan tener asociado un credito al producto y postventa que hacen referencia.
