import numpy as np
import matplotlib.pyplot as plt
import math

def f(t, y):
    return np.array([y[0] + y[2] - y[1], y[0] + y[1] - y[2], 2 * y[0] - y[1]])
def exact_solution(t):
    return np.array([math.e**t + math.e**(2*t) + math.e**(-t), math.e**t - 3 * math.e**(-t), math.e**t + math.e**(2*t) - 5 * math.e**(-t)])
"""def f(t, y):
    '''
    -2x+4y
    -x+3y
    x(0)=3
    y(0)=0
    '''
    return np.array([-2*y[0]+4*y[1],-y[0]+3*y[1]])


def exact_solution(t):
    return np.array([4*math.e**(-t) - math.e**(2*t), math.e**(-t) - math.e**(2*t)])"""

'''def f(t, y):
    return np.array([2*y[0]+y[1],y[0]+2*y[1]])
def exact_solution(t):
    return np.array([2*math.e**(3*t) - math.e**(t), 2*math.e**(3*t) + math.e**(t)])'''

'''def f(t, y):
    return np.array([np.log(y[0]+2*np.sin(t/2)*np.sin(t/2))-y[1]/2,(4-y[0]**2)*np.cos(t)-2*y[0]*np.sin(t)*np.sin(t)-np.cos(t)*np.cos(t)*np.cos(t)])
def exact_solution(t):
    return np.array([np.cos(t), 2*np.sin(t)])'''


def Adams4(f, y0, t0, tf, h):
    t = np.arange(t0, tf+h, h)
    n = len(t)
    y = np.zeros((n, len(y0)))
    y[0] = y0
    for i in range(4):
        k1 = f(t[i], y[i])
        k2 = f(t[i]+h/2, y[i]+h/2*k1)
        k3 = f(t[i]+h/2, y[i]+h/2*k2)
        k4 = f(t[i]+h, y[i]+h*k3)
        y[i+1] = y[i] + h/6*(k1 + 2*k2 + 2*k3 + k4)

    for i in range(3, n-1):
        y[i+1] = y[i] + h/24*(55*f(t[i], y[i]) - 59*f(t[i-1], y[i-1]) + 37*f(t[i-2], y[i-2]) - 9*f(t[i-3], y[i-3]))
    return t, y


y0 = np.array([3, -2, -3])
'''y0 = np.array([3, 0])'''
'''y0 = np.array([1, 3])'''

t, y = Adams4(f, y0, 0, 1, 0.1)
exact = np.array([exact_solution(ti) for ti in t])
#error = np.abs(exact - y)
#error = np.linalg.norm(exact - y)
error = np.max(np.abs(exact - y))

t1, y1 = Adams4(f, y0, 0, 1, 0.05)
exact1 = np.array([exact_solution(ti) for ti in t1])
#error1 = np.abs(exact1 - y1)
#error1 = np.linalg.norm(exact1 - y1)
error1 = np.max(np.abs(exact1 - y1))
#print(error[1:]/error1[1::2])
print(error/error1)

print(np.log2(error/error1))
plt.figure(figsize=(10,5))


plt.plot(t, y[:,0], label='Numerical (h=0.1)')
plt.plot(t1, y1[:,0], label='Numerical (h=0.05)')

t_exact = np.linspace(0,1,1000)
exact = np.array([exact_solution(ti) for ti in t_exact])
plt.plot(t_exact, exact[:,0], label='Exact')

plt.legend()
plt.xlabel('t')
plt.ylabel('y')
plt.title('Adams 4 (h=0.1, 0.05) vs Exact')
plt.show()
