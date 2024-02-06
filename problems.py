# l = ["1", "2", "9", "0", "-1", "-2"]
# print("Sorted numerically:",
#       sorted(l, key=lambda x: int(x)))
 
# print("Filtered positive even numbers:", 
#       list(filter(lambda x: not (int(x) % 2 == 0 and int(x) > 0), l)))
 
# print("Operation on each item using lambda and map()",
#       list(map(lambda x: str(int(x) + 10), l)))






# my_list = [1, 2, 3, 4, 5]

# print("odd number:", list(filter(lambda x:x%2!=0,my_list)))



# def fun(text):
#     return text.upper()
# print(fun("hello"))

# gun = fun("hello")

# print(gun)


# def fun(text):
#     return text.upper()

# def gun(text):
#     return text.lower()

# def cell(tab):
#     green = tab("Hi mobile where are u ")
#     print(green)
    
# cell(fun)
# cell(gun)


class Dog:
    attr1="animal"
    
    def __init__(self,name):
        self.name = name

Rodger = Dog("Rodger")
tommy = Dog("tommy")

print("rodger is a quit one:",(Rodger.__class__.attr1))
print("tommy is the smart one:",(tommy.__class__.attr1))


