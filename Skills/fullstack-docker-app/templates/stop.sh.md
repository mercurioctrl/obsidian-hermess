# stop.sh

> Detiene todos los servicios. Parte del skill [[SKILL|fullstack-docker-app]].
> Complemento de [[start.sh]]. Los datos persisten en volúmenes (ver [[architecture#Volúmenes nombrados]]).

## Template

```bash
#!/bin/bash
echo "Deteniendo {{NOMBRE_PROYECTO_UPPER}}..."
docker compose down
echo "✓ Todos los servicios detenidos"
```
