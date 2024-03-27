# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]):
        inOrder= []
        cur = root
        while cur != None:
            if cur.left == None:
                inOrder.append(cur.val)
                cur = cur.right
            else:
                prev = cur.left
                while(prev.right and prev.right !=cur):
                    prev = prev.right
                if prev.right == None:
                    prev.right = cur
                    cur = cur.left
                else:
                    prev.right = None
                    inOrder.append(cur.val)
                    cur = cur.right
        return inOrder

    #uses extra space of stack
    # def inorderTraversal(self, root: Optional[TreeNode]):
    #     ans = []
    #     stack = []
    #     cur = root
    #     while cur or stack:
    #         while cur:
    #             stack.append(cur)
    #             cur = cur.left
    #         cur = stack.pop()
    #         ans.append(cur.val)
    #         cur = cur.right
    #     return ans
        
    #using recursive
    # def inorderTraversal(self, root: Optional[TreeNode]):
    #     if root == None:
    #         return []
        
    #     left_vals = self.inorderTraversal(root.left)
    #     root_vals = [root.val]        
    #     right_vals = self.inorderTraversal(root.right)
    #     return left_vals + root_vals + right_vals        