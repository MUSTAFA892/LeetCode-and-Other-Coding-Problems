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
        
    def even_elements(self):
        print("The even elements in the LL are: ")
        current = self.head
        
        while current:
            if current.data % 2 == 0:
                print(current.data, '->' , end = " ")
            current = current.next
        print('None')            

    
ll = Linked()
ll.insert(4)
ll.insert(2)
ll.insert(4)
ll.traverse()
ll.even_elements()