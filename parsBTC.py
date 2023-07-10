import requests

# Отправляем GET-запрос к CoinGecko API для получения данных о курсах криптовалют
url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd'
response = requests.get(url)

# Проверяем успешность запроса
if response.status_code == 200:
    # Получаем данные в формате JSON
    data = response.json()

    # Получаем курсы BTC и ETH
    btc_price = data['bitcoin']['usd']
    eth_price = data['ethereum']['usd']

    # Выводим курсы
    print(f"Курс Bitcoin (BTC): {btc_price} USD")
    print(f"Курс Ethereum (ETH): {eth_price} USD")
else:
    print("Ошибка при запросе курса криптовалют")
