# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        check = [True]

        def helper(node):
            if not node:
                return 0
            
            left_height = helper(node.left)
            if check[0] == False:
                return 0
            right_height = helper(node.right)

            if abs(left_height - right_height) > 1:
                check[0] = False
                return 0

            return 1 + max(left_height , right_height)
        
        helper(root)
        return check[0]