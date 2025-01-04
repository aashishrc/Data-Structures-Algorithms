class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = prerequisites
        visited = set()
        graph = {i:[] for i in range(numCourses)}
        for i in pre:
            course, depency = i[0], i[1]
            graph[course].append(depency)
        if not pre:
            return True
                
        def dfs(course):
            if course in visited:
                return False
            if graph[course] == []:
                return True
            visited.add(course)
            for n in graph[course]:
                if not dfs(n):
                    return False
            visited.remove(course)
            graph[course] = []    
            return True
                
        for start in range(numCourses):  
            if not dfs(start): return False
            
        return True  