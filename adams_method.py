import numpy as np
import pandas as pd
import matplotlib.pyplot as plt # side-stepping mpl backend



# Start and end of interval
b=3
a=0
# Step size
N=15
h=(b-a)/(N)
t=np.arange(a,b+h,h)


"""def myfun_ty(t,y):
    return t*y**2


IC = 1 # Intial condtion
y = 2/(2-t**2)"""


"""def myfun_ty(t,y):
    return t-y


IC = 1 # Intial condtion
y = (IC+1)*np.exp(-t)+t-1"""



def myfun_ty(t,y):
    return np.exp(-np.sin(t))-y*np.cos(t)



IC=0 # Intial condtion
y=t*np.exp(-np.sin(t))




### Initial conditions
w=np.zeros(len(t))
w[0]=IC
w[1]=y[1] # NEED FOR THE METHOD


for k in range(1,N):
    w[k + 1] = w[k] + h / 24 * (55 * myfun_ty(t[k], w[k]) - 59 * myfun_ty(t[k - 1], w[k - 1]) + 37 * myfun_ty(t[k-2], w[k-2]) - 9 * myfun_ty(t[k-3], w[k-3]))
    #w[k+1]=w[k]+h/2.0*(3*myfun_ty(t[k],w[k])-myfun_ty(t[k-1],w[k-1]))


def plotting(t,w,y):
    fig = plt.figure(figsize=(10,4))
    plt.plot(t,y, 'o-',color='black',label='Exact')
    plt.plot(t,w,'s:',color='blue',label='Adams')
    plt.xlabel('time')
    plt.legend()
    plt.show()


plotting(t,w,y)

d = {'time t_i': t, 'Adams, w_i': w,'Exact':y,'Error |w-y|':np.round(np.abs(y-w),5)}
df = pd.DataFrame(data=d)
print(df)