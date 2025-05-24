#!/data/data/com.termux/files/usr/bin/bash
pkg update -y
pkg install -y python git chromium termux-exec
pip install selenium==4.9.1 webdriver-manager==4.0.0
termux-setup-storage
mkdir ~/tiktok-bot
cd ~/tiktok-bot
git clone https://github.com/tu_usuario/tiktok-android-bot.git
echo "¡Instalación completada! Ejecuta: python main.py"