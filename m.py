det=(matrix[0][0]*((matrix[1][1]*matrix[2][2])-(matrix[2][1]*matrix[1][2])))-(matrix[0][1]*((matrix[1][0]*matrix[2][2])-(matrix[2][0]*matrix[1][2])))+(matrix[0][2]*((matrix[1][0]*matrix[2][1])-(matrix[2][0]*matrix[1][1])))
    return det
matrix[i][j]=a[np.arange(3)!=i][:,np.arange(3)!=j]
