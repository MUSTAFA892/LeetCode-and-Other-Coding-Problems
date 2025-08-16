class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LL:
    def __init__(self):
        self.head = None
        self.reverse = None
    
    def insert(self,data):
        current = Node(data)
        current.next = self.head
        self.head = current
    
    def traverse(self):
        print('Linked List :-')
        print()

        current = self.head
        while current:
            print(current.data,'->',end=" ")
            current = current.next
            
        print('None')
        print()
        
    def reverse_LL(self):
        current = self.head
        prev = None
        
        while current:
            NextNode = current.next
            
            current.next = prev
            
            prev = current
            current = NextNode
            
            reverseData = Node(prev.data)
            reverseData.next = self.reverse
            self.reverse = reverseData
            
    def traverse_LL(self):
        print('Reverse Linked List :-')
        print()
        current = self.reverse
        while current:
            print(current.data,'->',end =" ")
            current = current.next
        print('None')
            
            
        
            

ll = LL()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.traverse()
ll.reverse_LL()
ll.traverse_LL()