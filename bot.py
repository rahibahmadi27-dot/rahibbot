
# -*- coding: utf-8 -*-
import telebot
import random
import time
from datetime import datetime

# ====== توکن ربات ======

bot = telebot.TeleBot(TOKEN, parse_mode="Markdown")

# ⚠️ ربات باید ادمین گروه باشد
GROUP_LINK = "https://t.me/+d1Mg7gpJ26diOGI9"

# ====== کشورها و پرچم و پیش‌شماره ======
countries = {
    "AF": {"flag": "🇦🇫", "prefix": "+937"},
    "TR": {"flag": "🇹🇷", "prefix": "90"},
    "VE": {"flag": "🇻🇪", "prefix": "58"},
    "AE": {"flag": "🇦🇪", "prefix": "971"}
}

# ====== تولید شماره ======
def generate_number(country_code):
    base = countries[country_code]["prefix"]
    if country_code == "AF":
        return f"{base}{random.randint(10000000, 99999999)}"
    else:
        return f"{base}{random.randint(500000000, 999999999)}"

# ====== تولید OTP ======
def generate_otp():
    return f"{random.randint(100,999)}-{random.randint(100,999)}"

# ====== ارسال خودکار OTP به گروپ ======
def send_otp():
    while True:
        country_code = random.choice(list(countries.keys()))
        number = generate_number(country_code)
        otp = generate_otp()
        now = datetime.now()
        date_str = now.strftime("%d %b %Y")
        time_str = now.strftime("%I:%M:%S %p")
        flag = countries[country_code]["flag"]

        message = f"""
🔥 *NEW OTP Received*

📅 Date: *{date_str}*
⏰ Time: *{time_str}*

🌎 Country: *{country_code} {flag}*
⚙️ Service: *NovaChat* (NC)
📱 Number: *{number}*

🔐 *OTP Code*
`{otp}`

📩 *Message*
# Your verification code is {otp}
Don't share this code with others.
"""
        bot.send_message(GROUP_LINK, message)
        time.sleep(60)  # هر ۶۰ ثانیه پیام بعدی

# ====== شروع ربات ======
print("🚀 Advanced OTP Bot is running...")
send_otp()
