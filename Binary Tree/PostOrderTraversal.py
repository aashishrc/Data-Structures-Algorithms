# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        return self.postorderTraversal(root.left) +  self.postorderTraversal(root.right) + [root.val]

        # ans = []
        # def postorder(root):
        #     if root == None:
        #         return 
        #     else:
        #         postorder(root.left)
        #         postorder(root.right)
        #         return ans.extend([root.val])
        # postorder(root)
        # return ans