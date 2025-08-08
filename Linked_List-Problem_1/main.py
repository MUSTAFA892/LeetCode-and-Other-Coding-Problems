class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Linked:
    def __init__(self):
        self.head = None
        self.length = 1
        
    def insert(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    
    def traverse(self):

        current = self.head
        
        while current:
            print(current.data,'->',end=" ")
            current = current.next
            self.length += 1
        print('None')
        
    def get_length(self):
        return self.length

    
ll = Linked()
ll.insert(1)
ll.insert(2)
ll.insert(5)
ll.traverse()
print("The lenght of the LL is",ll.get_length())