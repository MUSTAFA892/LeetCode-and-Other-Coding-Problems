# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def is_level(node):
            if node is None:
                return 0
            
            left = is_level(node.left)
            right = is_level(node.right)

            return max(left,right) + 1
        
        return is_level(root)
        
