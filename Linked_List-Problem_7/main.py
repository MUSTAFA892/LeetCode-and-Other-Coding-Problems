class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class LL:
    def __init__(self):
        self.head = None
        self.odd = None
        self.even = None
    
    def insert(self,data):
        current = Node(data)
        current.next = self.head
        self.head = current
    
    def traverse(self):
        current = self.head
        print("Linked List:-")
        while current:
            print(current.data,'->',end=" ")
            current = current.next
        print('None')
        
    def odd_even(self):
        current = self.head
        
        while current:
            if current.data % 2 == 0:
                even_current = Node(current.data)
                even_current.next = self.even
                self.even = even_current
            
            else:
                odd_current = Node(current.data)
                odd_current.next = self.odd
                self.odd = odd_current
            current = current.next
                
        self.traverse_odd()
        self.traverse_even()
                
    def traverse_odd(self):
        odd_current = self.odd
        print('The odd element Linked List:- ')
        while odd_current:
            print(odd_current.data,'->',end=" ")
            odd_current = odd_current.next
        print('None')
        
    def traverse_even(self):
        even_current = self.even
        print("The even element Linked List:- ")
        
        while even_current:
            print(even_current.data,'->',end=" ")
            even_current = even_current.next
            
        print('None')
        
    
ll = LL()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.traverse()
ll.odd_even()