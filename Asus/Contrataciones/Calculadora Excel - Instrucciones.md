# Calculadora Excel - Instrucciones

## Archivo

`Calculadora_Costos_Comercio.xlsx` — Hoja única "Calculadora" con 50 fórmulas interconectadas.

## Cómo usarla

Todas las **celdas amarillas** son editables. El resto se calcula automáticamente.

### Celdas de entrada principales

| Celda | Concepto | Valor default |
|-------|----------|---------------|
| **C5** | Salario neto deseado (en mano) | $2.200.000 |
| C8 | Básico Vendedor B | $1.094.044 |
| C9 | Suma Fija NR | $40.000 |
| C10 | Recomposición NR | $60.000 |
| C11 | Presentismo (%) | 8,33% |
| **C12** | Años de antigüedad | 1 |
| C13 | Antigüedad (% por año) | 1,0% |

### Celdas de aportes y contribuciones

| Celda | Concepto | Valor default |
|-------|----------|---------------|
| C16 | Jubilación | 11% |
| C17 | PAMI | 3% |
| C18 | Obra Social | 3% |
| C19 | Art. 100 (cuota solidaria) | 2% |
| **C24** | SUSS patronal (MiPyME) | 18% |
| C25 | Obra Social patronal | 6% |
| **C26** | ART | 3% |

### Celdas de coeficientes

| Celda | Concepto | Valor default |
|-------|----------|---------------|
| **C31** | Coeficiente Remunerativo | 1,57 |
| **C32** | Coeficiente No Remunerativo | 1,30 |
| C33 | IVA | 21% |

## Sección de resultados (columnas E-I)

La parte derecha de la hoja muestra:

1. **Desglose de liquidación**: cada ítem del recibo con su importe, coeficiente aplicado y cargo al cliente
2. **Resumen para el cliente**: las 4 cifras clave (salario en mano, gasto agencia, fee, total cliente)
3. **Verificaciones**: filas que confirman la consistencia del modelo

## Casos de uso comunes

### Simular otro monto neto
Cambiar **C5** y todo se recalcula.

### Empleado con más antigüedad
Cambiar **C12** (años). El básico no cambia, pero sube la antigüedad y baja el "A Cuenta".

### Actualizaciones paritarias
Cuando cambie el básico, actualizar **C8**. Si cambian los NR, actualizar C9 y C10.

### Empresa NO MiPyME
Cambiar **C24** de 18% a 20,40%. El coeficiente 1,57 ya no será suficiente para cubrir contribuciones + el mismo fee (habría que subirlo a ~1,594 para mantener 30% de fee).

### Cambiar el fee de la agencia
Ajustar **C31** y/o **C32**. El fee implícito se muestra en las celdas C35 y C36 como referencia.

## Estructura interna

```
Columnas B-C: Inputs (parámetros editables)
Columnas E-I: Resultados (todo calculado con fórmulas)
  - E: Concepto
  - F: Tipo (R o NR)
  - G: Importe
  - H: Coeficiente
  - I: Cargo al cliente (= G × H)
```

La fórmula más importante es la del **A Cuenta Futuros Aumentos** (celda G11), que se reverse-engineerea a partir del neto deseado. Ver [[Fórmulas del Modelo]] para la derivación completa.

---

Ver también: [[Coeficientes de Facturación]] | [[Escenarios de Contratación]]

#contrataciones #excel #calculadora #herramientas
