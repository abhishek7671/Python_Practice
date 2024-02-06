# fibonacci series 

# n=10
# n1=0
# n2=1
# next_number =n2
# c=1

# while c <=n:
#     print(next_number,end =" ")
#     c+=1
#     n1,n2 = n2, next_number
#     next_number=n1+ n2
# print()


# def fibonacci (n):
#     if n<0:
#         print("incorrect input")
#     elif n==0:
#         return 0
#     elif n==1 or n==2:
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
# print(fibonacci(9))


def fibonacci (n):
    a=0
    b=1
    if n<0:
        print("incorrect input")
    elif n==0:
        return a
    elif n==1 :
        return b
    else:
        for i in range(1,n):
            c= a+b
            a=b
            b=c
        return b
print(fibonacci(9))
    