from matrix import Matrix,SquareMatrix,ConstDiagonalMatrix

A = SquareMatrix([[1, 2, 1],
                 [2, 6, 1],
                 [1, 1, 4]], "A")
b = Matrix([[2, 3, 5]], "b")

if (A.num_of_rows < 4):
    L, U = A.LU()
    print(L)
    print(U)
else:
    print(A.gauss_method(b))