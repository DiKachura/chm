import numpy as np
import matplotlib.pyplot as plt


k = 1
L = 1
T = 1
dx = 0.1
dt = 0.01


x = np.arange(0, L+ dx, dx)
t = np.arange(0, T+dt, dt)
r = len(t)
n = len(x)
w = np.zeros([r, n])

#w[0] = np.sin(np.pi * x)
w[0] = 1


a = np.zeros(n)
b = np.zeros(n)
c = np.zeros(n)
d = np.zeros(n)

'''a[1] = 0
b[1] = 1
c[1] = 0
d[1] = 0

a[-1] = 0
b[-1] = 1
c[-1] = 0
d[-1] = dx'''

a[1] = 0
b[1] = 1
c[1] = 0
d[1] = 0

a[-1] = 0
b[-1] = 1
c[-1] = 0
d[-1] = t[0]/2


'''a[1] = 0
b[1] = 1
c[1] = 0
d[1] = 0

a[-1] = 0
b[-1] = 1
c[-1] = 0
d[-1] = 0'''

for j in range(1, r):
    for i in range(1, n-1):
        a[i] = - k * dt / dx**2
        b[i] = 1 + 2 * k * dt / dx**2
        c[i] = - k * dt / dx**2
        d[i] = w[j-1, i]


    d[-1] = d[-2] + dx


    for i in range(2, n):
        m = a[i]/b[i-1]
        b[i] = b[i] - m*c[i-1]
        d[i] = d[i] - m*d[i-1]

    w[j][-1] = d[-1] / b[-1]
    for i in range(n-2, 0, -1):
        w[j][i] = (d[i] - c[i]*w[j][i+1])/b[i]



x, t = np.meshgrid(x, t)
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(x, t, w, cmap='viridis')
ax.set_xlabel('x')
ax.set_ylabel('t')
ax.set_zlabel('u')
plt.show()

