from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import logging
import os

class TelegramBot:
    def __init__(self):
        self.token = os.getenv("TELEGRAM_TOKEN")
        self.app = ApplicationBuilder().token(self.token).build()
        self._register_handlers()
    
    def _register_handlers(self):
        self.app.add_handler(CommandHandler("start", self.start))
        self.app.add_handler(CommandHandler("stats", self.stats))
    
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="🤖 Bot de TikTok iniciado! Usa /stats para ver métricas."
        )
    
    async def stats(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        with open("tiktok_bot.log", "r") as f:
            logs = f.read()[-1000:]  # Últimos 1000 caracteres
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"📈 Últimas acciones:\n{logs}"
        )
    
    def run(self):
        self.app.run_polling()