class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
    
class LL:
    def __init__(self):
        self.head = None
        
    def insert(self,data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp
        
    def traverse(self):
        current = self.head
        while current:
            print(current.data,'->',end = " ")
            current = current.next
        print('None')
        
    def starting_deletion(self):
        self.head = self.head.next
        
        
    def deletion_by_val(self,val):
        current = self.head
        
        if current.data == val:
            self.head = self.head.next
            
        else:
            while current:
                if current.data == val:
                    prev.next = current.next
                    print(f"The value {val} is deleted from the node")
                    break
                prev = current
                current = current.next
    
    
    
ll = LL()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)
#ll.starting_deletion()
ll.traverse()
ll.deletion_by_val(4)
ll.traverse()

