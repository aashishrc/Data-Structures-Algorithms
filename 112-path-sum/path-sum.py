# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        stack = []
        stack.append(root)
        total = 0

        def preOrder(root, total):
            if root == None:
                return False
            
            total += root.val
            if not root.left and not root.right:
                return total == targetSum
            
            return preOrder(root.left, total) or preOrder(root.right, total)

        return preOrder(root, total)
