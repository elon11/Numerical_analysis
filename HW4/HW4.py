import sympy as sp
import math
from sympy.utilities.lambdify import lambdify


def find_derivative():

    x = sp.symbols('x')
    my_f = x ** 4 + x ** 3 - 3 * x ** 2

    my_f1 = sp.diff(my_f, x)
    d1 = sp.diff(my_f1)

    f = x ** 4 + x ** 3 - 3 * x ** 2

    f_prime = f.diff(x)
    return f_prime

def print_result(A):
    B = [-1] * 10
    index = 0
    check = True
    for num in A:
        check = True
        for x in B:
            if  round(float(num),2) ==  round(float(x),2):
                check = False
        if check:
            B[index] = num
            index+=1

    if A[0]== -1:
        print("There are no intersections in the field")
    else:
        for num in B:
            if num != -1:
                print(round(float(num), 2))



def stop_iter(start, end):
    x = math.log(((10**(-10))/(end - start)),math.e)
    y = math.log(2,math.e)
    return -x/y+1

def find_point(a,b):
    x = sp.symbols('x')
    f = x ** 4 + x ** 3 - 3 * x ** 2

    f = lambdify(x, f)
    i = 1
    c = 0
    epsilon = 0.00001
    print("\n")
    print("i                  a                          b                          c                           f(a)                               f(b)                        f(c)")
    while abs(float(b)-float(a))>epsilon:
        c = (a + b) / 2
        Fa = f(a)
        Fb = f(b)
        Fc = f(c)
        print(i, "       ", a, "       ", b, "       ", c, "           ", Fa, "           ", Fb, "          ", Fc)
        if Fa * Fc > 0:
            a = c
        elif Fa * Fc < 0:
            b = c
        else:
            return 0

        i+=1
    print("\n")
    return b



def Bisection_Method(my_f,start_point,end_point,epsilon):
    x = sp.symbols('x')
    f = my_f
    f = lambdify(x, f)
    temp = start_point
    index = 0
    A = [-1]*10
    i = 1
    g = 0
    result = 0
    print("i                 x                           f(x)")
    while(start_point <= end_point) :
        if i > stop_iter(start_point, end_point) and A[0] == -1:
            print("The function does not match the crossing method")
            return
        else:
            g = f(start_point)
            if i >1:
                if (float(g) > 0 and float(result) < 0) or (float(g) < 0 and float(result) > 0)or (float(g) > 0 and float(result) == 0)or(float(g) == 0 and float(result) < 0)or(float(g) < 0 and float(result) == 0)or(float(g) == 0 and float(result) > 0):
                    A[index] = find_point(start_point,start_point -0.1)
                    print("\n\ni                 x                                    f(x)")
                    index+=1


            print(i ,"              ",start_point ,"                  ",f'{g:.2f}'[:-1])
            result = g

            if round(start_point,2) == -0.10:
                start_point = 0.0
            else:
                start_point = start_point+0.1
            i+=1
    print("\n\n")
    print("The intersection points using a function: ")
    print_result(A)
    print("\n\n")
    print("********** Finding intersection points using a derivative **********\n\n\n")

    f_prime = find_derivative()
    f_prime = lambdify(x, f_prime)
    start_point = temp


    i = 1
    g = 0
    result = 0
    print("i                 x                     f'(x)")
    while (start_point <= end_point):
        g = f_prime(start_point)
        if i > 1:
            if (f'{start_point:.2f}'[:-1]) == '0.0':
                if (float(f_prime(0.1)) > 0 and float(f_prime(-0.1)) < 0) or (float(f_prime(0.1)) < 0 and float(f_prime(-0.1)) > 0):
                    if f(find_point(- 0.1, 0.1)) == 0:

                        A[index] = 0
                        index += 1
                    print("\n\ni                 x                                    f(x)")

            else:
                if (float(g) > 0 and float(result) < 0) or (float(g) < 0 and float(result) > 0):
                    if f(find_point(start_point, start_point - 0.1)) ==0:
                        A[index] = find_point(start_point, start_point - 0.1)
                        index += 1
                    print("\n\ni                 x                                    f(x)")

        print(i, "              ", start_point, "                  ", f'{g:.2f}'[:-1])
        result = g

        start_point = start_point + 0.1
        i += 1
    print("\nAll the intersection points : ")
    print_result(A)



