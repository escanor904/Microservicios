#!/bin/bash

# Ruta al steps.py en logs/features/steps
ruta_logs="pruebas/api_logs/features/steps"

# Ruta al steps.py en aute/features/steps
ruta_aute="pruebas/api_authentication/steps"

# Aquí puedes realizar acciones con los archivos steps.py
# Ejemplo de ejecución
echo "Ejecutando steps.py en logs/features/steps"
python "$ruta_logs"

echo "Ejecutando steps.py en aute/features/steps"
python "$ruta_aute"
