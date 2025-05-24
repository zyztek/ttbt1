from flask import Flask, render_template, jsonify
from core.tiktok_manager import TikTokBot

app = Flask(__name__)
bot = TikTokBot()

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/start_bot')
def start_bot():
    bot.run()
    return jsonify({"status": "Bot iniciado"})

@app.route('/get_stats')
def get_stats():
    return jsonify(bot.get_current_stats())