# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0  # If the tree is empty, depth is 0
        
        stack = [(root, 1)]  # Stack contains nodes and their depth
        maxDepth = 0
        
        while stack:
            node, depth = stack.pop()  # Pop the node and its depth
            
            if node:
                # Update the maximum depth
                maxDepth = max(maxDepth, depth)
                
                # Add left and right children to the stack with incremented depth
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))
        
        return maxDepth


            

