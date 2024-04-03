# link : https://www.codingninjas.com/studio/problems/bottom-view-of-binary-tree_893110?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

from typing import List
from collections import deque

# Following is the TreeNode class structure.


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def bottomView(root: BinaryTreeNode) -> List[int]:
    # Write your code here.
    q = deque()
    if not root:
        return
    q.append((root,0))
    wp = 0
    widthMap = {}
    ans = []
    widthMap[0] = root.data
    while q:
        for i in range(len(q)):
            cur, wp = q.popleft()
            if cur.left:
                wc = wp - 1
                q.append((cur.left,wc))
                widthMap[wc] = cur.left.data
            if cur.right:
                wc = wp + 1
                q.append((cur.right,wc))
                widthMap[wc] = cur.right.data
    sorted_dict = sorted(widthMap.items(), key = lambda x: x[0])
    for k,v in sorted_dict:
        ans.append(v)  
    return ans