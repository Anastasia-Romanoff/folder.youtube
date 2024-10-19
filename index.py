import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Генерируем 20 рандомных точек
np.random.seed(42)  # Устанавливаем начальное значение для генератора случайных чисел
x = np.random.rand(20)
y = np.random.rand(20)

# Строим график корреляции
plt.figure(figsize=(8, 6))
plt.scatter(x, y, label='Данные')

# Вычисляем коэффициент корреляции и уравнение прямой
slope, intercept, r_value, p_value, std_err = linregress(x, y)

# Строим линию регрессии
plt.plot(x, slope * x + intercept, color='red', label='Линия регрессии')

# Добавляем легенду и названия осей
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('График корреляции')

# Добавляем текст с коэффициентом корреляции и уравнением прямой
plt.text(0.1, 0.9, f'Коэффициент корреляции: {r_value:.2f}', transform=plt.gca().transAxes)
plt.text(0.1, 0.8, f'Уравнение прямой: y = {slope:.2f}x + {intercept:.2f}', transform=plt.gca().transAxes)

# Отображаем график
plt.show()