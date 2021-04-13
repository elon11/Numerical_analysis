class Matrix:
    def __init__(self, list_of_rows, name=None):
        # example m=Matrix([[1,2,3],
        #                   [2,3,4],
        #                   [5,5,6]])
        self.list_of_rows = list_of_rows
        self.num_of_cols = self.validation(list_of_rows)
        self.rows = [list(map(float, row ))for row in list_of_rows]
        self.num_of_rows = len(self.rows)
        self.det = None
        self.row_range = range(self.num_of_rows)
        self.col_range = range(self.num_of_cols)
        self.name = name

    @classmethod
    def validation(cls, rows):
        if not isinstance(rows, list):
            raise TypeError("Matrix must to be list")
        if len(rows) == 0:
            raise TypeError("There is no rows")
        num_of_cols = None
        for row in rows:
            if not isinstance(row, list):
                raise TypeError("All rows must be list")
            if num_of_cols is None:
                num_of_cols = len(row)
                if  num_of_cols == 0:
                    raise TypeError("There is no cols")
            elif num_of_cols != len(row):
                raise TypeError("All rows must be in the same length")
            for cell in row:
                if not (isinstance(cell, float) or  isinstance(cell, int)):
                    raise ValueError("All values must be float")
        return num_of_cols


    def __str__(self):
        # Matrix painting
        if self.name:
            result = "{2} Matrix({1}x{0}):\n".format(self.num_of_cols, self.num_of_rows, self.name)
        else:
            result = "Matrix({1}x{0}):\n".format(self.num_of_cols, self.num_of_rows)
        for row in self.rows:
            result += str(list(map(str, row))) + "\n"
        return result

    def __multiplication(self, other):
        # Function for multipcation between matrices.
        if not isinstance(other, Matrix):
            raise TypeError("multiplication is between two matrices")
        if not self.num_of_cols == other.num_of_rows:
            raise ValueError("can't multiplication this matrices")
        result = [[0 for j in other.col_range] for i in self.row_range]
        for i in self.row_range:
            for j in other.col_range:
                for k in range(other.num_of_rows):
                    result[i][j] += self.rows[i][k]*other.rows[k][j]
        if self.num_of_rows == other.num_of_cols:
            # Checking if the matrix is a SquareMatrix.
            return SquareMatrix(result)
        return Matrix(result)

    def __mul__(self, other):
        # A function that when there is a multiplication operator returs __multiplication function.
         return self.__multiplication(other)

    def __truediv__(self, other):
        # A function that when there is a divide operator returs __truediv__ function.
        if (isinstance(other, int) or isinstance(other, float)):
            return self._div_by_scalar(other)

    def _div_by_scalar(self, scalar):
        # Function that divied between matrix and scalar.
        # and return the new matrix.
        result = [[0 for j in self.col_range] for i in self.row_range]
        for i in self.row_range:
            for j in self.col_range:
                result[i][j] = self.rows[i][j]/scalar
        if self.num_of_rows == self.num_of_cols:
            # Checking if the matrix is a SquareMatrix.
            return SquareMatrix(result)
        return Matrix(result)

    def swap(self, i1, i2):
        # Function that swap beetween two rows.
        if i1 == i2:
            return
        self.rows[i1], self.rows[i2] = self.rows[i2], self.rows[i1]



