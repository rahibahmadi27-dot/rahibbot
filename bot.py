import os
import telebot
import random
import time
from datetime import datetime
from flask import Flask
from threading import Thread

# ====== توکن ربات ======
TOKEN = os.environ.get("TOKEN")
if not TOKEN:
    raise ValueError("TOKEN is not set in Environment Variables")

bot = telebot.TeleBot(TOKEN, parse_mode="Markdown")

# ====== آیدی گروه (عدد) ======
GROUP_ID = -1003797641493  # آیدی عددی گروه تو

# ====== راه‌اندازی Flask ======
app = Flask(__name__)

@app.route('/')
def home():
    return "OTP Bot is running!"

# ====== کشورها و پیش‌شماره ======
countries = {
    "AF": {"flag": "🇦🇫", "prefix": "+937"},
    "TR": {"flag": "🇹🇷", "prefix": "90"},
    "VE": {"flag": "🇻🇪", "prefix": "58"},
    "AE": {"flag": "🇦🇪", "prefix": "971"}
}

# ====== تولید شماره تصادفی ======
def generate_number(country_code):
    base = countries[country_code]["prefix"]
    if country_code == "AF":
        return f"{base}{random.randint(10000000, 99999999)}"
    else:
        return f"{base}{random.randint(500000000, 999999999)}"

# ====== تولید OTP تصادفی ======
def generate_otp():
    return f"{random.randint(100,999)}-{random.randint(100,999)}"

# ====== ارسال خودکار شماره و OTP ======
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
        try:
            bot.send_message(GROUP_ID, message)
        except Exception as e:
            print(f"⚠️ Error sending message: {e}")
        time.sleep(60)  # هر ۶۰ ثانیه پیام بعدی

# ====== اجرا ======
if __name__ == "__main__":
    # حلقه OTP در Thread جداگانه
    Thread(target=send_otp).start()
    # Flask برای Render (پورت باز)
    app.run(host="0.0.0.0", port=10000)
