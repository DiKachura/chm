import matplotlib.pyplot as plt
import numpy as np



n = 10
#754
'''a = 0
b = np.pi/2
k1 = 1
a1 = 0
l1 = 1
b1 = 0'''

#755
'''a = 0
b = np.pi
k1 = 1
a1 = 0
l1 = 1
b1 = 0'''

#749
a = 0
b = 1
k1 = 1
a1 = 0
l1 = 1
b1 = -1


def p(t):
   #return 0
   #return 0
   return 0



def g(t):
    #return 1
    #return 1
    return -1


def f(t):
    #return 1
    #return 2*t-np.pi
    return 2 * t

def yt(t):
    #return -np.cos(t) - np.sin(t)+1
    #return 2*t-np.pi+np.pi*np.cos(t)
    return np.e**(t+1)/(np.e**2-1) - np.e**(-t+1)/(np.e**2-1) - 2 * t




h = (b - a) / n


t = np.zeros(n+1)
aa = np.zeros(n+1)
bb = np.zeros(n+1)
cc = np.zeros(n+1)
ff = np.zeros(n+1)
for i in range(n+1):
    t[i] = a + h * i
    aa[i] = 1 - p(t[i]) * h / 2
    bb[i] = 1 + p(t[i]) * h / 2
    cc[i] = 2 - g(t[i]) * h ** 2
    ff[i] = h ** 2 * f(t[i])


al = np.zeros(n+1)
bet = np.zeros(n+1)

bet[1] = -a1 * h / (- k1 * h)


for i in range(1, n):
    al[i+1] = bb[i] / (cc[i] - al[i] * aa[i])
    bet[i+1] = (aa[i] * bet[i] - ff[i]) / (cc[i] - al[i] * aa[i])


u = np.zeros(n+1)
u[n] = (b1 * h) / (h * l1)


for i in range(n-1, -1, -1):
    u[i] = al[i+1] * u[i+1] + bet[i+1]


print('{:<4} {:<10} {:<10} {:<10} {:<10}'.format('i', 't[i]', 'y[i]', 'yt(t[i])', 'Погрешн.'))
epsmax = 0
for i in range(n+1):
    eps = abs(u[i] - yt(t[i]))
    if eps > epsmax:
        epsmax = eps
    print('{:<4} {:<10.4f} {:<10.4f} {:<10.4f} {:<10.4f}'.format(i, t[i], u[i], yt(t[i]), eps))

print('Максимальная погрешность =', epsmax)


plt.plot(t, u, label='u(t)')
plt.plot(t, yt(t), label='yt(t)')
plt.legend()
plt.show()
