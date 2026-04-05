---
jira_key: "PED-1190"
aliases: ["PED-1190"]
summary: "API - Refactor - Cálculo de precios de ítems internos de un kit (prorrateo por costo manteniendo iva del kit)"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-12-15 06:47"
updated: "2025-12-22 20:33"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1190"
---

# PED-1190: API - Refactor - Cálculo de precios de ítems internos de un kit (prorrateo por costo manteniendo iva del kit)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-12-15 06:47 |
| Actualizado | 2025-12-22 20:33 |
| Etiquetas | ninguna |
| Jira | [PED-1190](https://bluinc.atlassian.net/browse/PED-1190) |

## Relaciones

- **Padre:** [[PED-1170]] Kits

## Descripcion

Refactorizaremos el recurso para que **solo cuando estemos introduciendo un kit (dado el costo de hacer el cálculo cada vez)**, obtendremos de manera dinámica el precio para cada uno de los componentes. Esto puede hacerse dentro de los métodos de precio o no según este construido. 

```
PATCH /v1/orders/addItem
```

Para poder registrar correctamente las líneas internas del kit dentro de `NewBytes_DBF.dbo.pedclil` (cantidad, precio e IVA por fila), es necesario **descomponer el precio del kit en sus ítems**, garantizando que:

- la suma de los precios sin IVA de los ítems coincida con el precio sin IVA del kit


- la suma del IVA de los ítems coincida con el IVA total del kit


- la suma de los precios finales de los ítems coincida con el precio final del kit



Dentro del kit, el IVA aplicado a los ítems **es el IVA del kit**, independientemente del IVA real que tenga el producto cuando se vende por separado.

---

### Datos de entrada

**A nivel kit**

- `kitNetPrice`: precio del kit sin IVA (valor fijo)


- `kitVatRate`: IVA del kit (ej: 10,5% → `0.105`)



**A nivel ítem del kit**

- `quantity`: cantidad del ítem dentro del kit


- `unitCost`: costo unitario sin IVA del ítem
*(se utiliza únicamente como base para repartir el precio proporcionalmente)*



---

### Lógica de cálculo

#### 1. Calcular peso proporcional por ítem

```
itemWeight = quantity * unitCost
```

```
totalWeight = sum(itemWeight)
```

---

#### 2. Calcular precio sin IVA de la línea del ítem

El precio sin IVA de cada línea se asigna de forma proporcional a su peso:

```
itemNetTotal = kitNetPrice * (itemWeight / totalWeight)
```

Este valor representa **el precio sin IVA de toda la línea**, no el unitario.

---

#### 3. Calcular precio unitario sin IVA

```
itemNetUnitPrice = itemNetTotal / quantity
```

---

#### 4. Calcular IVA y precio final por línea

Se aplica **siempre el IVA del kit**:

```
itemVatAmount = itemNetTotal * kitVatRate
```

```
itemTotalWithVat = itemNetTotal + itemVatAmount
```

---

### Propiedades que deben cumplirse

```
sum(itemNetTotal)      = kitNetPrice
sum(itemVatAmount)     = kitNetPrice * kitVatRate
sum(itemTotalWithVat)  = kitNetPrice * (1 + kitVatRate)
```

---

### Reglas importantes de implementación

- El `unitCost` **no define el precio final**, solo el peso relativo del ítem dentro del kit.


- El IVA real del producto **no se utiliza** en la descomposición del kit.


- Todos los ítems internos del kit utilizan `kitVatRate`.


- Los valores deben persistirse redondeados a **2 decimales**.


- Si por redondeo la suma no coincide exactamente:

- ajustar los centavos en una línea (preferentemente la de mayor importe) para forzar el cierre exacto (ojo con esto, puede ajsutarse posteriormente en una linea del codigo para que de perfecto)





---

### Resultado esperado

Cada kit queda correctamente descompuesto en sus ítems internos, manteniendo consistencia matemática y permitiendo registrar líneas con cantidad, precio e IVA sin romper el total del kit.

---
