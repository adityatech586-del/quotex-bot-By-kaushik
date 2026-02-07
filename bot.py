import telebot
import random

TOKEN = 8209285323:AAGUBcTp0JnkvbCFrM7NUxO4zHTD9zExxd4
bot = telebot.TeleBot(TOKEN)

def generate_signal():
    # Simulated indicator values (logic based)
    rsi = random.randint(10, 90)
    ema_fast = random.randint(1, 100)
    ema_slow = random.randint(1, 100)
    macd = ema_fast - ema_slow
    atr = random.randint(1, 10)  # volatility

    trend = "UP" if ema_fast > ema_slow else "DOWN"

    # Volatility filter (OTC special)
    if atr < 4:
        return "⚠️ Market Low Volatility\n❌ NO TRADE"

    # STRONG CALL
    if rsi < 30 and trend == "UP" and macd > 5:
        return f"🔥 STRONG CALL (BUY)\nRSI: {rsi}\nTrend: {trend}\nVolatility: HIGH"

    # STRONG PUT
    if rsi > 70 and trend == "DOWN" and macd < -5:
        return f"🔥 STRONG PUT (SELL)\nRSI: {rsi}\nTrend: {trend}\nVolatility: HIGH"

    return f"⏳ WAIT\nRSI: {rsi}\nTrend: {trend}"

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message,
        "🤖 Quotex OTC Pro Bot\n"
        "Indicators: RSI + EMA + MACD + ATR\n"
        "Type /signal for 1-min OTC signal 🚀"
    )

@bot.message_handler(commands=['signal'])
def signal(message):
    bot.reply_to(message, generate_signal())

bot.polling()
