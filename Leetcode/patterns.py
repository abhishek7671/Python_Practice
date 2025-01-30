# Write a program to dispaly *'s in Right angled triangled form

# n = int(input('enter the no of rows:'))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()


# n= int(input('enter the no of rows:'))
# for i in range(1,n+1):
#     print("*"*i)


# Write a program to display *'s in pyramid style(also known as equivalent triangle)

# n= int(input('enter the no of rows:'))
# for i in range(1,n+1):
#     print(" " *(n-i),end="")
#     print("* " * i)


# n = int(input("Enter number of rows: "))
# for i in range(1, n + 1):
#     print(" " * (n - i), end="")  # Print spaces for alignment
#     print("*" * i)  # Print stars with a space after each


# n=int(input('Enter the row numbers:'))
# for i in range(1,n+1):
#     print(""*(n-i),end="")
#     print("*"*i)



s1=input('enter the first name:')
s2=input('enter the second name:')

output = ' ' 
i,j = 0,0
while i<len(s1) or j<len(s2):
    if i<len(s1):
        output= output+s1[i]
        i+=1
    if j<len(s2):
        output=output+s2[j]
        j+=1
print(output)