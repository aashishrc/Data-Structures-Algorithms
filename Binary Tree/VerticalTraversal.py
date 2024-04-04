#link : https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append((root, 0))
        m = {}
        m[0] = {1:[root.val]}
        ans =[]
        level = 1
        while q:
            level +=1
            for i in range(len(q)):
                cur, wp = q.popleft()
                if cur.left:
                    wc = wp -1
                    if wc not in m.keys():
                        m[wc] = {level:[cur.left.val]}
                    else:
                        if level in m[wc].keys():
                            m[wc][level].append(cur.left.val)
                        else:
                            m[wc][level] = [cur.left.val]
                    q.append((cur.left, wc))
                if cur.right:
                    wc = wp + 1
                    if wc not in m.keys():
                        m[wc] = {level:[cur.right.val]}
                    else:
                        if level in m[wc].keys():
                            m[wc][level].append(cur.right.val)
                        else:
                            m[wc][level] = [cur.right.val]
                    q.append((cur.right, wc))
            for i in m.keys():
                if level in m[i].keys():
                    m[i][level].sort()
        print(m)
        m = dict(sorted(m.items(), key = lambda x : x[0]))
        
        for k,v in m.items():
            lst = []
            for x,y in v.items():
                lst += y
            m[k] = lst
        # print(m)
        # return []
        for k,v in m.items():
            ans.append(v)
        return ans