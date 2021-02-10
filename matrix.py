import argparse

class Matrix:
    '''
        A class is used to represent the Matrix, various methods which are mentioned below are part of this class
        
        ...
        
        Attributes
        ----------
        
        mat1 & mat 2 : List of list (Nested list)
                    representing a Matrix in python
        degree : int
              the degree to be rotated, it should be in multiples of 90 only  
           
        
        Methods
        ---------
        
        add (mat1,mat2)
            returns the sum of the two matrices
    
        sub (mat1,mat2)
            returns the difference of the two matrices
            
        mul (mat1,mat2,n)
            returns the product of the two matrices or a number to a matrix 
            
        transpose (mat1)
            returns the tranpose of the matrix (swapping column to row)
            
        inverse (mat1)
            returns the inverse of the matrix
          
        reverseColumns (mat1)
            returns the matrix after reversing the columns
            
        rotate90clockwise (mat1)
            returns the matrix after rotating the 90 degress clock wise.  
            
        getMatrixMinor (mat1))
            returns the reciprocal of the sub matrix
            
        getMatrixDeternminant (mat1)
            returns the determinant if it is not equal to 0
        
    
    '''
    
    
    def __init__(self,mat1=None):
        self.mat1 = mat1

    def __add__(self,mat2):
        data = []

        row = len(self.mat1)
        col = len(self.mat1[0])
        if row != len(mat2.mat1) or col != len(mat2.mat1[0]):
            print("Matrix Addition Failed as the matrix rows and columns does not match.")
            return data

        data = [[self.mat1[x][y]+mat2.mat1[x][y] for y in range(row)] for x in range(col)]
        return Matrix(data)

    def __sub__(self,mat2):
        data = []

        row = len(self.mat1)
        col = len(self.mat1[0])
        if row != len(mat2.mat1) or col != len(mat2.mat1[0]):
            print("Matrix Subtraction Failed as the matrix rows and columns does not match.")
            return data

        data = [[self.mat1[x][y]-mat2.mat1[x][y] for y in range(row)] for x in range(col)]
        return Matrix(data)

    def __mul__(self,mat2):
        data = []
        row1 = len(self.mat1)
        col1 = len(self.mat1[0])

        #the below check is added if the user wants to multiple a integer to a matrix
        if isinstance(mat2,int):
            data = [[self.mat1[x][y] + m2 for y in range(row1)] for x in range(col1)]
            return data

        row2 = len(mat2.mat1)
        col2 = len(mat2.mat1[0])

        if col1 != row2 :
            print("Matrix Multiplication not possible ( matrix row) !=  (matrix column).")
            return False
        
        data = [[0 for y in range(col1)] for x in range(row2)]
        for i in range(row1):
            sum1 = 0
            for j in range(col1):
                for z in range(col1):
                    data[i][j] += self.mat1[i][z] * mat2.mat1[z][j]
        return Matrix(data)
 
    
    def transpose(self,data = None):
        # if no matrix is provided as input, it will take self.mat1. 
        if not data:
            data = self.mat1
            
        return [[data[j][i] for j in range(len(data))] for i in range(len(data[0]))] 
           
    
    def rotate90Clockwise(self,data):   
        # the matrix can be rotated 90 degree clock wise by first reversing the column and then transpose the matrix
        return self.transpose(self.reverseColumns(data))
    
    
    def inverse(self,m):
        determinant = self.getMatrixDeternminant(m)
        if determinant == 0:
            print('Inverse of this matrix is not possible, determinant is 0')
            return False
        if len(m) == 2:
            return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                    [-1*m[1][0]/determinant, m[0][0]/determinant]]

        cofactors = []
        for r in range(len(m)):
            cofactorRow = []
            for c in range(len(m)):
                minor = self.getMatrixMinor(m,r,c)
                cofactorRow.append(((-1)**(r+c)) * self.getMatrixDeternminant(minor))
            cofactors.append(cofactorRow)
        cofactors = self.transpose(cofactors)
        if determinant != 0:
            for r in range(len(cofactors)):
                for c in range(len(cofactors)):
                    cofactors[r][c] = cofactors[r][c]/determinant

        return cofactors

       
        
    def reverseColumns(self,data):
        # we need to reverse the column to rotate the matrix
        
        Col = len(data[0])
        for i in range(Col):
            j = 0
            key = Col-1
            while j < key:
                tempList = data[j][i]
                data[j][i] = data[key][i]
                data[key][i] = tempList
                j += 1
                key -= 1
        return data
    
    
    def rotateMatrix(self,inlistA,degree):
        
        print(inlistA)
        if len(args.inlistA) != 9:
            print ('Only 3x3 matrix is supported, please enter 9 numbers')
            return False
        else:
            data = [inlistA[x:x+3] for x in range(0, len(inlistA) - 2, 3)]
            
        if degree % 90 != 0:
            print('Sorry the matrix can be rotated only in multiples of 90')
            return False
        
        print("Matrix before rotation is:\n {} ".format(Matrix(data)))
        
        for rotation in range(degree//90):
            data = self.rotate90Clockwise(data)
            
        print("\nMatrix after {} degree rotation is:\n {} ".format(degree,Matrix(data)))
        return True

    
    def getMatrixMinor(self,m,i,j):
        return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

    def getMatrixDeternminant(self,m):
        if len(m) == 2:
            return m[0][0]*m[1][1]-m[0][1]*m[1][0]

        determinant = 0
        for c in range(len(m)):
            determinant += ((-1)**c)*m[0][c]*self.getMatrixDeternminant(self.getMatrixMinor(m,0,c))
        return determinant


    def __str__(self): 
        m = len(self.mat1) 
        mtxStr = ''
        mtxStr += ' ------------- output ----------\n'      
        for i in range(m):
            mtxStr += ('|' + ' | '.join( map(lambda x:'{0:8.0f}'.format(x), self.mat1[i])) + '| \n')
        mtxStr += ' -------------------------------'
        return mtxStr     
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='''A class is used to represent the Matrix, various methods are part of this class''')
    parser.add_argument('-lA', '--inlistA', nargs="*",type=int,required=True,metavar='',help='Enter the list of numbers to be added as part of Matrix rotation')
    parser.add_argument('-deg', '--degree', type=int,required=True,metavar='',help='Enter the degree to be rotated, it should be in multiples of 90 only:')

    args = parser.parse_args()
    m1 = [[1,2,3],[4,5,6],[7,8,9]]
    m2 = [[10,20,30],[40,50,60],[70,80,90]]
    m3 = [[1,0,2],[-1,5,0], [0,3,-9]]
    mat1 = Matrix(m1)
    mat2 = Matrix(m2)

    print(mat1+mat2)
    print(mat1-mat2)
    print(mat1*mat2)
    print(mat1.transpose(m1))
    print(mat1.inverse(m3))
    print(mat1.rotate90Clockwise(m1))
    u = Matrix()
    u.rotateMatrix(args.inlistA,args.degree)
 
    
    
    
    
