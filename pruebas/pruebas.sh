#!/bin/bash

echo "Ejecutando pruebas en API AUTHENTICATION"
cd "./api_authentication" || exit
./pruebas.sh

echo "Ejecutando pruebas en API GATEWAY"
cd "./api_gateway" || exit
./pruebas.sh

echo "Ejecutando pruebas en API LOGS"
cd "./api_logs" || exit
./pruebas.sh

echo "Ejecutando pruebas en API PROFILE"
cd "./api_profile" || exit
./pruebas.sh