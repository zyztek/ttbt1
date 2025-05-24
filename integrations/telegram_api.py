from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import logging
import json

class TelegramManager:
    """Sistema completo de control y monitoreo via Telegram"""
    
    def __init__(self, token, bot_instance):
        self.app = ApplicationBuilder().token(token).build()
        self.bot = bot_instance
        self._setup_handlers()
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def _setup_handlers(self):
        handlers = [
            CommandHandler('start', self.start),
            CommandHandler('stats', self.get_stats),
            CommandHandler('pause', self.pause_bot),
            CommandHandler('config', self.update_config)
        ]
        for handler in handlers:
            self.app.add_handler(handler)

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Inicia el sistema principal"""
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="🚀 Bot TikTok iniciado\n\nComandos disponibles:\n"
                 "/stats - Ver métricas\n"
                 "/pause - Pausar ejecución\n"
                 "/config - Actualizar configuración"
        )
        self.bot.start_automation()

    async def get_stats(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Muestra estadísticas en tiempo real"""
        stats = self.bot.get_performance_metrics()
        formatted_stats = (
            f"📊 Estadísticas Actuales:\n"
            f"• Videos Vistos: {stats['views']}\n"
            f"• Likes Dados: {stats['likes']}\n"
            f"• Comentarios: {stats['comments']}\n"
            f"• Proxies Activos: {stats['active_proxies']}"
        )
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=formatted_stats
        )

    async def update_config(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Actualiza configuración en tiempo real"""
        try:
            new_config = json.loads(' '.join(context.args))
            self.bot.update_configuration(new_config)
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="✅ Configuración actualizada exitosamente"
            )
        except Exception as e:
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=f"❌ Error actualizando configuración: {str(e)}"
            )

    def run(self):
        """Inicia el servidor de Telegram"""
        self.app.run_polling()