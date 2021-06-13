stopCalc = 0.00001
def gauss_Seidel(a, b):
    """
    find the solution with Gauss Seidel methode only for 3*3 matrix
    :param a: coefficient matrix
    :param b: result matrix
    :return: result of x,y,z
    """
    count = 1
    x0, y0, z0 = 0, 0, 0
    x1, y1, z1 = 0, 0, 0
    # chek if There is a dominant diagonal
    if a[0][0] > abs(a[0][1]) + abs(a[0][2]) and \
            a[1][1] > abs(a[1][0]) + abs(a[1][2]) and \
            a[2][2] > abs(a[2][0]) + abs(a[2][1]):
        stopCondition = True
        f1 = lambda y, z: (b[0] - y * a[0][1] - z * a[0][2]) / a[0][0]
        f2 = lambda x, z: (b[1] - x * a[1][0] - z * a[1][2]) / a[1][1]
        f3 = lambda x, y: (b[2] - x * a[2][0] - y * a[2][1]) / a[2][2]
        while stopCondition:
            x1 = f1(y0, z0)
            y1 = f2(x1, z0)
            z1 = f3(x1, y1)
            print('Iteration num %d:\tx=%0.7f\ty=%0.7f\tz=%0.7f\n' % (count, x1, y1, z1))
            error1 = abs(x0 - x1)
            error2 = abs(y0 - y1)
            error3 = abs(z0 - z1)
            count += 1
            x0 = x1
            y0 = y1
            z0 = z1
            stopCondition = error1 > stopCalc and \
                            error2 > stopCalc and \
                            error3 > stopCalc
    else:
        print("In the matrix there is no dominant diagonal")
    print('Total iteration for find the result %d\n' % count)
    return x1, y1, z1


def Jacobi(a, b):
    """
    find the solution with jacobi methode only for 3*3 matrix
    :param a: coefficient matrix
    :param b: result matrix
    :return: result of x,y,z
    """
    count = 1
    x0, y0, z0 = 0, 0, 0
    # chek if There is a dominant diagonal
    x1, y1, z1 = 0, 0, 0
    if a[0][0] > abs(a[0][1]) + abs(a[0][2]) and \
            a[1][1] > abs(a[1][0]) + abs(a[1][2]) and \
            a[2][2] > abs(a[2][0]) + abs(a[2][1]):
        stopCondition = True
        f1 = lambda y, z: (b[0] - y * a[0][1] - z * a[0][2]) / a[0][0]
        f2 = lambda x, z: (b[1] - x * a[1][0] - z * a[1][2]) / a[1][1]
        f3 = lambda x, y: (b[2] - x * a[2][0] - y * a[2][1]) / a[2][2]
        while stopCondition:
            x1 = f1(y0, z0)
            y1 = f2(x0, z0)
            z1 = f3(x0, y0)
            print('Iteration num %d:\tx=%0.7f\ty=%0.7f\tz=%0.7f\n' % (count, x1, y1, z1))
            error1 = abs(x0 - x1)
            error2 = abs(y0 - y1)
            error3 = abs(z0 - z1)
            count += 1
            x0 = x1
            y0 = y1
            z0 = z1
            stopCondition = error1 > stopCalc and \
                            error2 > stopCalc and \
                            error3 > stopCalc
    return x1, y1, z1


"""----------------main----------------------"""
A = [[0.04, 0.01, -0.01], [0.2, 0.5, -0.2], [1, 2, 4]]
B = [0.06, 0.3, 11]
x = input("Which way would you like to use?\nGauss Seidel enter 1\nYaakobi enter 2\n")
if int(x) == 1:
    print('the result with Gauss Seidel is: x=%0.4f\ty=%0.4f\tz=%0.4f\n' % (gauss_Seidel(A, B)))
elif int(x) == 2:
    print('the result with Gauss Seidel is: x=%0.4f\ty=%0.4f\tz=%0.4f\n' % (Jacobi(A, B)))
else:
    print("Wrong choice.\nRun again")