def Newton_Raphson (my_f,start_point,end_point,epsilon):
    x = sp.symbols('x')
    f = my_f
    f = lambdify(x, f)
    A = [-1] * 10
    index = 0
    i = 1
    x = (abs(start_point)+abs(end_point))/3
    temp_start = start_point
    temp_end = start_point + x
    while i<4:
        result = (temp(my_f, temp_start, temp_end, epsilon))
        if result == 0:
            if f(0)== 0:
                A[index] = result
                index += 1
        else:
            A[index] = result
            index += 1

        temp_start =  temp_end
        temp_end = temp_end+x
        i += 1
    print("\nAll the intersection points : ")
    print_result(A)





def temp (my_f,start_point,end_point,epsilon):

    i = 1
    x = sp.symbols('x')
    f = my_f
    f_prime = find_derivative()
    f = lambdify(x, f)
    f_prime = lambdify(x, f_prime)
    xr = (start_point + end_point) / 2
    if f_prime(xr) == 0.0:
        return -1
    xr1 = xr - (f(xr) / f_prime(xr))
    print("i    xr                      f(xr)                  f'(xr)")
    while  abs(xr1-xr) > epsilon:
        if (f'{xr:.2f}'[:-1]) == '0.0' or (f'{xr:.2f}'[:-1]) == '-0.0' :
            return 0
        xr = xr1
        print(i,"   ",xr,"                  ",f(xr),"                  ", f_prime(xr))
        xr1 = xr - (f(xr) / f_prime(xr))
        i += 1
    return xr





def secant_method(my_f, start_point, end_point, epsilon):
    x = sp.symbols('x')
    f = my_f
    f = lambdify(x, f)
    A = [-1] * 10
    index = 0
    i = 1
    chek_point0 = False
    x = (abs(start_point) + abs(end_point)) / 4
    temp_start = start_point
    temp_end = start_point + x
    while temp_end <= end_point:
        result = (temp2(my_f, temp_start, temp_end, epsilon))
        if result == 0 and  chek_point0 == False:
            if f(0) == 0:
                A[index] = result
                index += 1
                chek_point0 = True
        else:
            if result != 0:
                A[index] = result
                index += 1


        temp_start = temp_end
        temp_end = temp_end + x
        i += 1
    print("\nAll the intersection points : ")
    print_result(A)

def temp2 (my_f,start_point,end_point,epsilon):
    i = 1
    x = sp.symbols('x')
    f = my_f
    f = lambdify(x, f)
    xr = start_point
    xr1 = end_point
    print("i    xr                                xr1                                               f(xr)")
    while  abs(xr1-xr) > epsilon:

        if (f'{xr:.2f}'[:-1]) == '0.0' or (f'{xr:.2f}'[:-1]) == '-0.0' :
            return 0
        print(i,"   ",xr,"                         ",xr1,"                                  ", f(xr))
        temp = xr1
        xr1 = (xr * f(xr1) - xr1 * f(xr))/(f(xr1) - f(xr))
        xr = temp

        i += 1

    return xr






def main():
    x = sp.symbols('x')
   # my_f = (math.pow((2 * x * math.e), -x) + math.log(2, 2 * math.pow(x, 2))) * (
              #  2 * (math.pow((x, 3))) + 2 * (math.pow((x, 2))) - 3 * x - 5)
   # my_f = x ** 4 + x ** 3 - 3 * x ** 2

    log = math.log
    e = math.e
    a = lambda x: 2 * x * (e ** (-x))
    b = lambda x: log(e, 2 * (x ** 3))
    c = lambda x: 2 * (x ** 3)
    d = lambda x: 2 * (x ** 2)

    my_f = lambda x: (a + b) * (c + d - (3 * x) - 5)
    start_point = 0
    end_point = 1.5
    jump = 0.1
    epsilon = 0.00001
    check = input("choose option: 1 to Bisection_Method, 2 to Newton_Raphson, 3 to secant_method ")
    if check == '1':
        Bisection_Method(my_f,start_point,end_point,epsilon)

    elif check == '2':
        Newton_Raphson(my_f, start_point, end_point, epsilon)

    else:
        secant_method(my_f, start_point, end_point, epsilon)





main()