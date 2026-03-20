import numpy as np
import matplotlib.pyplot as plt

# Данные
x_data = np.array([0.234, 0.649, 1.382, 2.672, 2.849])
y_data = np.array([0.511, 0.982, 2.411, 3.115, 4.184])

# 1. Интерполяция Лагранжа
def lagrange(x, x_data, y_data):
    n = len(x_data)
    result = 0
    for i in range(n):
        term = y_data[i]
        for j in range(n):
            if j != i:
                term *= (x - x_data[j]) / (x_data[i] - x_data[j])
        result += term
    return result

# 2. Интерполяция Ньютона (разделенные разности)
def newton_coef(x_data, y_data):
    n = len(x_data)
    coef = y_data.copy()
    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            coef[i] = (coef[i] - coef[i-1]) / (x_data[i] - x_data[i-j])
    return coef

def newton_eval(coef, x_data, x):
    n = len(coef)
    result = coef[n-1]
    for i in range(n-2, -1, -1):
        result = result * (x - x_data[i]) + coef[i]
    return result

# Вычисление в точке x = 1.5
x_test = 1.5
lagrange_val = lagrange(x_test, x_data, y_data)
newton_c = newton_coef(x_data, y_data)
newton_val = newton_eval(newton_c, x_data, x_test)

print(f"Значение в точке x = {x_test}:")
print(f"Метод Лагранжа: {lagrange_val:.8f}")
print(f"Метод Ньютона: {newton_val:.8f}")

# Построение графика
x_plot = np.linspace(0, 3, 200)
y_lagrange = [lagrange(x, x_data, y_data) for x in x_plot]
y_newton = [newton_eval(newton_c, x_data, x) for x in x_plot]

plt.figure(figsize=(10, 6))
plt.plot(x_data, y_data, 'ro', label='Исходные точки', markersize=8)
plt.plot(x_plot, y_lagrange, 'b-', label='Полином Лагранжа')
plt.plot(x_plot, y_newton, 'g--', label='Полином Ньютона', alpha=0.7)
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Интерполяционный полином (4-й степени)')
plt.legend()
plt.show()
