from matrix import Matrix,SquareMatrix,ConstDiagonalMatrix

A = SquareMatrix([[1, 2, 4],
                  [5,1, 2],
                  [3, -1, 1], ], "A")
b = Matrix([[7], [8], [3]], "b")

if (A.num_of_rows > 4):
    L, U = A.LU()
    print(L)
    print(U)
else:
    print(A.gauss_method(b))

