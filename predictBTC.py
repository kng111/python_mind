import numpy as np
from sklearn.linear_model import LinearRegression

# Исторические данные курсов BTC и ETH
# Данные должны содержать два списка: timestamps (временные метки) и prices (цены)
timestamps = [1, 2, 3, 4, 5]  # Пример временных меток
btc_prices = [5000, 5500, 6000, 6500, 7000]  # Пример цен BTC
eth_prices = [200, 220, 240, 260, 280]  # Пример цен ETH

# Создание матрицы признаков X и вектора целевых значений y для BTC
X_btc = np.array(timestamps).reshape(-1, 1)
y_btc = np.array(btc_prices)

# Создание матрицы признаков X и вектора целевых значений y для ETH
X_eth = np.array(timestamps).reshape(-1, 1)
y_eth = np.array(eth_prices)

# Создание и обучение модели линейной регрессии для BTC
regressor_btc = LinearRegression()
regressor_btc.fit(X_btc, y_btc)

# Создание и обучение модели линейной регрессии для ETH
regressor_eth = LinearRegression()
regressor_eth.fit(X_eth, y_eth)

# Предсказание курса BTC и ETH для новой временной метки
new_timestamp = 6  # Пример новой временной метки

btc_prediction = regressor_btc.predict(np.array([[new_timestamp]]))
eth_prediction = regressor_eth.predict(np.array([[new_timestamp]]))

# Вывод предсказанных значений
print(f"Предсказание курса Bitcoin (BTC) для временной метки {new_timestamp}: {btc_prediction}")
print(f"Предсказание курса Ethereum (ETH) для временной метки {new_timestamp}: {eth_prediction}")
