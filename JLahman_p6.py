##-----Mat1-----

##initialize array1
rows1, cols1 = (6, 6)
arr1 = [[0 for i in range(cols1)] for j in range(rows1)]

# itterate every value  
count = 0       
for i in (range (0,6)) :
    for j in (range (0,6)) : 
        count = count + 1
        arr1[j][i] = count

##-----Mat2-----

##initialize array2
rows2, cols2 = (6, 6)
arr2 = [[0 for i in range(cols2)] for j in range(rows2)]

# itterate every value  
count = 0       
for i in (range (0,6)) :
    for j in (range (0,6)) : 
        count = count + 1
        arr2[i][j] = count

##-----Mat3-----

##initialize array3
rows3, cols3 = (6, 6)
arr3 = [[0 for i in range(cols3)] for j in range(rows3)]

# itterate every value  
count = 0       
for i in (range (0,6)) :
    for j in (range (0,6)) : 
        count = count + 1
        arr3[j][i] = ('%1.1f' % (count * .2))

##-----Mat4-----

##initialize array4
rows4, cols4 = (4, 6)
arr4 = [[0 for i in range(cols4)] for j in range(rows4)]

# itterate every value  
count = 0       
for i in (range (0,6)) :
    for j in (range (0,4)) : 
        count = count + 1
        arr4[j][i] = 12 - (count*2)

##-----Mat5-----

##initialize array5
rows5, cols5 = (4, 6)
arr5 = [[0 for i in range(cols5)] for j in range(rows5)]

# itterate every value  
count = 0       
for i in (range (0,4)) :
    for j in (range (0,6)) : 
        count = count + 1
        arr5[i][j] = ('%1.1f' % (1.5*count - 7.5))


##-----Mat6-----

##initialize array6
rows6, cols6 = (2, 4)
arr6 = [[0 for i in range(cols6)] for j in range(rows6)]

# itterate every value  
count = 0       
for i in (range (0,2)) :
    for j in (range (0,4)) : 
        count = count + 1
        arr6[i][j] = (10*count - 20)

#function to find transpose
def matTranspose(matrix) :
    numrows = len(matrix)
    numcols = len(matrix[0])

    #initialize transpose matrix
    matrixT = [[0 for i in range (numrows)]for j in range(numcols)]

    #set rows to transpose columns and columns to transpose rows
    for i in range(numrows) :
        for j in range((numcols)) :
            matrixT[j][i] = matrix[i][j]

    # print Mat2 
    print("Transpose Matrix: ")
    for row in matrixT:
        print(row)

    #output matrix to file
    with open(r'C:\School\Python_Output\JLahman_p6_mat1.txt', 'w') as f:
        for row in matrixT:
            f.writelines(str(row)+ '\n')
        f.close()

#call transpose function
matTranspose(arr1)