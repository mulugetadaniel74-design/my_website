import telebot
import random
import time

# ይህ ያንተ ልዩ የቦት ቁልፍ ነው
TOKEN = '8512547452:AAGs1M3bTUVd1rVxfJViuZ7Dbq1Rj4WXbkE'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "ሰላም ዳንኤል! 👋 የቴሌግራም ቦትህ ስራ ጀምሯል።\nለመጫወት /spin ብለው ይጻፉ።")

@bot.message_handler(commands=['spin'])
def spin_game(message):
    items = ["💰", "💎", "🍒", "7️⃣", "🍀"]
    s1, s2, s3 = random.choice(items), random.choice(items), random.choice(items)
    result = f"| {s1} | {s2} | {s3} |"
    
    if s1 == s2 == s3:
        bot.send_message(message.chat.id, f"{result}\n🎉 እንኳን ደስ አለዎት! አሸንፈዋል።")
    else:
        bot.send_message(message.chat.id, f"{result}\n❌ አልተሳካም፣ እንደገና ይሞክሩ።")

bot.polling()

