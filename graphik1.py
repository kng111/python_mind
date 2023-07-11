# import numpy as np
# import matplotlib.pyplot as plt

# # Исторические данные курсов доллара и евро
# timestamps = list(range(1, 31))  # Пример временных меток
# dollars = [73.25, 73.45, 73.55, 73.65, 73.75, 73.85, 73.95, 73.85, 73.95, 73.85, 73.75, 73.65, 73.75, 73.85, 73.95,
#            73.85, 73.95, 73.85, 73.75, 73.65, 73.55, 73.45, 73.55, 73.65, 73.75, 73.85, 73.95, 73.85, 73.95, 73.85]

# euros = [87.12, 87.28, 87.35, 87.42, 87.58, 87.75, 87.82, 87.75, 87.82, 87.75, 87.58, 87.42, 87.58, 87.75, 87.82,
#          87.75, 87.82, 87.75, 87.58, 87.42, 87.35, 87.28, 87.35, 87.42, 87.58, 87.75, 87.82, 87.75, 87.82, 87.75]

# # Функция для отображения графика
# def plot_currency(timestamps, prices, currency_name, predicted_prices=None, start_day=None, end_day=None):
#     plt.figure(figsize=(10, 6))  # Размер графика
#     plt.plot(timestamps, prices, marker='o', markersize=6, linewidth=2, color='white', label='Реальная цена')  # Стиль линии и маркеры
#     if predicted_prices:
#         plt.plot(timestamps[:end_day], predicted_prices[start_day-1:end_day], linestyle='--', linewidth=2, color='orange', label='Предсказанная цена')
#         for i in range(start_day-1, end_day):
#             if np.isnan(predicted_prices[i]):
#                 continue
#             if predicted_prices[i] >= prices[i]:
#                 plt.fill_between([timestamps[i], timestamps[i+1]], [prices[i], prices[i+1]], [predicted_prices[i], predicted_prices[i+1]], facecolor='green', alpha=0.3)
#             else:
#                 plt.fill_between([timestamps[i], timestamps[i+1]], [prices[i], prices[i+1]], [predicted_prices[i], predicted_prices[i+1]], facecolor='red', alpha=0.3)
#     plt.xlabel('Временная метка', fontsize=12)  # Размер шрифта осей
#     plt.ylabel('Цена', fontsize=12)
#     plt.title(f'Курс {currency_name}', fontsize=14)  # Размер шрифта заголовка
#     plt.xticks(fontsize=10)  # Размер шрифта меток на осях
#     plt.yticks(fontsize=10)
#     plt.grid(True, linestyle='--', alpha=0.5)  # Сетка со стилем пунктирной линии
#     plt.gca().set_facecolor('black')  # Цвет фона графика
#     plt.tight_layout()  # Автоматическое выравнивание
#     plt.show()

# # Отображение графика курса доллара
# plot_currency(timestamps, dollars, 'доллара')

# # Отображение графика курса евро
# # plot_currency(timestamps, euros, 'евро')

# # Изменение временной метки и обновление графиков
# new_timestamps = list(range(1, 31 + 7))  # Новая временная метка на 7 дней вперед

# predictions_dollars = [73.65, 73.75, 73.85, 73.95, 73.85, 73.95, 73.85, 73.75, 73.65, 73.55, 73.45, 73.55, 73.65, 73.75,
#                        73.85, 73.75, 73.65, 73.75, 73.85, 73.95, 73.85, 73.75, 73.65, 73.75, 73.85, 73.95, 73.85, 73.95,
#                        73.85, 73.75, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]  # Пример предсказанных цен доллара

# # Обновление графика курса доллара с новыми данными и ограничением промежутка от 1 до 30 дня
# plot_currency(new_timestamps, dollars + [np.nan] * 7, 'доллара', predicted_prices=predictions_dollars, start_day=1, end_day=30)


import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Исторические данные курса доллара (приближенные к реальным)
timestamps = list(range(1, 31))
dollars = [73.25, 73.45, 73.55, 73.65, 73.75, 73.85, 73.95, 73.85, 73.95, 73.85, 73.75, 73.65, 73.75, 73.85, 73.95,
           73.85, 73.95, 73.85, 73.75, 73.65, 73.55, 73.45, 73.55, 73.65, 73.75, 73.85, 73.95, 73.85, 73.95, 73.85]

# Функция для предсказания курса доллара на заданный период
def predict_dollar(timestamps, dollars, forecast_steps):
    model = ARIMA(dollars, order=(1, 1, 1))
    model_fit = model.fit()

    forecast = model_fit.forecast(steps=forecast_steps)[0]

    return forecast

# Прогноз на 4 недели (28 дней)
forecast_steps = 28
forecast = predict_dollar(timestamps, dollars, forecast_steps)

# Отображение графика прогноза
plt.figure(figsize=(10, 6))
plt.plot(timestamps, dollars, marker='o', markersize=6, linewidth=2, color='white', label='Реальная цена')
plt.plot(np.arange(len(timestamps), len(timestamps) + len(forecast)), forecast, linestyle='--', linewidth=2, color='orange', label='Прогноз')
plt.xlabel('Временная метка', fontsize=12)
plt.ylabel('Цена', fontsize=12)
plt.title('Прогноз курса доллара', fontsize=14)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.grid(True, linestyle='--', alpha=0.5)
plt.gca().set_facecolor('black')
plt.tight_layout()
plt.legend(fontsize=12)
plt.show()

# Вывод прогнозных значений
print("Прогноз курса доллара:")
for i, value in enumerate(forecast):
    print(f"День {i+1}: {value:.2f}")
