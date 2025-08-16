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
            
            
    def palindrome(self):
        current1 = self.head
        current2 = self.reverse
        flag = True
        
        while current1 and current2:
            if current1.data != current2.data:
                flag = False
                break
            
            current1 = current1.next if current1 else 0
            current2 = current2.next if current2 else 0
            
            
        if flag:
            print('The Linked List is palindrome')
        
        else:
            print("The Linked List is not palindrome")
            
            
        
            

ll = LL()
ll.insert(1)
ll.insert(2)
ll.insert(1)
ll.insert(2)
ll.insert(1)
ll.traverse()
ll.reverse_LL()
ll.palindrome()