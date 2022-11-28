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

