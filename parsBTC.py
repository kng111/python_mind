# import requests
# import time

# # Заголовки (headers)
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
# }

# # Отправляем GET-запрос к CoinGecko API для получения данных о курсах криптовалют

# while True:
#     time.sleep(1)
#     url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd'
#     response = requests.get(url, headers=headers)

#     # Проверяем успешность запроса
#     if response.status_code == 200:
#         # Получаем данные в формате JSON
#         data = response.json()

#         # Получаем курсы BTC и ETH
#         btc_price = data['bitcoin']['usd']
#         eth_price = data['ethereum']['usd']

#         # Выводим курсы
#         print(f"Курс Bitcoin (BTC): {btc_price} USD")
#         print(f"Курс Ethereum (ETH): {eth_price} USD")

#     else:
#         print("Ошибка при запросе курса криптовалют")

import time
import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
}
while True:
    # time.sleep(1)
    url = 'https://api.binance.com/api/v3/ticker/price'
    params = {'symbol': 'BTCUSDT'}

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        symbol = data['symbol']
        price = data['price']
        print(f"Символ: {symbol}")
        print(f"Цена: {price}")
    else:
        print("Ошибка при запросе курса криптовалют")
