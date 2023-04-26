import math
from math import *
import matplotlib.pyplot as plt
def f(x):
    #return -x
    return x*(x-1)
def p(x):
    #return 0
    return x
def q(x):
    #return 1
    return x**2
def ans(x):

    return sin(x)/sin(1)-x
def plotting(x, y, ansY) :
    plt.plot(x, y,  color = 'blue', label = 'method progonki', linewidth = 3.0, marker = ".", markersize = 5)
    plt.plot(x, ansY,  color = 'pink', label = 'exact solution', linewidth = 2.0, marker = ".", markersize = 5)
    plt.legend()
    plt.show()

"""A = 0
B = 0"""


A = 0
B = 0


a = 0
b = 1
x = [0.000]
y = []
m = []
k = []
n = 150
h = (b-a)/n
# прямой ход
for i in range(n-1):
    m.append(-2 + h * p(x[i]))
    k.append(1 - h * p(x[i]) + h ** 2 * q(x[i]))
    x.append(x[i] + h)
c = []
d = []
c.append((-h)/(m[0]*(-h)))
d.append((k[0]*A*h)/(-h) + f(x[0]) * (h**2))
for i in range(1, n-1):
    c.append(1/(m[i]-k[i]*c[i-1]))
    d.append(f(x[i]) * (h**2) - k[i] * c[i-1] * d[i-1])

# обратный ход
y.append((B*h)/h)
for i in range(n-2):
    y.append(c[n-2-i] * (d[n-2-i] - y[i]))
y.append((A*h)/h)
y.reverse()
print(y)
ansY = []
for i in range(n):
    ansY.append(ans(x[i]))
plotting(x, y, ansY)