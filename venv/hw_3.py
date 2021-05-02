
def yaakobi (A, B):
    #if !Dominant_diagonal_test (A):
     #   Dominant_diagonal_make(A):
    print("mdkkldmk")
    # keep diag value
    diag = [A[i][i] for i in range(len(A[0]))]
    c = [B[i][0]/diag[i] for i in range(len(A[0]))]
    Xr = [0 for i in range(len(A[0]))]

    #ניחוש התחלתי
    Xr1 = [(B[i][0]+sum(Xr)-Xr[i])/diag[i] for i in range(len(A[0]))]
    dist = lambda V , T : min([abs(V[i]-T[i]) for i in range(len(A[0]))])
    dot = lambda V, T : [V[i]*T[i] for i in range (len(A[0]))]
    eps = 0.0001
    i = 1
    print (dist(Xr1,Xr))
    while dist(Xr1,Xr)>eps :
        line_format = ",".join(["Xr[%s] = %s" % (j,Xr1[j]) for j in range(len(A[0]))])
        print (i,'.',line_format)
        # קידום איברים
        Xr = Xr1
        i+=1
        # Calculation of Xr1
        Xr1 = [c[i]-(sum(dot(A[i],Xr))/diag[i]) + Xr[i] for i in range(len(A[0]))]


A = [[3, -1, 1],
         [0, 1, -1],
         [1, 1, -2]]

B = [[4],
        [-1],
        [-3]]

yaakobi(A,B)