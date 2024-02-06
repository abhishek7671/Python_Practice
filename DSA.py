# def items(n):
#     return n*n

# print(items(2))



# def data(n):
#     for i in range(n):
#         print(i)

# data(10)



# def day(n):
#     for i in range(n):
#         print(i)
#     for j in range(n):
#         print(j)
# day(10)
         
         
# def daily (n):
#     for i in range(n):
#         for j in range(n):
#             for k in range(n):
#                 print(i,j,k)

# daily(10)   



# def days(n):
#     for i in range(n):
#         for j in range(n):
#             print(i,j)
#     for k in range(n):
#         print(k)
        
# days(10)


# def sum(n):
#     if n<=0:
#         return 0
#     return n+sum(n-1) 
# sum(2)
    
    
    

# import array

# array_map = array.array("i")
# print(array_map)

# array_obj = array.array("i",[1,1,2,3,4,5,6,7,8])
# print(array_obj)
# array_obj.insert(0, 10)
# print(array_obj)


# import numpy as np 
# np_array = np.array([], dtype=int)
# print(np_array)

# ap_array = np.array([1,2,3,4,5,6,7,8,9])
# print(ap_array)


# import array

# arr1 = array.array("i",[1,2,3,4,5,6,7,8])

# # def transport(array):
# #     for i in array:
# #         print(i)
# # transport(arr1)


# def trans(array, index):
#     if index > len(array):
#         print("not possible to work the code")
#     else:
#         print(array[index])
# trans(arr1,1)


# def tra(array, target):
#     for i in range(len(array)):
#         if array[i] == target:
#             return i
#     return -1 
# print(tra(arr1, 10)) 



from array import *

arr2 = array("i",[1,2,3,4,5,6,7,8,9])
print(arr2)

arr2.remove(2)
print(arr2)