import numpy as np

# ============================================
# УРАВНЕНИЕ 19a: -ln x - 3cos 2x = 0
# ============================================

def f1(x):
    return -np.log(x) - 3*np.cos(2*x)

def df1(x):
    return -1/x + 6*np.sin(2*x)

print("="*70)
print("УРАВНЕНИЕ 19a: -ln x - 3cos 2x = 0")
print("="*70)

# Метод половинного деления
def bisection(f, a, b, eps=1e-6):
    print("\n--- МЕТОД ПОЛОВИННОГО ДЕЛЕНИЯ ---")
    print(f"{'Итерация':<10} {'a':<15} {'b':<15} {'c':<15} {'f(c)':<15}")
    print("-"*70)
    
    iteration = 0
    while (b - a) > eps:
        c = (a + b) / 2
        fc = f(c)
        print(f"{iteration+1:<10} {a:<15.8f} {b:<15.8f} {c:<15.8f} {fc:<15.8f}")
        
        if f(a) * fc < 0:
            b = c
        else:
            a = c
        iteration += 1
    
    return (a + b) / 2, iteration

# Метод хорд
def chord(f, x0, x1, eps=1e-6):
    print("\n--- МЕТОД ХОРД ---")
    print(f"{'Итерация':<10} {'x':<15} {'f(x)':<15}")
    print("-"*40)
    
    iteration = 0
    x_prev = x0
    x_curr = x1
    
    while True:
        f_prev = f(x_prev)
        f_curr = f(x_curr)
        
        x_next = x_curr - f_curr * (x_curr - x_prev) / (f_curr - f_prev)
        iteration += 1
        print(f"{iteration:<10} {x_next:<15.8f} {f(x_next):<15.8f}")
        
        if abs(x_next - x_curr) < eps:
            return x_next, iteration
        
        x_prev = x_curr
        x_curr = x_next

# Метод Ньютона
def newton(f, df, x0, eps=1e-6):
    print("\n--- МЕТОД НЬЮТОНА ---")
    print(f"{'Итерация':<10} {'x':<15} {'f(x)':<15} {'f\'(x)':<15}")
    print("-"*55)
    
    iteration = 0
    x = x0
    
    while True:
        fx = f(x)
        dfx = df(x)
        iteration += 1
        print(f"{iteration:<10} {x:<15.8f} {fx:<15.8f} {dfx:<15.8f}")
        
        x_new = x - fx / dfx
        
        if abs(x_new - x) < eps:
            return x_new, iteration
        
        x = x_new

# Метод простой итерации
def simple_iteration(f, x0, lam, eps=1e-6, max_iter=100):
    print("\n--- МЕТОД ПРОСТОЙ ИТЕРАЦИИ ---")
    print(f"{'Итерация':<10} {'x':<15} {'f(x)':<15} {'x_new':<15}")
    print("-"*55)
    
    iteration = 0
    x = x0
    
    while iteration < max_iter:
        fx = f(x)
        x_new = x - lam * fx
        iteration += 1
        print(f"{iteration:<10} {x:<15.8f} {fx:<15.8f} {x_new:<15.8f}")
        
        if abs(x_new - x) < eps:
            return x_new, iteration
        
        x = x_new
    
    return x, iteration

# Вычисления для 19a
print("\nИнтервал [0.5; 1.2]")
root_bisect, iter_bisect = bisection(f1, 0.5, 1.2)
root_chord, iter_chord = chord(f1, 0.5, 1.2)
root_newton, iter_newton = newton(f1, df1, 0.85)
root_iter, iter_iter = simple_iteration(f1, 0.85, 0.1)

print("\n" + "="*70)
print("РЕЗУЛЬТАТЫ ДЛЯ УРАВНЕНИЯ 19a")
print("="*70)
print(f"Метод половинного деления: x = {root_bisect:.8f}, итераций = {iter_bisect}")
print(f"Метод хорд: x = {root_chord:.8f}, итераций = {iter_chord}")
print(f"Метод Ньютона: x = {root_newton:.8f}, итераций = {iter_newton}")
print(f"Метод простой итерации: x = {root_iter:.8f}, итераций = {iter_iter}")

# ============================================
# УРАВНЕНИЕ 19b: Полином 6-й степени
# ============================================

def f2(x):
    return (x**6 - 0.3*x**5 - 24.57*x**4 - 4.617*x**3 + 
            181.084*x**2 + 85.0306*x - 306.11)

def df2(x):
    return (6*x**5 - 1.5*x**4 - 98.28*x**3 - 13.851*x**2 + 
            362.168*x + 85.0306)

print("\n" + "="*70)
print("УРАВНЕНИЕ 19b: Полином 6-й степени")
print("="*70)

# Вычисления для 19b
print("\nИнтервал [1.0; 1.4]")
root_bisect2, iter_bisect2 = bisection(f2, 1.0, 1.4)
root_chord2, iter_chord2 = chord(f2, 1.0, 1.4)
root_newton2, iter_newton2 = newton(f2, df2, 1.2)
root_iter2, iter_iter2 = simple_iteration(f2, 1.1, 0.0028)

print("\n" + "="*70)
print("РЕЗУЛЬТАТЫ ДЛЯ УРАВНЕНИЯ 19b")
print("="*70)
print(f"Метод половинного деления: x = {root_bisect2:.8f}, итераций = {iter_bisect2}")
print(f"Метод хорд: x = {root_chord2:.8f}, итераций = {iter_chord2}")
print(f"Метод Ньютона: x = {root_newton2:.8f}, итераций = {iter_newton2}")
print(f"Метод простой итерации: x = {root_iter2:.8f}, итераций = {iter_iter2}")

# ============================================
# Сравнительная таблица
# ============================================

print("\n" + "="*70)
print("СРАВНИТЕЛЬНАЯ ТАБЛИЦА ИТЕРАЦИЙ")
print("="*70)
print(f"{'Метод':<25} {'Уравнение 19a':<20} {'Уравнение 19b':<20}")
print("-"*65)
print(f"{'Половинного деления':<25} {iter_bisect:<20} {iter_bisect2:<20}")
print(f"{'Хорд':<25} {iter_chord:<20} {iter_chord2:<20}")
print(f"{'Ньютона':<25} {iter_newton:<20} {iter_newton2:<20}")
print(f"{'Простой итерации':<25} {iter_iter:<20} {iter_iter2:<20}")
print("="*70)
