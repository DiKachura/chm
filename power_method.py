"""

5, 0, 0
0, -10, 0
0, 0, 13


2, 0, 3
0, -4, -11
3, -11, 15


13, 7, 4
1, 2, -17
2, 8, -9

"""
import numpy as np

def MaxFabs(v):
    m,n = v.shape
    assert n == 1
    ans = 0
    for i in range(m):
        if ans < np.fabs(v[i]):
            ans = v[i]
            maxn = i
    return ans

def PowerMethod(input,v,g):
    m,n = input.shape
    assert m == n
    times = 0
    u = v/MaxFabs(v)
    v = v.astype(float)  # Set the precision of x
    Lambda = 0
    with open('output.txt', 'w') as f:
        while True:
            tempv = v.copy()
            tempu = u.copy()    # Record the answer of the last iteration
            tempL = Lambda
            v=np.dot(input,u)
            u=v/MaxFabs(v)
            Lambda=MaxFabs(v)
            times += 1    # Number of iterations plus one

            gap = abs(Lambda-tempL)  # Difference from the last answer modulus

            if gap < g:    # Accuracy meets the requirements, end
                break

            elif times > 10000:    # If the iteration exceeds10000Times, over
                break
                print("10000 iterations still does not converge")
                f.write("10000 iterations still does not converge")
        print(times)
        f.write("Количество итераций: ")
        f.write(str(times))
        f.write('\n')
        print(Lambda)
        f.write("Лямбда1: ")
        f.write(str(Lambda))
        f.write('\n')
        f.write("x1: ")
        #print(id(Lambda),id(tempL))
        print(u)
        f.write(str(u))



if __name__ == '__main__':            #When the module is run directly, the following code blocks will be run. When the module is imported, the code blocks will not be run.
    input = np.loadtxt("input", dtype='i', delimiter=',')
    print(input)

    #a = np.array([[1,-1,2],[-2,0,5],[6,-3,6], [5, 8, 5]])

    v = np.array([[1],[1],[1]])

    g=1e-6
    PowerMethod(input,v,g)

