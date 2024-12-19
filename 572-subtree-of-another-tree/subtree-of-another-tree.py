# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False  # If the main tree is empty, it cannot contain the subtree.
        
        # Check if the trees are identical
        def isSameTree(tree1, tree2):
            if not tree1 and not tree2:
                return True  # Both trees are empty.
            if not tree1 or not tree2:
                return False  # One tree is empty, and the other is not.
            if tree1.val != tree2.val:
                return False  # Values of the roots don't match.
            
            # Recursively check the left and right subtrees.
            return isSameTree(tree1.left, tree2.left) and isSameTree(tree1.right, tree2.right)
        
        # Check if subRoot matches the current root, or isSubtree exists in left or right subtree
        return isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
