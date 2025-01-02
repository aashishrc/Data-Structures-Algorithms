"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        ans= {}
        if not node:
            return None
        def dfs(node):
            if node not in ans:
                n = Node(node.val)
                ans[node] = n

                for neighbor in node.neighbors:
                    neigh = dfs(neighbor)
                    n.neighbors.append(neigh)
            else:
                return ans[node]
                
            return n

        dfs(node)
        
        return ans[node]