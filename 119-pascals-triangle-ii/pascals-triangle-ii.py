class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex ==1 :
            return [1,1]
        temp = [1,1]
        for i in range(1, rowIndex):
            ans = []    
            ans.append(1)
            for j in range(len(temp)-1):
                ans.append(temp[j] + temp[j+1])
            ans.append(1)
            temp = ans
        return ans