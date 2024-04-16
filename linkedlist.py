class Node:
    def __init__(self,value):
        self.value = value
        
    


class Linkedlist:
    def __init__(self, value):
        new_node =Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

# class Linkedlist:
#     def __init__(self):
       
#         self.head = None
#         self.tail = None
#         self.length = 1


data = Linkedlist()

print(data.length)