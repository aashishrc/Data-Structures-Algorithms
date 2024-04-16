class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        adjList = {}
        for i in edges:
            if i[0] in adjList.keys():
                adjList[i[0]].append(i[1])
            else:
                adjList[i[0]] = [i[1]]
            if i[1] in adjList.keys():
                adjList[i[1]].append(i[0])
            else:
                adjList[i[1]] = [i[0]]
        for i, j in adjList.items():
            if len(j) == len(adjList.keys()) - 1:
                return i
        