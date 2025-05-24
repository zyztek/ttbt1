#!/data/data/com.termux/files/usr/bin/bash

# Verificar root
if [ "$(id -u)" -eq 0 ]; then
    echo "¡No ejecutar como root!"
    exit 1
fi

# Actualizar paquetes
echo "[1/6] Actualizando sistema..."
pkg update -y && pkg upgrade -y

# Instalar dependencias
echo "[2/6] Instalando dependencias..."
pkg install -y python git openssl proot clang libxml2 libxslt termux-exec

# Configurar Chromium
echo "[3/6] Instalando Chromium..."
pkg install -y chromium
termux-chroot <<EOF
apt update && apt install -y chromium-chromedriver
EOF

# Clonar repositorio
echo "[4/6] Clonando código..."
git clone https://github.com/tu_usuario/tiktok-bot.git
cd tiktok-bot

# Configurar Python
echo "[5/6] Instalando dependencias Python..."
pip install --upgrade pip wheel
pip install -r requirements.txt

# Configuración final
echo "[6/6] Preparando entorno..."
termux-setup-storage
mkdir -p ~/storage/shared/tiktok-bot/{db,logs}
cp .env.example .env
chmod 600 .env

echo "¡Instalación completada!"
echo "1. Edita .env con tus credenciales"
echo "2. Ejecuta: python utilities/add_accounts.py"
echo "3. Inicia el bot: python main.py --mode=safe"