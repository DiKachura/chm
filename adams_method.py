"""import numpy as np
import matplotlib.pyplot as plt

# Задаем начальные условия
y0 = 1
x0 = 0

# Задаем шаг и количество итераций
h = 0.1
N = 10

# Задаем функцию правой части дифференциального уравнения
def f(x, y):
    return -2*x*y**2

# Задаем массивы для решений методом Рунге-Кутты и явным методом Адамса
x_rk = [x0] * (N + 1)
y_rk = [y0] * (N + 1)
y_ad4 = [y0] * (N + 1)

# Решаем методом Рунге-Кутты
for i in range(N):
    K1 = h * f(x_rk[i], y_rk[i])
    K2 = h * f(x_rk[i] + h/2, y_rk[i] + K1/2)
    K3 = h * f(x_rk[i] + h/2, y_rk[i] + K2/2)
    K4 = h * f(x_rk[i] + h, y_rk[i] + K3)
    y_rk[i+1] = y_rk[i] + 1/6 * (K1 + 2*K2 + 2*K3 + K4)
    x_rk[i+1] = x_rk[i] + h

# Решаем методом Адамса 4-го порядка
for i in range(3, N):
    y_ad4[i+1] = y_ad4[i] + h/24 * (55*f(x_rk[i], y_ad4[i]) - 59*f(x_rk[i-1], y_ad4[i-1]) + 37*f(x_rk[i-2], y_ad4[i-2]) - 9*f(x_rk[i-3], y_ad4[i-3]))

# Сравниваем решения с шагом h и h/2
h2 = h/2
N2 = 2*N
x_rk2 = [x0] * (N2 + 1)
y_rk2 = [y0] * (N2 + 1)
y_ad4_2 = [y0] * (N2 + 1)
for i in range(N2):
    K1 = h2 * f(x_rk2[i], y_rk2[i])
    K2 = h2 * f(x_rk2[i] + h2/2, y_rk2[i] + K1/2)
    K3 = h2 * f(x_rk2[i] + h2/2, y_rk2[i] + K2/2)
    K4 = h2 * f(x_rk2[i] + h2, y_rk2[i] + K3)
    y_rk2[i+1] = y_rk2[i] + 1/6 * (K1 + 2*K2 + 2*K3 + K4)
    x_rk2[i+1] = x_rk2[i] + h2
for i in range(3, N2):
    y_ad4_2[i+1] = y_ad4_2[i] + h2/24 * (55*f(x_rk2[i], y_ad4_2[i]) - 59*f(x_rk2[i-1], y_ad4_2[i-1]) + 37*f(x_rk2[i-2], y_ad4_2[i-2]) - 9*f(x_rk2[i-3], y_ad4_2[i-3]))

# Строим график
#plt.plot(x_rk, y_rk,'o-', label='Метод Рунге-Кутты')
plt.plot(x_rk, y_ad4, 'o-', label='Явный метод Адамса 4-го порядка (h)')
plt.plot(x_rk2, y_ad4_2, 'o-', label='Явный метод Адамса 4-го порядка (h/2)')
plt.title('Решения методом Рунге-Кутты и явным методом Адамса 4-го порядка')
plt.legend()
plt.show()

# Оцениваем порядок точности метода Адамса 4-го порядка
e_h = np.abs(y_ad4[::2] - y_rk[::2]).max()
e_h2 = np.abs(y_ad4_2 - y_rk2[::2]).max()
p = np.log2(e_h2 / e_h)
print('Порядок точности метода Адамса 4-го порядка:', p)"""


import numpy as np
import matplotlib.pyplot as plt

# правая часть диффура
def f(x,y):
    return np.exp(-np.sin(x))-y*np.cos(x)

# точное решение
def y_exact(x):
    return x*np.exp(-np.sin(x))

# метод Адамса 4-шаговый
def Adams4(x,y,h):
    n = len(x)
    for i in range(3, n-1):
        y[i+1] = y[i] + h/24 * ( 55 * f(x[i], y[i]) - 59 * f(x[i-1], y[i-1]) + 37 * f(x[i-2], y[i-2]) - 9 * f(x[i-3], y[i-3]))
    return y

a = 0
b = 3
h = 0.1  # шаг
n = int((b - a) // h + 1)  # количество точек

x = np.linspace(a,b,n)
y = np.zeros(n)
y[0] = 0

# решение с шагом h
y1 = Adams4(x,y,h)
# решение с шагом h/2
n = int((b - a) // (h / 2) + 1)  # количество точек
x2 = np.linspace(a,b,n)
y2 = np.zeros(n)
y2[0] = 0
y2 = Adams4(x2,y2,h/2)
y_exact1 = y_exact(x)  # точное решение
y_exact2 = y_exact(x2)
err_norm1 = np.max(np.abs(y1 - y_exact1))
err_norm2 = np.max(np.abs(y2 - y_exact2))
print(f'Порядок точности для шага h: {np.log2(err_norm1 / err_norm2)}')

# рисуем графики
plt.plot(x, y_exact1,'r',label='Точное решение')
plt.plot(x, y1,'b',label=f'Численное решение с шагом {h:.1f}')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.legend()
plt.title('Численное решение ОДУ методом Адамса (4-шаговый)')
plt.show()

plt.plot(x2, y_exact2,'r',label='Точное решение')
plt.plot(x2, y2,'b',label=f'Численное решение с шагом {h/2:.2f}')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.legend()
plt.title('Численное решение ОДУ методом Адамса (4-шаговый)')
plt.show()
