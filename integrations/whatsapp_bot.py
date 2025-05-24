from flask import Flask, request
from twilio.twiml.messaging import MessagingResponse
from core.tiktok_manager import TikTokBot

app = Flask(__name__)
bot = TikTokBot()

@app.route("/whatsapp", methods=['POST'])
def whatsapp_webhook():
    user_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    
    if user_msg == '/start':
        bot.start()
        resp.message("✅ Bot iniciado. Envía /stats para ver métricas.")
    elif user_msg == '/stats':
        stats = bot.get_stats()
        resp.message(f"📊 Stats: Views={stats['views']}, Likes={stats['likes']}")
    
    return str(resp)