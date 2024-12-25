# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        def is_greater(node,level):
            if not node:
                return 

            if level == len(arr):
                arr.append(node.val) 
            else:
                arr[level] = max(arr[level], node.val)
            
            is_greater(node.left, level + 1)
            is_greater(node.right, level + 1)

        arr = []
        is_greater(root, 0)
        
        return arr