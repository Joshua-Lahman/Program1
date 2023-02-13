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


#define function to find dot product of two matrixes
def matDot(matrix1, matrix2) :
    #find matrix sizes
    numrows1 = len(matrix1)
    numcols1 = len(matrix1[0])
    numrows2 = len(matrix2)
    numcols2 = len(matrix2[0])

    #check if matrix1 columns and matrix2 rows are same size
    if (numcols1 == numrows2) :
        matrix3 = [[0 for a in range (numcols1)]for b in range(numcols1)]

        # dot product matrix1 and matrix2, set value to matrix3
        for i in range(numrows1) :
            for j in range((numcols2)) :
                sum = 0 #initialize and reset sum after each assignment 
                for k in range(numcols1) :
                    sum += float(matrix1[i][k]) * float(matrix2[k][j]) #sum all the products 

                matrix3[i][j] = ('%1.1f' % (sum))  
        
        #output matrix to file
        with open(r'C:\School\Python_Output\JLahman_p3_out12.txt', 'w') as f:
            for row in matrix3:
                f.writelines(str(row)+ '\n')
        f.close()

        print("result is: ")
        for row in matrix3:
            print(row)
        #return 0

    else :
        print("Matrix sizes do not match")
        #return 0 

#call dot product function
matDot(arr1, arr2)