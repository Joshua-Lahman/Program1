## Joshua = 6
## Lahman = 6

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

## print Mat1 
print("Mat1")
for row in arr1:
    print(row)
print("\n")

#output matrix to file
with open(r'C:\School\Python_Output\JLahman_mat1.txt', 'w') as f:
    for row in arr1:
        f.writelines(str(row)+ '\n')
    f.close()

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

# print Mat2 
print("Mat2")
for row in arr2:
    print(row)
print("\n")

#output matrix to file
with open(r'C:\School\Python_Output\JLahman_mat2.txt', 'w') as f:
    for row in arr2:
        f.writelines(str(row)+ '\n')
    f.close()

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

# print Mat3 
print("Mat3")
for row in arr3:
    print(row)
print("\n")

#output matrix to file
with open(r'C:\School\Python_Output\JLahman_mat3.txt', 'w') as f:
    for row in arr3:
        f.writelines(str(row)+ '\n')
    f.close()

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

# print Mat4 
print("Mat4")
for row in arr4:
    print(row)
print("\n")

#output matrix to file
with open(r'C:\School\Python_Output\JLahman_mat4.txt', 'w') as f:
    for row in arr4:
        f.writelines(str(row)+ '\n')
    f.close()

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

# print Mat5 
print("Mat5")
for row in arr5:
    print(row)
print("\n")

#output matrix to file
with open(r'C:\School\Python_Output\JLahman_mat5.txt', 'w') as f:
    for row in arr5:
        f.writelines(str(row)+ '\n')
    f.close()

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

# print Mat6 
print("Mat6")
for row in arr6:
    print(row)
print("\n")

#output matrix to file
with open(r'C:\School\Python_Output\JLahman_mat6.txt', 'w') as f:
    for row in arr6:
        f.writelines(str(row)+ '\n')
    f.close()