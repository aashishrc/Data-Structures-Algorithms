class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = {}
        for i in edges:
            if i[0] in adj.keys():
                adj[i[0]].append(i[1])
            else:
                adj[i[0]] = [i[1]]
            if i[1] in adj.keys():
                adj[i[1]].append(i[0])
            else:
                adj[i[1]] = [i[0]]
        print(adj)
    
        def dfs(root):
            found = False
            if root == destination:
                return True
        
            visited[root] = True
            stack.append(root)
            
            while stack:
                cur = stack.pop()
                neighbors = adj[cur]
                for node in neighbors:
                    if not visited[node]:
                        found = dfs(node)
                        if found:
                            break
            return found

        visited = [False]*n
        stack = []
        return dfs(source)