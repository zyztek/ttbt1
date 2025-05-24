#!/bin/bash

# Configuración predeterminada
HEADLESS=false
PROXY_ROTATION=5

# Parsear argumentos
while [[ $# -gt 0 ]]; do
    case $1 in
        --headless)
        HEADLESS=true
        shift
        ;;
        --proxy-rotation=*)
        PROXY_ROTATION="${1#*=}"
        shift
        ;;
        *)
        echo "Argumento desconocido: $1"
        exit 1
        ;;
    esac
done

# Verificar dependencias
if ! command -v chromium &> /dev/null; then
    echo "Instalando Chromium..."
    sudo apt-get install -y chromium
fi

# Ejecutar el bot con parámetros
python main.py \
    --headless=$HEADLESS \
    --proxy-rotation-interval=$PROXY_ROTATION \
    --max-views=500 \
    --enable-cleanup