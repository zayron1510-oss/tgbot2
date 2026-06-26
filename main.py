import telebot
import requests

# Вставьте сюда токен от BotFather
TOKEN = '8755308841:AAGM4UpBRMkp7ID_islWoOk-BqXDLIXKuF4'

bot = telebot.TeleBot(TOKEN)

def get_btc_price():
    """Получает цену BTC в USD через CoinGecko API."""
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin",
        "vs_currencies": "usd"
    }
    resp = requests.get(url, params=params, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    return data["bitcoin"]["usd"]

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(
        message,
        "Привет! Я бот с актуальной ценой на криптовалюту.\n"
        "Нажми /crypto, чтобы узнать цену биткоина в USD."
    )

@bot.message_handler(commands=["crypto"])
def send_crypto_info(message):
    try:
        price = get_btc_price()
        bot.reply_to(
            message,
            f"���на Bitcoin (BTC): ${price:,.2f} USD"
        )
    except Exception as e:
        bot.reply_to(message, f"Произошла ошибка при получении данных: {e}")

if __name__ == "__main__":
    print("Бот запущен...")
    bot.polling(non_stop=True)
