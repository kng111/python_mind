# import random
# import csv
# from datetime import datetime
# import calendar

# # Определение месяца и года
# year = 2023
# month = 7

# # Получение числа дней в указанном месяце
# _, num_days = calendar.monthrange(year, month)

# # Открываем файл historical_data.csv для записи
# with open('historical_data.csv', 'w', newline='') as file:
#     writer = csv.writer(file)

#     # Записываем заголовок
#     writer.writerow(['Date', 'USD_RUB'])

#     # Генерируем случайные значения для USD_RUB и записываем их в файл
#     for day in range(1, num_days + 1):
#         date = datetime(year=year, month=month, day=day)  # Создаем объект datetime с нужной датой
#         usd_rub = random.uniform(70.0, 80.0)  # Генерация случайного значения в диапазоне от 70.0 до 80.0
#         writer.writerow([date.strftime('%Y-%m-%d'), usd_rub])


import random
import csv

# Открываем файл historical_data.csv для записи
with open('historical_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    # Записываем заголовок
    writer.writerow(['Date', 'USD_RUB'])

    # Генерируем случайные значения для USD_RUB и записываем их в файл
    for month in range(7, 13):  # Генерация значений для 3 месяцев (1, 2, 3)
        for day in range(1, 31):  # Генерация значений для 30 дней в каждом месяце
            date = f"2023-{month:02d}-{day:02d}"  # Генерация даты в формате "2023-01-01", "2023-01-02" и т.д.
            usd_rub = random.uniform(70.0, 85.0)  # Генерация случайного значения в диапазоне от 70.0 до 77.0
            writer.writerow([date, str(usd_rub)])  # Преобразуем usd_rub в строку

