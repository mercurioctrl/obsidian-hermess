---
jira_key: "PED-151"
aliases: ["PED-151"]
summary: "API - Refactor - Repository - Medios de envio"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-10-18 14:24"
updated: "2023-10-19 17:25"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-151"
---

# PED-151: API - Refactor - Repository - Medios de envio

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-10-18 14:24 |
| Actualizado | 2023-10-19 17:25 |
| Etiquetas | ninguna |
| Jira | [PED-151](https://bluinc.atlassian.net/browse/PED-151) |

## Relaciones

- **Padre:** [[PED-7 - Repositorios y base del proyecto|PED-7]] Repositorios y base del proyecto

## Descripcion

Segun lo conversado, refactorizaremos [link](https://lioteam.atlassian.net/browse/PED-38)  segun lo hicimos en expedicion.

Para esto nos basaremos en la tabla envios

```
SELECT 
  id,
  RTRIM(nombre) as nombre,
  activo as activo,
  eliminado,
  tipo,
  descripcion,
  plusDiasExtraMin,
  plusDiasExtraMax
  FROM [LO].[dbo].[mediosEnvio]
  WHERE eliminado <> 1 AND tipo = 2 AND activoInterno = 1
```

Pero adicionaremos el retiro, como se hiciera oportunamente en expedicion.

```

    public function getShippingMethods()
    {
        $shippingMethods = $this->repository->getShippingMethods();

        if (empty($shippingMethods)) {
            return [];
        }

        $shipping = array_map(static function ($shipping) {
            return [
                'id'               => (int)$shipping->id,
                'nombre'           => (string)$shipping->nombre,
                'activo'           => (int)$shipping->activo,
                'eliminado'        => $shipping->eliminado,
                'tipo'             => $shipping->tipo,
                'descripcion'      => (string)$shipping->descripcion,
                'plusDiasExtraMin' => $shipping->plusDiasExtraMin,
                'plusDiasExtraMax' => $shipping->plusDiasExtraMax
            ];
        }, $shippingMethods);

        # Agregamos el metodo de envio Retiro.
        $shipping[] = [
            'id'               => 3999,
            'nombre'           => 'Retiro',
            'activo'           => 1,
            'eliminado'        => 0,
            'tipo'             => 2,
            'descripcion'      => 'Retiro',
            'plusDiasExtraMin' => 0,
            'plusDiasExtraMax' => 0
        ];

        return $shipping;
    }
```
