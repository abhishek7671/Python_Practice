# hi = ["milk", "curd", "data", "entry"]
# print(hi[2])

# print("data" in hi )   # in operator 
# print("ram" in hi )
# for i in hi:
#     print(i)
    

# for i in range(len(hi)):
#     hi[i] = hi[i]+"+"
#     print(hi[i])


# mylist = [1,2,3,4,5,6,7,8,9]
# print(mylist)
# mylist[2] = 33
# print(mylist)

# mylist.insert(4,11)
# print(mylist)

# mylist.append(55)
# print(mylist)

# new = [55,66,77]
# mylist.extend(new)
# print(mylist)



# data = ['a','b','c','d','e','f','g','h','i']
# data.pop()
# print(data)

# for i in range(len(data)):
#     data.pop()
#     print(i)


# data.remove('e')
# print(data)
# del data[2]
# del data[:4]
# print(data)
# data.clear()
# print(data)


# mydata = [1,3,6,8,2,5,78,44,77,22,54,45,25,55,35]
# target = 55
# # if target in mydata:
# #     print(f"{target} is available")
# # else:
# #     print(f"{target} is not available")
    

# def listdata (data, targe):
#     for i in range(len(data)):
#         if data[i]== target:
#             return i
#     return -1        
# print(listdata(mydata, target))



# def data(day, tar):
#     if target in day:
#         print(f"{target} is available")
#     else:
#         print(f"{target} is not available")

# data(mydata, target)




# -----------------------------------------------------------------------------------------------------------------------------------
# concatenate the both lists

# a=[1,2,3]
# b=[4,5,6]
# c= a+b
# print(c)

# a=[2]
# a=a*4
# print(a)


# a=[2,2,5,67,8,9,5,4,3,5,5,4,6,8,33,5,5,66,54,4]
# print(len(a))


# data = [[[1,2],[3,4]],[[5,6],7,8]]
# def fun(m):
#     v = m[0][0]
#     for row in m:
#         for element in row:
#             if v < element :
#                 v=element
#     return v
# print(fun(data[0]))


# list comprehension

# pre = [1,2,3,4,5]
# new = [i*3 for i in pre]
# print(new)

# language = "python"

# data = [i for i in language]
# print(data)

# pre = [-1,2,-3,4,-5,6,-7,8,-9,10]
# data= [ i*i for i in pre if i>0]
# print(data)



# sentence  = "my name is abhi"
# def fun(letter):
#     vowels = 'aeiou'
#     return letter.isalpha() and letter.lower() not in vowels

# data = [i for i in sentence if fun(i)]
# print(data)