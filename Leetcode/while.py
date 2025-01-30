#To print numbers from 1 to 10 by using while loop

# x = 1
# y = []
# while x<=10:
#     print(x)
#     y.append(x)
#     x=x+1
# print(y)


# To display the sum of first n numbers

n = int(input('enter the numbers:'))
sum = 0
i=1
while i<=n:
    sum = sum + i 
    i=i+1
print(sum)