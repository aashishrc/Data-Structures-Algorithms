# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque()
        max_width = -1
        q.append((root,1))
        level = []
        while q:
            iflag = 0
            fflag = 0
            level = []
            # print(q)
            for i in range(len(q)):
                cur,w = q.popleft()
            
                if cur.left:
                    q.append((cur.left,2*w))
                    fflag = 2*w
                    if iflag == 0:
                        # level.append(2*w)
                        iflag = 2*w
                
                if cur.right:
                    q.append((cur.right, 2*w +1 ))
                    fflag = 2*w +1
                    if iflag == 0:
                        iflag = 2*w + 1
                    # level.append(2*w + 1)
            # width = 1
            width = fflag - iflag + 1
            # if level:
            #     width = level[-1] - level[0] + 1
            if width > max_width:
                max_width = width
        return max_width
            
