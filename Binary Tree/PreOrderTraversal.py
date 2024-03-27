# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = []
        if root == None:
            return []
        stack.append(root)
        while stack:
            cur = stack.pop()
            if cur:
                ans.append(cur.val)
                stack.append(cur.right)
                stack.append(cur.left)
        return ans
    # using recursion
    # def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     if root == None:
    #         return []
    #     root_val = [root.val]
    #     left_vals = self.preorderTraversal(root.left)
    #     right_vals = self.preorderTraversal(root.right)
    #     return root_val + left_vals + right_vals