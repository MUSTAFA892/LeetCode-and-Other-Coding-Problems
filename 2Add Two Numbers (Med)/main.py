# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = ListNode(0)  # Make the new node for storing the
        root = head  # Initialize the new node in the root variable
        carry = 0  # Track the carry value now take it as 0

        while l1 or l2:  # If two LL has elements
            v1 = l1.val if l1 else 0  # Track the elements of l1 in v1
            v2 = l2.val if l2 else 0  # Track the elements of l2 in v2
            s = v1 + v2 + carry

            carry = s // 10  # Update the carry value by adding v1 and v2
            head.next = ListNode(s % 10)  # Also update the sum element in the new node
            head = head.next

            if l1:
                l1 = l1.next #Update the next element of l1
            if l2:
                l2 = l2.next #Update the next element of l2

        if carry:
            head.next = ListNode(carry) #if the carry contains the value after initializing all the element in l1 and l2 then add it in the new node

        return root.next # Return the next node