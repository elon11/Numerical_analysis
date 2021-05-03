def Dominant_diagonal_test (A):
    sum1 = 0
    i = 0
    temp = [[abs(A[j][i]) for i in range(len(A))]for j in range(len(A[0]))]
    for i in range(len(A[0])):
        sum1 = sum(temp[i])
        if ((sum1 - temp[i][i])>temp[i][i]):
            print("The matrix has no dominant diagonal ")
            return False
    return True

def convert_to_diagonally_dominant(A):

    if len(A[0]) != len(A):
        raise TypeError("can't convert non-square matrix to diagonally dominant matrix")

    # convert all values in matrix to abs values
    abs_matrix = [[abs(A[j][i]) for i in range(len(A))]for j in range(len(A[0]))]

    # list of new indexes for swap
    swap_list = []

    for i in range(len(abs_matrix[0])):

        # get values of row i
        row = abs_matrix[i]

        # find max value and his index
        max_value = max(row)
        max_value_index = row.index(max_value)

        # check if max value is bigger then sum of all other cells in the row
        if max_value < (sum(row) - max_value):
            # if not, than cant convert this matrix to diagonally_dominant matrix
            return None

        # else, store index of maximum value into swap list at the index of i
        swap_list.append(max_value_index)

    # check if there is diff max value in 2 different columns
    # each index should appear only one time.
    if len(set(swap_list)) != len(swap_list):
        return None

    # copy org matrix
    res_matrix = A.copy()
    # swap rows in the res matrix
    for i, j in enumerate(swap_list):
        swap(res_matrix,i, j)
    return res_matrix



def swap(A, i1, i2):
     # Function that swap beetween two rows.
    if i1 == i2:
        return
    A[i1], A[i2] = A[i2], A[i1]











def yaakobi (A, B):
    #if !Dominant_diagonal_test (A):
     #   Dominant_diagonal_make(A):

    # keep diag value
    diag = [A[i][i] for i in range(len(A[0]))]
    c = [B[i][0]/diag[i] for i in range(len(A[0]))]
    Xr = [0 for i in range(len(A[0]))]

    # an initial guess
    Xr1 = [(B[i][0]+sum(Xr)-Xr[i])/diag[i] for i in range(len(A[0]))]
    dist = lambda V , T : max([abs(V[i]-T[i]) for i in range(len(A[0]))])
    dot = lambda V, T : [V[i]*T[i] for i in range (len(A[0]))]
    eps = 0.00001
    i = 1
    print (dist(Xr1,Xr))
    while dist(Xr1,Xr)>eps :
        line_format = ",".join(["Xr[%s] = %s" % (j,Xr1[j]) for j in range(len(A[0]))])
        print (i,'.',line_format)
        # organ promotion
        Xr = Xr1
        i+=1
        # Calculation of Xr1
        Xr1 = [c[i]-(sum(dot(A[i],Xr))/diag[i]) + Xr[i] for i in range(len(A[0]))]


def gaus_zaidel(A,B):
    # keep diag value
    diag = [A[i][i] for i in range(len(A[0]))]
    c = [B[i][0] / diag[i] for i in range(len(A[0]))]
    Xr = [0 for i in range(len(A[0]))]

    # an initial guess
    Xr1 = [(B[i][0] + sum(Xr) - Xr[i]) / diag[i] for i in range(len(A[0]))]
    dist = lambda V, T: max([abs(V[i] - T[i]) for i in range(len(A[0]))])
    dot = lambda V, T: [V[i] * T[i] for i in range(len(A[0]))]
    eps = 0.00001
    i = 1
    print(dist(Xr1, Xr))
    while dist(Xr1, Xr) > eps:
        line_format = ",".join(["Xr[%s] = %s" % (j, Xr1[j]) for j in range(len(A[0]))])
        print(i, '.', line_format)
        # organ promotion
        Xr = Xr1[:]
        i += 1
        # Calculation of Xr1
        for j in range (len(A)):
            Xr1[j] = c[j]-(sum(dot(A[j],Xr1))/diag[j])+Xr1[j]
        #Xr1 = [c[i] - (sum(dot(A[i], Xr)) / diag[i]) + Xr[i] for i in range(len(A[0]))]


A = [[3, -1, 1],
     [0, 1, -1],
     [1, 1, -2]]

B = [[4],
     [-1],
     [-3]]


if not Dominant_diagonal_test(A):
    C = convert_to_diagonally_dominant(A)
    if C != None:
        A = C

x = input("choose option: 1 to yaakobi and 2 to gaus_zaidel: ")
if x == '1':
    yaakobi(A, B)
else:
    gaus_zaidel(A, B)