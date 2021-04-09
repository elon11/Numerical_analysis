from matrix import Matrix,SquareMatrix,ConstDiagonalMatrix


a= SquareMatrix([[1, 0, 0], [0, 5, 0], [0, 0, 6]])
#b= Matrix([[1], [3], [2]])
#print(a.gauss_method(b))
#c = ConstDiagonalMatrix(9, 3)
print(a.inverse())