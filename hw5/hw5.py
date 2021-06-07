import sympy as sp
import math
import numpy as np
from sympy.utilities.lambdify import lambdify



def eliminate(r1, r2, col, target=0):
    fac = (r2[col]-target) / r1[col]
    for i in range(len(r2)):
        r2[i] -= fac * r1[i]

def gauss (a):
    for i in range(len(a)):
        if a[i][i] == 0:
            for j in range(i+1, len(a)):
                if a[i][j] != 0:
                    a[i], a[j] = a[j], a[i]
                    break
            else:
                raise ValueError("Matrix is not invertible")
        for j in range(i+1, len(a)):
            eliminate(a[i], a[j], i)
    for i in range(len(a)-1, -1, -1):
        for j in range(i-1, -1, -1):
            eliminate(a[i], a[j], i)
    for i in range(len(a)):
        eliminate(a[i], a[i], i, target=1)
    return a

#A function that receives a matrix and returns the inverse matrix using Gauss' elimination method
def find_inv(a):
    tmp = [[] for _ in a]
    for i,row in enumerate(a):
        assert len(row) == len(a)
        tmp[i].extend(row + [0]*i + [1] + [0]*(len(a)-i-1))
    gauss(tmp)
    ret = []
    for i in range(len(tmp)):
        ret.append(tmp[i][len(tmp[i])//2:])
    return ret


def linarit(A,P):
    y1 = 0
    y2 = 0
    x1 = 0
    x2 = 0
    for i in range(len(A)-1):
        if P > A[i][0] and P < A[i+1][0]:
            y1 = A[i][2]
            y2 = A[i+1][2]
            x1 = A[i][1]
            x2 = A[i+1][1]

    result = (y1 - y2)*P/(x1 -x2) + (y2*x1 - y1*x2) / (x1 - x2)
    return result

def polinomit(A,P):
    B = A
    X = [[0],
         [0],
         [0]]
    for i in range(len(A)):
        B[i][0] = 1
        B[i][1] = A[i][1]
        B[i][2] = math.pow(A[i][1],2)
    b = find_inv(B)
    a = [[0.112463],
         [0.167996],
         [0.222709]]

    X = np.matmul(b, a)
    x = sp.symbols('x')
    my_f = X[0][0] + X[1][0] * x + X[2][0] * x ** 2
    my_f = lambdify(x, my_f)
    result = my_f(P)
    return result

def lagranz(A,P):
    x = sp.symbols('x')
    x0 = A[0][1]
    x1 = A[1][1]
    x2 = A[2][1]

    l0 = ((x - x1)/(x0 - x1)) * ((x - x2)/(x0 - x2))
    l1 = ((x - x0) / (x1 - x0)) * ((x - x2) / (x1 - x2))
    l2 = ((x - x0) / (x2 - x0)) * ((x - x1) / (x2 - x1))

    my_f = l0 * A[0][2] + l1 * A[1][2] + l2 * A[2][2]
    my_f = lambdify(x, my_f)
    return my_f(P)


def nevil(A,P):
    x = sp.symbols('x')
    x0 = A[0][1]
    x1 = A[1][1]
    x2 = A[2][1]
    y0 = A[0][2]
    y1 = A[1][2]
    y2 = A[2][2]
    p12 = ((x - x0)*y1 - (x-x1)*y0)/(x1 - x0)
    p23 = ((x - x1)*y2 - (x-x2)*y1)/(x2 - x1)
    p12 = lambdify(x, p12)
    p23 = lambdify(x, p23)
    p13 = ((x - x0)*p23(P) - (x-x2)*p12(P))/(x2 - x0)
    p13 = lambdify(x, p13)
    return p13(P)


def main():

    A = [[1, 1.2, 0.112463],
         [2, 1.3, 0.167996],
         [3, 1.4, 0.222709]]

    P = 1.28
    check = input("choose option: 1 to linarit, 2 to polinomit, 3 to lagranz, 4 to nevil ")
    if check == '1':
        print(round(linarit(A, P),4))

    elif check == '2':
        print(round(polinomit(A, P), 5))

    elif check == '3':
        print(round(lagranz(A, P), 5))

    else:
        print(round(nevil(A, P), 5))

main()