class SquareMatrix(Matrix):
    # A class that representing a square matrix that heiress from Matrix class.
    @classmethod
    def validation(cls, rows):
        num_of_cols = Matrix.validation(rows)
        if num_of_cols != len(rows):
            raise TypeError("Num of cols and rows must be equals")
        return num_of_cols

    def is_invertible(self):
        # A function that return if the matrix is invertible or not.
        return self.deteminante() != 0

    def deteminante(self):
        if self.det is not None:
            # If the determinant has already been calculated return it.
            return self.det
        if self.num_of_cols == 1:
            self.det = self.rows[0][0]
            return self.det
        sign = 1
        # First line development
        i = 0
        result = 0
        for j in self.col_range:
            factor = self.rows[i][j]
            if factor != 0:
                # Calculation by minor.
                result += sign*factor*self.minor(i, j).deteminante()
            sign *= -1
        self.det = result
        return self.det

    def minor(self, row_index, col_index):
        if not (0 <= row_index < self.num_of_rows):
            raise ValueError("Row index not valid")
        if not (0 <= col_index < self.num_of_cols):
            raise ValueError("Col index not valid")
        result =[]
        for i in self.row_range:
            if i == row_index:
                continue
            row = []
            for j in self.col_range:
                if j == col_index:
                    continue
                row.append(self.rows[i][j])
            result.append(row)
        return SquareMatrix(result)

    def gauss_method(self,b):
        return self._gauss_methodA(b)

    def _gauss_methodA(self, b):
        # Calculation b*inverse(A) according to Gauss.
        x = self.inverse()*b
        x.name = "x"
        return x

    def _gauss_methodB(self, b):
        # Another function to calculate - on this exercise we don't use that .
        L, U = self.LU()
        return U.inverse()*L.inverse()*b

    def inverse(self):
        if self.is_invertible():
            return self._inverseA()
        else:
            raise ValueError("Matrix must be invertible")

    def _inverseA(self):
        # A function that inverse the matrix
        unit_matrix = ConstDiagonalMatrix(self.num_of_rows, 1, "A inverse") # Creating unit metrix.
        temp_matrix = SquareMatrix((self.list_of_rows.copy())) # Copy the matrix so as not to change the source.
        for i in self.row_range:
            new_row_index, pivot_value = temp_matrix.pivot(i)
            if i != new_row_index:
                # Swap rows
                temp_matrix.swap(i, new_row_index)
                unit_matrix.swap(i, new_row_index)
            factors = [-row[i]/pivot_value for row in temp_matrix.rows]
            # All the elementary operations we do both on the temp matrix and on the unit matrix.
            for j in self.row_range:
                if i == j:
                    continue
                else:
                    factor = factors[j]
                    for k in self.col_range:
                        temp_matrix.rows[j][k] += factor*temp_matrix.rows[i][k]
                        unit_matrix.rows[j][k] += factor * unit_matrix.rows[i][k]

            for k in self.col_range:
                    temp_matrix.rows[i][k] /= pivot_value
                    unit_matrix.rows[i][k] /= pivot_value

        # Returning the inverse matrix.
        return unit_matrix

    def pivot(self, i):
        # Function for finding pivot.
        max_value = self.rows[i][i]
        max_row = i
        col = [row[i] for row in self.rows]
        for j in self.col_range:
            if j <= i:
                continue
            value = abs(col[j])
            if value > abs(max_value):
                max_value = value
                max_row = j
        if max_value == 0:
            raise ValueError("can't find pivot")  # if in the whole cols there are zeros.
        return max_row, max_value

# Another way to do n inverse matrix. (_inverseB , adjoint)
    def _inverseB(self):
        return self.adjoint() / self.deteminante()
    def adjoint(self):
        result = [[0 for j in self.col_range] for i in self.row_range]
        for i in self.row_range:
            for j in self.col_range:
                result[i][j] = ((-1)**(i+j))*self.minor(i, j).deteminante()
        return SquareMatrix(result)

    def LU(self):
        # Function for finding L U matrices.
        p = ConstDiagonalMatrix(self.num_of_rows, 1, "p")
        L_matrix= ConstDiagonalMatrix(self.num_of_rows, 1, "L") # L matrix.
        U_matrix = SquareMatrix(self.list_of_rows.copy(), "U") # U matrix.
        for i in self.row_range:
            pivot_value = U_matrix.rows[i][i]
            if pivot_value == 0: # The lecturer said not to change lines.
                max_row, pivot_value = U_matrix.pivot(i)
                p.swap(i,max_row)
                U_matrix.swap(i, max_row)
                print(U_matrix)
            for j in self.row_range:
                if j <= i:
                    continue
                factor = -U_matrix.rows[j][i]/pivot_value
                L_matrix.rows[j][i] -= factor
                for k in self.col_range:
                    if j <= i:
                        continue
                    U_matrix.rows[j][k] += factor * U_matrix.rows[i][k]


        return L_matrix, U_matrix


class ConstDiagonalMatrix(SquareMatrix):
    # A class describing a digonal matrix.
    def __init__(self, size, value, name = None):
        Range = range(size)
        result = [[0 if j != i else value for j in Range ] for i in Range]
        SquareMatrix.__init__(self, result, name)







