from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler
import asyncio

class TelegramManager:
    def __init__(self, token, bot_instance):
        self.app = ApplicationBuilder().token(token).build()
        self.bot = bot_instance
        self._setup_handlers()
    
    def _setup_handlers(self):
        self.app.add_handler(CommandHandler("start", self.start))
        self.app.add_handler(CommandHandler("stats", self.stats))
    
    async def start(self, update: Update, context):
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="🤖 Bot TikTok iniciado!\n\n"
                 "Comandos disponibles:\n"
                 "/stats - Ver estadísticas\n"
                 "/pause - Pausar ejecución"
        )
    
    async def stats(self, update: Update, context):
        stats = self.bot.get_stats()
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"📊 Estadísticas:\nVistos: {stats['views']}\nLikes: {stats['likes']}"
        )
    
    def run_in_background(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        self.app.run_polling()