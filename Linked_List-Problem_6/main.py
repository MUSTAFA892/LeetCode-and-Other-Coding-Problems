class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LL:
    def __init__(self):
        self.head_1 = None
        self.head_2 = None
        self.addition = None
        
    def insert_LL1(self,data):
        current = Node(data)
        current.next = self.head_1
        self.head_1 = current
        
    def traverse_LL1(self):
        print("The first Linked List:-")
        current = self.head_1
        
        while current:
            print(current.data,'->',end=" ")
            current = current.next
        print('None')
        
    def insert_LL2(self,data):
        current = Node(data)
        current.next = self.head_2
        self.head_2 = current
        
    def traverse_LL2(self):
        print("The second Linked List:-")
        current = self.head_2
        while current:
            print(current.data,'->',end=" ")
            current = current.next
        print('None')
        
    def addition_carry(self):
        l1 = self.head_1
        l2 = self.head_2
        carry = 0
        tail = 0
        
        while l1 and l2:
            val1 = l1.data
            val2 = l2.data
            
            sum_ = val1 + val2 + carry
            
            carry = sum_ // 10
            last_val = sum_ % 10
            current = Node(last_val)
            if not self.addition:
                self.addition = current
                tail = current
            else:
                tail.next = current 
                tail = current
                
            l1 = l1.next if l1 else 0
            l2 = l2.next if l2 else 0
            
      
        
        
        self.addition_traverse()
        
    def addition_traverse(self):
        current = self.addition
        print("The addtion of the LL with carry logic Implemented: ")
        while current:
            print(current.data, '->', end=" ")
            current = current.next
            
        print('None')
        
        
    
ll = LL()
ll.insert_LL1(3)
ll.insert_LL1(4)
ll.insert_LL1(2)
ll.traverse_LL1()
ll.insert_LL2(4)
ll.insert_LL2(6)
ll.insert_LL2(5)
ll.traverse_LL2()
ll.addition_carry()