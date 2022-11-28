"""# RK-4 method python program
import numpy as np
from math import *
# function to be solved
def f(x):
    return 1/(1 + pow(x, 2))

def trapezian(left, right, n, function):
    h = (right - left) / (n)

    return (function(left) + function(right) +
        sum(function(left + step * h) for step in range(1, n))) * h


# or
# f = lambda x: x+y

# RK-4 method
def rk4(x0, y0, xn, n):
    # Calculating step size
    h = (xn - x0) / n

    print('\n--------SOLUTION--------')
    print('-------------------------')
    print('x0\ty0\tyn')
    print('-------------------------')
    for i in range(n):
        k1 = h * (f(x0, y0))
        k2 = h * (f((x0 + h / 2), (y0 + k1 / 2)))
        k3 = h * (f((x0 + h / 2), (y0 + k2 / 2)))
        k4 = h * (f((x0 + h), (y0 + k3)))
        k = (k1 + 2 * k2 + 2 * k3 + k4) / 6
        yn = y0 + k
        print('%.4f\t%.4f\t%.4f' % (x0, y0, yn))
        print('-------------------------')
        y0 = yn
        x0 = x0 + h

    print('\nAt x=%.4f, y=%.4f' % (xn, yn))


# Inputs
print('Enter initial conditions:')
x0 = float(input('x0 = '))
y0 = float(input('y0 = '))

print('Enter calculation point: ')
xn = float(input('xn = '))

print('Enter number of steps:')
step = int(input('Number of steps = '))

# RK4 method call
rk4(x0, y0, xn, step)"""



from math import *


def fn(x):
    return sin(x)+cos(x)
    #return 7/(pow(x, 2)+1)

#метод трапеций
def tr_integral(f,xmin,xmax,n):
    dx=(xmax-xmin)/n
    area=0
    x=xmin
    for i in range(n):
        area+=dx*(f(x)+f(x+dx))/2
        x+=dx
    return area


n = 1
e=0.0001
tr1 = tr_integral(fn, 0, pi/4, n)
tr = 0
while(fabs(tr1-tr)/3>e):
    tr = tr1
    n=2*n
    tr1 = tr_integral(fn, 0, pi/4, n)
print("Интеграл = {} достигает нужной точности при n = {}".format(tr1, n))
print("tr_integral = {}".format(tr_integral(fn,0, pi/4,10000)))
#print("tr_integral = {}".format(tr_integral(fn,0, 5,10)))
#Интеграл = 9.613752702493288 достигает нужной точности при n = 64

