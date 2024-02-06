# from array import *

# arr1 = array("i",[1,2,3,4,5,6,7,8,9])

# for i in arr1:
#     print(i)
    
    
# print("step2")
# print(arr1[3])   #index value 

# print("step3")
# arr1.append(10)
# print(arr1)         # append the value in the array 


# print("step4")
# arr1.insert(1, 22)
# print(arr1)

# print("step5")
# arr2= array("i",[23,24,25])
# arr1.extend(arr2)
# print(arr1)


# # add items from list into array using fromlist() method
# print("step6")
# templist = [20,30,40]
# arr1.fromlist(templist)
# print(arr1)

# # remove method 
# print("step7")
# arr1.remove(23)
# print(arr1)

# # pop method means last value remove 

# print("step8")
# arr1.pop()
# print(arr1)


# # using index method() for particular value 
# print("step9")
# print(arr1.index(24))


# # reverse the array data
# print("step10")
# arr1.reverse()
# print(arr1)

# # bufferinfo () method
# print("step11")
# print(arr1.buffer_info())

# print("step12")
# arr1.append(22)
# print(arr1.count(22))

# # array convert into list using  tolist() method
# print("step13")
# print(arr1.tolist())

# # slice method
# print("step14")
# print(arr1[1:5:])
# print(arr1[:3])


# ----------------------------------------------------------------------------------------------------------------------------------

# day1 = 11,12,13,14
# day2 = 22,23,24,25
# day3 = 33,34,35,36
# day4 = 44,45,46,47


import numpy as np
# twoDarray = np.array([[11,12,13,14],[22,23,24,25],[33,34,35,36],[44,45,46,47]])
# print(twoDarray) 

# insert the row and column in the 2d array

# new2darray = np.insert(twoDarray, 1, [[1,2,3,4]], axis=0)  # 1 is the postion axis= 0 row wise changing axis= 1 columen data wise changing 
# print(new2darray)

# new2darray = np.append(twoDarray,  [[44,44,44,44]], axis=0)  # 1 is the postion axis= 0 row wise changing axis= 1 columen data wise changing 
# print(new2darray)


# #  accessing the 2d array data elements
# def arra(array, rowIndex, colIndex):
#     if rowIndex >= len(array) and colIndex >=len(array):
#         print("incorrect solution")
#     else:
#         print(array[rowIndex][colIndex])
# arra(twoDarray, 2, 3)



arra = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]])
print(arra)


# def trans(array):
#     for i in range(len(array)):
#         for j in range(len(array)):
#             print(array[i][j])
    
# trans(arra)


# def trasnport(array, value):
#     for i in range(len(array)):
#         for j in range(len(array)):
#             if array[i][j] == value:
#                 return "Index of the value is " + str(i)+" "+str(j)
#     return "the value is not exist"

# print(trasnport(arra, 14))



# data = np.delete(arra, 0, axis=0) # delete the row and column in the 2d array
# print(data)


