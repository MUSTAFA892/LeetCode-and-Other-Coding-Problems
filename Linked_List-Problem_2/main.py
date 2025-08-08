class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Linked:
    def __init__(self):
        self.head = None
        self.length = 1
        self.middle_index = None
        self.middle_element = None 
    
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
        
    def middle_value(self):
        current = self.head
        self.middle_index = self.length // 2
        
        track_length = 1
        while current:
            if track_length == self.middle_index+1:
                self.middle_element = current.data
            
            current = current.next
            track_length += 1
                
            
        print(self.middle_element)
        
    
ll = Linked()
ll.insert(1)
ll.insert(2)
ll.insert(5)
ll.insert(4)
ll.insert(7)
ll.insert(9)
ll.traverse()
print("The lenght of the LL is",ll.get_length())
ll.middle_value()
