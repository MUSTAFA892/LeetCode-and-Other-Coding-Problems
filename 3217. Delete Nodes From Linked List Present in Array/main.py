# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:

        del_vals = set(nums)

        dummy = ListNode(0)
        dummy.next = head
        prev , current = dummy , head

        while current:
            if current.val in del_vals:
                prev.next = current.next
            else:
                prev = current
            
            current = current.next 

        
        return dummy.next