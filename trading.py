import requests
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

# প্রাইস সংরক্ষণের জন্য লিস্ট
prices = []
timestamps = []

# ক্রিপ্টো প্রাইস ফাংশন
def get_crypto_price(crypto, currency):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies={currency}"
    try:
        response = requests.get(url)
        data = response.json()
        price = data[crypto][currency]
        return price
    except Exception as e:
        print(f"Error: {e}")
        return None

# চার্ট আপডেট ফাংশন
def update_chart(frame):
    global prices, timestamps
    crypto = "bitcoin"  # ক্রিপ্টো আইডি (যেমন: bitcoin, ethereum)
    currency = "usd"    # মুদ্রা (যেমন: usd, eur, bdt)

    price = get_crypto_price(crypto, currency)
    if price is not None:
        prices.append(price)
        timestamps.append(time.strftime('%H:%M:%S'))  # টাইমস্ট্যাম্প যোগ করা

        # চার্ট পরিষ্কার করে আপডেট করুন
        plt.cla()
        plt.plot(timestamps, prices, label=f"{crypto.capitalize()} Price in {currency.upper()}")
        plt.xlabel("Time")
        plt.ylabel("Price")
        plt.title("Real-Time Cryptocurrency Price Chart")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.legend()

# Matplotlib অ্যানিমেশন
fig = plt.figure()
ani = FuncAnimation(fig, update_chart, interval=10000)  # প্রতি ১০ সেকেন্ডে চার্ট আপডেট
plt.show()

