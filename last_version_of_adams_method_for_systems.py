import math
from math import *
import matplotlib.pyplot as plt

"""def functionX(x, y, t):
    return 2 * x + y

def functionY(x, y, t):
    return 3 * x + 4 * y

def ansfunX(t) :
    return math.exp(t) + math.exp(5 * t)

def ansfunY(t) :
    return -1 * math.exp(t) + 3 * math.exp(5 * t)"""


def functionX(x, y, t):
    return log(x+2*sin(t/2)**2)-y/2

def functionY(x, y, t):
    return (4-x**2)*cos(t)-2*x*sin(t)**2-cos(t)**3

def ansfunX(t) :
    return cos(t)

def ansfunY(t) :
    return 2 * sin(t)

def plotting(x, y, t) :
    plt.plot(t, x,  color = 'blue', label = 'xAdams', linewidth = 3.0, marker = ".", markersize = 5)
    plt.plot(t, y,  color='pink', label='exact solution X', linewidth = 2.0, marker = ".", markersize = 5)
    plt.legend()
    plt.show()
def plotting1(ansX, ansY, t):
    plt.plot(t, ansX, color='blue', label='yAdams', linewidth=3.0, marker=".", markersize=5)
    plt.plot(t, ansY, color='pink', label='exact solution Y', linewidth=2.0, marker=".", markersize=5)
    plt.legend()
    plt.show()
# промежуток от 0 до 4
a = 1
b = 4
N = 50
h = (b - a) / N
t = [0.0]
x = [2.0]
y = [2.0]
ansX = []
ansY = []
for i in range (3) :
    x.append(x[i] + h * functionX(x[i], y[i], t[i]))
    y.append(y[i] + h * functionY(x[i], y[i], t[i]))
    t.append(t[i] + h)
    print(f"{t[i]}                    {x[i]}                  {y[i]}")
for i in range (3, N):
    x.append(x[i] + (h / 24) * (55 * functionX(x[i], y[i], t[i]) - 59 * functionX(x[i-1], y[i-1],
    t[i-1]) + 37 * functionX(x[i-2], y[i-2], t[i-2]) - 9 * functionX(x[i-3], y[i-3], t[i-3])))
    y.append(y[i] + (h / 24) * (55 * functionY(x[i], y[i], t[i]) - 59 * functionY(x[i-1], y[i-1],
    t[i-1]) + 37 * functionY(x[i-2], y[i-2], t[i-2]) - 9 * functionY(x[i-3], y[i-3], t[i-3])))
    t.append(t[i] + h)
    print(f"{t[i]}                    {x[i]}                  {y[i]}")

for i in range (N+1) :
    ansX.append(ansfunX(t[i]))
    ansY.append(ansfunY(t[i]))
    print(f"{ansX[i]}       {ansY[i]} ")

plotting(x, ansX, t)
plotting1(y, ansY, t)
