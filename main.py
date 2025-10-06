from bot import Bot
from flask import Flask
from threading import Thread
import os

# --- Flask app for health check ---
app = Flask(__name__)

@app.route('/')
def home():
    return "Saikat Forward Bot is alive!"

def run_web():
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)

# --- Run bot + web together ---
def run_bot():
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    # Run web server in background thread
    Thread(target=run_web).start()
    # Start Telegram bot
    run_bot()
