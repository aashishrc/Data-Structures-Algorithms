# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0  # If the tree is empty, depth is 0
        
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right)) 
        
        # q = deque()      
        
        # depth = 1
        # maxDepth = -9999
        # q.append((root,1))
        # while q:
        #     node,depth = q.popleft()
        #     if node:
        #         maxDepth = max(maxDepth, depth)
        #         q.append((node.left, depth+1))
        #         q.append((node.right, depth+1))  
        # return maxDepth