import requests
from bs4 import BeautifulSoup

# Отправляем GET-запрос к странице с курсом валют
url = 'https://www.cbr.ru/currency_base/daily/'
response = requests.get(url)

# Проверяем успешность запроса
if response.status_code == 200:
    # Создаем объект BeautifulSoup для парсинга HTML
    soup = BeautifulSoup(response.content, 'html.parser')

    # Находим таблицу с курсами валют
    table = soup.find('table', class_='data')

    # Находим строки таблицы
    rows = table.find_all('tr')

    # Проходимся по строкам и выводим курсы доллара и евро
    for row in rows:
        cells = row.find_all('td')
        if len(cells) >= 5 and (cells[1].text == 'USD' or cells[1].text == 'EUR'):
            currency = cells[1].text
            rate = cells[4].text
            print(f"Курс {currency}: {rate}")
else:
    print("Ошибка при запросе курса валют")
