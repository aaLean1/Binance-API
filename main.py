from binance.client import Client
from secrets import api_key, api_secret

client = Client(api_key, api_secret, testnet=True)

avg_price = client.get_avg_price(symbol='BTCUSDT')
print(avg_price)