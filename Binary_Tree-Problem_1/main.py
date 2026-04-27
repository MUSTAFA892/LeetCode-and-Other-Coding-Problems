"""n = 3
arr =  [1,2,3,-1,5,-1,7,-1,-1,6]

pointer = 1
count = 2
round_ = 0

map_ = [[arr[0]]]
final_arr = [arr[0]]
while round_ <= n:
    temp = pointer
    map_.append(arr[pointer:temp+count])
    pointer += count 
    count *= 2  
    round_ += 1

change = 1

for i in range(1,len(map_)):
    if change == 1:
        for j in map_[i]:
            if j != -1:
                final_arr.append(j)
    else:
        for j in map_[i][::-1]:  
            if j != -1:
                final_arr.append(j)
    change *= -1

print(final_arr)"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        # Step 1: Group nodes by level using BFS
        from collections import deque
        
        queue = deque([root])
        map_ = []  # List of levels
        
        while queue:
            level_size = len(queue)
            current_level = []
            
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            map_.append(current_level)
        
        # Step 2: Zigzag processing (same as your code!)
        final_arr = []
        change = 1
        
        for i in range(len(map_)):
            if change == 1:
                # Left to right
                for val in map_[i]:
                    final_arr.append(val)
            else:
                # Right to left
                for val in map_[i][::-1]:
                    final_arr.append(val)
            
            change *= -1
        
        return final_arr