# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        path_nodes = []

        def dfs(root):
            if not root:
                return 0
            path_nodes.append(root.val)
            
            dfs(root.left)
            dfs(root.right)
            if root.val >= max(path_nodes):
                self.count +=1
            path_nodes.pop()
        dfs(root)
        return self.count