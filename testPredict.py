import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Загрузка данных из файла historical_data.csv
data = pd.read_csv('historical_data.csv')

# Проверка наличия столбца 'Date'
if 'Date' not in data.columns:
    raise KeyError("Столбец 'Date' не найден в данных.")

# Извлечение числовых признаков из даты
data['Date'] = pd.to_datetime(data['Date'])
data['Day'] = data['Date'].dt.day
data['Month'] = data['Date'].dt.month
data['Year'] = data['Date'].dt.year

# Разделение данных на признаки (X) и целевую переменную (y)
X = data[['Day', 'Month', 'Year']]
y = data['USD_RUB']

# Разделение данных на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Инициализация и обучение модели
model = LinearRegression()
model.fit(X_train, y_train)

# Предсказание на тестовых данных
y_pred = model.predict(X_test)

# Оценка точности модели
mae = mean_absolute_error(y_test, y_pred)
print(f'Mean Absolute Error: {mae}')
new_data = pd.DataFrame({'DayOfWeek': [0, 1, 2], 'Month': [12, 12, 12], 'Year': [2023, 2023, 2023]})  # Пример новых признаков
new_data['Day'] = new_data['DayOfWeek']
predictions = model.predict(new_data[['Day', 'Month', 'Year']])

print(f'Predictions: {predictions}')
# Построение графика предсказанных значений и истинных значений
plt.figure(figsize=(12, 6))  # Размер графика
plt.plot(data['Date'], data['USD_RUB'], label='True Values', marker='o', linestyle='-', color='blue')
plt.plot(data.loc[X_test.index, 'Date'], y_pred, label='Predicted Values', marker='s', linestyle='--', color='red')
plt.scatter(data.loc[X_test.index, 'Date'], y_pred, color='red')
plt.xlabel('Date', fontsize=12)  # Размер и подпись оси X
plt.ylabel('USD_RUB', fontsize=12)  # Размер и подпись оси Y
plt.title('True Values vs Predicted Values', fontsize=14)  # Размер и заголовок графика
plt.legend(fontsize=12)  # Размер легенды
plt.grid(True)  # Включение сетки
plt.xticks(rotation=45)  # Поворот подписей оси X
plt.tight_layout()  # Улучшение компоновки графика
plt.show()
