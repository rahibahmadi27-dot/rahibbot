import os
import telebot
import random
import time
from datetime import datetime
from flask import Flask
from threading import Thread

# گرفتن توکن از Environment
TOKEN = os.environ.get("TOKEN")

if not TOKEN:
    raise ValueError("TOKEN is not set in Environment Variables")

bot = telebot.TeleBot(TOKEN, parse_mode="Markdown")

GROUP_ID = -100XXXXXXXXXX  # آیدی عددی گروهت را اینجا بگذار

app = Flask(__name__)

@app.route('/')
def home():
    return "OTP Bot is running!"

countries = {
    "AF": {"flag": "🇦🇫", "prefix": "+937"},
    "TR": {"flag": "🇹🇷", "prefix": "90"},
    "VE": {"flag": "🇻🇪", "prefix": "58"},
    "AE": {"flag": "🇦🇪", "prefix": "971"}
}

def generate_number(country_code):
    base = countries[country_code]["prefix"]
    if country_code == "AF":
        return f"{base}{random.randint(10000000, 99999999)}"
    else:
        return f"{base}{random.randint(500000000, 999999999)}"

def generate_otp():
    return f"{random.randint(100,999)}-{random.randint(100,999)}"

def send_otp():
    while True:
        country_code = random.choice(list(countries.keys()))
        number = generate_number(country_code)
        otp = generate_otp()
        now = datetime.now()

        message = f"""
🔥 *NEW OTP Received*

📅 {now.strftime("%d %b %Y")}
⏰ {now.strftime("%I:%M:%S %p")}

🌎 {country_code} {countries[country_code]["flag"]}
📱 `{number}`

🔐 OTP: `{otp}`
"""

        bot.send_message(GROUP_ID, message)
        time.sleep(60)

if __name__ == "__main__":
    Thread(target=send_otp).start()
    app.run(host="0.0.0.0", port=10000)
