# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []

        def inOrder(root):
            if root == None:
                return 0

            inOrder(root.left)
            ans.append(root.val)
            inOrder(root.right)

        inOrder(root)
        return ans[k-1]