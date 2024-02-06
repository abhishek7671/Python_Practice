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


a = '"The unexamined life is not worth living." - Socrates'
b=a.replace('.','')
print(b)
c=b.split('-')
print(c[0])
