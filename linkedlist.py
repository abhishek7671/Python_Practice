# class Node:
    # def __init__(self,value):
    #     self.value = value
        
    


# # class Linkedlist:
# #     def __init__(self, value):
#         # new_node =Node(value)      #---------------------------------o(1)   time complexity O(1) and space complexity O(1)
# #         self.head = new_node       #---------------------------------o(1)    time complexity O(1) and space complexity O(1)
# #         self.tail = new_node       #---------------------------------o(1)    time complexity O(1) and space complexity O(1)
# #         self.length = 1            #---------------------------------o(1)   time complexity O(1) and space complexity O(1)

# class Linkedlist:
#     def __init__(self):
       
#         self.head = None
#         self.tail = None
#         self.length = 0
        
        
#     def append(self, value):
#         new_node =Node(value)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
#         self.length +=1
            
            
# data = Linkedlist()
# data.append(10)
# data.append(20)

# print(data)


# ------------------------------------

# class Person:
#     def __init__(self, Name, Age):
#         self.name = Name
#         self.age = Age
    
    
#     def __str__(self):
#         return f"(Person {self.name} - {self.age})"
    
    
# new_person = (Person('Abhi',24))
# print(new_person)


# ---------------------------------------------------
class Node:
    def __init__(self,value):
        self.value = value
    




    class LinkedList:
        def  __init__(self):
            self.head = None
            self.tail = None
            self.length = 0
    
        def Append (self, value):
            new_node = Node (value)
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = new_node
            self.length +=1
            
        def __str__(self):
            temp_node = self.head
            result = ''
            while temp_node is not None 