import sympy as sp
import math
from sympy.utilities.lambdify import lambdify
import sympy

def find_derivative(my_f):

    x = sp.symbols('x')
    f_prime = my_f.diff(x)
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





def Newton_Raphson (my_f,start_point,end_point,epsilon):
    x = sp.symbols('x')
    f = my_f
    f = lambdify(x, f)
    A = [-1] * 20
    index = 0
    i = 1
    x = 0.1
    temp_start = start_point
    temp_end = start_point + x
    while round(temp_end,2) <= round(end_point,2):
        result = (temp(my_f, temp_start, temp_end, epsilon))
        if result == 0:
            if f(0)== 0:
                A[index] = result
                index += 1
        else:
            if result >= temp_start and result <= temp_end:
                A[index] = result
                index += 1

        temp_start = temp_end
        temp_end = temp_end+x
        i += 1
    print("\nAll the intersection points : ")
    print_result(A)





def temp (my_f,start_point,end_point,epsilon):

    i = 1
    x = sp.symbols('x')
    f = my_f
    f_prime = find_derivative(my_f)
    f = lambdify(x, f)
    f_prime = lambdify(x, f_prime)
    xr = (start_point + end_point) / 2
    if f_prime(xr) == 0.0:
        return -1
    xr1 = xr - (f(xr) / f_prime(xr))
    print("i    xr                      f(xr)                  f'(xr)")
    while abs(xr1-xr) > epsilon:
        if (f'{xr:.2f}'[:-1]) == '0.0' or (f'{xr:.2f}'[:-1]) == '-0.0':
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
    A = [-1] * 20
    index = 0
    i = 1
    chek_point0 = False
    x = 0.1
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
                if result >= start_point and result <= end_point :
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

    start_point = -1
    end_point = 1.5
    epsilon = 0.00001
    my_f = (sympy.sin(2 * x * 3 + 5 * x * 2 - 6)) / (2 * math.e ** (-2 * x))

    check = input("choose option: 1 to Newton_Raphson, 2 to secant_method ")
    if check == '1':
        Newton_Raphson(my_f, start_point, end_point, epsilon)
    else:
        secant_method(my_f, start_point, end_point, epsilon)





main()