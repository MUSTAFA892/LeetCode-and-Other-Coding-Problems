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
        
    def addition_normal(self):
        print("The addition of the two Linked List:-")
        ll_1 = self.head_1
        ll_2 = self.head_2
        
        while ll_1 and ll_2:
            print(ll_1.data + ll_2.data,'->',end =" ")
            ll_1 = ll_1.next if ll_1 else 0
            ll_2 = ll_2.next if ll_2 else 0
        print('None')
    
    def addition_in_LL(self):
        ll_1 = self.head_1
        ll_2 = self.head_2
        
        while ll_1 and ll_2:
            val_1 = ll_1.data
            val_2 = ll_2.data
            addition_current = Node(val_1+val_2)
            addition_current.next = self.addition
            self.addition = addition_current
            
            ll_1 = ll_1.next if ll_1 else 0
            ll_2 = ll_2.next if ll_2 else 0

        self.addition_current_traverse()
    
    def addition_current_traverse(self):
        current = self.addition
        print("The addition of the Linked List in new LL:")
        while current:
            print(current.data,'->',end=" ")
            current = current.next
            
        print('None')
        
ll = LL()
ll.insert_LL1(1)
ll.insert_LL1(2)
ll.insert_LL1(3)
ll.traverse_LL1()
ll.insert_LL2(4)
ll.insert_LL2(5)
ll.insert_LL2(6)
ll.traverse_LL2()
ll.addition_normal()
ll.addition_in_LL()