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
