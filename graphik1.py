import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Загрузка исторических данных
historical_data = pd.read_csv('historical_data.csv')

# Загрузка предсказанных данных
predicted_data = pd.read_csv('predicted_data.csv')

# Извлечение дат и курсов
timestamps = historical_data['Date'].tolist()
prices = historical_data['USD_RUB'].tolist()
predicted_prices = predicted_data['USD_RUB'].tolist()

# Функция для отображения графика
def plot_currency(timestamps, prices, currency_name, predicted_prices=None):
    plt.figure(figsize=(10, 6))
    plt.plot(timestamps, prices, marker='o', markersize=6, linewidth=2, color='white', label='Реальная цена')
    if predicted_prices:
        plt.plot(timestamps[-len(predicted_prices):], predicted_prices, linestyle='--', linewidth=2, color='red', label='Предсказанная цена')
    plt.xlabel('Дата', fontsize=10)
    plt.ylabel('USD_RUB', fontsize=12)
    plt.title(f'Курс {currency_name}', fontsize=14)
    plt.xticks(rotation=45, ha='right')
    plt.gca().set_facecolor('black')
    plt.grid(color='white', linestyle='--', linewidth=0.5)
    plt.legend(fontsize=12)
    plt.grid(False)
    plt.tight_layout()
    plt.show()

# Отображение графика
plot_currency(timestamps, prices, 'доллара', predicted_prices)


# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

# # Загрузка исторических данных
# historical_data = pd.read_csv('historical_data.csv')

# # Загрузка предсказанных данных
# predicted_data = pd.read_csv('predicted_data.csv')

# # Извлечение дат и курсов
# timestamps = pd.to_datetime(historical_data['Date']).dt.date.tolist()
# prices = historical_data['USD_RUB'].astype(float).tolist()
# predicted_prices = predicted_data['USD_RUB'].astype(float).tolist()

# # Функция для отображения графика с временными отрезками покупки и продажи
# def plot_currency_with_trading(timestamps, prices, currency_name, predicted_prices=None):
#     plt.figure(figsize=(10, 6))
#     plt.plot(timestamps, prices, marker='o', markersize=6, linewidth=2, color='blue', label='Реальная цена')
#     if predicted_prices:
#         plt.plot(timestamps[-len(predicted_prices):], predicted_prices, linestyle='--', linewidth=2, color='orange', label='Предсказанная цена')
#         buy_indices = np.where(np.array(predicted_prices[:-1]) < np.array(predicted_prices[1:]) - 0.5)[0] + len(prices) - 1
#         sell_indices = np.where(np.array(predicted_prices[:-1]) > np.array(predicted_prices[1:]) + 0.5)[0] + len(prices) - 1
#         if len(buy_indices) > 0 and len(sell_indices) > 0:
#             plt.axvspan(timestamps[buy_indices[0]], timestamps[sell_indices[0]], ymin=0, ymax=max(prices), facecolor='green', alpha=0.3)
#             for i in range(1, min(len(buy_indices), len(sell_indices))):
#                 plt.axvspan(timestamps[sell_indices[i-1]], timestamps[buy_indices[i]], facecolor='red', alpha=0.3)
#             if len(buy_indices) > len(sell_indices):
#                 plt.axvspan(timestamps[buy_indices[-1]], timestamps[-1], facecolor='red', alpha=0.3)
#             elif len(buy_indices) < len(sell_indices):
#                 plt.axvspan(timestamps[sell_indices[-1]], timestamps[-1], facecolor='green', alpha=0.3)
#     plt.xlabel('Дата', fontsize=12)
#     plt.ylabel('USD_RUB', fontsize=12)
#     plt.title(f'Курс {currency_name} с временными отрезками покупки и продажи', fontsize=14)
#     plt.xticks(rotation=45, ha='right')
#     plt.gca().set_facecolor('black')
#     plt.grid(color='white', linestyle='--', linewidth=0.5)
#     plt.legend(fontsize=12)
#     plt.tight_layout()
#     plt.show()

# # Отображение графика с временными отрезками покупки и продажи
# plot_currency_with_trading(timestamps, prices, 'доллара', predicted_prices)
