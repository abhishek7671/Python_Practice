# def reverse(s):
#     str = ""
#     for i in s:
#         str = i + str
#     return str
# s= "geeksforgeeks"
# print("the original data:", end="")
# print(s)
# print("the reverse data:", end="")
# print(reverse(s))



# reverse the string using recursion function 

# def reverse(s):
#     if len(s)==0:
#         return s
#     else:
#         return reverse(s[1:])+s[0]

# s="geeksforgeeks"

import shelve


# print("original data:",end="")
# print(shelve)
# print("reverse data:", end="")
# print(reverse(s))


# def reverse(s):
#     s=s[::-1]
#     return s
# string="geeksforgeeks"

# print("original data:",end="")
# print(string)
# print("reverse data:", end="")
# print(reverse(string))


# a = '"The unexamined life is not worth living." - Socrates'
# b=a.replace('.','')
# print(b)
# c=b.split('-')
# print(c[0])


# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result

# print("\n\nRecursion Example Results")
# tri_recursion(6)


# def tri_recursion(k):
#     if k < 0:
#         return 0
    
#     result = k + tri_recursion(k - 1)
#     print(result)
    
#     return result

# print("\n\nRecursion Example Results")
# tri_recursion(6)



# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
#     def printname(self):
#         print(self.firstname,self.lastname)
# x = Person("ram","krishna")
# x.printname()



class Mynum:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        x=self.a
        self.a +=1
        return x
myclass = Mynum()
myiter = iter(myclass)

print (next(myiter))
print (next(myiter))
print (next(myiter))
print (next(myiter))	
print (next(myiter))