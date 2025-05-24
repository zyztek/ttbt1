#!/bin/bash

# Configurar entorno
export $(grep -v '^#' .env | xargs)

# Ejecutar bot con parámetros
python main.py \
    --headless \
    --proxy-rotation=$PROXY_ROTATION_INTERVAL \
    --max-views=$MAX_DAILY_VIEWS \
    --enable-metrics