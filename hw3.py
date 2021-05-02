import math



def Print_Matrix (A):
    print('The result vector X is:')
    for r in range(len(A)):
        print([A[r][0]])




def Dominant_diagonal_test (A):
    sum = 0
    check = True
    i = 0
    j = 0
    for i in range(len(A)):
        num = abs(A[i][i])
        for j in range(len(A)):
            sum = sum + abs(A[i][j])
        sum = sum - abs(num)
        if num <= sum:
            print("The matrix has no dominant diagonal ")
            return False
    return True

#def Dominant_diagonal_make (A):
    sum = 0
    check = True
    i = 0
    j = 0
    for i in range(len(A)):
        num = abs(A[i][i])
        for j in range(len(A)):
            sum = sum + abs(A[i][j])
        sum = sum - abs(num)
       # if num <= sum:
      #      for k in range(len(A)):







def yaakobi (A, B):
    #if !Dominant_diagonal_test (A):
     #   Dominant_diagonal_make(A):

    Xr = Yr = Zr = 0
    XR1 = YR1 = ZR1 = 0
    num1 = Xr1 = A[0][0]
    num2 =Yr1 = A[1][1]
    num3 =Zr1 =  A[2][2]
    i = 1
    check = False
    XR1 = (B[0][0] + Yr + Zr) / num1
    Yr1 = (B[1][0] + Xr + Zr) / num2
    Zr1 = (B[2][0] + Yr + Xr) / num3
    while check == False :
        print (i,'.','XR+1 =' , XR1 ,',' , 'Yr+1 =' , Yr1 ,',','Zr+1 =' ,Zr1)
        check = (abs(XR1 - Xr) < 0.00001) or (abs(Yr1 - Yr) < 0.00001) or (abs(Zr1 - Zr) < 0.00001)
        Xr = XR1
        Yr = Yr1
        Zr = Zr1
        i+=1

        # Calculation of XR1
        if A[0][1]>0:
            if A[0][2] == 0:
                XR1 = (B[0][0] - Yr ) / num1
            elif A[0][2] < 0:
                XR1 = (B[0][0] - Yr + Zr) / num1
            else:
                XR1 = (B[0][0] - Yr - Zr) / num1

        elif A[0][1]<0:
            if A[0][2] == 0:
                XR1 = (B[0][0] + Yr ) / num1
            elif A[0][2] < 0:
                XR1 = (B[0][0] + Yr + Zr) / num1
            else:
                XR1 = (B[0][0] + Yr - Zr) / num1

        else:
            if A[0][2] == 0:
                XR1 = (B[0][0]) / num1
            elif A[0][2] < 0:
                XR1 = (B[0][0] + Zr) / num1
            else:
                XR1 = (B[0][0] - Zr) / num1

        # Calculation of Yr1
        if A[1][0] > 0:
            if A[1][2] == 0:
                Yr1 = (B[1][0] - Xr) / num2
            elif A[1][2] < 0:
                Yr1 = (B[1][0] - Xr + Zr) / num2
            else:
                Yr1 = (B[1][0] - Xr - Zr) / num2
        elif A[1][0] < 0:
            if A[1][2] == 0:
                Yr1 = (B[1][0] + Xr) / num2
            elif A[1][2] < 0:
                Yr1 = (B[1][0] + Xr + Zr) / num2
            else:
                Yr1 = (B[1][0] + Xr - Zr) / num2
        else:
            if A[1][2] == 0:
                Yr1 = (B[1][0]) / num2
            elif A[1][2] < 0:
                Yr1 = (B[1][0] + Zr) / num2
            else:
                Yr1 = (B[1][0] - Zr) / num2

        # Calculation of Zr1
        if A[2][0] > 0:
            if A[2][1] == 0:
                Zr1 = (B[2][0] - Xr) / num3
            elif A[2][1] < 0:
                Zr1 = (B[2][0] - Xr + Yr) / num3
            else:
                Zr1 = (B[2][0] - Xr - Yr) / num3
        elif A[2][0] < 0:
            if A[2][1] == 0:
                Zr1 = (B[2][0] + Xr) / num3
            elif A[2][1] < 0:
                Zr1 = (B[2][0] + Xr + Yr) / num3
            else:
                Zr1 = (B[2][0] + Xr - Yr) / num3
        else:
            if A[2][1] == 0:
                Zr1 = (B[2][0]) / num3
            elif A[2][1] < 0:
                Zr1 = (B[2][0] + Yr) / num3
            else:
                Zr1 = (B[2][0] - Yr) / num3




