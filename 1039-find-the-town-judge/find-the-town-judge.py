class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustDict = {i+1 :[] for i in range(n)}
        # print(trustDict)
        for i in trust:
            trustDict[i[0]].append(i[1])
        flag = 0
        print(trustDict)
        for i,j in trustDict.items():
            if flag == 0 and len(j) == 0:
                flag = i
            elif flag and j == 0:
                return -1
        # print(flag)
        if flag:
            for i,j in trustDict.items():
                if i != flag and flag not in j:   
                    return -1
            return flag     
        return -1
        