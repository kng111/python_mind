import numpy as np
from sklearn.linear_model import LinearRegression

# Исторические данные курсов доллара и евро
# Данные должны содержать два списка: timestamps (временные метки) и prices (цены)
timestamps = [1, 2, 3, 4, 5]  # Пример временных меток
dollar_prices = [70, 72, 75, 78, 80]  # Пример цен доллара
euro_prices = [80, 82, 85, 88, 90]  # Пример цен евро

# Создание матрицы признаков X и вектора целевых значений y для доллара
X_dollar = np.array(timestamps).reshape(-1, 1)
y_dollar = np.array(dollar_prices)

# Создание матрицы признаков X и вектора целевых значений y для евро
X_euro = np.array(timestamps).reshape(-1, 1)
y_euro = np.array(euro_prices)

# Создание и обучение модели линейной регрессии для доллара
regressor_dollar = LinearRegression()
regressor_dollar.fit(X_dollar, y_dollar)

# Создание и обучение модели линейной регрессии для евро
regressor_euro = LinearRegression()
regressor_euro.fit(X_euro, y_euro)

# Предсказание курса доллара и евро для новой временной метки
new_timestamp = 6  # Пример новой временной метки

dollar_prediction = regressor_dollar.predict(np.array([[new_timestamp]]))
euro_prediction = regressor_euro.predict(np.array([[new_timestamp]]))

# Вывод предсказанных значений
print(f"Предсказание курса доллара для временной метки {new_timestamp}: {dollar_prediction}")
print(f"Предсказание курса евро для временной метки {new_timestamp}: {euro_prediction}")
