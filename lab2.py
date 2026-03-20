import numpy as np

# Матрица коэффициентов (из image.png)
A = np.array([
    [3.910, 0.129, 0.283, 0.107],
    [0.217, 4.691, 0.279, 0.237],
    [0.201, 0.372, 2.987, 0.421],
    [0.531, 0.196, 0.236, 5.032]
])

# Вектор свободных членов
b = np.array([0.395, 0.432, 0.127, 0.458])

# Точность
eps = 1e-6
n = len(b)

print("=" * 70)
print("МЕТОД ЯКОБИ")
print("=" * 70)

# Начальное приближение
x = b / np.diag(A)
iteration = 0

# Печать заголовка таблицы
print(f"{'k':<4} {'x1':<15} {'x2':<15} {'x3':<15} {'x4':<15}")
print("-" * 70)

while True:
    x_old = x.copy()
    x_new = np.zeros(n)
    iteration += 1
    
    # Итерация Якоби
    for i in range(n):
        s = 0
        for j in range(n):
            if i != j:
                s += A[i][j] * x_old[j]
        x_new[i] = (b[i] - s) / A[i][i]
    
    x = x_new
    
    # Вывод итерации
    print(f"{iteration:<4} {x[0]:<15.8f} {x[1]:<15.8f} {x[2]:<15.8f} {x[3]:<15.8f}")
    
    # Проверка точности
    if np.max(np.abs(x - x_old)) < eps:
        break

print("-" * 70)
print(f"\nОТВЕТ (Метод Якоби):")
print(f"x1 = {x[0]:.8f}")
print(f"x2 = {x[1]:.8f}")
print(f"x3 = {x[2]:.8f}")
print(f"x4 = {x[3]:.8f}")
print(f"Количество итераций: {iteration}")
print(f"Достигнутая точность: {eps}")

print("\n" + "=" * 70)
print("МЕТОД ГАУССА-ЗЕЙДЕЛЯ")
print("=" * 70)

# Начальное приближение
x = b / np.diag(A)
iteration = 0

# Печать заголовка таблицы
print(f"{'k':<4} {'x1':<15} {'x2':<15} {'x3':<15} {'x4':<15}")
print("-" * 70)

while True:
    x_old = x.copy()
    iteration += 1
    
    # Итерация Гаусса-Зейделя
    for i in range(n):
        # Сумма для уже найденных переменных на текущей итерации
        s1 = 0
        for j in range(i):
            s1 += A[i][j] * x[j]
        
        # Сумма для еще не найденных переменных (с предыдущей итерации)
        s2 = 0
        for j in range(i+1, n):
            s2 += A[i][j] * x_old[j]
        
        x[i] = (b[i] - s1 - s2) / A[i][i]
    
    # Вывод итерации
    print(f"{iteration:<4} {x[0]:<15.8f} {x[1]:<15.8f} {x[2]:<15.8f} {x[3]:<15.8f}")
    
    # Проверка точности
    if np.max(np.abs(x - x_old)) < eps:
        break

print("-" * 70)
print(f"\nОТВЕТ (Метод Гаусса-Зейделя):")
print(f"x1 = {x[0]:.8f}")
print(f"x2 = {x[1]:.8f}")
print(f"x3 = {x[2]:.8f}")
print(f"x4 = {x[3]:.8f}")
print(f"Количество итераций: {iteration}")
print(f"Достигнутая точность: {eps}")

# Сравнение
print("\n" + "=" * 70)
print("СРАВНЕНИЕ МЕТОДОВ")
print("=" * 70)
print("Для точности 10⁻⁶:")
print("-" * 40)
# Здесь нужно будет подставить реальные значения после запуска программы
