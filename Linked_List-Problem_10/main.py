class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LL:
    def __init__(self):
        self.head = None
        
    def insert(self,data):
    
        newNode = Node(data)
        
        if not self.head:
            self.head = newNode
            return self.head
            
        current = self.head
        
        while current.next:
            current = current.next
            
        
        current.next = newNode
        

    def traverse(self):
        current = self.head
        
        while current:
            print(current.data,'->',end = " ")
            current = current.next
            
        print('None')
        

ll = LL()
ll.insert(1)
ll.insert(2)
ll.insert(3)

ll.traverse()