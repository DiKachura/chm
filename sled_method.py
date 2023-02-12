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


-3, 4, -2
1, 0, 1
6, -6, 5


1, -2, 2
1, 4, -2
1, 5, -3


2, 1, 1
1, 2, 1
1, 1, 2


"""

def diag(input):
    diag = 0
    for i in range(len(input)):
        diag += input[i][i]
    return diag

def SledMethod(input, g):
    print("Метод следов")
    times = 0
    predA = input

    Lambda = 0

    with open('output.txt', 'w') as f:
        f.write("Метод следов: \n")
        while True:

            tempL = Lambda

            #A = predA@input
            length = len(input)
            A = [[0 for i in range(length)] for i in range(length)]
            for i in range(length):
                for j in range(length):
                    for k in range(length):
                        A[i][j] += predA[i][k] * input[k][j]


            Lambda = diag(A)/diag(predA)

            predA = A

            times += 1

            gap = abs(Lambda - tempL)  # Difference from the last answer modulus


            if gap < g:  # Accuracy meets the requirements, end
                break

            elif times > 10000:  # If the iteration exceeds10000Times, over
                break
                print("10000 iterations still does not converge")
                f.write("10000 iterations still does not converge ")

        print(times)
        f.write("Количество итераций: ")
        f.write(str(times))
        f.write('\n')
        print(Lambda)
        f.write("Лямбда: ")
        f.write(str(Lambda))
        f.write('\n')


if __name__ == '__main__':
    with open('input', 'r') as f:
        input = [[int(num) for num in line.split(',')] for line in f]

    g=1e-8
    SledMethod(input, g)
