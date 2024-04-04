link: https://www.geeksforgeeks.org/problems/top-view-of-binary-tree/1

from collections import deque

class Solution:
    
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        q = deque()
        lot = []
        q.append((root,0))
        width = set()
        level = []
        while q:
            for i in range(len(q)):
                cur, w = q.popleft()
                if w not in width:
                    level.append((cur.data,w))
                    width.add(w)
            
                if cur.left:
                    q.append((cur.left,w-1))
                if cur.right:
                    q.append((cur.right,w+1))

        sorted_list = sorted(level,key = lambda x : x[1])
        return [x[0] for x in sorted_list]