def gaus_zaidel(A,B):
    #if !Dominant_diagonal_test(A):
     #   Dominant_diagonal_make(A):

    Xr = Yr = Zr = 0
    XR1 = YR1 = ZR1 = 0
    num1 = Xr1 = A[0][0]
    num2 =Yr1 = A[1][1]
    num3 =Zr1 =  A[2][2]
    i = 1
    check = False
    XR1 = (B[0][0] + Yr + Zr) / num1
    Yr1 = (B[1][0] + Xr + Zr) / num2
    Zr1 = (B[2][0] + Yr + Xr) / num3
    while check == False:
        print (i,'.','XR+1 =' , XR1 ,',' , 'Yr+1 =' , Yr1 ,',','Zr+1 =' ,Zr1)

        Xr = XR1
        Yr = Yr1
        Zr = Zr1
        i+=1

        # Calculation of XR1
        if A[0][1]>0:
            if A[0][2] == 0:
                XR1 = (B[0][0] - Yr ) / num1
            elif A[0][2] < 0:
                XR1 = (B[0][0] - Yr + Zr) / num1
            else:
                XR1 = (B[0][0] - Yr - Zr) / num1

        elif A[0][1]<0:
            if A[0][2] == 0:
                XR1 = (B[0][0] + Yr ) / num1
            elif A[0][2] < 0:
                XR1 = (B[0][0] + Yr + Zr) / num1
            else:
                XR1 = (B[0][0] + Yr - Zr) / num1

        else:
            if A[0][2] == 0:
                XR1 = (B[0][0]) / num1
            elif A[0][2] < 0:
                XR1 = (B[0][0] + Zr) / num1
            else:
                XR1 = (B[0][0] - Zr) / num1

        if abs(XR1 - Xr) < 0.00001:
            check = True
        Xr = XR1

        # Calculation of Yr1
        if A[1][0] > 0:
            if A[1][2] == 0:
                Yr1 = (B[1][0] - Xr) / num2
            elif A[1][2] < 0:
                Yr1 = (B[1][0] - Xr + Zr) / num2
            else:
                Yr1 = (B[1][0] - Xr - Zr) / num2
        elif A[1][0] < 0:
            if A[1][2] == 0:
                Yr1 = (B[1][0] + Xr) / num2
            elif A[1][2] < 0:
                Yr1 = (B[1][0] + Xr + Zr) / num2
            else:
                Yr1 = (B[1][0] + Xr - Zr) / num2
        else:
            if A[1][2] == 0:
                Yr1 = (B[1][0]) / num2
            elif A[1][2] < 0:
                Yr1 = (B[1][0] + Zr) / num2
            else:
                Yr1 = (B[1][0] - Zr) / num2

        if abs(Yr1 - Yr) < 0.00001:
            check = True
        Yr = Yr1

        # Calculation of Zr1
        if A[2][0] > 0:
            if A[2][1] == 0:
                Zr1 = (B[2][0] - Xr) / num3
            elif A[2][1] < 0:
                Zr1 = (B[2][0] - Xr + Yr) / num3
            else:
                Zr1 = (B[2][0] - Xr - Yr) / num3
        elif A[2][0] < 0:
            if A[2][1] == 0:
                Zr1 = (B[2][0] + Xr) / num3
            elif A[2][1] < 0:
                Zr1 = (B[2][0] + Xr + Yr) / num3
            else:
                Zr1 = (B[2][0] + Xr - Yr) / num3
        else:
            if A[2][1] == 0:
                Zr1 = (B[2][0]) / num3
            elif A[2][1] < 0:
                Zr1 = (B[2][0] + Yr) / num3
            else:
                Zr1 = (B[2][0] - Yr) / num3

        if abs(Zr1 - Zr) < 0.00001:
            check = True



# main function
def find_result():

    A = [[3, -1, 1],
         [0, 1, -1],
         [1, 1, -2]]

    B = [[4],
         [-1],
         [-3]]

    X = [[0],
         [0],
         [0]]

    x = input("choose option: 1 to yaakobi and 2 to gaus_zaidel: ")
    if x == '1':
      yaakobi(A,B)
    else:
      gaus_zaidel(A,B)



    #כאן מצאתי את המטריצות D L U  אפשר לעשות את השיטה שלהם אבל לא חייב

    D = A
    for i in range(len(A)):
        for j in range(len(A)):
            if i == j:
               D[i][i] = A[i][i]
            else:
                D[i][j] = 0
                L = A[0][0]
                U = A[0][0]
                if i<j:
                    L = A[i][j]
                    U = A[0][0]
                else:
                    U = A[i][j]
                    L = A[0][0]

find_result()
